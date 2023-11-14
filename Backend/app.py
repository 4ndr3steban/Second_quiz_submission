from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routes import bigQueryConsults, usersQueries


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(bigQueryConsults.router)

app.include_router(usersQueries.router)