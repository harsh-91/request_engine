Request Engine

A modular Python engine for sending HTTPS requests through rotating proxies with TLS fingerprinting, structured logging, and Prometheus-based observability.

🚀 Features

Rotating Proxies — Avoid IP bans using configurable proxy rotation

TLS Fingerprinting — Simulate browser behavior via header spoofing

Asynchronous Requests — Built with httpx.AsyncClient for speed

Response Classification — Categorize outcomes (Success, Blocked, CAPTCHA, Unknown)

Structured Logging — Log request/response events in JSONL format

Prometheus Metrics — Built-in metrics exposed via HTTP

📁 Project Structure

Request_Engine/
├── config/
│   └── config.yaml            # User-defined config file
├── core/
│   ├── config_loader.py       # YAML loader
│   ├── proxy_manager.py       # Proxy rotation
│   ├── tls_module.py          # TLS header simulation
│   ├── https_engine.py        # Request executor
│   ├── response_classifier.py # Response analyzer
│   ├── structured_logger.py   # Log handler
│   └── metrics_collector.py   # Prometheus metrics
├── logs/
│   └── logs.jsonl             # JSONL log output
├── main.py                    # CLI entrypoint
└── README.md                  # This file

⚙️ Setup

Prerequisites

Python 3.8+

pip

Install Dependencies

pip install -r requirements.txt

🛠️ Configuration

Edit config/config.yaml:

targets:
  - https://httpbin.org/get
  - https://example.com

proxies:
  - http://127.0.0.1:8080
  - http://proxy.example.com:3128

tls_profiles:
  - Chrome_108
  - Firefox_102

🧪 Run the Engine

python main.py

Sample output:

https://httpbin.org/get → 200 → SUCCESS
https://example.com → 403 → BLOCKED

📊 Observability

View Metrics

Start the engine, then:

curl http://localhost:8000/metrics

Exports metrics like:

requests_success_total

requests_failure_total

View Logs

Logs are written to logs/logs.jsonl in JSONL format:

{"timestamp": "2025-07-15T09:12:23.364Z", "event": "request_sent", "url": "https://httpbin.org/get"}

🧩 Extending the Engine

Task

How to Extend

Add new response types

Edit ResponseClassifier logic

Change logging format

Modify StructuredLogger class

Add retry logic

Enhance RequestManager with backoff

Integrate GUI

Hook into main.py using Gradio/Streamlit

🔒 Security Notes

No credentials are hardcoded

Proxy auth is configurable via YAML

TLS spoofing is header-based only (safe fallback)

👤 Author

Built by Harsh Nair — for performance testing, scraping, and observability use cases.

📜 License

MIT License

