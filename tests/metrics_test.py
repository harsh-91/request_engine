from prometheus_client import Counter, start_http_server
import time

success_counter = Counter("requests_success_total", "Total successful requests")

if __name__ == "__main__":
    print("🚀 Starting Prometheus server on port 8000...")
    start_http_server(8000)
    while True:
        success_counter.inc()
        time.sleep(5)
