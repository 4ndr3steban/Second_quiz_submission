from sqlalchemy import Engine, create_engine
from settings import settings
from .models import Base, Tcomment, Tpost, Tquery
from time import sleep

# ---------------------------------------
# NOTA: las credenciales de conexion a la db
# estan escritas dentro del codigo, esto es una
# mala practica (deberian ser variables de entorno)
# pero se hace por simplicidad y facilidad para enviar
# la prueba.
# ---------------------------------------

flag = False

while not flag:
    try:
        # Conexión a la base de datos MySql para datos de usuarios y queries
        engine = create_engine(f"mysql://{settings.MYSQL_USER}:{settings.MYSQL_PASS}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DB}")

        # Metadata para crear las tablas en la db y los tipos de datos en ellas
        Base.metadata.create_all(bind=engine)

        flag = True
    except Exception:
        sleep(15)