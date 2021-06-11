# Freetrace topology extraction example

This self-contained example explains how to set up topology extraction configurations in order to automatically extract vertical and horizontal topology 
through a multi-dimensional metric data stream.
This example contains:
- A load generator that sends two metrics (demo.service.requestcount and demo.service.responsetime)
- A Dynatrace extension 2.0 yaml file that contains all necessary declarative extraction rules to generate a dynamic service topology, as it is shown below. 

## Load generator

A self-contained Python script that sends two metrics with random mesurements into a Dynatrace monitoring environment. Schedule this load generator to run every minute by using a cron-job to receive a 
continous random metric stream.

See below an example of the raw dimensional metric line protocol that the load generator generates and sends every minute:

demo.service.requestcount,cl_service=bookingService,cl_ip=52.18.160.40,cl_port=8000,cl_tech=java,cl_processname=java,srv_service=databaseService,srv_ip=52.18.160.51,srv_port=7000,srv_tech=oracle,srv_processname=oracle.exe,response_code=200 7
