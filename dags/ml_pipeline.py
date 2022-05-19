
from airflow.models import DAG

from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup

from datetime import datetime

from utils.load_data import load_data
from utils.preprocess_data import preprocess_data
from utils.train_model import train_model
from utils.calculate_result import calculate_result

default_args= {
    'owner': 'Olga Kravchenko',
    'email_on_failure': False,
    'email': ['olga.kravchenko@prophecylabs.com'],
    'start_date': datetime(2022, 1, 1)
}

with DAG(
    "ml_pipeline",
    description='End-to-end ML pipeline example',
    schedule_interval='@daily',
    default_args=default_args, 
    catchup=False) as dag:

    #load data
    load_data_task = PythonOperator(task_id = 'reading_input_data',
    							python_callable = load_data)

    #preprocess data
    preprocess_data_task = PythonOperator(task_id = 'preprocess_input_data',
    								 python_callable = preprocess_data)


    # #train two models
    with TaskGroup('training_models') as train_models:

    	train_first_model = PythonOperator(task_id = 'training_first_model',
    										python_callable = train_model,
    										op_kwargs = {'alpha':'0.1'})

    	train_second_model = PythonOperator(task_id = 'training_second_model',
    										python_callable = train_model,
    										op_kwargs = {'alpha':'0.01'})


    # #calculate final prediction
    calculate_result_task = PythonOperator(task_id = 'calculate_results',
    									python_callable = calculate_result)


    load_data_task >> preprocess_data_task >> train_models >> calculate_result_task

    