from dotenv import load_dotenv
from google.cloud import bigquery
import os
from dataclasses import dataclass

# Configuracion de las variables de entorno
@dataclass
class Settings:
    test: str
    BQclient: bigquery

# Cargar variables de entorno
load_dotenv()
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'second-test-fellows-gc.json'

# Guardar variables de entorno
settings = Settings(test=os.getenv("test"), BQclient=bigquery.Client())