from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from Config.db import engine
from Config.models import Tpost, Tquery, Tcomment
from Schemas.comment import Comment
from Schemas.post import Post
from Schemas.query import Query


def insert_item(db: Session, table: Tpost | Tquery | Tcomment, item: Query | Post | Comment):
    """ insertar un elemento en la db

    input: - db: session de conección con la db
           - table: tabla en la cual se va a insetar el dato
           - item: elemento a insertar

    output: id del elemento en la db
    
    """
    # Formatear el item a diccionario
    db_item = item.model_dump()

    # Insertar el item en la db
    res = db.execute(insert(table).values(db_item))

    # Hacer el commit a la db
    db.commit()

    return res.lastrowid


def get_query(db: Session, id_post: int):
    """ Obtener una query de un post guardado en la db

    input: - db: session de conección con la db
           - id_post: id del post en el que está publicada la query

    output: query
    
    """
    
    # Obtener la query de la db filtrando por el id del post
    db_query = db.query(Tquery).filter(Tquery.id_pos == id_post).all()

    return db_query[0]


def get_comments(db: Session, id_post: int):
    """ Obtener los comentarios de un post guardado en la db

    input: - db: session de conección con la db
           - id_post: id del post

    output: lista de comentarios
    
    """
    
    # Obtener los comentarios de la db filtrando por el id del post
    db_query = db.query(Tcomment).filter(Tcomment.id_post == id_post).all()

    return db_query


def get_posts(db: Session):
    """ Obtener los posts guardados en la db

    input: - db: session de conección con la db

    output: lista de posts
    
    """
    
    # Obtener los posts de la db
    db_query = db.query(Tpost).all()

    return db_query