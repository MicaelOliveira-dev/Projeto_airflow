from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


def teste():
    print('ola')

default_args = {
    'owner': 'me',
    'start_date': datetime(2023, 3, 7),
    'schedule_interval': timedelta(minutes=1)
}

with DAG('Projeto_cotacao', default_args=default_args) as dag:
    task1 = PythonOperator(
        task_id='task1',
        python_callable=teste
    )

    task1
