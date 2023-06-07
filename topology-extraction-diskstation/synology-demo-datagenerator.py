"""
This is part of the 'Synology Diskstation' demo that shows how to ingest dimensional metric data into Dynatrace
and automatically extract a vertical topology by using topology definition rules.
"""
import requests, time, sched, random, datetime

# Enter your target Dynatrace environment and API token (with APIv2 ingest metrics scope) here. 
YOUR_DT_API_URL = 'https://xxx.live.dynatrace.com'
YOUR_DT_API_TOKEN = 'yourtoken'

# You can change the values below to vary the example Synology Diskstation properties 		
host = "synologyhost-1"
ip = "192.168.0.198"
serialnumber = "1920PCN690411"
sysname = "storage-2"

# Now the metric template is loaded and replaced with simulated metric values in a loop
with open('metric-template.txt') as f:
    metric_template = f.read()
    metric_template = metric_template.replace("#host#", host)
    metric_template = metric_template.replace("#ip#", ip)
    metric_template = metric_template.replace("#serialnumber#", serialnumber)
    metric_template = metric_template.replace("#sysname#", sysname)
    while(True):
        cpu_user = random.randint(1,50)
        cpu_system = random.randint(1,20)
        cpu_idle = 100 - cpu_user
        mem_available = random.randint(100000,150000)
        metric_data = metric_template.replace("#cpu_user#", str(cpu_user))
        metric_data = metric_data.replace("#cpu_system#", str(cpu_system))
        metric_data = metric_data.replace("#cpu_idle#", str(cpu_idle))
        metric_data = metric_data.replace("#mem_available#", str(mem_available))
        r = requests.post(YOUR_DT_API_URL + '/api/v2/metrics/ingest', headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN}, data=metric_data)
        print(r)
        print(r.text)
        time.sleep(60)
