from fastapi import APIRouter, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from Config.db import engine
from Config.models import Tpost, Tquery, Tcomment
from Schemas.comment import Comment
from Schemas.post import Post
from Schemas.query import Query

router = APIRouter(prefix="/userqueries",
                    tags=["saved of user queries"],
                    responses={status.HTTP_404_NOT_FOUND: {"response": "not found"}})


@router.post("/savequery", status_code = status.HTTP_200_OK)
async def savequery(query: Query):

    session = Session(engine)
    qr = select(Tpost)

    return "correct"


@router.post("/savecomment", response_model=dict, status_code = status.HTTP_200_OK)
async def savecomment():

    session = Session(engine)
    qr = select(Tpost)

    return session.scalars(qr)


@router.get("/showqueries", response_model=dict, status_code = status.HTTP_200_OK)
async def showqueries():

    session = Session(engine)
    qr = select(Tpost)

    return {"res": session.scalars(qr)}


@router.get("/showcomments", status_code = status.HTTP_200_OK)
async def showcomment():

    session = Session(engine)
    qr = select(Tpost)

    return session.scalars(qr)


@router.get("/getquerytouse", status_code = status.HTTP_200_OK)
async def getquerytouse():

    session = Session(engine)
    qr = select(Tpost)

    return session.scalars(qr)