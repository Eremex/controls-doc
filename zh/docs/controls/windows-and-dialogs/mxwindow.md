---
title: MxWindow
order: 200
seealso: []
---

# MxWindow

如果您正在使用 Eremex Avalonia UI 控件,建议在应用程序的主窗口和其他窗口中使用 `MxWindow` 组件。这可以使您在整个 Avalonia UI 项目中保持一致的用户界面。

`MxWindow` 是一种窗口,它根据 [Eremex 视觉主题](../themes/index.md) 绘制其元素(背景、边框和标题栏)。

![mxwindow-big](../../images/mxwindow-big.png)

## 添加主题包并注册绘制主题

要使用 `MxWindow` 和其他 Eremex Avalonia UI 控件,请引入包含 Eremex 绘制主题的[程序包](../../whats-included/assemblies.md)。下面的主题展示了如何在您的应用程序中注册绘制主题: 

- [注册 Eremex 绘制主题](../themes/register-an-eremex-paint-theme.md)。


## 创建 MxWindow

`MxWindow` 是标准 Avalonia UI `Window` 组件的派生类。您可以将现有应用程序中的 `Window` 组件无缝替换为 `MxWindow`,以使用 Eremex 绘制主题。以下 XAML 代码展示了一个示例 `MxWindow` 对象声明:

``` xml
<mx:MxWindow 
    xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
    Title="MxWindow"
    ...
>

</mx:MxWindow>
```

[Eremex 项目模板](../../whats-included/project-templates.md)允许您创建带有 Eremex Controls 的新 Avalonia UI 应用程序。这些模板创建的新项目中,主窗口由 `MxWindow` 组件封装。

![mxwindow](../../images/mxwindow.png)

## MxWindow 设置

`MxWindow` 在标准 `Window` 组件公开的设置基础上扩展了以下选项,用于指定标题栏中标准按钮的可见性和图形:

- `ShowCloseButton` — 指定关闭按钮的可见性。
- `ShowMaximizeButton` — 指定最大化按钮的可见性。
- `ShowMinimizeButton` — 指定最小化按钮的可见性。

- `CloseButtonGlyph` — 关闭按钮的图形。
- `MaximizeButtonGlyph` — 最大化按钮的图形。
- `MinimizeButtonGlyph` — 最小化按钮的图形。
- `RestoreButtonGlyph` — 还原按钮的图形。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
