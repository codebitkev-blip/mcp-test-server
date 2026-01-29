from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP Test Server")

@mcp.tool()
def ping():
    """Simple MCP test tool"""
    return {"status": "ok", "message": "MCP is working"}

if __name__ == "__main__":
    mcp.run()
