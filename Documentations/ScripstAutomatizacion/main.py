import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
import json

class TransformData(beam.DoFn):
    def process(self, element):
        keys_to_remove = ['price', 'hours', 'MISC', 'state', 'relative_results', 'url']
        
        for key in keys_to_remove:
            if key in element:
                del element[key]
        
        for key in element.keys():
            if isinstance(element[key], str):
                element[key] = element[key].strip()

                if key == 'name' or key == 'address':
                    element[key] = element[key].title()

            elif not element[key]:
                element[key] = ''
                    
            elif isinstance(element[key], list):
                element[key] = [item.strip() for item in element[key] if isinstance(item, str)]

        yield element

class FilterCategories(beam.DoFn):
    def process(self, element):
        if 'category' in element and element['category'] is not None:
            categories = [category.lower() for category in element['category']]
            categories = " ".join(categories)

            if 'hotel' in categories:
                element['etiqueta'] = 'Hotel'
                yield element
            elif 'restaurant' in categories:
                element['etiqueta'] = 'Restaurante'
                yield element
       
def run():
    pipeline_options = PipelineOptions(
        project='proven-mystery-394422',
        job_name='dataflow-job',
        temp_location='gs://bucket_gmaps/temp',
        region='southamerica-east1',
    )

    with beam.Pipeline(options=pipeline_options) as p:
        
        # Leer el archivo JSON desde Cloud Storage
        data = (p | "Read JSON" >> beam.io.ReadFromText('gs://bucket_gmaps/metadata_sitios_copia/*.jsonl'))

         # Eliminar registros duplicados
        deduplicated_data = data | "Deduplicate Data" >> beam.Distinct()

        # Cargar los datos JSON en un formato estructurado
        json_data = deduplicated_data | "Parse JSON" >> beam.Map(json.loads)

        # Transformar los datos eliminando las columnas
        transformed_data = (json_data | "Transform and Clean Data" >> beam.ParDo(TransformData()))

        # Filtrar y agregar etiquetas 'hotel' o 'restaurante'
        labeled_data = (transformed_data | "Filter and Add Label" >> beam.ParDo(FilterCategories()))

        # Especificar los metadatos de BigQuery para la tabla de destino general
        general_table_spec = 'proven-mystery-394422:dataflow.business_google'
        general_table_schema = {
            "fields": [
                {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                {"name": "address", "type": "STRING", "mode": "NULLABLE"},
                {"name": "gmap_id", "type": "STRING", "mode": "NULLABLE"},
                {"name": "description", "type": "STRING", "mode": "NULLABLE"},
                {"name": "latitude", "type": "FLOAT", "mode": "NULLABLE"},
                {"name": "longitude", "type": "FLOAT", "mode": "NULLABLE"},
                {"name": "category", "type": "STRING", "mode": "REPEATED"},
                {"name": "avg_rating", "type": "FLOAT", "mode": "NULLABLE"},
                {"name": "num_of_reviews", "type": "INTEGER", "mode": "NULLABLE"},
                {"name": "etiqueta", "type": "STRING", "mode": "NULLABLE"},
            ]
        }

        # Especificar los metadatos de BigQuery para la tabla de destino de 'hotels'
        hotels_table_spec = 'proven-mystery-394422:dataflow.hotels'
        hotels_table_schema = {
            "fields": general_table_schema["fields"]
        }

        # Especificar los metadatos de BigQuery para la tabla de destino de 'restaurants'
        restaurants_table_spec = 'proven-mystery-394422:dataflow.restaurants'
        restaurants_table_schema = {
            "fields": general_table_schema["fields"]
        }

        # Dividir los datos etiquetados en 'hotels' y 'restaurants'
        hotels_data = (labeled_data | "Filter Hotels" >> beam.Filter(lambda element: element['etiqueta'] == 'Hotel'))
        restaurants_data = (labeled_data | "Filter Restaurants" >> beam.Filter(lambda element: element['etiqueta'] == 'Restaurante'))

        # Cargar los datos en las tablas correspondientes en BigQuery
        hotels_data | "Write to Hotels BigQuery" >> WriteToBigQuery(
            hotels_table_spec,
            schema=hotels_table_schema,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
        )

        restaurants_data | "Write to Restaurants BigQuery" >> WriteToBigQuery(
            restaurants_table_spec,
            schema=restaurants_table_schema,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
        )

        labeled_data | "Write to BigQuery" >> WriteToBigQuery(
            general_table_spec,
            schema=general_table_schema,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
        )

if __name__ == '__main__':
    run()