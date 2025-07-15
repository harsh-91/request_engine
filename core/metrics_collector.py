from prometheus_client import Counter, start_http_server, CollectorRegistry

class MetricsCollector:
    def __init__(self, port: int = 8000):
        self.registry = CollectorRegistry()
        self.success_counter = Counter(
            'requests_success_total', 
            'Number of successful requests',
            registry=self.registry
        )
        self.failure_counter = Counter(
            'requests_failure_total', 
            'Number of failed requests',
            registry=self.registry
        )
        start_http_server(port, registry=self.registry)

    def increment_success(self):
        self.success_counter.inc()

    def increment_failure(self):
        self.failure_counter.inc()
