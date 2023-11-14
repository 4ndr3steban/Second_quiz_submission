from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    id: int | None = None
    username: str
    name: str
    descript: str