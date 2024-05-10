from files.gcp_utils import storage
import logging

def save_file(file_path,bucket):

    logging.info('save task')
    storage.GCS().save_file(file_path, file_path.split('/')[-1], bucket)
    logging.info('after save to gcs')
