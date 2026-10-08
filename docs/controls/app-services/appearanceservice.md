---
title: IAppearanceService
order: 500
seealso: []
---


# IAppearanceService

[`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) provides a platform-agnostic way to access the appearance choices supported by the DeltaDesign theme and apply the chosen one. It allows your ViewModel to change the theme variant, color palette, and layout density at runtime without referencing any UI framework type directly.

<!-- TODO
image
app-services-iappearanceservice
-->

Main features include:

- Theme variants — Provides access to available theme variants (`Light` and `Dark`).
- Color palettes — Provides access to the color palettes in the DeltaDesign theme, such as `Nova`, `Helios`, `Terra`, `Vega`, and `Atlas`.
- Layout densities — Provides access to the layout densities available in the DeltaDesign theme (`Compact`, `Standard`, and `Spacious`).
- Immediate application — You can change a dedicated option of [`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) to immediately change the corresponding theme setting.
- Bindable to selectors — The service implements the `INotifyPropertyChanged` interface and is designed to be bound directly to a ribbon gallery, a combo box, a menu, or any other selector.


## Interface Definition

```csharp
public interface IAppearanceService : INotifyPropertyChanged
{
    // A list of available theme variants (light/dark).
    IReadOnlyList<IAppearanceOption> ThemeVariants { get; }

    // A list of available color palettes.
    IReadOnlyList<IAppearanceOption> Palettes { get; }

    // A list of available layout densities.
    IReadOnlyList<IAppearanceOption> Densities { get; }

    // The chosen theme variant. Assigning it recolors the running application at once.
    IAppearanceOption SelectedThemeVariant { get; set; }

    // The chosen theme palette. Assigning it recolors the running application at once.
    IAppearanceOption SelectedPalette { get; set; }

    // The chosen density. Assigning it resizes the controls of the running application at once.
    IAppearanceOption SelectedDensity { get; set; }
}
```

## IAppearanceOption

Each item in the [`ThemeVariants`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService/ThemeVariants.md), [`Palettes`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService/Palettes.md), and [`Densities`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService/Densities.md) lists implements the [`IAppearanceOption`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceOption.md) interface:

```csharp
public interface IAppearanceOption
{
    // The text shown for this choice.
    string Header { get; }
}
```

Like the other service interfaces, the [`IAppearanceOption`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceOption.md) interface is free of UI framework types. It only contains a string property that specifies the caption of a theme option. However, actual implementations of the [`IAppearanceOption`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceOption.md) interface return richer objects, listed below:

| [`IAppearanceOption`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceOption.md) Implementation | Description |
|---|---|
| [`ThemeOption`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ThemeOption.md) class | A light or dark theme variant. Additional properties include: <br> - [`ThemeOption.Variant`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ThemeOption/Variant.md) — the Avalonia.Styling.ThemeVariant applied when this option is chosen. |
| [`PaletteOption`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/PaletteOption.md) class | A color palette.  Additional properties include: <br>- [`PaletteOption.Palette`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/PaletteOption/Palette.md) — the palette applied when this option is chosen (Nova, Helios, Terra, Vega, Atlas, etc.);<br> - [`PaletteOption.Accent`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/PaletteOption/Accent.md) — a read-only brush that represents the palette's accent color. The [`PaletteOption.Accent`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/PaletteOption/Accent.md) property allows you to show a color swatch in a selector, so the user can preview a palette before picking it.|
| [`DensityOption`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DensityOption.md) class | A layout density. Additional properties include: <br>- [`DensityOption.Density`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DensityOption/Density.md) — the density applied when this option is chosen (Compact, Standard, or Spacious). |

The [`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) implementation returns these richer objects. For instance, the actual return value of [`IAppearanceService.SelectedPalette`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService/SelectedPalette.md) is a [`PaletteOption`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/PaletteOption.md) object.

## How to Use IAppearanceService

1. In your ViewModel, expose the [`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) service as a property. 
2. In your View, bind your selector controls to the members of this property.

### Access the Service

You need to access the [`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) service in your ViewModel to expose it as a property.

There are two ways to access an [`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) object in a ViewModel:

- Through the `Service<T>()` helper method. This is a convenient approach to obtain registered application services shipped with the Eremex Controls library.
- Through constructor injection.

#### Service<T>() Helper

Implement a helper `Service<T>()` method in your ViewModel to get a requested service using the static `ApplicationServicesContext.GetRequiredService<T>()` method.

```csharp
using Eremex.AvaloniaUI.Controls.ApplicationServices;
using CommunityToolkit.Mvvm.Input;

public partial class MyViewModel : ObservableObject
{
    // Provides access to any registered service
    protected static T Service<T>() where T : class
        => ApplicationServicesContext.GetRequiredService<T>();

    public IAppearanceService Appearance { get; } = Service<IAppearanceService>();
}
```

In the App.axaml.cs file, ensure that Eremex application services are registered using [`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) and [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md) as follows:

```csharp
public class App : Application
{
    public override void OnFrameworkInitializationCompleted()
    {
        RegisterApplicationServices();
        //...
    }

    static void RegisterApplicationServices()
    {
        // Register built-in services.
        var serviceProvider = new SimpleServiceProvider();
        ApplicationServicesContext.RegisterApplicationServices(serviceProvider.AddSingleton);
        ApplicationServicesContext.SetCurrent(serviceProvider);
    }
}
```

#### Constructor Injection

Implement a constructor in your ViewModel with [`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) as a parameter. When you instantiate the ViewModel, pass the service object to this constructor.

```csharp
public partial class MainViewModel : ObservableObject
{
    public MainViewModel(IAppearanceService appearance)
    {
        Appearance = appearance;
    }

    public IAppearanceService Appearance { get; }
}
```

### Expose the Service from the ViewModel

Expose [`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) as a public property. UI controls in the View will bind to it directly:

The following example creates an _Appearance_ property of the [`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) type and initializes it using the `Service<T>` helper. 

```csharp
public partial class MainViewModel : ObservableObject
{
    public IAppearanceService Appearance { get; }

    public MainViewModel(ThemeVariant? startupThemeVariant = null)
    {
        Appearance = Service<IAppearanceService>();
        Appearance.SelectedThemeVariant = FindTheme(startupThemeVariant);
        //...
    }

    private IAppearanceOption? FindTheme(ThemeVariant? variant)
        => variant is null
            ? null
            : Appearance.ThemeVariants.FirstOrDefault(
                x => string.Equals(x.Header, variant.ToString(), StringComparison.OrdinalIgnoreCase));

    // Provides access to any registered service
    protected static T Service<T>() where T : class
        => ApplicationServicesContext.GetRequiredService<T>();
}
```

### Example - Create a Palette Selector in a View

This example creates a combo box ([`ComboBoxEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md) control) that lists the available theme palettes. When an item is selected in the control's dropdown menu, the corresponding palette is applied to the application.

In this example: 

- [`ComboBoxEditor.ItemsSource`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor/ItemsSource.md) is bound to `Appearance.Palettes` to list all available palettes in the dropdown menu.
- [`ComboBoxEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) is bound to `Appearance.SelectedPalette`. Picking an item in the control's dropdown applies the corresponding theme palette.
- The ComboBoxEditor's item template displays the palette's accent color as a swatch next to the palette's name (header).

```xml
<mxe:ComboBoxEditor x:Name="themePaletteComboBox"
                    ItemsSource="{Binding Appearance.Palettes}"
                    EditorValue="{Binding Appearance.SelectedPalette}"
                    IsTextEditable="False"
                    ApplyItemTemplateToEditBox="True"
                    Width="150" Margin="0,0,10,0">
    <mxe:ComboBoxEditor.ItemTemplate>
        <DataTemplate x:DataType="appsvc:PaletteOption">
            <StackPanel Orientation="Horizontal" Spacing="8">
                <Border Width="12" Height="12" CornerRadius="2" VerticalAlignment="Center"
                        Background="{Binding Accent}"
                        BorderThickness="1"
                        BorderBrush="{DynamicResource Outline/Neutral/Transparent/Medium}"/>
                <TextBlock Text="{Binding Header}" VerticalAlignment="Center"/>
            </StackPanel>
        </DataTemplate>
    </mxe:ComboBoxEditor.ItemTemplate>
</mxe:ComboBoxEditor>
```

See the complete code in the [Controls Demo](../../index.md#demo-application) application.

### Example - Create a Density Selector

This example creates a combo box ([`ComboBoxEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md) control) populated with layout density options. When a user selects an item, the corresponding layout density is automatically applied.

To show custom images for density values in the combo box, this example populates the control with items directly from the `Eremex.AvaloniaUI.Themes.DeltaDesign.Density` enumeration. The images are provided using a custom `NameToImageConverter` converter and displayed using the [`ComboBoxEditor.ItemTemplate`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor/ItemTemplate.md) property.

```xml
<mxe:ComboBoxEditor x:Name="densityComboBox"
                    ItemsSource="{mxc:EnumItemsSource EnumType=ddt:Density, ShowImages=True,
                                  NameToImageConverter={views:DensityToIconConverter}}"
                    EditorValueChanged="DensityComboBoxEditor_EditorValueChanged"
                    IsTextEditable="False"
                    Margin="0,0,10,0">
    <mxe:ComboBoxEditor.ItemTemplate>
        <DataTemplate x:DataType="mxc:EnumMemberInfo">
            <StackPanel Orientation="Horizontal" Spacing="8">
                <Image Source="{Binding Image}" Stretch="None" VerticalAlignment="Center"/>
                <TextBlock Text="{Binding Name}" VerticalAlignment="Center"/>
            </StackPanel>
        </DataTemplate>
    </mxe:ComboBoxEditor.ItemTemplate>
</mxe:ComboBoxEditor>
```

See the complete code in the [Controls Demo](../../index.md#demo-application) application.



### Change Theme Settings in Code

Use the [`SelectedThemeVariant`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService/SelectedThemeVariant.md), [`SelectedPalette`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService/SelectedPalette.md), and [`SelectedDensity`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService/SelectedDensity.md) properties to change theme settings in code. 

```csharp
public IAppearanceService Appearance { get; } = Service<IAppearanceService>();

public void ChangeThemeSettings() 
{
    Appearance.SelectedThemeVariant = Appearance.ThemeVariants[0]; // Switch to the default theme variant.
    Appearance.SelectedPalette = Appearance.Palettes[2];  // Apply the third palette.
    Appearance.SelectedDensity = Appearance.Densities[0]; // Switch to the most compact density.
}
```

