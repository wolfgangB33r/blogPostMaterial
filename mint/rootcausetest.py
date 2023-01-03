"""
Example script
"""
import requests, time, sched, random, datetime

YOUR_DT_API_URL = ['https://??.live.dynatrace.com']
YOUR_DT_API_TOKEN = ['??']

def genSeries():
    metrics = ""
    now = datetime.datetime.now()
    value = random.randint(90,100)
    # ingest a problem pattern
    if now.hour == 7 and now.minute >= 45:
        value = random.randint(0,5)
    
    metrics += "test.fdi.rootcausemetric,dt.entity.service=SERVICE-907DC3F55716BCC9,dt.entity.process_group_instance=PROCESS_GROUP_INSTANCE-D531B99A90A3C030,reason=badcache" + " " + str(value) + "\n"
    metrics += "test.fdi.rootcausemetric,dt.entity.service=SERVICE-907DC3F55716BCC9,dt.entity.process_group_instance=PROCESS_GROUP_INSTANCE-D531B99A90A3C030,reason=goodcache 95\n"
    return metrics

i = 0
payload = genSeries()
print(payload)
for url in YOUR_DT_API_URL:
    r = requests.post(url + '/api/v2/metrics/ingest', headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN[i]}, data=payload)
    print(r)
    print(r.text)
    i = i + 1
