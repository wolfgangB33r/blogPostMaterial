"""
This is part of the 'Freetrace' demo example that shows how to ingest dimensional metric data and automatically extract a 
vertical and horizontal topology by using topology definition rules.
"""
import requests, time, sched, random, datetime

YOUR_DT_API_URL = 'https://xxx.live.dynatrace.com'
YOUR_DT_API_TOKEN = 'YOUR-APIv2-TOKEN-WITH-METRIC-INGEST-SCOPE'
		
# The map of all simulated service (instances)
services = {
    "webserver" : { "service" : "webserver", "ip" : "52.18.160.10", "port" : 80, "tech" : "tomcat", "processname" : "tomcat.exe", "jar" : "com.dynatrace.easytravel.pluginservice.jar", "path" : "\"/home/labuser/easytravel-*-x*/jre/bin/java, /home/labuser/easytravel-2.0.0-x64/jre/bin/java\"" },
    "authenticationService" : { "service" : "authenticationService", "ip" : "52.18.160.20", "port" : 8080, "tech" : "jetty", "processname" : "java"  },
    "paymentService" : { "service" : "paymentService", "ip" : "52.18.160.30", "port" : 9000, "tech" : "golang", "processname" : "payment.exe" },
    "bookingService" : { "service" : "bookingService", "ip" : "52.18.160.40", "port" : 8000, "tech" : "java", "processname" : "java" },
    "databaseService1" : { "service" : "databaseService", "ip" : "52.18.160.50", "port" : 7000, "tech" : "oracle", "processname" : "oracle.exe" },
    "databaseService2" : { "service" : "databaseService", "ip" : "52.18.160.51", "port" : 7000, "tech" : "oracle", "processname" : "oracle.exe" }
}

# The call tree
calls = [
    { "caller" : "webserver", "callee" : "bookingService", "min" : 3000, "max" : 4500, "calls" : 2 },
    { "caller" : "bookingService", "callee" : "authenticationService", "min" : 20, "max" : 40, "calls" : 1 },
    { "caller" : "bookingService", "callee" : "paymentService", "min" : 100, "max" : 500, "calls" : 1 },
    { "caller" : "paymentService", "callee" : "databaseService1", "min" : 200, "max" : 400, "calls" : 10 },
    { "caller" : "bookingService", "callee" : "databaseService2", "min" : 200, "max" : 400, "calls" : 7 }
]

payload = ""
for call in calls:
    caller = call['caller']
    callerAttributes = ""
    for key in services[call['caller']]:
        callerAttributes += "cl_" + key + "=" + str(services[call['caller']][key]) + ","
    callee = call['callee']
    calleeAttributes = ""
    for key in services[call['callee']]:
        calleeAttributes += "srv_" + key + "=" + str(services[call['callee']][key]) + ","
    responsetime = str(random.randint(call['min'],call['max']))
    callcount = call['calls']
    
    payload += "demo.service.responsetime," + callerAttributes + calleeAttributes + "response_code=200 " + str(responsetime) + "\n"
    payload += "demo.service.requestcount," + callerAttributes + calleeAttributes + "response_code=200 " + str(callcount) +"\n"
    

print(payload)
r = requests.post(YOUR_DT_API_URL + '/api/v2/metrics/ingest', headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + YOUR_DT_API_TOKEN}, data=payload)
print(r)
print(r.text)
