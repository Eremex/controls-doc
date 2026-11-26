---
title: 快速访问工具栏
order: 600
seealso: []
---

# 快速访问工具栏 {#quick-access-toolbar}

Ribbon 快速访问工具栏是一个可自定义的工具栏，显示常用的 [Ribbon 项](ribbon-items.md)。

![ribbon-qat](../../images/ribbon-qat.png)

用户可以在运行时使用上下文菜单向 Ribbon 快速访问工具栏添加项目或从中删除项目。

## 在快速访问工具栏中添加和删除项目 {#add-and-remove-items-to-the-quick-access-toolbar}

要将项目添加到快速访问工具栏在运行时，用户可以右键单击项，然后在出现的上下文菜单中选择“**添加到快速访问工具栏**”。

![ribbon-qat-add-items-menu](../../images/ribbon-qat-add-items-menu.png)

要从快速访问工具栏删除项，请右键单击项并选择 **从快速访问工具栏删除**。

![ribbon-qat-remove-items-menu](../../images/ribbon-qat-remove-items-menu.png)

要了解如何在应用程序运行之间保存和恢复对 Ribbon 快速访问工具栏的用户更改，请遵循以下主题：

- [Ribbon 序列化和反序列化](ribbon-serialization-and-deserialization.md)

### 禁用快速访问工具栏自定义 {#disable-quick-access-toolbar-customization}

将 [`RibbonControl.AllowQuickAccessToolbarCustomizationMenu`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonControl/AllowQuickAccessToolbarCustomizationMenu.md) 属性设置为 `false` 可隐藏 **添加到快速访问工具栏** 和 **从快速访问工具栏删除** 命令，从而阻止用户自定义快速访问工具栏。

### 在代码中将项目添加到快速访问工具栏 {#add-items-to-the-quick-access-toolbar-in-code}

要使用代码中的项目填充快速访问工具栏，请使用 [`RibbonControl.QuickAccessToolbarItems`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonControl/QuickAccessToolbarItems.md) 集合。您还可以使用此集合来访问然后修改代码隐藏中的快速访问工具栏项目。

``` xml
<mxr:RibbonControl.QuickAccessToolbarItems>
    <mxb:ToolbarButtonItem Header="Cut" KeyTip="CT"
                           Glyph="{x:Static icons:Basic.Cut}" />
    <mxb:ToolbarButtonItem Header="Copy" KeyTip="CP"
                           Glyph="{x:Static icons:Basic.Copy}" />
    <mxb:ToolbarButtonItem Header="Paste" KeyTip="P"
                           Glyph="{x:Static icons:Basic.Paste}" />
</mxr:RibbonControl.QuickAccessToolbarItems>
```

使用 [`RibbonControl.QuickAccessToolbarItemsSource`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonControl/QuickAccessToolbarItemsSource.md) 属性可使用存储在视图模型中的业务对象集合中的项目填充快速访问工具栏。相应的数据模板应定义功能区项目并从基础业务对象初始化其设置。


## 更改位置和可见性 {#change-the-position-and-visibility}

Ribbon 快速访问工具栏可以显示在 Ribbon 主命令区域的上方（默认）或下方。

用户可以单击快速访问工具栏中的下拉按钮，然后选择 **在 Ribbon 下方/上方显示快速访问工具栏** 命令来更改工具栏的位置。

![ribbon-qat-change-position-menu](../../images/ribbon-qat-change-position-menu.png)

![ribbon-qat-below-change-position-menu](../../images/ribbon-qat-below-change-position-menu.png)

您可以使用 [`RibbonControl.IsQuickAccessToolbarCustomizationButtonVisible`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonControl/IsQuickAccessToolbarCustomizationButtonVisible.md) 属性隐藏快速访问工具栏中的下拉按钮。

以下属性允许您在代码中控件位置和快速访问工具栏的可见性：

- [`RibbonControl.QuickAccessToolbarLocation`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonControl/QuickAccessToolbarLocation.md) — 允许您将快速访问工具栏设置为 choose between、`Top` 和 `Bottom` 位置。
- [`RibbonControl.IsQuickAccessToolbarVisible`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonControl/IsQuickAccessToolbarVisible.md) — 允许您隐藏快速访问工具栏。

## 另请参阅 {#see-also}

- [Ribbon 序列化和反序列化](ribbon-serialization-and-deserialization.md)

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
