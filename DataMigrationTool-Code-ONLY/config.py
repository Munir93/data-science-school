


# Giving access to use client library
#for the purpose of migration user needs to be granted the following access levels
# bigquery.admin and storage.objectViewer

ACCOUNT_NAME = 'munirs_account'

PROJECT_ID ='warm-airline-207713'

KEY_PATH = 'C://Users/709231/Desktop/authkey1.json'

#creating dataset

DATASET = 'test_dataset'

#google cloud storage info

BUCKET_NAME = 'dod-mwja-project1'

STORAGE_KEY_PATH = 'C://Users/709231/Desktop/storage_key.json'

#loading from gcs to big q

#can create function to auto genrate list of files directly from bucket using list blobs method
#ALL_files =
LIST_OF_FILES = ['SampleCSVFile_119kb.csv', 'SampleCSVFile_556kb.csv', 'sample_with_headers.csv', 'blaaah',]

#header available = yes/no





