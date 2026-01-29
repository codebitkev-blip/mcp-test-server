# MCP Test Server

This repository is a **minimal, clean implementation of a Model Context Protocol (MCP) server**.

It exists **solely for testing MCP detection, audits, and tooling**.

---

## Purpose

- Provide a minimal MCP implementation
- Enable source-code repository MCP audits
- Avoid application-specific complexity
- Demonstrate correct MCP structure

---

## Files of Interest

- `mcp.json` — MCP server configuration
- `mcp.manifest.json` — Static MCP declaration for audits
- `server.py` — Minimal MCP server
- `requirements.txt` — Required dependencies

---

## Running Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python server.py
