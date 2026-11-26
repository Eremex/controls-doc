---
title: MCP 服务器
order: 30
seealso: []
---

# MCP 服务器 {#mcp-server}

AI 编程助手（Cursor、Claude Code、OpenCode、GitHub Copilot、Windsurf、Cline 以及其他兼容 [MCP](https://modelcontextprotocol.io) 的工具）可以通过自托管的 MCP 服务器访问 Eremex Controls 文档、演示示例和公开的支持答复：

```
https://mcp.eremexcontrols.net/
```

连接后，助手可以将最新的 Eremex Controls 上下文直接引入其回答中 — 真实的 API 名称、真实的 XAML/C# 示例以及我们支持工程师的真实答复 — 而不是猜测 API 或依赖过时的训练数据。

## 索引内容 {#whats-indexed}

| 来源 | 内容 |
|---|---|
| 文档 | [eremexcontrols.net](https://eremexcontrols.net) 上的完整公开文档 |
| 演示示例 | 来自 [controls-demo](https://github.com/Eremex/controls-demo) 示例应用程序的真实用法示例，每个演示功能一条 |
| 支持中心 | 来自 [EMX Support Center](https://sc.eremexcontrols.net) 的公开问答帖子 |

使用该服务器无需 API 密钥或账户。

## 配置 AI 助手 {#configure-your-ai-assistant}

### Cursor {#cursor}

添加到 `.cursor/mcp.json`（项目）或 `~/.cursor/mcp.json`（全局）：

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

### Claude Code {#claude-code}

```bash
claude mcp add --transport http eremex-controls https://mcp.eremexcontrols.net/mcp
```

### Claude Desktop {#claude-desktop}

添加到 `claude_desktop_config.json`：

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

### VS Code (Copilot / Cline / Roo) {#vs-code-copilot-cline-roo}

添加到 MCP 设置中（VS Code `settings.json` 中的 `mcp.servers` 下，或扩展自己的 MCP 配置面板）：

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

### OpenCode {#opencode}

在项目文件夹中运行以下命令（添加 `--global` 可使服务器在所有项目中可用）：

```bash
opencode mcp add eremex-controls --url https://mcp.eremexcontrols.net/mcp
```

或者手动将服务器添加到 `opencode.json` / `opencode.jsonc` 配置中：

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "servers": {
      "eremex-controls": {
        "type": "remote",
        "url": "https://mcp.eremexcontrols.net/mcp",
        "oauth": false
      }
    }
  }
}
```

该服务器无需登录：`"oauth": false` 可防止 OpenCode 启动 OAuth 流程。如果 OpenCode 要求您对服务器进行身份验证，请在配置中设置此选项。

### 其他 MCP 客户端 {#other-mcp-clients}

任何支持通过 Streamable HTTP 或 SSE 连接远程 MCP 服务器的客户端都可以直接连接：

- Streamable HTTP：`https://mcp.eremexcontrols.net/mcp`
- SSE（较旧的客户端）：`https://mcp.eremexcontrols.net/sse`

## 验证是否正常工作 {#verify-it-works}

添加配置后，请重新启动编辑器或客户端（大多数客户端仅在启动时扫描 MCP 配置），然后向助手提出类似以下的问题：

> Using the Eremex Controls docs, show me how to add a custom in-place editor to a DataGrid column.

> How do I enable drag-and-drop between two Eremex DataGrid controls? Show a real example.

如果服务器已连接，助手会引用具体的 Eremex API 成员（例如 [`GridColumn.EditorProperties`](../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md)、`AllowDragDrop`）以及来自文档、演示应用程序或支持中心的真实代码，而不是给出泛泛的 Avalonia 猜测。

## 故障排除 {#troubleshooting}

- **工具未显示**：添加配置后重新启动编辑器或客户端。
- **没有结果或上下文为空**：尝试使用控件名称重新表述问题，例如 "DataGrid"、"TreeList" 或 "PropertyGrid" — 搜索会匹配 Eremex 文档和演示页面标题中使用的相同术语。
- **仍未解决**：请通过 [Support Center](https://sc.eremexcontrols.net) 与我们联系，或参阅[技术支持服务](technical-support-services.md)。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
