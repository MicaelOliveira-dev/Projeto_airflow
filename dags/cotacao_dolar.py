from airflow.models import DAG
from airflow.utils.dates import datetime, timedelta
from airflow.operators.python import PythonOperator
from server.consultas.scrapping import Cotacao

def cotacao():
    cotacao = Cotacao()
    return cotacao.cotacao_dolar()


with DAG(
        'meu_primeiro_dag',
        start_date=datetime(2023,3,6),
        schedule_interval=timedelta(minutes=1)
) as dag:

    task_one = PythonOperator(
        task_id='executa_codigo',
        python_callable = cotacao
    )

    task_one