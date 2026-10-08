---
title: Themes
order: 10000
seealso: []
---

# Themes

In Avalonia UI, paint themes define appearance settings, resources and templates for controls. The Eremex Controls library includes the following paint themes to render the controls shipped with the library:

| Paint&nbsp;Theme | Description | Package |
| --- | --- | --- |
| `DeltaDesign` | Contains visual settings for the Eremex Controls (except [`Graphics3DControl`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl.md)) and a set of standard Avalonia UI controls. | `Eremex.Avalonia.Themes.DeltaDesign` package |
| `Controls3D` | Contains visual settings for the [`Graphics3DControl`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl.md). | `Eremex.Avalonia.Controls3D` package |

You must [add and register](register-an-eremex-paint-theme.md) an appropriate theme(s) for the Eremex controls to render correctly. Without a corresponding theme, controls will appear blank.

Eremex paint themes support Light and Dark theme variants:

![control-themes](../../images/control-themes.png)

To specify the required theme variant, use the `Application.RequestedThemeVariant` property. See the following topic for more information: 

- [Register an Eremex Paint Theme](register-an-eremex-paint-theme.md)


The `DeltaDesign` paint theme also includes styles for common standard Avalonia controls. If you use standard Avalonia controls not supported by the `DeltaDesign` theme, you must also register the `Fluent` theme. See the following topic for instructions:

- [Register the 'FluentTheme' Theme for Standard Avalonia Controls](register-an-eremex-paint-theme.md#register-the-fluenttheme-theme-for-standard-avalonia-controls).

## Theme Customization

To modify the appearance of Eremex Controls, you should customize corresponding theme settings.
The following topic explains how to modify styles for individual controls or for all Eremex controls in your project::

- [Modify Control Themes](modify-control-themes.md)


## See Also

- [Choose the Light or Dark Theme Variant](register-an-eremex-paint-theme.md#choose-the-light-or-dark-theme-variant)