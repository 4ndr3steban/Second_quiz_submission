from fastapi import APIRouter, HTTPException, status
from settings import settings

router = APIRouter(prefix="/userqueries",
                    tags=["saved of user queries"],
                    responses={status.HTTP_404_NOT_FOUND: {"response": "not found"}})


@router.get("/save", response_model = dict, status_code = status.HTTP_200_OK)
async def macrochallenges(x: str):
    pass