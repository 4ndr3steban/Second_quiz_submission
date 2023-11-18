from fastapi import APIRouter, HTTPException, status
from typing import Union
from datetime import datetime as dt, timedelta
from Config.BQclient import BQclient
from Schemas.query import Query

# Instancia para manejar el endpoint para consultas a BigQuery
router = APIRouter(prefix="/bigquery",
                    tags=["user consults"],
                    responses={status.HTTP_404_NOT_FOUND: {"response": "not found"}})


@router.get("/consult", status_code = status.HTTP_200_OK)
async def macrochallenges(date: str = str(dt.now().date()-timedelta(days=1)),
                          georange: str = "us",
                          country: Union[str, None] = None,
                          numtop: int = 25,
                          ascentop: str = "",
                          id_post: int = 0):
    
    """ Consulta sql manejada con filtros a BigQuery

    input: datos sobre los filtros de la consulta
            - date: fecha de la cual se quiere ver el top
            - georange: top internacional o de estados unidos
            - country: si el top es internacional, especificar el pais
            - numtop: rango del top (ej: top 5, top 10, ...)
            - ascentop: ver top establecido o ver trends en ascenso
            - id_post: se establece automaticamente (se usa solo en caso de guardar la query)

    output: nombre del trend y posición en el ranking
    
    """
    try:
        # Instancia de la query para manejar los datos como un Schema
        query = Query(date=date, georange=georange, country=country, numtop=numtop, ascentop=ascentop, id_pos=id_post)
    except:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Incorrect query format")

    # Query con los filtros aplicados para top de us
    query_top =f"""

    SELECT term, rank FROM `bigquery-public-data.google_trends.top_{query.ascentop}terms` 
    Where refresh_date = "{query.date}" group by term, rank order by rank limit {query.numtop};

    """

    # Query con los filtros aplicados para top internacional
    query_intr_top =f"""

    SELECT term, rank FROM `bigquery-public-data.google_trends.international_top_{query.ascentop}terms` 
    Where refresh_date = "{query.date}" and country_name = "{query.country}" group by term, rank order by rank limit {query.numtop};

    """

    # Usar una de las queries anteriores según sea el caso (us o internacional)
    try:
        if query.georange == "us":
            res = BQclient.query(query_top)
        elif query.georange == "intr":
            res = BQclient.query(query_intr_top)

        return res
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="fail request to BigQuery (try to change inputs)")        