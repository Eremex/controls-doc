---
title: 注册 Eremex 视觉主题
order: 200
seealso: []
---

# 注册 Eremex 视觉主题

您需要将 Eremex 视觉主题添加到项目中并注册它们，以确保 Eremex 控件正确渲染。如果未找到 Eremex 视觉主题，相应的 Eremex 控件将显示为空白。

Eremex Controls 库包含以下视觉主题：

| 主题 | 描述 | 包 |
| --- | --- | --- |
| `DeltaDesign` | 包含 Eremex 控件（`Graphics3DControl` 除外）以及一组标准 Avalonia UI 控件的视觉设置。 | `Eremex.Avalonia.Themes.DeltaDesign` 包 |
| `Controls3D` | 包含 `Graphics3DControl` 的视觉设置。 | `Eremex.Avalonia.Controls3D` 包 |


## 向项目中添加包含主题的 NuGet 包

- 如果您使用任何 Eremex 控件（`Graphics3DControl` 除外），请将 `Eremex.Avalonia.Themes.DeltaDesign` 包添加到项目中。

- 如果您使用 `Graphics3DControl`，则不需要额外的主题包。`Controls3D` 主题已在 `Eremex.Avalonia.Controls3D` 包中实现，该包也包含控件本身。

## 应注册哪个主题

- 如果您使用除 `Graphics3DControl` 之外的任何 Eremex 控件，只需要注册 `DeltaDesign` 主题。

- 如果您只使用 `Graphics3DControl`，只需要注册 `Controls3D` 主题。

- 如果您将 `Graphics3DControl` 与其他 Eremex 控件一起使用，则需要注册这两个主题。

- `DeltaDesign` 视觉主题还包含常见标准 Avalonia 控件的样式。如果您使用的标准 Avalonia 控件不受 `DeltaDesign` 主题支持，还必须注册 `Fluent` 主题。请参阅[为标准 Avalonia 控件注册 'FluentTheme' 主题](#register-the-fluenttheme-theme-for-standard-avalonia-controls)。


## 注册 Eremex 视觉主题


- 打开项目中的 _App.axaml_ 文件。
- 将所需的主题命名空间添加到 `Application` 对象中：

    ``` xml
    <!-- App.axaml file -->
    <Application ...
        xmlns:theme="clr-namespace:Eremex.AvaloniaUI.Themes.DeltaDesign;assembly=Eremex.Avalonia.Themes.DeltaDesign"

        xmlns:theme3D="clr-namespace:Eremex.AvaloniaUI.Themes.Controls3D;assembly=Eremex.Avalonia.Controls3D"
    >
    ```
  
- 在 `Application.Styles` 集合中注册 `DeltaDesign` 和/或 `Controls3D` 主题：

    ``` xml
    <Application 
        xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        x:Class="DemoCenter.App"
        xmlns:theme="clr-namespace:Eremex.AvaloniaUI.Themes.DeltaDesign;assembly=Eremex.Avalonia.Themes.DeltaDesign"
        xmlns:theme3D="clr-namespace:Eremex.AvaloniaUI.Themes.Controls3D;assembly=Eremex.Avalonia.Controls3D"
        RequestedThemeVariant="Light"
    >
    <!-- "Default" - The application's theme variant is defined by the system setting. 
        "Light" - Enables the Light theme variant.
        "Dark" - Enables the Dark theme variant. 
    -->
        <!-- .... -->
        <Application.Styles>
            <FluentTheme/>
            <theme:DeltaDesignTheme/>
            <theme3D:Controls3DTheme />
            <!-- .... -->
        </Application.Styles>
    </Application>
    ```

## 为标准 Avalonia 控件注册 'FluentTheme' 主题

`Eremex.Avalonia.Themes.DeltaDesign` 视觉主题为常见标准 Avalonia 控件定义了样式，确保它们与 `DeltaDesign` 视觉主题的渲染效果保持一致。`DeltaDesign` 主题支持的标准 Avalonia 控件包括但不限于：
Button、
Calendar、
CheckBox、
ContextMenu、
Label、
ListBox、
NotificationCard、
ProgressBar、
RadioButton、
ScrollBar、
ScrollViewer、
Separator、
Slider、
TextBox、
ToggleButton、
ToggleSwitch、
ToolTip、
UserControl 和
WindowNotificationManager。

有关支持的标准 Avalonia 控件的完整列表，请参阅主题的源代码：[Eremex Controls Themes](https://github.com/Eremex/controlthemes)

为确保 `DeltaDesign` 主题不支持的标准 Avalonia 控件正确渲染，请在项目中包含 `FluentTheme` 主题。Eremex 视觉主题应在 `FluentTheme` 主题之后注册：

``` xml
<!-- App.axaml file -->
<Application.Styles>
    <FluentTheme/>
    <theme:DeltaDesignTheme/>
</Application.Styles>
```

## 选择浅色或深色主题变体

Eremex 视觉主题支持两种颜色变体：浅色和深色。

设置 `Application.RequestedThemeVariant` 属性（例如在 _App.axaml_ 文件中），以指定主题的颜色变体。

``` xml
<Application 
    RequestedThemeVariant="Default" ... >
    <!-- "Default" - The application's theme is defined by the system setting. 
         "Light" - Enables the Light theme.
         "Dark" - Enables the Dark theme. 
    -->
</Application>
```


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
