---
title: 视觉主题
order: 10000
seealso: []
---

# 视觉主题

在 Avalonia UI 中，视觉主题定义了控件的外观设置、资源和模板。Eremex Controls 库包含以下视觉主题，用于渲染库中提供的控件：

| 视觉&nbsp;主题 | 说明 | 程序包 |
| --- | --- | --- |
| `DeltaDesign` | 包含 Eremex 控件（`Graphics3DControl` 除外）以及一组标准 Avalonia UI 控件的视觉设置。 | `Eremex.Avalonia.Themes.DeltaDesign` 程序包 |
| `Controls3D` | 包含 `Graphics3DControl` 的视觉设置。 | `Eremex.Avalonia.Controls3D` 程序包 |

您必须[添加并注册](register-an-eremex-paint-theme.md)适当的主题，Eremex 控件才能正确渲染。如果没有相应的主题，控件将显示为空白。

Eremex 视觉主题支持浅色和深色两种主题变体：

![control-themes](../../images/control-themes.png)

要指定所需的主题变体，请使用 `Application.RequestedThemeVariant` 属性。有关更多信息，请参阅以下主题：

- [注册 Eremex 视觉主题](register-an-eremex-paint-theme.md)


`DeltaDesign` 视觉主题还包含常用标准 Avalonia 控件的样式。如果您使用的标准 Avalonia 控件不受 `DeltaDesign` 主题支持，则还必须注册 `Fluent` 主题。有关说明，请参阅以下主题：

- [为标准 Avalonia 控件注册 'FluentTheme' 主题](register-an-eremex-paint-theme.md#register-the-fluenttheme-theme-for-standard-avalonia-controls)。

## 主题自定义

要修改 Eremex 控件的外观，您应该自定义相应的主题设置。
以下主题说明了如何为单个控件或项目中的所有 Eremex 控件修改样式：

- [修改控件主题](modify-control-themes.md)


## 另请参阅

- [选择浅色或深色主题变体](register-an-eremex-paint-theme.md#choose-the-light-or-dark-theme-variant)


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
