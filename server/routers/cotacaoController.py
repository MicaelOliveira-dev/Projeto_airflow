from fastapi import APIRouter, status, Response
from server.consultas.scrapping import Cotacao

cotacao = APIRouter()


@cotacao.get("/cotacao_dolar", status_code=status.HTTP_200_OK)
async def Cotacao_dolar():
    try:
        cotacao = Cotacao()
        return {"cotacao": cotacao.cotacao_dolar()}

    except Exception as ex:
        print(ex)
        return Response(status_code=500)
