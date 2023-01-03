"""
Example script that reports the hosts uptime in seconds to a given host.
"""
import requests, time, sched, random, datetime
from uptime import uptime

YOUR_DT_API_URL = 'YOUR_DT_ENV'
YOUR_DT_API_TOKEN = 'YOUR_API_TOKEN_SECRET'

payload = "host.system.uptime,dt.entity.host=HOST-44FBD6A68DFEF57E " + str(int(uptime()))
# uptime in seconds
print(payload)
r = requests.post(YOUR_DT_API_URL + '/api/v2/metrics/ingest', headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN}, data=payload)
print(r)
print(r.text)

