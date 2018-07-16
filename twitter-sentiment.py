from googleapiclient import discovery
from google.cloud import bigquery

#client = bigquery.Client.from_service_account_json(json_credentials_path=config.KEY_PATH,project=config.PROJECT_ID)
#dataset_id = config.DATASET
#dataset_ref = client.dataset(dataset_id, project=config.PROJECT_ID)

client = bigquery.Client()
dataset_ref = client.dataset('test_dataset', 'warm-airline-207713')

datasets = client.list_datasets()
list_of_datasets = []

for dataset in datasets:
    list_of_datasets.append(dataset.dataset_id)

print(list_of_datasets)

job_config = bigquery.LoadJobConfig()

job_config.autodetect = True

uri = 'gs://dod-mwja-project1/Tweets2018_07_12_17_21_16.csv'
table_name = 'pleasework'

load_job = client.load_table_from_uri(
        source_uris=uri,destination=dataset_ref.table(table_name),job_config=job_config)


