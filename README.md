# ZARQ Crypto Risk Intelligence — MCP Server

[![Smithery](https://smithery.ai/badge/agentidx/zarq-crypto)](https://smithery.ai/server/agentidx/zarq-crypto)

Independent crypto risk intelligence via the Model Context Protocol (MCP). Trust Score ratings, Distance-to-Default analysis, structural collapse warnings, and pre-trade safety checks for 198 tokens.

<a href="https://glama.ai/mcp/servers/zarq-ai/zarq-risk-intelligence">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/zarq-ai/zarq-risk-intelligence/badge" alt="zarq-risk-intelligence MCP server" />
</a>

## Quick Start

### Remote (SSE / Streamable HTTP)

No installation needed — connect directly:
```json
{
  "mcpServers": {
    "zarq-crypto": {
      "url": "https://mcp.zarq.ai/mcp"
    }
  }
}
```

### Local (stdio)
```bash
pip install mcp httpx
python zarq_mcp_server.py
```

## Tools (8)

| Tool | Description |
|------|-------------|
| `crypto_safety_check` | Quick pre-trade safety validation (<100ms) |
| `crypto_rating` | Full Trust Score with 5-pillar breakdown (A+ to F) |
| `crypto_dtd` | Distance-to-Default with 7 distress signals |
| `crypto_signals` | Active Structural Collapse/Stress signals |
| `crypto_compare` | Head-to-head token risk comparison |
| `crypto_distress_watch` | All tokens with DtD < 2.0 |
| `crypto_alerts` | Structural collapse/stress warnings |
| `crypto_ratings_bulk` | Bulk ratings for multiple tokens |

## Performance

- **100% death recall** — every token collapse detected (out-of-sample)
- **98% precision** — only 1 genuine false positive in OOS validation
- **198 tokens** rated with daily updates
- **<100ms** response time for safety checks

## Architecture
```
Client (Claude, Cursor, etc.)
    ↓ MCP Protocol
ZARQ MCP Server
    ↓ HTTPS
zarq.ai API (free, no key required)
```

## API

Free API at [zarq.ai](https://zarq.ai). No API key required during Early Access.

## Tags

`crypto` `risk` `defi` `safety` `trust-score` `crash-prediction` `distance-to-default` `ratings` `blockchain` `token-analysis`

## License

MIT