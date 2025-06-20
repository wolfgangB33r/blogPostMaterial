'''
    Example that fetches a Davis detected problem from a given Dynatrace tenant by using the Grail Platform Storage service and then
    calls Davis CoPilot to summarize the given problem text.

    Steps:
    1. Create an OAuth client in Dynatrace Account Management / Identity & Access Management with the following access scopes:
        davis-copilot:conversations:execute davis-copilot:nl2dql:execute storage:logs:read storage:events:read storage:metrics:read storage:bucket-definitions:read storage:buckets:read'
    2. Set the following environment variables through a .env file:
        DYNATRACE_TENANT="********"
        OAUTH_CLIENT_ID="***"
        OAUTH_ACCOUNT_ARN="***"
        OAUTH_CLIENT_SECRET="***"

    @author: Wolfgang Beer
    @date: 05/14/2025
'''

import requests
import json
import urllib.parse
from dotenv import load_dotenv
load_dotenv()
import os

TENANT = os.environ.get("DYNATRACE_TENANT")
# OAUTH
OAUTH_CLIENT_ID = os.environ.get("OAUTH_CLIENT_ID")
OAUTH_ACCOUNT_ARN = os.environ.get("OAUTH_ACCOUNT_ARN")
OAUTH_CLIENT_SECRET = os.environ.get("OAUTH_CLIENT_SECRET")
# Use-case endpoints
DT_AI_CONVERSATION_SKILL = "/platform/davis/copilot/v0.2/skills/conversations:message"
DT_AI_NL2DQL_SKILL = "/platform/davis/copilot/v0.2/skills/nl2dql:generate"

STORAGE_SERVICE_ENDPOINT = "/platform/storage/query/v1/query:execute?enrich=metric-metadata"
CONVERSATION_URL = f"https://{TENANT}.apps.dynatrace.com/{DT_AI_CONVERSATION_SKILL}"
NL2DQL_URL = f"https://{TENANT}.apps.dynatrace.com/{DT_AI_NL2DQL_SKILL}"

# Necessary permission scopes for the use-case example
PERMISSION_SCOPES = 'davis-copilot:conversations:execute davis-copilot:nl2dql:execute storage:logs:read storage:events:read storage:metrics:read storage:bucket-definitions:read storage:buckets:read'

def get_oauth_token():
    # Replace these values with your OAuth provider's details
    client_id = OAUTH_CLIENT_ID
    client_secret = OAUTH_CLIENT_SECRET
    token_url = 'https://sso.dynatrace.com/sso/oauth2/token'
    account_arn = OAUTH_ACCOUNT_ARN
    scopes = PERMISSION_SCOPES
    sso_request = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scopes,
        'resource': account_arn
    }
    response = requests.post(token_url, data=urllib.parse.urlencode(sso_request), headers={
        'Content-Type': 'application/x-www-form-urlencoded'
        })
    # Print the response from the server
    # print(response.status_code)
    # print(response.text)
    if response.status_code == 200:
        return response.json()['access_token']
    
    return ""

def fetchProblem(token):
    url = 'https://{tenant}.apps.dynatrace.com{storage_service_endpoint}'.format(tenant=TENANT, storage_service_endpoint=STORAGE_SERVICE_ENDPOINT)
    # Data to be sent in the JSON payload
    data = {
        "query": "fetch dt.davis.problems, from:Now()-15d, to:Now() | limit 1",
        "defaultTimeframeStart": "2022-04-20T12:10:04.123Z",
        "defaultTimeframeEnd": "2022-04-20T13:10:04.123Z",
        "timezone": "UTC",
        "locale": "en_US",
        "maxResultRecords": 1000,
        "maxResultBytes": 1000000,
        "fetchTimeoutSeconds": 60,
        "requestTimeoutMilliseconds": 1000,
        "enablePreview": True,
        "defaultSamplingRatio": 1000,
        "defaultScanLimitGbytes": 100,
        "queryOptions": None,
        "filterSegments": None
    }

    # Convert the data to a JSON string
    json_data = json.dumps(data)

    # Send the POST request
    response = requests.post(url, data=json_data, headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
        })

    if response.status_code != 200:
        # Print the response from the server
        print(response.status_code)
        print(response.text)
    
    if response.json()["state"] == "SUCCEEDED":
        return response.json()["result"]["records"]

def summarizeProblem(token, text):
    request={
            "text": "Summarize the Dynatrace detected problem",
            "context": [
                {"type": "document-retrieval", "value": "dynatrace"},
                {"type": "supplementary", "value": text},
            ],
        }
    # do the request
    response = requests.post(
        CONVERSATION_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        json=request,
    )

    if response.status_code == 200:
        # process the response
        result = response.json()
        answer = result["text"]
        if sources := result["metadata"].get("sources"):
            print("The following sources were used:")
            print(json.dumps(sources, indent=4))
        return answer
    else:
        print(response.content)
        print("Error", response)


def generateDQL(token, question):
    request={
            "text": question,
            "context": [
                {"type": "document-retrieval", "value": "disabled"}
            ],
        }
    # do the request
    response = requests.post(
        NL2DQL_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        },
        json=request,
    )

    if response.status_code == 200:
        # process the response
        result = response.json()
        answer = result["dql"]
        if sources := result["metadata"].get("sources"):
            print("The following sources were used:")
            print(json.dumps(sources, indent=4))
        return answer
    else:
        print(response.content)
        print("Error", response)

def main():
    token = get_oauth_token()
    problems = fetchProblem(token)
    # Summarize a single problem description
    summary = summarizeProblem(token, problems[0]['event.description'])
    print(summary)
    dql = generateDQL(token, "Count number of problems in the last 24h")
    print(dql)


if __name__ == "__main__":
    main()
    
