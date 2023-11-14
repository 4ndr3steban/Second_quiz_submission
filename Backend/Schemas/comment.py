from pydantic import BaseModel
from typing import Optional

class Comment(BaseModel):
    id: int | None = None
    user: str
    comment: str
    id_post: str