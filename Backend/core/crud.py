from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from Config.db import engine
from Config.models import Tpost, Tquery, Tcomment
from Schemas.comment import Comment
from Schemas.post import Post
from Schemas.query import Query


def insert_item(db: Session, table: Tpost | Tquery | Tcomment, item: Query | Post | Comment):
    db_item = item.model_dump()
    db.execute(insert(table).values(db_item))
    db.commit()
    return db_item


def get_query(db: Session, id_post: int):
    
    db_query = db.query(Tquery).filter(Tquery.id_pos == id_post).all()

    return db_query


def get_comments(db: Session, id_post: int):
    
    db_query = db.query(Tcomment).filter(Tcomment.id_post == id_post).all()

    return db_query


def get_posts(db: Session):
    
    db_query = db.query(Tpost).all()

    return db_query