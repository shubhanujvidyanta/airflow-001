import logging

def transform_task(ti):
    logging.info("transform task")
    logging.info(ti.xcom_pull(task_ids='read_task'))