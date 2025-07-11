#import libraries
from airflow.operators.python import PythonOperator 
from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import timedelta
from main import extract, transform, load

default_args={
     'owner': 'Cley',
     'start_date': days_ago(1),
     'retries': 1,
     'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='finance_pipeline',
    default_args=default_args,
    description='Finance ETL',
    schedule_interval = "0 6 * * *" # 6:00 AM
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