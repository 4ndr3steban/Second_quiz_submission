from typing import Optional
from pydantic import BaseModel

class Query(BaseModel):
    id: int | None = None
    date: str
    georange: str
    country: str | None = None
    numtop: int
    ascentop: bool
    id_pos: int