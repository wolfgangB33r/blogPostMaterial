# Imports the Google Cloud client library
from google.cloud import storage
import os  
import sys

# Locate your Google Cloud ADC credential JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=".../gcp/application_default_credentials.json"

def upload(project, bucket, blobname, data):
    print("upload")
    # Initialize the client by specifying your Google GCP project id
    storage_client = storage.Client(project=project)

    # Opens the existing bucket
    bucket = storage_client.bucket(bucket)

    blob = bucket.blob(blobname)

    with blob.open("w") as f:
        f.write(data)

    print(f"Data stored in bucket: {bucket.name}.")

def load(project, bucket, blobname):
    print("load")
    # Initialize the client by specifying your Google GCP project id
    storage_client = storage.Client(project=project)

    bucket = storage_client.bucket(bucket)

    blob = bucket.blob(blobname)

    with blob.open("r") as f:
        print(f.read())

upload("myplayground-3", "train-data-22342343242", "train.csv", "test, test, test")

load("myplayground-3", "train-data-22342343242", "train.csv")
