from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from Config.db import engine
from Core.crud import insert_item, get_query, get_comments, get_posts
from Config.models import Tpost, Tquery, Tcomment
from Schemas.comment import Comment
from Schemas.post import Post
from Schemas.query import Query

router = APIRouter(prefix="/userqueries",
                    tags=["saved of user queries"],
                    responses={status.HTTP_404_NOT_FOUND: {"response": "not found"}})


@router.post("/savequeryandpost", response_model=list, status_code = status.HTTP_200_OK)
async def savequery(query: Query, post: Post):

    post = insert_item(Session(engine), Tpost, post)
    qry = insert_item(Session(engine), Tquery, query)
    
    return [post, qry]


@router.post("/savecomment", response_model=dict, status_code = status.HTTP_200_OK)
async def savecomment(comment: Comment):

    item = insert_item(Session(engine), Tcomment, comment)

    return item



@router.get("/showposts", response_model=list, status_code = status.HTTP_200_OK)
async def showqueries():

    posts = get_posts(Session(engine))

    return posts


@router.get("/showcomments/{id_post}", response_model=list, status_code = status.HTTP_200_OK)
async def showcomment(id_post: int):

    comments = get_comments(Session(engine), id_post)

    return comments


@router.get("/getquerytouse/{id_post}", response_model=list, status_code = status.HTTP_200_OK)
async def getquerytouse(id_post: int):

    db_qery = get_query(Session(engine), 2)

    return db_qery