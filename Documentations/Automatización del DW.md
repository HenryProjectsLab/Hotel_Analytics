# Scripts de Dataflow para Automatización del Datawarehouse

Este repositorio contiene scripts de Google Dataflow en la carpeta `ScripstAutomatizacion` para automatizar el datawarehose de Google Cloud. Los scripts se encargan de extraer datos de negocios de hoteles, limpiar y transformar los datos, y cargarlos en Google BigQuery para su análisis.

## Descripción general

El proyecto se divide en dos scripts principales:

1. `main.py`: Este script extrae datos de negocios de hoteles, realiza limpieza y transformación, y carga los datos en la tabla `hotels` de BigQuery.

2. `mainkeys.py`: Este script extrae datos de reviews de hoteles, filtra por los `gmap_id` de la tabla `hotels`, realiza limpieza y transformación, y carga los datos en las tablas `hotels_reviews` y `restaurant_reviews` de BigQuery.

## Requisitos previos

Antes de ejecutar los scripts, asegúrate de haber configurado adecuadamente las credenciales de autenticación de Google Cloud.

## `main.py`

### Funcionamiento

1. Lee datos de negocios de hoteles desde archivos JSON ubicados en Cloud Storage.

2. Elimina columnas no deseadas y realiza limpieza de los datos.

3. Filtra los negocios que tienen la etiqueta "Hotel" en la columna `etiqueta`.

4. Carga los datos limpios en la tabla `hotels` de BigQuery.

### Ejecución

```bash
python main.py --runner DataflowRunner \
               --project proven-mystery-394422 \
               --temp_location gs://bucket_gmaps/tmp/ \
               --staging_location gs://bucket_gmaps/staging/ \
               --region southamerica-east1 \
               --dataflow_service_options=enable_prime \
               --setup_file ./setup.py
```

## `mainkeys.py`

### Funcionamiento

1. Obtiene la lista de todos los `gmap_id` de la tabla `hotels` creada anteriormente en BigQuery.

2. Lee datos de reviews desde archivos JSON ubicados en Cloud Storage.

3. Filtra las reviews por los `gmap_id` de la tabla `hotels`.

4. Realiza limpieza y transformación de los datos de reviews.

5. Carga los datos limpios en las tablas `hotels_reviews` y `restaurant_reviews` de BigQuery.

### Ejecución

```bash
python mainkeys.py --runner DataflowRunner \
               --project proven-mystery-394422 \
               --temp_location gs://bucket_gmaps/tmp/ \
               --staging_location gs://bucket_gmaps/staging/ \
               --region southamerica-east1 \
               --dataflow_service_options=enable_prime \
               --setup_file ./setup.py
```

## Programación y Automatización

Para automatizar el proceso de carga de datos y análisis, se pueden utilizar programadores de tareas (por ejemplo, Cron en sistemas Unix) para ejecutar los scripts en intervalos regulares.

## Contribuciones

Si deseas contribuir a este proyecto, ¡no dudes en crear un pull request!

---

**Nota:** Asegúrate de que todos los valores de configuración, como nombres de tablas, ubicaciones de archivos y credenciales, se ajusten a tu entorno antes de ejecutar los scripts.

Autor: Jeison Suárez
