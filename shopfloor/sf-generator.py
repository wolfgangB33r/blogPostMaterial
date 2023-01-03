"""
Example script for generating shop floor machinery telemetry data
"""
import requests, time, sched, random, datetime

YOUR_DT_API_URL = 'YOUR_ENV_URL'
YOUR_DT_API_TOKEN = 'YOUR_TOKEN'

METRICS = [
    # Simulates two material silos, for one extrusion line 
    {'id' : 'silo.material.level', 'dims' : {'factory' : 'GF-23', 'line' : 'EXTRUSION-5', 'cell' : 'C-1', 'machine' : 'Silo-C-1-S-1'}, 'min' : 70, 'max' : 70 },
    {'id' : 'silo.material.temperature', 'dims' : {'factory' : 'GF-23', 'line' : 'EXTRUSION-5', 'cell' : 'C-1', 'machine' : 'Silo-C-1-S-1'}, 'min' : 25, 'max' : 27 },
    {'id' : 'silo.material.level', 'dims' : {'factory' : 'GF-23', 'line' : 'EXTRUSION-5', 'cell' : 'C-1', 'machine' : 'Silo-C-1-S-2'}, 'min' : 10, 'max' : 80 },
    {'id' : 'silo.material.temperature', 'dims' : {'factory' : 'GF-23', 'line' : 'EXTRUSION-5', 'cell' : 'C-1', 'machine' : 'Silo-C-1-S-2'}, 'min' : 30, 'max' : 30 }
    # 
]

scheduler = sched.scheduler(time.time, time.sleep)

def genSeries():
    mStr = ""
    for metric in METRICS:
        dimStr = ""
        for dK in metric['dims']:
            dimStr += "," + dK + "=" + metric['dims'][dK]
        mStr += metric['id'] + dimStr + " " + str(random.randint(metric['min'], metric['max'])) + "\n"
    return mStr


def doit():
    scheduler.enter(60, 1, doit)
    payload = genSeries()
    print(payload)
    r = requests.post(YOUR_DT_API_URL + '/api/v2/metrics/ingest', headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN}, data=payload)
    print(r)
    print(r.text)

print("START")
scheduler.enter(1, 1, doit)
scheduler.run()
