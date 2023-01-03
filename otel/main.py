# pip install opentelemetry-api
# pip install opentelemetry-sdk
# pip install opentelemetry-exporter-otlp-proto-http
# pip install opentelemetry-instrumentation-wsgi
# python3 oteltest.py & disown
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.propagate import extract
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
import http.server
import json

resource = Resource(attributes={
    "service.name": "python-otel-service"
})

trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(
    endpoint="https://<YOUR>.live.dynatrace.com/api/v2/otlp/v1/traces", 
    headers={"Authorization" : "Api-Token <YOUR>"},
)

span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

class Handler(http.server.SimpleHTTPRequestHandler) :
    def do_GET(self) :
        with tracer.start_as_current_span("calcRecommendation", context=extract(self.headers), kind=trace.SpanKind.SERVER):
            with tracer.start_as_current_span("train"):
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Hello, world!')

s = http.server.HTTPServer( ('', 9090), Handler )
s.serve_forever()


