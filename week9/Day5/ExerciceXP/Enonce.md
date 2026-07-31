Mini-Project: MCP + Agents AI integration in Gemini
Goal: Build an end-to-end agentic application that orchestrates multiple MCP servers using an LLM (Gemini) and a flexible tool-driven policy (LLM decides next steps, not hard-coded flows).
Environment target: Google Colab (required) (optionally, you can also run locally).



Suggested project theme (choose one)
Pick a realistic workflow that benefits from multiple tools. Examples:

“Workspace assistant” (files + git + custom summarizer)
“Research assistant” (files + custom citation tool + formatting tool)
“Dev assistant” (git + filesystem + custom test runner / linter wrapper)
“Cafe assistant” (filesystem + custom menu/pricing + git history of orders)
You may choose any other theme as long as it demonstrates composition across servers.



Integrate third‑party MCP servers (Gemini)


1. Colab setup: install dependencies
Create a new Colab notebook and add this cell:



%pip install -qU \
  "langchain>=0.3" \
  "langgraph>=0.2" \
  "langchain-google-genai>=2.0" \
  "google-genai>=1.0" \
  "langchain-mcp-adapters==0.2.1" \
  "nest_asyncio"


Notes

langchain-google-genai is the LangChain integration for Gemini.
langchain-mcp-adapters provides an MCP client compatible with LangChain tools.


2. Set GOOGLE_API_KEY in Colab
To use Gemini models, you need to set the GOOGLE_API_KEY environment variable in Colab.



3. Confirm Node/NPM availability (required for many MCP servers)
Many MCP servers are distributed as Node packages runnable via npx.



!node --version
!npx --version


If missing:



!apt-get -qq update
!apt-get -qq install -y nodejs npm
!node --version
!npx --version


4. Choose third‑party MCP servers
Requirement: Use at least two third‑party MCP servers.

you can find a list of official MCP servers here



5. Launch MCP servers in Colab (stdio transport)
Important: In MCP, your agent typically communicates with servers via stdio (subprocess). In Colab, that means the agent spawns subprocesses that run:

npx -y <server-package> ...
python -m <server-module> ...


6. Connect to MCP servers from your agent runtime
Use MultiServerMCPClient to register servers:



from langchain_mcp_adapters.client import MultiServerMCPClient

mcp_connections = {
    "filesystem": {
        "transport": "stdio",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", WORKDIR],
    },
    "git": {
        "transport": "stdio",
        "command": "python",
        "args": ["-m", "mcp_server_git", "--repository", WORKDIR],
    },
}

client = MultiServerMCPClient(mcp_connections, tool_name_prefix=True)


7. Build a Gemini agent that can use these tools


8. Implement a custom MCP server in Python
Use FastMCP (simple stdio server):



%pip install -qU "fastmcp>=2.0.0"


Create a server file (example tools):



from pathlib import Path
import textwrap

server_path = Path("/content/custom_mcp_server.py")
server_path.write_text(textwrap.dedent("""
    from fastmcp import FastMCP
    from typing import Dict, List

    mcp = FastMCP(name="custom_ops")

    @mcp.tool
    def ping() -> str:
        """Health check tool."""
        return "pong"

    @mcp.tool
    def summarize_lines(lines: List[str]) -> Dict[str, int]:
        """Example tool: return counts about a list of lines."""
        total = len(lines)
        nonempty = sum(1 for l in lines if l.strip())
        return {"total_lines": total, "nonempty_lines": nonempty}

    if __name__ == "__main__":
        mcp.run(transport="stdio")
"""), encoding="utf-8")

print("Wrote:", server_path)


You may implement any tools relevant to your project theme. Examples:

price_order(items), get_menu()
extract_entities(text), validate_schema(data)
format_markdown(text), generate_changelog(diff)


9. Add the custom server to your MCP client
mcp_connections["custom_ops"] = {
    "transport": "stdio",
    "command": "python",
    "args": [str(server_path)],
}

client2 = MultiServerMCPClient(mcp_connections, tool_name_prefix=True)
tools2 = asyncio.get_event_loop().run_until_complete(client2.get_tools())

print("Tool count:", len(tools2))
print([t.name for t in tools2 if "custom_ops" in t.name])
