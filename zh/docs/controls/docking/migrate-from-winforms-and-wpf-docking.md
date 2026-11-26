---
title: 从 WinForms 和 WPF 停靠迁移到 Avalonia Docking UI
order: 64000
seealso: []
---

# 从 WinForms 和 WPF 停靠迁移到 Avalonia Docking UI {#migrate-from-winforms-and-wpf-docking-to-avalonia-docking-ui}

如果您曾在 Windows Forms 或 WPF 中使用停靠管理器构建 IDE 风格的界面，并正在迁移到 Avalonia UI，那么 Eremex Avalonia UI Controls 库的 Docking UI 会让您感到熟悉。该库仅面向 Avalonia UI：不包含用于 Windows Forms 或 WPF 的控件。**Dock 管理器**组件可在跨平台的 Avalonia UI 应用程序（Windows、Linux、macOS）中创建可停靠、可自动隐藏和可浮动的工具面板，以及选项卡式文档区域。

本主题将您已熟悉的概念映射到该库的构建块，并说明在何处可以找到详细信息。

## 概念对照 {#concept-map}

| 您需要的功能 | Eremex 库中的构建块 |
| --- | --- |
| 管理整个停靠布局的组件 | [`DockManager`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager.md) - 请参阅 [Dock 管理器和 Dock 项目](dock-manager.md) |
| 工具窗口（Solution Explorer、Properties、Output 等） | [`DockPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane.md) - 请参阅[停靠面板和容器](dock-panes-and-containers.md) |
| 主区域中的文档选项卡（选项卡式 MDI） | [`DocumentPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentPane.md) - 请参阅[文档面板](document-panes.md) |
| 一组选项卡 | [`TabbedGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/TabbedGroup.md)（停靠窗格的选项卡容器）和 [`DocumentGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentGroup.md)（文档窗格的选项卡容器） |
| 并排或堆叠、由拆分器分隔的面板 | [`DockGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup.md)（拆分容器）- 请参阅[拆分面板](dock-panes-and-containers.md#split-panels) |
| 从窗口边缘滑出的面板 | 自动隐藏 - 请参阅[自动隐藏面板](dock-panes-and-containers.md#auto-hide-panels) |
| 位于独立窗口中的面板 | [`FloatGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup.md) - 请参阅[浮动面板](dock-panes-and-containers.md#floating-panels) |
| 显示面板将停靠位置的拖放指示 | 停靠引导 - 请参阅 [Dock 管理器和 Dock 项目](dock-manager.md#dock-guides)，以及用于隐藏特定指示的 [`DockManager.CustomizeDockGuide`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/CustomizeDockGuide.md) 事件（1.5 版） |
| 使用 Ctrl+Tab 切换窗口 | [文档切换器](document-switcher.md) |
| 在会话之间保存和恢复布局 | [保存和恢复面板布局](save-and-restore-layout.md) |
| 在代码中构建布局（排列、拆分、浮动、激活、关闭） | [在代码中执行停靠操作](perform-dock-operations-in-code.md) |
| 由 ViewModel 驱动的布局 | [使用 MVVM 模式填充停靠项](use-mvvm-pattern-to-populate-dock-items.md) |

## 值得了解的差异 {#differences-worth-knowing}

- **XAML 优先。** 布局在 XAML 中声明（Dock 管理器包含停靠窗格、文档窗格和组），停靠操作也可以在代码中执行。
- **MVVM 支持。** 可以从 ViewModel 集合创建面板，因此停靠布局无需代码隐藏即可融入 MVVM 应用程序。
- **布局序列化。** 可以使用 [`DockManager.SaveLayout`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/SaveLayout.md) 和 [`DockManager.RestoreLayout`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/RestoreLayout.md) 方法保存和恢复停靠面板和文档的布局。
- **跨平台。** 同一 Docking UI 可在 Avalonia UI 支持的所有平台上运行。

## 最小布局 {#a-minimal-layout}

以下示例展示了典型布局的结构：一个文档区域，其下方是 *Error List* 面板，旁边是一个包含两个工具面板的选项卡容器。有关分步演练，请参阅 [Docking 入门指南](get-started-with-docking.md)。

``` xml
xmlns:mxd="https://schemas.eremexcontrols.net/avalonia/docking"

<mxd:DockManager>
    <mxd:DockGroup>
        <mxd:DockGroup Orientation="Vertical">
            <mxd:DocumentGroup></mxd:DocumentGroup>
            <mxd:DockPane Header="Error List"/>
        </mxd:DockGroup>
        <mxd:TabbedGroup>
            <mxd:DockPane Header="Properties"/>
            <mxd:DockPane Header="Debug"/>
        </mxd:TabbedGroup>
    </mxd:DockGroup>
</mxd:DockManager>
```

## 后续步骤 {#where-to-go-next}

- [Docking 入门指南](get-started-with-docking.md)
- [Docking 界面概述](index.md)
- [示例](examples/index.md)

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
