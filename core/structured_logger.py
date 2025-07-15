from loguru import logger
import json
from datetime import datetime

class StructuredLogger:
    def __init__(self, logfile: str = "logs.jsonl"):
        logger.add(logfile, format="{message}", rotation="500 KB", serialize=True)

    def log_request(self, url: str, proxy: str, tls_profile: str):
        logger.info({
            "timestamp": datetime.utcnow().isoformat(),
            "event": "request_sent",
            "url": url,
            "proxy": proxy,
            "tls_profile": tls_profile
        })

    def log_response(self, url: str, status_code: int, classification: str):
        logger.info({
            "timestamp": datetime.utcnow().isoformat(),
            "event": "response_received",
            "url": url,
            "status_code": status_code,
            "classification": classification
        })
