"""
Example script cleaning up given Settings 2.0 namespaces after a configurable period of time.
"""
import requests, time, sched, random, datetime
from datetime import datetime

YOUR_DT_API_URL = 'YOUR_ENV_URL'
YOUR_DT_API_TOKEN = 'YOUR_API_TOKEN' # Dynatrace API token with v2 settings read and write scope activated
NAMESPACES = [ # A list of namespaces that should be automatically cleaned
    'builtin:anomaly-detection.metric-events', 
    'builtin:alerting.profile', 
    'builtin:alerting.maintenance-window', 
    'builtin:problem.notifications'
]
# the number of days a setting entry is kept until its deleted and cleaned up again
KEEP_PERIOD_DAYS = 14 

now = datetime.now().timestamp()
def check(items):
    for item in items:
        if item['modified'] / 1000 < now - (86400 * KEEP_PERIOD_DAYS): # item older than X days, delete it
            dr = requests.delete(YOUR_DT_API_URL + '/api/v2/settings/objects/' + item['objectId'], headers={'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN})
            if dr.status_code == 204:
                print("Successfully removed settings object with id: %s" % (item['objectId']))
        

for ns in NAMESPACES:
    print("Start cleaning up namespace: %s" % (ns))
    count = 0
    r = requests.get(YOUR_DT_API_URL + '/api/v2/settings/objects?fields=objectId,modified&schemaIds=' + ns, headers={'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN})
    if r.status_code == 200: 
        count = count + len(r.json()['items'])
        check(r.json()['items'])  
        while count < r.json()['totalCount']:
            r = requests.get(YOUR_DT_API_URL + '/api/v2/settings/objects?nextPageKey=' + r.json()['nextPageKey'], headers={'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN})
            if r.status_code == 200: 
                count = count + len(r.json()['items'])
                check(r.json()['items'])
            else:
                print("Http error: %d" % (r.status_code))
                break
    else:
        print("Http error: %d" % (r.status_code))