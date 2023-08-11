import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from google.cloud import bigquery
import json

class FilterJsonByKeys(beam.DoFn):
    def __init__(self, keys):
        self.keys = keys
    
    def process(self, element):
        json_data = json.loads(element)
        if json_data['gmap_id'] in self.keys:
            yield json_data

class TransformData(beam.DoFn):
    def process(self, element):
        keys_to_remove = ['resp', 'pics']
        
        for key in keys_to_remove:
            if key in element:
                del element[key]
        
        for key in element.keys():
            if isinstance(element[key], str):
                element[key] = element[key].strip()

                if key == 'name':
                    element[key] = element[key].title()

            elif not element[key]:
                element[key] = ''
            
        yield element

def run():
    pipeline_options = PipelineOptions(
        project='proven-mystery-394422',
        job_name='dataflow-job',
        temp_location='gs://bucket_gmaps/temp',
        region='southamerica-east1',
    )

    client = bigquery.Client()

    # Realiza la consulta en BigQuery para obtener las claves de la primera tabla
    query_table1 = """
        SELECT DISTINCT gmap_id
        FROM `proven-mystery-394422.dataflow.hotels`
    """
    query_job_table1 = client.query(query_table1)
    keys_table1 = [row['gmap_id'] for row in query_job_table1]

    # Realiza la consulta en BigQuery para obtener las claves de la segunda tabla
    query_table2 = """
        SELECT DISTINCT gmap_id
        FROM `proven-mystery-394422.dataflow.restaurants`
    """
    query_job_table2 = client.query(query_table2)
    keys_table2 = [row['gmap_id'] for row in query_job_table2]

    with beam.Pipeline(options=pipeline_options) as p:
        
        # Lee el archivo JSON y filtra los registros
        json_lines = p | "Read JSON File" >> beam.io.ReadFromText("gs://bucket_gmaps/reviews-estados/*/*.json")

         # Eliminar registros duplicados
        deduplicated_data = json_lines | "Deduplicate Data" >> beam.Distinct()      

        filtered_records_table1 = deduplicated_data | "Filter JSON Records Table 1" >> beam.ParDo(FilterJsonByKeys(keys_table1))

        # Lee el archivo JSON y filtra los registros para la tabla 2
        filtered_records_table2 = deduplicated_data | "Filter JSON Records Table 2" >> beam.ParDo(FilterJsonByKeys(keys_table2))

        #Limpieza y transformación
        transformed_table1 = (filtered_records_table1 | "Transform and Clean Data Table 1" >> beam.ParDo(TransformData()))

        transformed_table2 = (filtered_records_table2 | "Transform and Clean Data Table 2" >> beam.ParDo(TransformData()))

        # Especificar los metadatos de BigQuery para la tabla de destino de 'hotels_reviews'
        hotels_reviews_table_spec = 'proven-mystery-394422:dataflow.hotels_reviews'
        hotels_reviews_table_schema = {
            "fields": [
                {"name": "gmap_id", "type": "STRING", "mode": "NULLABLE"},
                {"name": "rating", "type": "INTEGER", "mode": "NULLABLE"},
                {"name": "text", "type": "STRING", "mode": "NULLABLE"},
                {"name": "time", "type": "INTEGER", "mode": "NULLABLE"},
                {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                {"name": "user_id", "type": "STRING", "mode": "NULLABLE"},
            ]
        }

        # Especificar los metadatos de BigQuery para la tabla de destino de 'restaurant_reviews'
        restaurant_reviews_table_spec = 'proven-mystery-394422:dataflow.restaurant_reviews'
        restaurant_reviews_table_schema = {
            "fields": [
                {"name": "gmap_id", "type": "STRING", "mode": "NULLABLE"},
                {"name": "rating", "type": "INTEGER", "mode": "NULLABLE"},
                {"name": "text", "type": "STRING", "mode": "NULLABLE"},
                {"name": "time", "type": "INTEGER", "mode": "NULLABLE"},
                {"name": "name", "type": "STRING", "mode": "NULLABLE"},
                {"name": "user_id", "type": "STRING", "mode": "NULLABLE"},
            ]
        }


        transformed_table1 | "Write to Hotels Reviews BigQuery" >> WriteToBigQuery(
            hotels_reviews_table_spec,
            schema=hotels_reviews_table_schema,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
        )

        transformed_table2 | "Write to Restaurant Reviews BigQuery" >> WriteToBigQuery(
            restaurant_reviews_table_spec,
            schema=restaurant_reviews_table_schema,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND,
        )


if __name__ == "__main__":
    run()
