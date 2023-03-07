import datetime
import pytz

class DolarDatabase:
    def __init__(self, collection):
        self.collection = collection

    def insert_document(self, bid_value):
        doc = {
            'data': datetime.datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%Y-%m-%d %H:%M:%S'),
            'cotacao': bid_value
        }
        result = self.collection.insert_one(doc)
        return result.inserted_id















