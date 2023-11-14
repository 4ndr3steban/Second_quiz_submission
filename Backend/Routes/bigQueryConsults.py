from fastapi import APIRouter, HTTPException, status
from Config.BQclient import BQclient
from Schemas.query import Query

router = APIRouter(prefix="/bigquery",
                    tags=["user consults"],
                    responses={status.HTTP_404_NOT_FOUND: {"response": "not found"}})


@router.get("/consult", status_code = status.HTTP_200_OK)
async def macrochallenges(query: Query):
    tabla = ""
    if query.georange == "us":
        tabla = "`bigquery-public-data.google_trends.top_terms`"

    test_query =f"""

    SELECT term, rank FROM {tabla}`bigquery-public-data.google_trends.top_terms` 
    Where refresh_date = DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY) and country_name = "Belgium" order by rank;

    """
    res = BQclient.query(test_query)

    return res