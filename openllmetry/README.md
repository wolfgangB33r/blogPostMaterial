# Example for observing your OpenAI LLM model with Traceloop, OpenLLMetry and Dynatrace

### Install Traceloop sdk

```console
pip install traceloop-sdk
```

### Configure Traceloop to export to Dynatrace

Export the collected traces by setting the below environment variables.

The Dynatrace Access Token needs the following permission scopes: openTelemetryTrace.ingest, metrics.ingest, logs.ingest

```console
export TRACELOOP_BASE_URL=https://<YOUR_TENANT>.live.dynatrace.com/api/v2/otlp
export TRACELOOP_HEADERS=Authorization=Api-Token%20<YOUR_DYNATRACE_ACCESS_TOKEN>
```
