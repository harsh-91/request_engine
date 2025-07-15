import httpx
import asyncio

class HTTPSRequestEngine:
    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    async def make_request(self, url: str, proxy: str = None, tls_profile: str = None) -> httpx.Response:
        headers = self.set_headers(tls_profile)
        proxies = {"https://": proxy} if proxy else None

        async with httpx.AsyncClient(headers=headers, proxies=proxies, timeout=self.timeout) as client:
            try:
                response = await client.get(url)
                return response
            except httpx.RequestError as e:
                print(f"❌ Request failed: {e}")
                return None

    def set_headers(self, tls_profile: str) -> dict:
        if tls_profile == "Chrome_108":
            return {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/108.0"}
        elif tls_profile == "Firefox_102":
            return {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}
        else:
            return {"User-Agent": "Python-Client"}
