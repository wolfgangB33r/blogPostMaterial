from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import aworkflow
import os
import chromadb
import asyncio

Traceloop.init(app_name="chromadb-obs", disable_batch=True)

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

@aworkflow(name="query")
async def queryIt(text):
    results = collection.query(
        query_texts=[text],
        n_results=2
    )
    test = chroma_client.create_collection(name="different_collection")
    print(results)

@aworkflow(name="doit")
async def doit():

    collection.add(
        documents=["This is a document", "This is another document"],
        metadatas=[{"source": "my_source"}, {"source": "my_source"}],
        ids=["id1", "id2"]
    )

    await queryIt("This is a document")

loop = asyncio.get_event_loop()

res = loop.run_until_complete(doit())

loop.close()


