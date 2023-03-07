from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from server.config.db import MongoConnection
from server.consultas.scrapping import Cotacao


mongo_connection = MongoConnection('dolar')
cotacao = Cotacao()

default_args = {
    'owner': 'me',
    'start_date': datetime(2023, 3, 7),
    'schedule_interval': timedelta(minutes=1)
}

with DAG('cotacao_dolar', default_args=default_args) as dag:
    task1 = PythonOperator(
        task_id='Conexão com Mongo',
        python_callable=mongo_connection.get_connection
    )

    task2 = PythonOperator(
        task_id='Pega Cotação e salva no banco',
        python_callable=cotacao.cotacao_dolar
    )

    task1 >> task2
