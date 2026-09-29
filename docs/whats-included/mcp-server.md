---
title: MCP Server
order: 30
seealso: []
---

# MCP Server

Eremex Controls documentation, demo examples, and public support answers are available to AI coding assistants (Cursor, Claude Code, GitHub Copilot, Windsurf, Cline, and other [MCP](https://modelcontextprotocol.io)-compatible tools) through a self-hosted MCP server:

```
https://mcp.eremexcontrols.net/
```

Once connected, your assistant can pull up-to-date Eremex Controls context directly into its responses — real API names, real XAML/C# examples, and real answers from our support engineers — instead of guessing at APIs or relying on outdated training data.

## What's Indexed

| Source | Contents |
|---|---|
| Documentation | The full public documentation at [eremexcontrols.net](https://eremexcontrols.net) |
| Demo examples | Real usage examples from the [controls-demo](https://github.com/Eremex/controls-demo) sample application, one entry per demoed feature |
| Support Center | Public Q&A threads from the [EMX Support Center](https://sc.eremexcontrols.net) |

No API key or account is required to use the server.

## Configure Your AI Assistant

### Cursor

Add to `.cursor/mcp.json` (project) or `~/.cursor/mcp.json` (global):

```json
{
  "mcpServers": {
    "eremex-controls": {
      "type": "streamableHttp",
      "url": "https://mcp.eremexcontrols.net/mcp"
    }
  }
}
```

### Claude Code

```bash
claude mcp add --transport http eremex-controls https://mcp.eremexcontrols.net/mcp
```

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "eremex-controls": {
      "type": "sse",
      "url": "https://mcp.eremexcontrols.net/sse"
    }
  }
}
```

### VS Code (Copilot / Cline / Roo)

Add to your MCP settings (VS Code `settings.json` under `mcp.servers`, or the extension's own MCP configuration panel):

```json
{
  "mcp": {
    "servers": {
      "eremex-controls": {
        "type": "http",
        "url": "https://mcp.eremexcontrols.net/mcp"
      }
    }
  }
}
```

### Other MCP Clients

Any client that supports a remote MCP server over Streamable HTTP or SSE can connect directly:

- Streamable HTTP: `https://mcp.eremexcontrols.net/mcp`
- SSE (older clients): `https://mcp.eremexcontrols.net/sse`

## Verify It Works

After adding the configuration, restart your editor or client (most clients only scan MCP configuration on startup), then ask your assistant something like:

> Using the Eremex Controls docs, show me how to add a custom in-place editor to a DataGrid column.

> How do I enable drag-and-drop between two Eremex DataGrid controls? Show a real example.

If the server is connected, the assistant cites specific Eremex API members (for example, `GridColumn.EditorProperties`, `AllowDragDrop`) and real code from the documentation, demo application, or Support Center, instead of generic Avalonia guesses.

## Troubleshooting

- **The tool doesn't show up**: restart your editor or client after adding the configuration.
- **No results, or empty context**: try rephrasing your question using the control's name, for example "DataGrid", "TreeList", or "PropertyGrid" — search matches the same terms used in the Eremex documentation and demo page titles.
- **Still stuck**: contact us through the [Support Center](https://sc.eremexcontrols.net) or see [Technical Support Services](technical-support-services.md).
