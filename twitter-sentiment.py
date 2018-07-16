from googleapiclient import discovery
from google.cloud import bigquery

#client = bigquery.Client.from_service_account_json(json_credentials_path=config.KEY_PATH,project=config.PROJECT_ID)
#dataset_id = config.DATASET
#dataset_ref = client.dataset(dataset_id, project=config.PROJECT_ID)


client1 = bigquery.Client()
list1 = client1.list_dataset_tables('test_dataset')
print(list1)