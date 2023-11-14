from fastapi import APIRouter, HTTPException, status
from Config.BQclient import BQclient

router = APIRouter(prefix="/bigquery",
                    tags=["user consults"],
                    responses={status.HTTP_404_NOT_FOUND: {"response": "not found"}})


@router.get("/consult", status_code = status.HTTP_200_OK)
async def macrochallenges():
    test_query ="""

    SELECT distinct term, rank FROM `bigquery-public-data.google_trends.international_top_terms` 
    Where refresh_date = DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY) and country_name = "Belgium" order by rank;

    """

    res = BQclient.query(test_query)

    return res