---
title: MCP-сервер
order: 30
seealso: []
---

# MCP-сервер

Документация Eremex Controls, примеры из демонстрационного приложения и публичные ответы службы поддержки доступны AI-ассистентам для программирования (Cursor, Claude Code, OpenCode, GitHub Copilot, Windsurf, Cline и другим инструментам, совместимым с [MCP](https://modelcontextprotocol.io)) через собственный MCP-сервер:

```
https://mcp.eremexcontrols.net/
```

После подключения ассистент может подставлять в свои ответы актуальный контекст Eremex Controls — реальные имена API, реальные примеры XAML/C# и реальные ответы наших инженеров поддержки — вместо того чтобы угадывать API или опираться на устаревшие обучающие данные.

## Что индексируется

| Источник | Содержимое |
|---|---|
| Документация | Полная публичная документация на [eremexcontrols.net](https://eremexcontrols.net) |
| Примеры из демо | Реальные примеры использования из демонстрационного приложения [controls-demo](https://github.com/Eremex/controls-demo), по одной записи на каждую показанную в демо возможность |
| Центр поддержки | Публичные темы вопросов и ответов из [EMX Support Center](https://sc.eremexcontrols.net) |

Для использования сервера не нужны ни API-ключ, ни учётная запись.

## Настройка AI-ассистента

### Cursor

Добавьте в `.cursor/mcp.json` (проект) или `~/.cursor/mcp.json` (глобально):

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

Добавьте в `claude_desktop_config.json`:

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

Добавьте в настройки MCP (в `settings.json` VS Code в разделе `mcp.servers` или в собственную панель настройки MCP расширения):

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

### OpenCode

Выполните эту команду в папке проекта (добавьте `--global`, чтобы сервер был доступен во всех проектах):

```bash
opencode mcp add eremex-controls --url https://mcp.eremexcontrols.net/mcp
```

Или добавьте сервер в конфигурацию `opencode.json` / `opencode.jsonc` вручную:

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

Сервер не требует входа: `"oauth": false` не даёт OpenCode запускать авторизацию OAuth. Если OpenCode предлагает авторизоваться на сервере, задайте этот параметр в конфигурации.

### Другие MCP-клиенты

Любой клиент, поддерживающий удалённый MCP-сервер по Streamable HTTP или SSE, может подключиться напрямую:

- Streamable HTTP: `https://mcp.eremexcontrols.net/mcp`
- SSE (для старых клиентов): `https://mcp.eremexcontrols.net/sse`

## Проверка работы

После добавления конфигурации перезапустите редактор или клиент (большинство клиентов считывают конфигурацию MCP только при запуске), а затем задайте ассистенту вопрос, например:

> Using the Eremex Controls docs, show me how to add a custom in-place editor to a DataGrid column.

> How do I enable drag-and-drop between two Eremex DataGrid controls? Show a real example.

Если сервер подключён, ассистент ссылается на конкретные члены API Eremex (например, [`GridColumn.EditorProperties`](../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md), `AllowDragDrop`) и на реальный код из документации, демонстрационного приложения или центра поддержки, а не выдаёт общие догадки об Avalonia.

## Устранение неполадок

- **Инструмент не появляется**: перезапустите редактор или клиент после добавления конфигурации.
- **Нет результатов или пустой контекст**: попробуйте переформулировать вопрос, используя название контрола, например "DataGrid", "TreeList" или "PropertyGrid" — поиск сопоставляет те же термины, что используются в документации Eremex и в заголовках страниц демо.
- **Проблема не решена**: обратитесь к нам через [Support Center](https://sc.eremexcontrols.net) или см. [Услуги технической поддержки](technical-support-services.md).

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
