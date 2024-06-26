from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from Config.db import engine
from Core.crud import insert_item, get_query, get_comments, get_posts
from Config.models import Tpost, Tquery, Tcomment
from Schemas.comment import Comment
from Schemas.post import Post
from Schemas.query import Query

# Instancia para manejar el endpoint para el manejo de la db de MySql
router = APIRouter(prefix="/userqueries",
                    tags=["saved of user queries"],
                    responses={status.HTTP_404_NOT_FOUND: {"response": "not found"}})


@router.post("/savequeryandpost", response_model=dict, status_code = status.HTTP_201_CREATED)
async def savequery(query: Query, post: Post):
    """ Guardar una consulta en la db

    input: - post: tiene los datos del usuario que guarda la consulta
           - query: tiene los datos de la consulta

    output: ids de los elementos guardados en la db para verificaciones
    
    """
    try:
        # Guardar el post (datos del usuario)
        post = insert_item(Session(engine), Tpost, post)

        # Setear el id del post en la query para identificar de que post es cada query
        query.id_pos = post

        # Guardar la query
        qry = insert_item(Session(engine), Tquery, query)
    
        return {"id_post": post,"id_query": qry}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="fail to create post (review inputs and try again)")


@router.post("/savecomment/{id_post}", response_model=dict, status_code = status.HTTP_201_CREATED)
async def savecomment(id_post: str, comment: Comment):
    """ Guardar un comentario a un post en la db

    input: - comment: la información del comentario

    output: ids de los elementos guardados en la db para verificaciones
    
    """

    try:
        # Setear el id del post en el que se hace el comentario (se setea como str pero se guarda como int)
        comment.id_post = id_post

        # Guardar el comentario en la db
        item = insert_item(Session(engine), Tcomment, comment)

        return {"id_comment": item}
    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="fail to create post (review inputs and try again)")


@router.get("/showposts", status_code = status.HTTP_200_OK)
async def showqueries():
    """ Obtener todos los posts guardados en la db

    input: non

    output: lista con todos los posts guardados hasta el momento
    
    """
    try:
        # Obtener los posts de la db
        posts = get_posts(Session(engine))

        return posts
    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="server failure")


@router.get("/showcomments/{id_post}", status_code = status.HTTP_200_OK)
async def showcomment(id_post: int):
    """ Obtener los comentarios de un post

    input: - id_post: id del post del que se quieren los comentarios

    output: lista con los comentarios del post
    
    """
    try:
        # obtener los comentarios del post
        comments = get_comments(Session(engine), id_post)

        return comments
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="server failure")

@router.get("/getquerytouse/{id_post}", status_code = status.HTTP_200_OK)
async def getquerytouse(id_post: int):
    """ Obtener los datos de una query guardada en un post para ser usada de nuevo

    input: - id_post: id del post en el cual está la query que se quiere obtener

    output: lista con la query que se quiere
    
    """
    try:
        # Obtener la query
        db_query = get_query(Session(engine), id_post)

        return db_query
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="server failure")