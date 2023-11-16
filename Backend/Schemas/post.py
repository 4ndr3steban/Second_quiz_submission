from pydantic import BaseModel
from typing import Optional

# Clase para manejar los datos de un post como un Schema
class Post(BaseModel):
    id: int | None = None
    username: str
    name: str
    descript: str