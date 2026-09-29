---
title: Register an Eremex Paint Theme
order: 200
seealso: []
---

# Register an Eremex Paint Theme

You need to add Eremex paint themes to your project and register them to ensure the Eremex controls are rendered correctly. If no Eremex paint theme is found, corresponding Eremex controls are displayed blank.

The Eremex Controls library includes the following paint themes:

| Paint&nbsp;Theme | Description | Package |
| --- | --- | --- |
| `DeltaDesign` | Contains visual settings for the Eremex Controls (except `Graphics3DControl`) and a set of standard Avalonia UI controls. | `Eremex.Avalonia.Themes.DeltaDesign` package |
| `Controls3D` | Contains visual settings for the `Graphics3DControl`. | `Eremex.Avalonia.Controls3D` package |


## Add a NuGet Package with a Theme to Your Project

- If you use any Eremex control (except `Graphics3DControl`), add the `Eremex.Avalonia.Themes.DeltaDesign` package to your project. 

- If you use `Graphics3DControl`, no additional package with a theme is required. The `Controls3D` theme is implemented in the `Eremex.Avalonia.Controls3D` package, which contains the control itself.

## Which Theme to Register

- If you use any Eremex control except `Graphics3DControl` you only need to register the `DeltaDesign` theme. 

- If you only use `Graphics3DControl`, you only need to register the `Controls3D` theme.

- If you use `Graphics3DControl` with other Eremex controls, register both themes.

- The `DeltaDesign` paint theme also includes styles for common standard Avalonia controls. If you use standard Avalonia controls not supported by the `DeltaDesign` theme, you must also register the `Fluent` theme. See [Register the 'FluentTheme' Theme for Standard Avalonia Controls](#register-the-fluenttheme-theme-for-standard-avalonia-controls).


## Register Eremex Paint Themes


- Open the _App.axaml_ file in your project.
- Add required theme namespaces to the `Application` object:

    ``` xml
    <!-- App.axaml file -->
    <Application ...
        xmlns:theme="clr-namespace:Eremex.AvaloniaUI.Themes.DeltaDesign;assembly=Eremex.Avalonia.Themes.DeltaDesign"

        xmlns:theme3D="clr-namespace:Eremex.AvaloniaUI.Themes.Controls3D;assembly=Eremex.Avalonia.Controls3D"
    >
    ```
  
- Register the `DeltaDesign` and/or `Controls3D` theme in the `Application.Styles` collection:

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

## Register the 'FluentTheme' Theme for Standard Avalonia Controls

The `Eremex.Avalonia.Themes.DeltaDesign` paint theme defines styles for common standard Avalonia controls, ensuring they are rendered consistently with the `DeltaDesign` paint theme. The standard Avalonia controls supported by the `DeltaDesign` theme include, but are not limited to: 
Button, 
Calendar, 
CheckBox, 
ContextMenu, 
Label, 
ListBox, 
NotificationCard, 
ProgressBar, 
RadioButton, 
ScrollBar, 
ScrollViewer, 
Separator, 
Slider, 
TextBox, 
ToggleButton, 
ToggleSwitch, 
ToolTip, 
UserControl, and 
WindowNotificationManager.

For a complete list of supported standard Avalonia controls, refer to the theme's source code at: [Eremex Controls Themes](https://github.com/Eremex/controlthemes)

To ensure correct rendering of standard Avalonia controls that are not supported by the `DeltaDesign` theme, include the `FluentTheme` theme in your project. The Eremex paint themes should be registered after the `FluentTheme` theme:

``` xml
<!-- App.axaml file -->
<Application.Styles>
    <FluentTheme/>
    <theme:DeltaDesignTheme/>
</Application.Styles>
```

## Choose the Light or Dark Theme Variant

The Eremex paint themes support two color variants, light and dark.

Set the `Application.RequestedThemeVariant` property (for instance, in the _App.axaml_ file) to specify the theme's color variant.

``` xml
<Application 
    RequestedThemeVariant="Default" ... >
    <!-- "Default" - The application's theme is defined by the system setting. 
         "Light" - Enables the Light theme.
         "Dark" - Enables the Dark theme. 
    -->
</Application>
```