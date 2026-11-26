---
title: 工具栏和菜单
order: 60000
seealso: []
---

# 工具栏和菜单 {#toolbars-and-menus}

EMX Controls 库包含 [`ToolbarManager`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarManager.md) 组件，允许您在应用程序中创建传统的 Toolbars & Menus 或 [Ribbon UI](../ribbon/index.md)。 [`ToolbarManager`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarManager.md) 为 arrange 提供了丰富的功能，可以管理传统工具栏、创建上下文菜单、调整工具栏视图和行为设置以及在运行时自定义工具栏。

![toolbars](../../images/toolbars.png)

您可以使用多种工具栏项类型来创建菜单 UI：常规按钮、复选按钮、编辑器、标签、子菜单和组项目。

用户可以自定义工具栏。在运行时他们可以选择显示他们需要的命令。

Toolbar&Menu 库的主要特性包括：

- 用户定制：
    - 栏拖放 — 允许用户使用拖动手柄重新排列栏。
    - 自定义模式和自定义窗口 - 在自定义窗口中，用户可以更改现有工具栏的可见性，并创建自定义工具栏。用户可以使用拖放操作隐藏、恢复和移动工具栏项目。
    - 快速自定义 - 用户可以按住 Alt 键，使用拖放功能在栏内和栏之间移动项目。无需激活定制模式/定制窗口即可执行快速定制。

- 众多栏布局选项：
    - 各个条的水平和垂直方向。
    - 窗口内的任何位置。
    - 杠铃伸展。
    - 栏自适应布局 — 工具栏在其容纳的空间发生变化时自动隐藏和恢复其项目。
    - 选项用于显示/隐藏栏拖动手柄。
    - 选项用于显示/隐藏栏自定义按钮。
    
- 支持的栏项目：[`ToolbarButtonItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarButtonItem.md)、[`ToolbarCheckItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem.md)、[`ToolbarMenuItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarMenuItem.md)、[`ToolbarEditorItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem.md)、[`ToolbarTextItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarTextItem.md)、[`ToolbarItemGroup`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItemGroup.md) 和 [`ToolbarCheckItemGroup`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItemGroup.md)。

- 上下文菜单 — 您可以为外部控件创建上下文菜单。上下文菜单的样式设置与Toolbar&Menu库的所有组件一致。

请参阅以下主题以获取更多信息：

- [工具栏入门](get-started-with-toolbars.md)
- [Toolbars](toolbars.md)
- [弹出菜单和上下文菜单](popup-and-context-menus.md)
- [工具栏项](toolbar-items.md)
- [Toolbar Serialization](toolbar-serialization-and-deserialization.md)

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
