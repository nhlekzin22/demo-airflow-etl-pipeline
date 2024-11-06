from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from getData import extractData

default_args = {
    'owner': 'Blessing',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 6),
    'email': ['nhlakaniphoblessing16@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'getData_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_getData_etl',
    python_callable=extractData,
    dag=dag, 
)

run_etl