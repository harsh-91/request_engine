class RequestManager:
    def __init__(self, config, proxy_mgr, tls_mod, engine, classifier, logger, metrics):
        self.config = config
        self.proxy_mgr = proxy_mgr
        self.tls_mod = tls_mod
        self.engine = engine
        self.classifier = classifier
        self.logger = logger
        self.metrics = metrics

    async def run_once(self):
        for url in self.config.get("targets", []):
            proxy = self.proxy_mgr.rotate_proxy() if self.proxy_mgr else None
            tls_profile = self.tls_mod.select_profile() if self.tls_mod else None

            self.logger.log_request(url, proxy, tls_profile)
            response = await self.engine.make_request(url, proxy, tls_profile)

            if response:
                classification = self.classifier.classify(response)
                print(f"{url} → {response.status_code} → {classification}")
                self.logger.log_response(url, response.status_code, classification)

                if classification == "SUCCESS":
                    self.metrics.increment_success()
                else:
                    self.metrics.increment_failure()
            else:
                print(f"{url} → ❌ Request failed")
                self.metrics.increment_failure()
