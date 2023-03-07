from fastapi import FastAPI
from server.routers.cotacaoController import cotacao


def inclui_rota():
    app = FastAPI(
        title="PROJETO API COTAÇÃO COM APACHE AIRFLOW",
    )
    app.include_router(cotacao)
