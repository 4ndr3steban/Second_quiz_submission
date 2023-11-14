from sqlalchemy import Engine, create_engine
from settings import settings
from .models import Base, Tcomment, Tpost, Tquery


engine = create_engine(f"mysql://{settings.MYSQL_USER}:{settings.MYSQL_PASS}@localhost:{settings.MYSQL_HOST}/{settings.MYSQL_DB}")

Base.metadata.create_all(bind=engine)