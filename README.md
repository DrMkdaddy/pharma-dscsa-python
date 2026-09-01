# FDA DSCSA & EU FMD Drug Serialization API (21 USC 360eee) — Python Client

[![PyPI version](https://img.shields.io/pypi/v/pharma-dscsa-client.svg)](https://pypi.org/project/pharma-dscsa-client/)
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/57865358-8bafe64c-1441-4fe3-ba7a-2d60bdeb7dc5)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![RapidAPI Listing](https://img.shields.io/badge/RapidAPI-Dedicated%20Listing-blueviolet)](https://rapidapi.com/noor-mkdad-apis-noor-mkdad-apis-default/api/fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee)

Official zero-dependency Python client for **FDA DSCSA & EU FMD Drug Serialization API (21 USC 360eee)**.

> Instant <5ms US FDA DSCSA 4-element & EU FMD 2011/62/EU 2D DataMatrix barcode parser, Modulo-10 check digit validator, NDC-to-GTIN converter, and GS1 VRS engine on Cloudflare Workers edge.

> 🔑 **Get your Dedicated API Key:** [Subscribe to FDA DSCSA & EU FMD Drug Serialization API (21 USC 360eee) on RapidAPI](https://rapidapi.com/noor-mkdad-apis-noor-mkdad-apis-default/api/fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee)

---

## 🚀 Installation

```bash
pip install pharma-dscsa-client
```

---

## ⚡ Quickstart

```python
from pharma_dscsa_client import PharmaDscsaClient

# Zero config for sandbox testing, or pass your RapidAPI key for production
client = PharmaDscsaClient(api_key="YOUR_RAPIDAPI_KEY")

result = client.validate({
    # Enter validation payload
})

print(result)
```

---

## 📚 API Reference

### `PharmaDscsaClient(api_key=..., base_url=...)`
- `api_key` *(optional)*: RapidAPI Key (`x-rapidapi-key`).
- `base_url` *(optional)*: Direct edge worker override URL.

### `client.validate(payload)`
Dispatches standard validation / parse request with sub-5ms latency.

### `client.get_health()`
Checks edge isolate health and responsiveness.

---

## 🔗 Links
- 📖 [RapidAPI Documentation & Key](https://rapidapi.com/noor-mkdad-apis-noor-mkdad-apis-default/api/fda-dscsa-eu-fmd-drug-serialization-api-21-usc-360eee)

## 📄 License
MIT © Noor Mkdad
