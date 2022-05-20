

'''
This demonstrates the case where DAG/pipeline code has a bug.
The DAG will not appear in Airflow UI, instead you'll get a 
"Broken DAG" notification. To fix the bug, uncomment DAG
import below
'''

# from airflow.models import DAG #uncomment this line to fix bug
from airflow.operators.python import PythonOperator

from datetime import datetime


def hello_world():
    pass

default_args= {
    'owner': 'Olga Kravchenko',
    'email_on_failure': False,
    'email': ['olga.kravchenko@prophecylabs.com'],
    'start_date': datetime(2022, 1, 1)
}

with DAG(
    "broken_dag",
    description='End-to-end ML pipeline example',
    schedule_interval='@daily',
    default_args=default_args, 
    catchup=False) as dag:

    hello_world_task = PythonOperator(task_id = 'hello_world',
    							python_callable = hello_world)