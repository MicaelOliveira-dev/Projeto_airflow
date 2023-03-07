from airflow.models import DAG
from airflow.utils.dates import datetime, timedelta
from airflow.operators.python import PythonOperator
from server.config.db import MongoConnection

def get_connection():
    try:
        mongo_connection = MongoConnection('dolar')
        return mongo_connection.get_connection()
    except Exception:
        raise Exception

with DAG(
        'meu_primeiro_dag',
        start_date=datetime(2023,3,6),
        schedule_interval=timedelta(minutes=1)
) as dag:

    task = PythonOperator(
        task_id='Executando',
        python_callable = get_connection()
    )

    task