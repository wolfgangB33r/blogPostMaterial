"""
Example script
"""
import requests, time, sched, random, datetime

YOUR_DT_API_URL = 'YOUR_ENV_URL'
YOUR_DT_API_TOKEN = 'YOUR_TOKEN'

METRICS = [
    {'id' : 'batchjobs.execution.successes', 'dims' : {'dt.entity.host' : 'HOST-123', 'jobname' : 'payslip'}, 'min' : 10, 'max' : 80 },
    {'id' : 'batchjobs.execution.fails', 'dims' : {'dt.entity.host' : 'HOST-123', 'jobname' : 'payslip'}, 'min' : 0, 'max' : 2 }
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
