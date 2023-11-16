from pydantic import BaseModel

# Clase para manejar los datos de una query como un Schema
class Query(BaseModel):
    id: int | None = None
    date: str
    georange: str
    country: str | None = None
    numtop: int
    ascentop: str
    id_pos: int