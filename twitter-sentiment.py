from googleapiclient import discovery
from google.cloud import bigquery

#client = bigquery.Client.from_service_account_json(json_credentials_path=config.KEY_PATH,project=config.PROJECT_ID)
#dataset_id = config.DATASET
#dataset_ref = client.dataset(dataset_id, project=config.PROJECT_ID)

client = bigquery.Client()

datasets = client.list_datasets()
list_of_datasets = []

for dataset in datasets:
    list_of_datasets.append(dataset.dataset_id)

print(list_of_datasets)