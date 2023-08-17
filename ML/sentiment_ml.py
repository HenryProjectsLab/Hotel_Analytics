import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from google.cloud import storage

# Descargar el recurso necesario para VADER (ejecuta solo una vez)
nltk.download('vader_lexicon')

# Inicializar el analizador de sentimientos de VADER
analyzer = SentimentIntensityAnalyzer()

def get_sentiment_score(comentario):
    return analyzer.polarity_scores(comentario)['compound']

def process_reviews_from_gcs(bucket_name, blob_name):
    # Crear un cliente de GCS
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Descargar el archivo del bucket
    blob = bucket.blob(blob_name)
    blob.download_to_filename('/tmp/hoteles.parquet') # Guardar temporalmente en /tmp
    
    # Leer el archivo Parquet con pandas
    df = pd.read_parquet('/tmp/hoteles.parquet')
    
    # Calcular el sentimiento para cada comentario y agregarlo como columna 'puntaje_sentimiento'
    df['puntaje_sentimiento'] = df['comentario'].apply(get_sentiment_score)

    # Guardar el dataframe modificado nuevamente como Parquet
    df.to_parquet('/tmp/hoteles_modified.parquet')
    
    # Subir el archivo Parquet modificado al bucket, reemplazando el original
    blob.upload_from_filename('/tmp/hoteles_modified.parquet')

# Ejecuta la función
BUCKET = 'carga-drive-yelp'
ARCHIVO = 'tabla_final_hoteles_google_yelp.parquet'
process_reviews_from_gcs(BUCKET, ARCHIVO)
