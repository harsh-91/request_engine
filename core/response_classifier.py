class ResponseClassifier:
    def classify(self, response) -> str:
        if response.status_code in (403, 429):
            return "BLOCKED"
        if self.is_captcha(response):
            return "CAPTCHA"
        if response.status_code == 200:
            return "SUCCESS"
        return f"UNKNOWN ({response.status_code})"

    def is_captcha(self, response) -> bool:
        content = response.text.lower()
        keywords = ["captcha", "verify you are human", "recaptcha", "cloudflare"]
        return any(kw in content for kw in keywords)

    def is_blocked(self, response) -> bool:
        return response.status_code in (403, 429)
