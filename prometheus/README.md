# Prometheus Metric Simulator and Alerting Test

Generates a large number of service related timeseries with a simple simulator. A generator script is used to create a huge number of alerting rule configs.

```bash
nohup python3 /home/ec2-user/promsim/promsim.py &
./prometheus --config.file=./prometheus.yml --web.listen-address=:8080 &
```

## Some notes about scaleout

* 1-3 KB of memory per active series
* 1-3 KB disk per series per scrape, where scrape interval can be configured
* 8-16 CPU cores suggested for around 1M series

## Alerting

* Evaluation period can be configured globally
* Individual alerting rule can override the evaluation period
* Evaluates in bulks on a scalar series rollup
* Can be organized as alert groups with shared Alert labels
* Don't have a sliding window like 3/5 but allow the config of 'for' for the min violation period and 'keep_firing_for' to keep the alert in active state for a min amount of time
* Reload of rules through curl -X POST http://localhost:9090/-/reload
* 
