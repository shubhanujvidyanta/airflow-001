import requests
import logging

def read_task(url,file_path):


    logging.info("read_task")
    logging.info(url)
    logging.info(file_path)
    logging.info("--------------")

    #  Download the data behind the URL
    response = requests.get(url)
    response.raise_for_status()

    logging.info('after api call')

    import os
    os.rmdir(file_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    logging.info(f'makedir - {os.path.dirname(file_path)}')
    logging.info('after filepath')

    #  Open the response generated into a new file in your local called image.jpg
    with open(file_path, "wb") as file:
        file.write(response.content)

    logging.info('after file save')

    
    return {"file_saved":True, "file_name": file_path}


# url="https://raw.githubusercontent.com/shubhanujvidyanta/airflow-001/main/data/yearly_sales_data-1982.csv"
# file_path="data/temp/yearly_sales_data-1982.csv"
# read_task(url, file_path)

