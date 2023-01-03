"""
Example script for service version clustering simulation
Use it in a one-minute cron-job
"""
import requests, random, datetime

YOUR_DT_API_URL = ''
YOUR_DT_API_TOKEN = ''

METRICS = [
    {'id' : 'test.service.responsetime', 'dims' : { 'service' : 'payment', 'instance' : 'pgi-1', 'version' : 'v-1.0' }, 'min' : 20, 'max' : 30 },
    {'id' : 'test.service.responsetime', 'dims' : { 'service' : 'payment', 'instance' : 'pgi-2', 'version' : 'v-1.0' }, 'min' : 23, 'max' : 33 },
    {'id' : 'test.service.responsetime', 'dims' : { 'service' : 'payment', 'instance' : 'pgi-3', 'version' : 'v-1.0' }, 'min' : 25, 'max' : 29 },
#   {'id' : 'test.service.responsetime', 'dims' : { 'service' : 'payment', 'instance' : 'pgi-4', 'version' : 'v-2.0' }, 'min' : 30, 'max' : 40 }, 
    {'id' : 'test.service.responsetime', 'dims' : { 'service' : 'sso', 'instance' : 'pgi-1', 'version' : 'v-5.5.4' }, 'min' : 90, 'max' : 100 },
    {'id' : 'test.service.responsetime', 'dims' : { 'service' : 'sso', 'instance' : 'pgi-2', 'version' : 'v-5.5.3' }, 'min' : 90, 'max' : 100 },
#   {'id' : 'test.service.responsetime', 'dims' : { 'service' : 'sso', 'instance' : 'pgi-3', 'version' : 'v-6.1' }, 'min' : 50, 'max' : 100 }, 
]

def genSeries():
    mStr = ""
    for metric in METRICS:
        dimStr = ""
        for dK in metric['dims']:
            dimStr += "," + dK + "=" + metric['dims'][dK]
        mStr += metric['id'] + dimStr + " " + str(random.randint(metric['min'], metric['max'])) + "\n"
    return mStr

payload = genSeries()
r = requests.post(YOUR_DT_API_URL + '/api/v2/metrics/ingest', headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN}, data=payload)
print(r)
print(r.text)