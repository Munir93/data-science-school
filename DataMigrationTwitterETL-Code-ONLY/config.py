import time
from time import gmtime, strftime

# Giving access to use client library
#for the purpose of migration user needs to be granted the following access levels
# bigquery.admin and storage.objectViewer

#ACCOUNT_NAME = 'munirs_account'

PROJECT_ID ='warm-airline-207713'

KEY_PATH = 'authkey1.json'

#creating dataset

DATASET = 'test_dataset'

#google cloud storage info

BUCKET_NAME = 'dod-mwja-project1'

STORAGE_KEY_PATH = 'storage_key.json'

#loading from gcs to big q

#can create function to auto genrate list of files directly from bucket using list blobs method
#ALL_files =
#LIST_OF_FILES = ['SampleCSVFile_119kb.csv', 'SampleCSVFile_556kb.csv', 'sample_with_headers.csv', 'blaaah',]

#header available = yes/no

#logging

LOGGING_FILENAME = 'DoD-Project1-logs1.log'




'''Twitter ETL start'''

TRACK_TERMS = ["brexit"]

TWITTER_APP_KEY = 'KPVEb25geZ1WUxMrJz3flS6je'
TWITTER_APP_SECRET = 'BcjmYWEJmDuU81gwW3Hs64mnzH4I67EzgS0H5FfuIs7VFjkXtH'
TWITTER_KEY = '1014592058215059456-Z1pGlZHdMvx8vsszkDWpsEdTCjfz4o'
TWITTER_SECRET = 'Zsw17mh9OiXDfaf993njgHhGZHxYTHrrD9Ae8fgqEc1mq'



time = strftime("%Y_%m_%d_%H_%M_%S", gmtime())

CSV_NAME = 'Tweets'+time+'.csv'
