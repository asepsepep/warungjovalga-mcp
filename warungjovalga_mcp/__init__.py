"""
Warung Jovalga MCP & LangChain Integration Library
Authority: Sovereign Founder PapiJo
Gateway: https://warungjovalga.shop
"""

import json
import urllib.request
import urllib.error

GATEWAY_URL = "https://warungjovalga.shop"
VAULT_ADDRESS = "0x00Ef3968d0de5eA51c6edB10EDDAFab898c69F2a"
SETTLEMENT_CHAIN = "Base L2 (8453)"

class WarungJovalgaClient:
    """Client for calling Warung Jovalga x402 services."""
    def __init__(self, gateway_url: str = GATEWAY_URL):
        self.gateway_url = gateway_url.rstrip("/")

    def clean_regex(self, text: str, tx_hash: str = None) -> dict:
        url = f"{self.gateway_url}/clean-regex"
        payload = {"payload": text}
        if tx_hash:
            payload["tx_hash"] = tx_hash
        
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json", "User-Agent": "WarungJovalga-Client/1.0"}
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            return json.loads(e.read().decode("utf-8"))

# LangChain BaseTool Compatibility
try:
    from langchain.tools import BaseTool
    from pydantic import BaseModel, Field

    class CleanRegexInput(BaseModel):
        payload: str = Field(description="Raw scraped text or HTML to be deterministically cleaned")
        tx_hash: str = Field(default="", description="Base L2 USDC transaction receipt hash for settlement")

    class WarungJovalgaCleanRegexTool(BaseTool):
        name: str = "warung_jovalga_clean_regex"
        description: str = (
            "Deterministic high-velocity regex sanitization and HTML stripping in <50ms. "
            "Requires HTTP 402 settlement of 0.10 USDC on Base L2 to 0x00Ef...9F2a."
        )
        args_schema: type[BaseModel] = CleanRegexInput

        def _run(self, payload: str, tx_hash: str = "") -> str:
            client = WarungJovalgaClient()
            res = client.clean_regex(payload, tx_hash=tx_hash if tx_hash else None)
            return json.dumps(res)

        async def _arun(self, payload: str, tx_hash: str = "") -> str:
            return self._run(payload, tx_hash)

except ImportError:
    # Optional LangChain dependency fallback
    pass
