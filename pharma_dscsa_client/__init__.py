"""
FDA DSCSA & EU FMD Drug Serialization API (21 USC 360eee) Python Client SDK (Zero External Dependencies)
"""
import os
import json
import urllib.request
import urllib.error
from typing import Any, Dict, Optional


class PharmaDscsaClient:
    """
    Client for FDA DSCSA & EU FMD Drug Serialization API (21 USC 360eee).

    :param api_key: RapidAPI key ('x-rapidapi-key').
                    Get your key at: https://rapidapi.com/noor-mkdad-apis-noor-mkdad-apis-default/api/fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee
    :param base_url: Custom API endpoint override. Defaults to https://fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee.p.rapidapi.com.
    :param rapidapi_host: RapidAPI host header. Defaults to fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee.p.rapidapi.com.
    """
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        rapidapi_host: str = "fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee.p.rapidapi.com"
    ):
        self.api_key = api_key or os.environ.get("RAPIDAPI_KEY", "")
        self.rapidapi_host = rapidapi_host
        self.base_url = (base_url or f"https://{self.rapidapi_host}").rstrip("/")

    def request(self, endpoint: str, method: str = "GET", payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        if not self.api_key:
            return {
                "success": False,
                "error": "RapidAPI API key is required. Subscribe and obtain your key at: https://rapidapi.com/noor-mkdad-apis-noor-mkdad-apis-default/api/fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee",
                "code": "MISSING_API_KEY",
                "subscribe_url": "https://rapidapi.com/noor-mkdad-apis-noor-mkdad-apis-default/api/fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee"
            }

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "pharma-dscsa-python-client/1.0",
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.rapidapi_host
        }

        data = json.dumps(payload).encode("utf-8") if payload else None
        req = urllib.request.Request(url, data=data, headers=headers, method=method)

        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                return res_data
        except urllib.error.HTTPError as e:
            try:
                return json.loads(e.read().decode("utf-8"))
            except Exception:
                return {
                    "success": False,
                    "error": f"HTTP {e.code}: {e.reason}",
                    "code": f"HTTP_{e.code}",
                    "upgrade_url": "https://rapidapi.com/noor-mkdad-apis-noor-mkdad-apis-default/api/fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee"
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "code": "NETWORK_ERROR",
                "subscribe_url": "https://rapidapi.com/noor-mkdad-apis-noor-mkdad-apis-default/api/fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee"
            }

    def get_health(self) -> Dict[str, Any]:
        """Check API health status via RapidAPI."""
        return self.request("/health", method="GET")

    def validate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Submit validation/parse request via RapidAPI."""
        return self.request("/api/v1/validate", method="POST", payload=payload)
