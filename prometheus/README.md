# Prometheus Metric Simulator and Alerting Test

Generates a large number of service related timeseries with a simple simulator. A generator script is used to create a huge number of alerting rule configs.

```bash
nohup python3 /home/ec2-user/promsim/promsim.py &
./prometheus --config.file=./prometheus.yml --web.listen-address=:8080 &
```
