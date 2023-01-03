"""
Simulation of disk capacity metrics that fill up over the period of a month and then resets back to a given level.
This simulated metrics are used to test and demo capacity prediction and forecasts.
"""
import requests, time, sched, random, datetime

from secret import *

def genSeries():
    now = datetime.datetime.now()
    day_num = int(now.strftime("%d"))
    # decreases the level day by day a bit until end of each month, then resets back.
    level_1 = 75 - day_num
    level_2 = 30 - day_num
    # Free disk space in percent
    mStr = "host.disk.free,hostname=prod-useast-01,diskname=c " + str(level_1 + random.randint(0, 5)) + "\n"
    mStr += "host.disk.free,hostname=prod-useast-01,diskname=mnt " + str(10) + "\n"
    mStr += "host.disk.free,hostname=prod-sydney-05,diskname=/ " + str(level_2 + random.randint(0, 3)) + "\n"
    mStr += "host.disk.free,hostname=prod-sydney-05,diskname=/root " + str(40) + "\n"
    return mStr

payload = genSeries()
print(payload)
r = requests.post(YOUR_DT_API_URL + '/api/v2/metrics/ingest', headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN}, data=payload)
print(r)
print(r.text)
