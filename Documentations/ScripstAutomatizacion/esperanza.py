import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

CREDENTIALS_PATH = "/home/oleaibarra/credenciales_cta_servicio.json"
BUCKET = "carga-drive-joi"
DOWNLOAD_PATH = "/home/oleaibarra/Yelp"


def get_drive_service():
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH, 
        scopes=["https://www.googleapis.com/auth/drive"]
    )
    return build('drive', 'v3', credentials=creds)

def list_files_and_folders_in_folder(folder_id, indent=0):
    """Listar archivos y carpetas dentro del folder con el ID dado de forma recursiva."""
    drive_service = get_drive_service()
    results = drive_service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name, mimeType)").execute()
    items = results.get('files', [])
    
    prefix = ' ' * indent
    print(f"{prefix}Archivos y carpetas en el folder con ID {folder_id}:")
    
    for item in items:
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            print(f"{prefix}Carpeta: {item['name']}")
            print(f"{prefix}IdCarpeta: {item['id']}")
            list_files_and_folders_in_folder(item['id'], indent + 2)
        else:
            print(f"{prefix}Archivo: {item['name']}")

def download_files_from_folder(folder_id, download_path):
    """Descargar archivos de una carpeta dada."""
    drive_service = get_drive_service()
    results = drive_service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name, mimeType)").execute()
    items = results.get('files', [])
    
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    for item in items:
        if item['mimeType'] != 'application/vnd.google-apps.folder':
            request = drive_service.files().get_media(fileId=item['id'])
            filename = os.path.join(download_path, item['name'])
            with open(filename, 'wb') as f:
                downloader = MediaIoBaseDownload(f, request)
                done = False
                while done is False:
                    _, done = downloader.next_chunk()
            print(f"Archivo {item['name']} descargado en {filename}")

def upload_folder_to_bucket(folder_path, bucket_name):
    """Upload folder and its files to GCP bucket."""
    # Assuming you've set up `gsutil` (a part of the Google Cloud SDK) on your machine
    os.system(f"gsutil -m cp -r {folder_path} gs://{bucket_name}/")

# 1. listar carpetas y archivos recursivamente
folder_id = '1lk0t6raq7cC21npJ8g4oW_dFJjEUZaP9'
list_files_and_folders_in_folder(folder_id)

# 2. descargar la carpeta yelp con sus archivos
yelp_folder_id = '1hlTR3E8jMKqxLsLNsnKJ-bfwQUPKvtMC'  # ID of the Yelp folder, which you provided
download_files_from_folder(yelp_folder_id, DOWNLOAD_PATH)

# 3. cargar la carpeta yelp al bucket
upload_folder_to_bucket(DOWNLOAD_PATH, BUCKET)
