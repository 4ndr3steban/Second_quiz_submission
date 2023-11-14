from sqlalchemy import select
from sqlalchemy.orm import Session
from Config.db import engine
from Config.models import Tpost, Tquery, Tcomment


def create_item(db: Session, item: Item):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

