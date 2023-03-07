import json
import requests
from server.database.database import DolarDatabase
from server.config.db import MongoConnection

class Cotacao:
    def __init__(self):
        pass
    def cotacao_dolar(self):
        try:
            response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
            mongo_connection = MongoConnection('dolar')

            if response.status_code == 200:
                data = json.loads(response.content)
                bid_value = data['USDBRL']['bid']
                db = DolarDatabase(get_connection())
                inserted_id = db.insert_document(bid_value)
                return f"O Id da cotação é ID: {inserted_id}"
            else:
                return ("Erro ao fazer requisição à API.")
        except Exception:
            raise Exception





