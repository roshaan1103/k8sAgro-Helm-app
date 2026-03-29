from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

# Example metric: count total requests per endpoint
REQUEST_COUNTER = Counter("requests_total", "Total HTTP requests", ["endpoint"])

@app.get("/")
def read_root():
    REQUEST_COUNTER.labels(endpoint="/").inc()
    return {"message": "Hello from AIops App!, Checking the status"}

# Prometheus metrics endpoint
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
