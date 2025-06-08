#import libraries
from airflow.operators.python import PythonOperator # type: ignore
from airflow import DAG
from datetime import timedelta, datetime
from main import extract, transform, load

default_args={
     'owner': 'Cley',
     'start_date': datetime(2025, 6, 6),
     'retries': 1,
     'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='finance',
    default_args=default_args,
    description='Finance',
    schedule='@daily',
)

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

extract_result = extract()

transform_task = PythonOperator(
    task_id='transform',
    python_callable=lambda: transform(extract_result),
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=lambda: load(transform(extract())),
    dag=dag,
)

extract_task >> transform_task >> load_task