import random
from typing import List

class TLSFingerprintModule:
    def __init__(self, profiles: List[str]):
        if not profiles:
            raise ValueError("TLS profile list cannot be empty.")
        self.profiles = profiles

    def select_profile(self) -> str:
        return random.choice(self.profiles)

    def apply_fingerprint(self, request: dict, profile: str):
        # Placeholder for real implementation
        request['tls_profile'] = profile
        return request
