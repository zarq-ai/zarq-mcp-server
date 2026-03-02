# ZARQ Crypto Risk Intelligence — MCP Server

> Pre-trade safety checks, trust ratings, crash prediction, and structural collapse alerts for 15,000+ crypto tokens.

[![Smithery](https://smithery.ai/badge/zarq-crypto)](https://smithery.ai/server/zarq-crypto)

## What is ZARQ?

ZARQ provides institutional-grade crypto risk intelligence:

- **Trust Ratings** — Aaa–D scale for 15,000+ tokens, 1,000+ exchanges, 7,000+ DeFi protocols
- **Distance-to-Default (DtD)** — 7-signal model (0–5 scale) adapted from Merton's structural credit model
- **Structural Collapse Detection** — 100% recall (113/113 token deaths), 98% precision out-of-sample
- **Portable Alpha Strategy** — Backtested Sharpe 2.02–5.56 (Apr 2021–Dec 2025)

## Tools (8)

| Tool | Description | Latency |
|------|-------------|---------|
| `crypto_safety_check` | Quick pre-trade safety validation | <100ms |
| `crypto_rating` | Full Trust Score with 5-pillar breakdown | <200ms |
| `crypto_dtd` | Distance-to-Default with 7 signals | <200ms |
| `crypto_signals` | Active Structural Collapse/Stress signals | <300ms |
| `crypto_compare` | Head-to-head token comparison | <300ms |
| `crypto_distress_watch` | All tokens with DtD < 2.0 | <300ms |
| `crypto_alerts` | Structural collapse/stress warnings | <300ms |
| `crypto_ratings_bulk` | Bulk ratings for multiple tokens | <500ms |

## Quick Start

### Install via Smithery
```bash
npx @smithery/cli install zarq-crypto --client claude
```

### Manual Installation
```bash
pip install mcp httpx
python server.py
```

### Claude Desktop Configuration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "zarq-crypto": {
      "command": "python",
      "args": ["/path/to/zarq-mcp-server/server.py"]
    }
  }
}
```

## Example Usage

Ask Claude:

- *"Is Solana safe to buy right now?"* → calls `crypto_safety_check`
- *"Compare Bitcoin vs Ethereum risk"* → calls `crypto_compare`
- *"Which tokens are at risk of collapse?"* → calls `crypto_alerts`
- *"Get the DtD score for Cardano"* → calls `crypto_dtd`
- *"Rate these tokens: bitcoin, ethereum, solana"* → calls `crypto_ratings_bulk`

## Validation

| Metric | Value |
|--------|-------|
| Token deaths detected | 113/113 (100%) |
| Precision (>50% threshold) | 98% |
| Out-of-sample period | Jan 2024 – Feb 2026 |
| False positives | 1 genuine FP |

## API

All tools call the free ZARQ API at `zarq.ai`. No API key required during beta. Rate limit: 1,000 calls/day.

- API Docs: [zarq.ai/docs](https://zarq.ai/docs)
- Methodology: [zarq.ai/methodology](https://zarq.ai/methodology)
- Track Record: [zarq.ai/track-record](https://zarq.ai/track-record)

## License

MIT
