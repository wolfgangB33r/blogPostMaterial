import json
import os
import requests

# Those two environment variables must be present
if 'OTEL_EXPORTER_OTLP_TRACES_ENDPOINT' not in os.environ:
    print("Environment variable OTEL_EXPORTER_OTLP_TRACES_ENDPOINT is missing!")
    
if 'OTEL_EXPORTER_OTLP_TRACES_HEADERS' not in os.environ:
    print("Environment variable OTEL_EXPORTER_OTLP_TRACES_HEADERS is missing!")

from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter,
)

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter
)

from opentelemetry.sdk.resources import Resource

from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

trace_provider = TracerProvider(resource=Resource.create({"service.name": "client"}),)

# Sets the global default tracer provider
trace.set_tracer_provider(trace_provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer(__name__)

# Processor for console export
processor = BatchSpanProcessor(ConsoleSpanExporter())
trace_provider.add_span_processor(processor)

# Processor for OTLP span export to Dynatrace or any other receiver
span_exporter = OTLPSpanExporter()

span_processor = BatchSpanProcessor(span_exporter)
trace_provider.add_span_processor(span_processor)

prop = TraceContextTextMapPropagator()
carrier = {}

with tracer.start_as_current_span("pythonclientprompt") as child:
    child.set_attribute("test.count.value", 99)
    child.set_attribute("operation.name", "client_prompt")

    # Attach the span context to the outgoing HTTP request
   
    prop.inject(carrier=carrier)

    # A GET request to the API
    response = requests.get("https://bookadvisor.smartlab.at/api/v1/completion?prompt=similar+to+novel+by+daniel+suarez&lang=en-US", headers=carrier)
    # Print the response
    response_json = response.json()
    print(response_json)


