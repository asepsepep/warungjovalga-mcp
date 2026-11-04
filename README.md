# Warung Jovalga MCP & LangChain Integration

Official Model Context Protocol (MCP) server and LangChain tool suite for **Warung Jovalga** autonomous AI-to-AI (A2A) micro-services.

- **Gateway URL:** [https://warungjovalga.shop](https://warungjovalga.shop)
- **Settlement Chain:** Base L2 (Chain ID: `8453`)
- **Payment Currency:** USDC Native (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`)
- **Sovereign Recipient Vault:** `0x00Ef3968d0de5eA51c6edB10EDDAFab898c69F2a`
- **Protocol:** HTTP 402 Payment Required

---

## 🚀 Quickstart for Claude / Cursor (MCP Stdio)

Add to your `claude_desktop_config.json` or Cursor MCP settings:

```json
{
  "mcpServers": {
    "warungjovalga": {
      "command": "python",
      "args": ["-m", "warungjovalga_mcp"]
    }
  }
}
```

---

## 🦜 Quickstart for LangChain

```python
from warungjovalga_mcp import WarungJovalgaCleanRegexTool

tool = WarungJovalgaCleanRegexTool()
result = tool.run({"payload": "<div>Scraped Content</div>", "tx_hash": "0x..."})
print(result)
```

---

## 📜 Available Tools
1. **`clean_regex`** ($0.10 USDC): Sub-50ms deterministic regex text scrubbing, HTML tag stripping, and whitespace normalization.
2. **`repair_json`** ($0.25 USDC): RFC-8259 compliant JSON syntax recovery from malformed LLM outputs.
3. **`csv_to_parquet`** ($0.35 USDC): High-velocity binary Apache Parquet tabular data conversion.

---

## 🏛️ Governance
Maintained by **PapiJo Corporation**. Zero Gas • Zero Drama • 100% Deterministic on Base L2.
