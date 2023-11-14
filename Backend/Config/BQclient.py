from google.cloud import bigquery
import os

# Cargar variables de entorno
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'second-test-fellows-gc.json'

BQclient=bigquery.Client()
