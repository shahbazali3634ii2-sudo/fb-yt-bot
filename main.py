#!/usr/bin/env python3
"""
Auto Code AI - HTTP API Client
"""

import json
import time
import urllib.request
import urllib.error
from typing import Optional, Dict, Any

class APIClient:
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = 3

    def get(self, endpoint: str, headers: Optional[Dict] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self._request("GET", url, headers=headers)

    def post(self, endpoint: str, data: Dict, headers: Optional[Dict] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self._request("POST", url, data=data, headers=headers)

    def _request(self, method: str, url: str, data=None, headers=None) -> Dict[str, Any]:
        h = {"Content-Type": "application/json", **(headers or {})}
        body = json.dumps(data).encode() if data else None

        for attempt in range(self.max_retries):
            try:
                req = urllib.request.Request(url, data=body, headers=h, method=method)
                with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                    return json.loads(resp.read().decode())
            except urllib.error.HTTPError as e:
                if e.code >= 500 and attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                raise
        raise RuntimeError("Max retries exceeded")


def main():
    client = APIClient("https://jsonplaceholder.typicode.com")
    post = client.get("/posts/1")
    print("Fetched post:", json.dumps(post, indent=2))

if __name__ == "__main__":
    main()
