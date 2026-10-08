# ToolbarItem class

Provides the base functionality for items displayed in toolbars, menus, and ribbons.

**Namespace:** [`Eremex.AvaloniaUI.Controls.Bars`](./index.md)  
**Assembly:** `Eremex.Avalonia.Controls.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Declaration

```csharp
public class ToolbarItem : TemplatedControl, IBorderStateProvider, ICommandSource, INavigationItem, 
    IToolbarActionItem
```

## Public Members

| name | description |
| --- | --- |
| [ToolbarItem](ToolbarItem/ToolbarItem.md)() | Initializes a new instance of the ToolbarItem class. |
| [Alignment](ToolbarItem/Alignment.md) { get; set; } | Gets or sets the alignment of the item within its toolbar. |
| [Category](ToolbarItem/Category.md) { get; set; } | Gets or sets the category used to organize the item during customization. |
| [CloseMenuOnClick](ToolbarItem/CloseMenuOnClick.md) { get; set; } | Gets or sets whether clicking the item closes its containing menu. |
| [Command](ToolbarItem/Command.md) { get; set; } | Gets or sets the command executed when the item is activated. |
| [CommandParameter](ToolbarItem/CommandParameter.md) { get; set; } | Gets or sets the parameter passed to the item's command. |
| [CustomizationName](ToolbarItem/CustomizationName.md) { get; set; } | Gets or sets the name displayed for the item during customization. |
| [Description](ToolbarItem/Description.md) { get; set; } | Gets or sets the additional descriptive text displayed for the item. |
| [DisplayMode](ToolbarItem/DisplayMode.md) { get; set; } | Gets or sets which parts of the item are displayed. |
| [Glyph](ToolbarItem/Glyph.md) { get; set; } | Gets or sets the image displayed for the item. |
| [GlyphAlignment](ToolbarItem/GlyphAlignment.md) { get; set; } | Gets or sets the position of the glyph relative to the item header. |
| [GlyphSize](ToolbarItem/GlyphSize.md) { get; set; } | Gets or sets the size used to display the item's glyph. |
| [GlyphSizeMode](ToolbarItem/GlyphSizeMode.md) { get; set; } | Gets or sets how the size of the item's glyph is determined. |
| [GlyphTemplate](ToolbarItem/GlyphTemplate.md) { get; set; } | Gets or sets the template used to display the item's glyph. |
| [Group](ToolbarItem/Group.md) { get; } | Gets the toolbar item group that contains the item, or null if its holder is not a group. |
| [Header](ToolbarItem/Header.md) { get; set; } | Gets or sets the item's header content. |
| [HeaderContentHorizontalAlignment](ToolbarItem/HeaderContentHorizontalAlignment.md) { get; set; } | Gets or sets the horizontal alignment of the item header's content. |
| [HeaderTemplate](ToolbarItem/HeaderTemplate.md) { get; set; } | Gets or sets the template used to display the item's header. |
| [Hint](ToolbarItem/Hint.md) { get; set; } | Gets or sets the tooltip text displayed for the item. |
| [Holder](ToolbarItem/Holder.md) { get; } | Gets the container that owns the item. |
| [HotKey](ToolbarItem/HotKey.md) { get; set; } | Gets or sets the keyboard shortcut that activates the item. |
| [HotKeyDisplayString](ToolbarItem/HotKeyDisplayString.md) { get; set; } | Gets or sets the text displayed for the item's keyboard shortcut. |
| [Id](ToolbarItem/Id.md) { get; set; } | Gets or sets the identifier of the toolbar item. |
| [IsLocatedInRibbon](ToolbarItem/IsLocatedInRibbon.md) { get; } | Gets whether the item belongs to a ribbon. |
| [IsSelected](ToolbarItem/IsSelected.md) { get; set; } | Gets or sets whether the item is selected. |
| [KeyTip](ToolbarItem/KeyTip.md) { get; set; } | Gets or sets the key sequence displayed to activate this item during key tip navigation. |
| [Manager](ToolbarItem/Manager.md) { get; set; } | Gets or sets the toolbar manager associated with this object. |
| [Palette](ToolbarItem/Palette.md) { get; set; } | Gets or sets the palette used to render the item's glyph. |
| [RecognizesAccessKey](ToolbarItem/RecognizesAccessKey.md) { get; set; } | Gets or sets whether an underscore in the header identifies an access key. |
| [RibbonCommandLayout](ToolbarItem/RibbonCommandLayout.md) { get; } | Gets the ribbon command layout used to display the item. |
| [ScreenBounds](ToolbarItem/ScreenBounds.md) { get; } | Gets the bounds of the item in screen coordinates. |
| [SerializationInfo](ToolbarItem/SerializationInfo.md) { get; } | Gets the layout information used during serialization or deserialization. |
| [SerializationName](ToolbarItem/SerializationName.md) { get; set; } | Gets or sets the name used to identify this object during layout serialization. |
| [ShowSeparator](ToolbarItem/ShowSeparator.md) { get; set; } | Gets or sets whether a separator is displayed before the item. |
| [Toolbar](ToolbarItem/Toolbar.md) { get; } | Gets the toolbar that contains the item. |
| event [Click](ToolbarItem/Click.md) | Occurs when the item is clicked. |
| event [Press](ToolbarItem/Press.md) | Occurs when the pointer button is pressed over the item. |
| [GetRootHolder](ToolbarItem/GetRootHolder.md)() | Returns the outermost holder of the toolbar item. |
| virtual [GetShortcutDisplayString](ToolbarItem/GetShortcutDisplayString.md)() | Returns the text used to display the item's keyboard shortcut. |
| [OnDragLeave](ToolbarItem/OnDragLeave.md)() | Clears the item's drag-over state. |
| [OnDropDownBorderEnter](ToolbarItem/OnDropDownBorderEnter.md)(…) | Processes the pointer entering the item's drop-down area. |
| [OnDropDownBorderLeave](ToolbarItem/OnDropDownBorderLeave.md)(…) | Processes the pointer leaving the item's drop-down area. |
| [OnDropDownBorderReleased](ToolbarItem/OnDropDownBorderReleased.md)(…) | Processes a pointer release over the item's drop-down area. |
| override [ToString](ToolbarItem/ToString.md)() |  |

## See Also

* namespace [Eremex.AvaloniaUI.Controls.Bars](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->
