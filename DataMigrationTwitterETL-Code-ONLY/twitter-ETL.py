import tweepy
# for connection to google biqQ later pip install --upgrade google-cloud-bigquery
# https://cloud.google.com/bigquery/docs/reference/libraries#client-libraries-install-python
import json
import csv
import config
import os
import time
import multiprocessing

from google.cloud import bigquery, storage

storage_client = storage.Client.from_service_account_json(json_credentials_path=config.STORAGE_KEY_PATH,project=config.PROJECT_ID)
bucket = storage_client.get_bucket(config.BUCKET_NAME)

class StreamListener(tweepy.StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        super(StreamListener, self).__init__()


    def on_status(self, status):

        if status.retweeted:
            return

        loc = status.user.location
        # The user's location (status.user.location). This is the location the user who created the tweet wrote in their biography.
        text = status.text
        # the text of the tweet
        geo = status.geo

        name = status.user.screen_name
        # The screen name of the user (status.user.screen_name).
        user_created = status.user.created_at
        # When the user's account was created (status.user.created_at).
        followers = status.user.followers_count
        # How many followers the user has (status.user.followers_count).
        id_str = status.id_str

        created = status.created_at
        # When the tweet was sent (status.created_at).
        retweets = status.retweet_count
        # numer of retweets

        if geo is not None:
            geo = json.dumps(geo)

        # print(loc, text, geo, name, user_created, followers, id_str, created, retweets )
        print(text)
        # here we need to connect to database and store tweets line by line
        line = [name, text.encode('utf-8'), created]
        with open(config.CSV_NAME, 'a') as f:
            line_writer = csv.writer(f, dialect='unix')
            line_writer.writerow(line)

        if (time.time() - self.start_time) < self.limit:
            return True
        else:
            return False
        # create method for table creation

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


def send_to_GCS(csv):
    blob = bucket.blob(csv)
    blob.upload_from_filename('C://Users/709231/PycharmProjects/DataMigrationProjectGCP/'+csv)
print('File {} uploaded to {}.'.format(csv,config.BUCKET_NAME))

if __name__ == '__main__':

    os.system('')
    auth = tweepy.OAuthHandler(config.TWITTER_APP_KEY, config.TWITTER_APP_SECRET)
    auth.set_access_token(config.TWITTER_KEY, config.TWITTER_SECRET)
    api = tweepy.API(auth)


    stream_listener = StreamListener(time_limit=30)
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=config.TRACK_TERMS)
    send_to_GCS(config.CSV_NAME)
    #os.system('gsutil cp '+config.CSV_NAME+ 'gs://'+config.BUCKET_NAME+'/Source/')