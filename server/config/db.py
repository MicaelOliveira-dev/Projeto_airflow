import pymongo



class MongoConnection:
    def __init__(self, db_name):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        try:
            return self.db[collection_name]
        except Exception:
            raise Exception

    def get_connection(self):
        try:
            mongo = MongoConnection('dolar')
            collection = mongo.get_collection('cotacao')
            return collection
        except Exception:
            raise Exception
