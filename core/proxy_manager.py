import random
from typing import List

class ProxyManager:
    def __init__(self, proxies: List[str]):
        if not proxies:
            raise ValueError("Proxy list cannot be empty.")
        self.proxies = proxies
        self.index = 0  # For round-robin rotation

    def rotate_proxy(self) -> str:
        proxy = self.proxies[self.index]
        self.index = (self.index + 1) % len(self.proxies)
        return proxy

    def validate_proxy(self, proxy: str) -> bool:
        # TODO: Add real validation (e.g., test against httpbin)
        return True
