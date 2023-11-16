from pydantic import BaseModel
from typing import Optional

# Clase para manejar los datos de un comentario como un Schema 
class Comment(BaseModel):
    id: int | None = None
    user: str
    comment: str
    id_post: str