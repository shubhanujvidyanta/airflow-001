
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.models import Variable
from datetime import datetime
from files.read_csv import read_task
from files.save_csv import save_file
from files.transform_csv import transform_task



dag = DAG('copy_github_to_gcs',
          description='dummy dag to copy files from GitHub to GCS bucket',
        #   default_args=default_args,
          schedule_interval=None,
          # depends_on_past= False,
          start_date=datetime(2024, 3, 4),
          catchup=False,
          )

year = 1982
data = {
    "url":f"https://raw.githubusercontent.com/shubhanujvidyanta/airflow-001/main/data/yearly_sales_data-{year}.csv",
    "bucket":"data-airflow-001",
    "file_path":f"data/temp/yearly_sales_data-{year}.csv"
}

start_task = DummyOperator(task_id='start_task', dag=dag)
end_task = DummyOperator(task_id='end_task', dag=dag)

read_task = PythonOperator(task_id='read_task', python_callable=read_task, provide_context=True, op_kwargs=data, dag=dag)
transform_task = PythonOperator(task_id='transform_task', python_callable=transform_task, provide_context=True, dag=dag)
save_task = PythonOperator(task_id='save_task', python_callable=save_file, provide_context=True, op_kwargs=data, dag=dag)

start_task >> read_task >> transform_task >> save_task >> end_task




