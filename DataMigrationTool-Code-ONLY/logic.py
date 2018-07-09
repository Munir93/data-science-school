from google.cloud import bigquery, storage
import config as config
import logging

storage_client = storage.Client.from_service_account_json(json_credentials_path=config.STORAGE_KEY_PATH,project=config.PROJECT_ID)
bucket = storage_client.get_bucket(config.BUCKET_NAME)

client = bigquery.Client.from_service_account_json(json_credentials_path=config.KEY_PATH,project=config.PROJECT_ID)
dataset_id = config.DATASET
dataset_ref = client.dataset(dataset_id, project='warm-airline-207713')


#blob = bucket.blob('DOD-GCP-MIGRATION-TOOL')
#blob.upload_from_filename('C://Users/709231/PycharmProjects/DataMigrationProjectGCP')


#logging.basicConfig(filename='testlogs.log',level=logging.DEBUG)
#logging.debug('this is my first log')