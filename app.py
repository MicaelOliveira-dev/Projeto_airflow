from fastapi import FastAPI
from server.routers.cotacaoController import cotacao


app = FastAPI(
    title="PROJETO API COTAÇÃO COM APACHE AIRFLOW",
)
app.include_router(cotacao)
