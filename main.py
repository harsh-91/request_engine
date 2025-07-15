import asyncio
from core.config_loader import ConfigLoader
from core.proxy_manager import ProxyManager
from core.tls_fingerprint import TLSFingerprintModule
from core.https_engine import HTTPSRequestEngine
from core.response_classifier import ResponseClassifier
from core.structured_logger import StructuredLogger
from core.metrics_collector import MetricsCollector
from core.request_manager import RequestManager

async def main():
    config = ConfigLoader("config/config.yaml").load_config()

    proxy_mgr = None  # disable proxying temporarily
    #proxy_mgr = ProxyManager(config.get("proxies", []))
    tls_mod = TLSFingerprintModule(config.get("tls_profiles", []))
    engine = HTTPSRequestEngine()
    classifier = ResponseClassifier()
    logger = StructuredLogger()
    metrics = MetricsCollector(port=8000)

    manager = RequestManager(config, proxy_mgr, tls_mod, engine, classifier, logger, metrics)
    await manager.run_once()

    await asyncio.sleep(10)  # Keep server alive for metrics testing

if __name__ == "__main__":
    asyncio.run(main())
