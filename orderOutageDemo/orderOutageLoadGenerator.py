"""
This is part of the 'Order Outage' demo that shows to alert on a situation where the order count metric stops to
count.
"""
import requests, time, sched, random, datetime

# Enter your target Dynatrace environment and API token (with APIv2 ingest metrics scope) here. 
YOUR_DT_API_URL = ''
YOUR_DT_API_TOKEN = ''

metric_template = "business.ordercount 10"
while(True):
    r = requests.post(YOUR_DT_API_URL + '/api/v2/metrics/ingest', headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN}, data=metric_template)
    print(r)
    print(r.text)
    time.sleep(60)
