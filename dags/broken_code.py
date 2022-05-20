
'''
This demonstrates the case where DAG/pipeline code is OK
so the DAG will appear in Airflow UI, but the task will
fail id you try to execute it to fix the bug, uncomment
the numpy import below
'''

from airflow.models import DAG 
# import numpy as np #uncomment this to fix bug
from airflow.operators.python import PythonOperator

from datetime import datetime


def hello_numpy():
    var = np.array([1])

default_args= {
    'owner': 'Olga Kravchenko',
    'email_on_failure': False,
    'email': ['olga.kravchenko@prophecylabs.com'],
    'start_date': datetime(2022, 1, 1)
}

with DAG(
    "broken_code",
    description='End-to-end ML pipeline example',
    schedule_interval='@daily',
    default_args=default_args, 
    catchup=False) as dag:

    hello_numpy_task = PythonOperator(task_id = 'hello_numpy',
    							python_callable = hello_numpy)
    