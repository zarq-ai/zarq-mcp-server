#!/usr/bin/env python3
"""
ZARQ + Nerq MCP Server
=======================
Crypto risk intelligence (ZARQ) + AI agent trust verification (Nerq).
Designed for registration on Smithery and Glama registries.

Crypto tools (ZARQ):
  1. crypto_safety_check    — Quick pre-trade safety validation (<100ms)
  2. crypto_rating          — Full Trust Score with 5-pillar breakdown
  3. crypto_dtd             — Distance-to-Default with 7 signals
  4. crypto_signals         — Active Structural Collapse/Stress signals
  5. crypto_compare         — Head-to-head token comparison
  6. crypto_distress_watch  — All tokens with DtD < 2.0
  7. crypto_alerts          — Structural collapse/stress warnings
  8. crypto_ratings_bulk    — Bulk ratings for multiple tokens

AI agent tools (Nerq):
  9. preflight_trust_check  — Pre-interaction trust check between agents
  10. kya_report            — Full Know Your Agent due diligence report
  11. find_best_agent       — Find top agents by category and trust
  12. agent_benchmark       — Benchmark leaderboard for a category
  13. get_agent_stats       — Full Nerq ecosystem statistics
  14. nerq_scout_status     — Scout autonomous discovery status
  15. nerq_scout_findings   — Latest top agents discovered by Scout

Usage:
  python zarq_mcp_server.py                    # stdio transport (default)
  python zarq_mcp_server.py --transport sse    # SSE transport for web

Requirements:
  pip install mcp httpx

Registry tags: crypto, risk, ai, agents, trust-score, mcp
"""

import json
import asyncio
import argparse
import httpx
from typing import Any

# ─── MCP SDK Import ───
try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp.types import Tool, TextContent
except ImportError:
    print("MCP SDK not installed. Run: pip install mcp")
    print("Falling back to standalone HTTP mode.")
    Server = None

# ─── Configuration ───
ZARQ_API_BASE = "https://zarq.ai"
NERQ_API_BASE = "https://nerq.ai"
API_TIMEOUT = 10.0

# ─── API Client ───
async def zarq_api(path: str, params: dict = None) -> dict:
    """Call ZARQ API endpoint and return JSON response."""
    async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
        url = f"{ZARQ_API_BASE}{path}"
        resp = await client.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

async def nerq_api(path: str, params: dict = None) -> dict:
    """Call Nerq API endpoint and return JSON response."""
    async with httpx.AsyncClient(timeout=API_TIMEOUT) as client:
        url = f"{NERQ_API_BASE}{path}"
        resp = await client.get(url, params=params)
        resp.raise_for_status()
        return resp.json()


# ─── Tool Definitions ───
TOOLS = [
    Tool(
        name="crypto_safety_check",
        description=(
            "Quick pre-trade safety check for a crypto token. Returns risk level, "
            "trust grade, DtD score, alert status, crash probability, and any active flags. "
            "Optimized for <100ms response. Use before any crypto trade or investment decision. "
            "Example: crypto_safety_check(token_id='bitcoin')"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "token_id": {
                    "type": "string",
                    "description": "Token identifier (e.g., 'bitcoin', 'ethereum', 'solana', 'cardano'). Use lowercase CoinGecko-style IDs."
                }
            },
            "required": ["token_id"]
        }
    ),
    Tool(
        name="crypto_rating",
        description=(
            "Get the full ZARQ Trust Score for a crypto token. Returns overall score (0-100), "
            "letter grade (A+ to F), and breakdown across 5 pillars: Security (30%), "
            "Compliance (25%), Maintenance (20%), Popularity (15%), Ecosystem (10%). "
            "198 tokens rated. Example: crypto_rating(token_id='ethereum')"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "token_id": {
                    "type": "string",
                    "description": "Token identifier (e.g., 'bitcoin', 'ethereum'). Use lowercase CoinGecko-style IDs."
                }
            },
            "required": ["token_id"]
        }
    ),
    Tool(
        name="crypto_dtd",
        description=(
            "Get the Distance-to-Default (DtD) score for a crypto token. DtD measures "
            "distance-to-default on a 0-5 scale (5=healthy, 0=imminent collapse). Returns "
            "7 signal scores (Liquidity, Holders, Resilience, Fundamental, Contagion, "
            "Structural, Relative Weakness), trend classification (FREEFALL/FALLING/SLIDING/"
            "STABLE/IMPROVING), crash probability, and Structural Collapse status. "
            "Example: crypto_ndd(token_id='solana')"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "token_id": {
                    "type": "string",
                    "description": "Token identifier (e.g., 'solana'). Use lowercase CoinGecko-style IDs."
                }
            },
            "required": ["token_id"]
        }
    ),
    Tool(
        name="crypto_signals",
        description=(
            "Get all active crypto risk signals: Structural Collapse and Structural Stress alerts "
            "and recovery recovery signals. Each signal includes token, DtD score, trend, "
            "crash probability, streak duration, SHA-256 hash, and timestamp. Also returns "
            "a running scoreboard with precision metrics. Use to monitor the crypto market "
            "for emerging risks. Example: crypto_signals()"
        ),
        inputSchema={
            "type": "object",
            "properties": {},
            "required": []
        }
    ),
    Tool(
        name="crypto_compare",
        description=(
            "Compare two crypto tokens head-to-head. Returns Trust Score, NDD, risk level, "
            "and key differences for both tokens. Useful for relative value analysis or "
            "deciding between two investments. "
            "Example: crypto_compare(token_a='bitcoin', token_b='ethereum')"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "token_a": {
                    "type": "string",
                    "description": "First token identifier"
                },
                "token_b": {
                    "type": "string",
                    "description": "Second token identifier"
                }
            },
            "required": ["token_a", "token_b"]
        }
    ),
    Tool(
        name="crypto_distress_watch",
        description=(
            "Get all tokens currently showing distress (DtD < 2.0). Returns a watchlist "
            "of tokens with elevated crash risk, sorted by DtD score ascending (most "
            "distressed first). Use to identify tokens to avoid or potentially short. "
            "Example: crypto_distress_watch()"
        ),
        inputSchema={
            "type": "object",
            "properties": {},
            "required": []
        }
    ),
    Tool(
        name="crypto_alerts",
        description=(
            "Get all active ZARQ structural warnings. Two levels: STRUCTURAL COLLAPSE "
            "(≥3 weakness signals, historically 98% lost >50% value) and STRUCTURAL STRESS "
            "(≥2 weakness signals, requires monitoring). Out-of-sample validated: 113/113 "
            "token deaths detected with 98% precision. "
            "Example: crypto_alerts(level='CRITICAL') or crypto_alerts()"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "level": {
                    "type": "string",
                    "description": "Filter by alert level: 'CRITICAL' (structural collapse) or 'WARNING' (structural stress). Omit for all.",
                    "enum": ["CRITICAL", "WARNING"]
                }
            },
            "required": []
        }
    ),
    Tool(
        name="crypto_ratings_bulk",
        description=(
            "Get Trust Score ratings for all 198 rated tokens in bulk. Returns token_id, "
            "name, symbol, trust_score, trust_grade, and risk_level for each. "
            "Useful for screening, portfolio construction, or building filtered lists. "
            "Example: crypto_ratings_bulk()"
        ),
        inputSchema={
            "type": "object",
            "properties": {},
            "required": []
        }
    ),

    # ─── Nerq AI Agent Tools ───
    Tool(
        name="preflight_trust_check",
        description=(
            "Pre-interaction trust check between AI agents. Returns trust scores, grades, "
            "risk level, and PROCEED/CAUTION/DENY recommendation. Use before delegating "
            "tasks to or accepting requests from another agent. 204K+ agents indexed. "
            "Example: preflight_trust_check(target='SWE-agent')"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "target": {"type": "string", "description": "Agent name to check trust for"},
                "caller": {"type": "string", "description": "Your agent name (optional)"}
            },
            "required": ["target"]
        }
    ),
    Tool(
        name="kya_report",
        description=(
            "Get a full Know Your Agent (KYA) due diligence report for an AI agent. Returns "
            "trust score, grade, category, description, stars, source URL, compliance data, "
            "and risk assessment. 204K+ agents indexed. "
            "Example: kya_report(name='langchain')"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Agent name to look up"}
            },
            "required": ["name"]
        }
    ),
    Tool(
        name="find_best_agent",
        description=(
            "Find the top agents in a category that meet a minimum trust score. Returns "
            "ranked agents with trust scores, compliance, and risk levels. "
            "Example: find_best_agent(category='coding', min_trust_score=70)"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "category": {"type": "string", "description": "Category to search (e.g. coding, security, finance)"},
                "min_trust_score": {"type": "number", "description": "Minimum trust score 0-100 (default 50)", "default": 50}
            },
            "required": ["category"]
        }
    ),
    Tool(
        name="agent_benchmark",
        description=(
            "Get the benchmark leaderboard for a category — top 20 agents ranked by trust "
            "score with compliance data, stars, and platform info. "
            "Example: agent_benchmark(category='coding')"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "category": {"type": "string", "description": "Category to benchmark"}
            },
            "required": ["category"]
        }
    ),
    Tool(
        name="get_agent_stats",
        description=(
            "Get full Nerq ecosystem statistics: total AI assets (5M+), breakdown by type "
            "(agents, tools, MCP servers, models, datasets), top categories, frameworks, "
            "languages, and trust distribution. Example: get_agent_stats()"
        ),
        inputSchema={"type": "object", "properties": {}}
    ),
    Tool(
        name="nerq_scout_status",
        description=(
            "Get Nerq Scout status: how many agents evaluated, featured, and claimed. "
            "The Scout autonomously discovers and evaluates high-trust agents daily. "
            "Example: nerq_scout_status()"
        ),
        inputSchema={"type": "object", "properties": {}}
    ),
    Tool(
        name="nerq_scout_findings",
        description=(
            "Get latest top agents discovered by Nerq Scout — high-trust agents (85+) "
            "with stars, categories, and trust scores. Updated daily. "
            "Example: nerq_scout_findings(limit=5)"
        ),
        inputSchema={
            "type": "object",
            "properties": {
                "limit": {"type": "integer", "description": "Max results (default 10)", "default": 10}
            }
        }
    ),
]


# ─── Tool Handlers ───
async def handle_tool(name: str, arguments: dict) -> str:
    """Route tool calls to ZARQ API endpoints."""
    try:
        if name == "crypto_safety_check":
            token_id = arguments["token_id"]
            data = await zarq_api(f"/v1/crypto/safety/{token_id}")
            return json.dumps(data, indent=2)

        elif name == "crypto_rating":
            token_id = arguments["token_id"]
            data = await zarq_api(f"/v1/crypto/rating/{token_id}")
            return json.dumps(data, indent=2)

        elif name == "crypto_dtd":
            token_id = arguments["token_id"]
            data = await zarq_api(f"/v1/crypto/ndd/{token_id}")
            return json.dumps(data, indent=2)

        elif name == "crypto_signals":
            data = await zarq_api("/v1/crypto/signals")
            return json.dumps(data, indent=2)

        elif name == "crypto_compare":
            token_a = arguments["token_a"]
            token_b = arguments["token_b"]
            data = await zarq_api(f"/v1/crypto/compare/{token_a}/{token_b}")
            return json.dumps(data, indent=2)

        elif name == "crypto_distress_watch":
            data = await zarq_api("/v1/crypto/distress-watch")
            return json.dumps(data, indent=2)

        elif name == "crypto_alerts":
            params = {}
            if "level" in arguments:
                params["level"] = arguments["level"]
            data = await zarq_api("/v1/crypto/alerts", params=params)
            return json.dumps(data, indent=2)

        elif name == "crypto_ratings_bulk":
            data = await zarq_api("/v1/crypto/ratings")
            return json.dumps(data, indent=2)

        # ─── Nerq AI Agent Tools ───
        elif name == "preflight_trust_check":
            params = {"target": arguments["target"]}
            if arguments.get("caller"):
                params["caller"] = arguments["caller"]
            data = await nerq_api("/v1/preflight", params=params)
            return json.dumps(data, indent=2)

        elif name == "kya_report":
            data = await nerq_api(f"/v1/agent/kya/{arguments['name']}")
            return json.dumps(data, indent=2)

        elif name == "find_best_agent":
            params = {"domain": arguments["category"], "limit": 5}
            if arguments.get("min_trust_score"):
                params["min_trust"] = arguments["min_trust_score"]
            data = await nerq_api("/v1/agent/search", params=params)
            return json.dumps(data, indent=2)

        elif name == "agent_benchmark":
            data = await nerq_api(f"/v1/agent/benchmark/{arguments['category']}")
            return json.dumps(data, indent=2)

        elif name == "get_agent_stats":
            data = await nerq_api("/v1/agent/stats")
            return json.dumps(data, indent=2)

        elif name == "nerq_scout_status":
            data = await nerq_api("/v1/scout/status")
            return json.dumps(data, indent=2)

        elif name == "nerq_scout_findings":
            params = {"limit": arguments.get("limit", 10)}
            data = await nerq_api("/v1/scout/findings", params=params)
            return json.dumps(data, indent=2)

        else:
            return json.dumps({"error": f"Unknown tool: {name}"})

    except httpx.HTTPStatusError as e:
        return json.dumps({
            "error": f"ZARQ API returned {e.response.status_code}",
            "detail": e.response.text[:500]
        })
    except httpx.ConnectError:
        return json.dumps({"error": "Could not connect to ZARQ API at zarq.ai"})
    except Exception as e:
        return json.dumps({"error": str(e)})


# ─── MCP Server Setup ───
def create_server() -> "Server":
    """Create and configure the MCP server."""
    server = Server("zarq-crypto")

    @server.list_tools()
    async def list_tools():
        return TOOLS

    @server.call_tool()
    async def call_tool(name: str, arguments: dict) -> list:
        result = await handle_tool(name, arguments)
        return [TextContent(type="text", text=result)]

    return server


async def run_stdio():
    """Run server with stdio transport (default for MCP)."""
    server = create_server()
    async with stdio_server() as (read_stream, write_stream):
        from mcp.server import InitializationOptions
        from mcp.server.models import ServerCapabilities
        init_options = InitializationOptions(
            server_name="zarq-crypto",
            server_version="1.0.0",
            capabilities=ServerCapabilities(tools={})
        )
        await server.run(read_stream, write_stream, init_options)


async def run_sse(host: str = "0.0.0.0", port: int = 8001):
    """Run server with Streamable HTTP + SSE transport."""
    from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
    from mcp.server.sse import SseServerTransport
    from mcp.server import InitializationOptions
    from mcp.server.models import ServerCapabilities
    from starlette.applications import Starlette
    from starlette.routing import Route
    from starlette.responses import JSONResponse
    import contextlib
    import uvicorn

    server = create_server()
    init_options = InitializationOptions(
        server_name="zarq-crypto",
        server_version="1.0.0",
        capabilities=ServerCapabilities(tools={})
    )

    # --- Streamable HTTP via SessionManager ---
    session_manager = StreamableHTTPSessionManager(
        app=server,
        json_response=True,
        stateless=True,
    )

    async def handle_mcp(request):
        await session_manager.handle_request(request.scope, request.receive, request._send)

    # --- Legacy SSE transport ---
    sse = SseServerTransport("/messages")

    async def handle_sse(request):
        async with sse.connect_sse(request.scope, request.receive, request._send) as streams:
            await server.run(streams[0], streams[1], init_options)

    async def handle_messages(request):
        await sse.handle_post_message(request.scope, request.receive, request._send)

    # --- Utility endpoints ---
    async def handle_server_card(request):
        return JSONResponse({
            "name": "zarq-crypto",
            "display_name": "ZARQ + Nerq: Crypto Risk & AI Agent Trust",
            "description": "ZARQ crypto risk intelligence + Nerq AI agent trust verification. 198 tokens rated, 204K agents & tools indexed. Trust scores, crash prediction, preflight checks, KYA reports. Free API.",
            "version": "1.1.0",
            "author": "ZARQ",
            "homepage": "https://zarq.ai",
            "transport": ["sse", "streamable-http"],
            "sse_url": "https://mcp.zarq.ai/sse",
            "streamable_http_url": "https://mcp.zarq.ai/mcp",
            "tools": [t.name for t in TOOLS],
            "tags": ["crypto", "risk", "defi", "ai", "agents", "trust-score", "mcp", "safety"]
        })

    async def handle_health(request):
        return JSONResponse({"status": "ok", "server": "zarq-crypto", "version": "1.0.0"})

    @contextlib.asynccontextmanager
    async def lifespan(app):
        async with session_manager.run():
            yield

    app = Starlette(
        routes=[
            Route("/.well-known/mcp/server-card.json", handle_server_card),
            Route("/health", handle_health),
            Route("/mcp", handle_mcp, methods=["GET", "POST", "DELETE"]),
            Route("/sse", handle_sse),
            Route("/messages", handle_messages, methods=["POST"]),
        ],
        lifespan=lifespan,
    )

    config = uvicorn.Config(app, host=host, port=port)
    server_instance = uvicorn.Server(config)
    await server_instance.serve()


# ─── Smithery Configuration ───
SMITHERY_CONFIG = {
    "name": "zarq-crypto",
    "display_name": "ZARQ + Nerq: Crypto Risk & AI Agent Trust",
    "description": (
        "ZARQ crypto risk intelligence + Nerq AI agent trust verification. "
        "198 tokens rated (Trust Score, DtD, crash prediction). "
        "204K agents & tools indexed (preflight checks, KYA reports, benchmarks). "
        "Free API."
    ),
    "version": "1.1.0",
    "author": "ZARQ",
    "homepage": "https://zarq.ai",
    "tags": [
        "crypto", "risk", "defi", "safety", "trust-score",
        "ai", "agents", "mcp", "preflight", "kya"
    ],
    "tools": len(TOOLS),
    "transport": ["stdio", "sse", "streamable-http"],
    "license": "MIT"
}


# ─── Entry Point ───
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ZARQ Crypto MCP Server")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio",
                        help="Transport type (default: stdio)")
    parser.add_argument("--port", type=int, default=8001,
                        help="Port for SSE transport (default: 8001)")
    parser.add_argument("--config", action="store_true",
                        help="Print Smithery configuration JSON")
    args = parser.parse_args()

    if args.config:
        print(json.dumps(SMITHERY_CONFIG, indent=2))
    elif args.transport == "sse":
        asyncio.run(run_sse(port=args.port))
    else:
        asyncio.run(run_stdio())
