from fastapi import APIRouter, HTTPException, status
from settings import settings

router = APIRouter(prefix="/bigquery",
                    tags=["user consults"],
                    responses={status.HTTP_404_NOT_FOUND: {"response": "not found"}})


@router.get("/consult", response_model = dict, status_code = status.HTTP_200_OK)
async def macrochallenges(x: str):
    pass