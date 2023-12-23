import weaviate
import json
import requests
import os

WEAVIATE_ENDPOINT = 'http://192.168.0.110:8080' # Replace with your endpoint

client = weaviate.Client(
    url = WEAVIATE_ENDPOINT,  
)

client.schema.delete_class("Travel")

class_obj = {
    "class": "Travel",
    "vectorizer": "none",  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
    "moduleConfig": {
        
    }
}

if not client.schema.exists('Travel'): # Creates a class of 'Question', if it does not already exist
    # Create class
    client.schema.create_class(class_obj) 
    # Load a tiny jeopardy question sample set
    resp = requests.get('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json')
    data = json.loads(resp.text)  # Load data

    client.batch.configure(batch_size=100)  # Configure batch
    with client.batch as batch:  # Initialize a batch process
        for i, d in enumerate(data):  # Batch import data
            print(f"importing travel destinations: {i+1}")
            properties = {
                "destination": d["destination"],
                "advise": d["advise"]
            }
            batch.add_data_object(
                data_object=properties,
                class_name="Travel",
                vector=d["vector"]
            )

# Start a query
response = (
    client.query
    .get("Travel", ["destination", "advise"])
    .with_near_text({"destination": ["Vienna"]})
    .with_limit(2)
    .do()
)

print(json.dumps(response, indent=4))