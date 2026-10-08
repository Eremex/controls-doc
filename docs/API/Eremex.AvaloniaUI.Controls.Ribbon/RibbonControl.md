# RibbonControl class

Displays commands organized into pages and groups, with an application button and a Quick Access Toolbar.

**Namespace:** [`Eremex.AvaloniaUI.Controls.Ribbon`](./index.md)  
**Assembly:** `Eremex.Avalonia.Controls.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Declaration

```csharp
public class RibbonControl : TemplatedControl, IMxMainMenu, INavigatable
```

## Public Members

| name | description |
| --- | --- |
| [RibbonControl](RibbonControl/RibbonControl.md)() | Initializes a new instance of the RibbonControl class. |
| [AllowQuickAccessToolbarCustomizationMenu](RibbonControl/AllowQuickAccessToolbarCustomizationMenu.md) { get; set; } | Gets or sets whether users can open the Quick Access Toolbar customization menu. |
| [ApplicationButtonCommand](RibbonControl/ApplicationButtonCommand.md) { get; set; } | Gets or sets the command executed when the application button is activated. |
| [ApplicationButtonCommandParameter](RibbonControl/ApplicationButtonCommandParameter.md) { get; set; } | Gets or sets the parameter passed to the application button's command. |
| [ApplicationButtonContent](RibbonControl/ApplicationButtonContent.md) { get; set; } | Gets or sets the content displayed on the application button. |
| [ApplicationButtonContentTemplate](RibbonControl/ApplicationButtonContentTemplate.md) { get; set; } | Gets or sets the template used to display the application button's content. |
| [ApplicationButtonDropDownControl](RibbonControl/ApplicationButtonDropDownControl.md) { get; set; } | Gets or sets the popup displayed by the application button. |
| [ApplicationButtonGlyph](RibbonControl/ApplicationButtonGlyph.md) { get; set; } | Gets or sets the image displayed on the application button. |
| [ApplicationButtonKeyTip](RibbonControl/ApplicationButtonKeyTip.md) { get; set; } | Gets or sets the key tip used to activate the application button. |
| [CommandLayout](RibbonControl/CommandLayout.md) { get; set; } | Gets or sets the command layout used by the ribbon. |
| [GlyphSizeInSimplifiedLayout](RibbonControl/GlyphSizeInSimplifiedLayout.md) { get; set; } | Gets or sets the glyph size used in the simplified ribbon layout. |
| [IsApplicationButtonVisible](RibbonControl/IsApplicationButtonVisible.md) { get; set; } | Gets or sets whether the application button is visible. |
| [IsCommandLayoutSelectionButtonVisible](RibbonControl/IsCommandLayoutSelectionButtonVisible.md) { get; set; } | Gets or sets whether the button for switching the ribbon command layout is visible. |
| [IsQuickAccessToolbarCustomizationButtonVisible](RibbonControl/IsQuickAccessToolbarCustomizationButtonVisible.md) { get; set; } | Gets or sets whether the Quick Access Toolbar customization button is visible. |
| [IsQuickAccessToolbarVisible](RibbonControl/IsQuickAccessToolbarVisible.md) { get; set; } | Gets or sets whether the Quick Access Toolbar is visible. |
| [Manager](RibbonControl/Manager.md) { get; set; } | Gets or sets the toolbar manager associated with this object. |
| [PageHeaderItems](RibbonControl/PageHeaderItems.md) { get; } | Gets the collection of items displayed beside the ribbon page headers. |
| [PageHeaderItemsSource](RibbonControl/PageHeaderItemsSource.md) { get; set; } | Gets or sets the collection whose items are used to generate items beside the ribbon page headers. |
| [Pages](RibbonControl/Pages.md) { get; } | Gets the collection of ribbon pages. |
| [PagesSource](RibbonControl/PagesSource.md) { get; set; } | Gets or sets the collection whose items are used to generate ribbon pages. |
| [QuickAccessToolbarItems](RibbonControl/QuickAccessToolbarItems.md) { get; } | Gets the collection of items displayed in the Quick Access Toolbar. |
| [QuickAccessToolbarItemsSource](RibbonControl/QuickAccessToolbarItemsSource.md) { get; set; } | Gets or sets the collection whose items are used to generate Quick Access Toolbar items. |
| [QuickAccessToolbarLocation](RibbonControl/QuickAccessToolbarLocation.md) { get; set; } | Gets or sets the location of the Quick Access Toolbar relative to the ribbon. |
| [SelectedPage](RibbonControl/SelectedPage.md) { get; set; } | Gets or sets the currently selected ribbon page. |
| [SerializationInfo](RibbonControl/SerializationInfo.md) { get; } | Gets the layout information used during serialization or deserialization. |
| [SmallGlyphSize](RibbonControl/SmallGlyphSize.md) { get; set; } | Gets or sets the size used to display small ribbon glyphs. |
| event [ApplicationButtonClick](RibbonControl/ApplicationButtonClick.md) | Occurs when the application button is clicked. |
| event [ApplicationButtonPress](RibbonControl/ApplicationButtonPress.md) | Occurs when the pointer button is pressed over the application button. |
| [ResetNavigation](RibbonControl/ResetNavigation.md)() | Resets keyboard navigation within the ribbon. |
| [RestoreLayout](RibbonControl/RestoreLayout.md)(…) | Restores the layout from the specified stream using the default serialization settings. (2 methods) |
| [SaveLayout](RibbonControl/SaveLayout.md)(…) | Saves the layout to the specified stream using the default serialization settings. (2 methods) |
| static [GetDisplayMode](RibbonControl/GetDisplayMode.md)(…) | Gets the allowed ribbon display modes for the specified item. |
| static [SetDisplayMode](RibbonControl/SetDisplayMode.md)(…) | Sets the allowed ribbon display modes for the specified item. |

## See Also

* namespace [Eremex.AvaloniaUI.Controls.Ribbon](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->
