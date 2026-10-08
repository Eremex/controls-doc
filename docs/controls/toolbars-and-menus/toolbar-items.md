---
title: Toolbar Items
order: 80000
seealso: []
---

# Toolbar Items

Toolbar items are used to display buttons, check buttons, text labels, sub-menus, and in-place editors in toolbars and menus. You can add any number of items to each bar/menu, and create multiple hierarchy levels using sub-menus.

![toolbar-items](../../images/toolbar-items.png)

## Add Toolbar Items to a Bar and Context Menu

Use the [`Toolbar.Items`](../../API/Eremex.AvaloniaUI.Controls.Bars/Toolbar/Items.md) and [`PopupMenu.Items`](../../API/Eremex.AvaloniaUI.Controls.Bars/PopupMenu/Items.md) collections to populate bars and menus with items. In XAML, you can define items directly between the start and end `<Toolbar>`/`<PopupMenu>` tags.

The following example displays three items in a toolbar.

``` xml
xmlns:mxb="https://schemas.eremexcontrols.net/avalonia/bars"

<mxb:Toolbar x:Name="EditToolbar" ToolbarName="Edit" ShowCustomizationButton="False">
    <mxb:ToolbarButtonItem Header="Cut" Command="{Binding #textBox.Cut}" 
     IsEnabled="{Binding #textBox.CanCut}" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=Cut.svg'}" 
     Category="Edit"/>
    <mxb:ToolbarButtonItem Header="Copy" Command="{Binding #textBox.Copy}" 
     IsEnabled="{Binding #textBox.CanCopy}" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=Copy.svg'}" 
     Category="Edit"/>
    <mxb:ToolbarButtonItem Header="Paste" Command="{Binding #textBox.Paste}" 
     IsEnabled="{Binding #textBox.CanPaste}" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=Paste.svg'}" 
     Category="Edit"/>
</mxb:Toolbar>
```
## Toolbar Item Types

The toolbar library supports multiple toolbar item types. All of them are descendants of the [`ToolbarItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem.md) class, which contains settings common to all toolbar items.

### Common Toolbar Item Settings

- [`Alignment`](../../API/Eremex.AvaloniaUI.Controls.Bars/Alignment.md) — The item's alignment within the toolbar.
- [`Category`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Category.md) — The category to which the item belongs. Categories are used to organize items into logical groups within the Customization window. See the following section for more information: [Toolbar Item Categories](#toolbar-item-categories).
- [`Command`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Command.md) — A command executed when the button is clicked.
- [`CommandParameter`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/CommandParameter.md) — A command parameter passed to the specified command.
- [`DisplayMode`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/DisplayMode.md) — Gets or sets whether to display only the glyph, the header, or both.
- [`Glyph`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Glyph.md) — The item's image.
- [`GlyphAlignment`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/GlyphAlignment.md) — The glyph alignment relative to the item's header.
- [`GlyphSize`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/GlyphSize.md) — The glyph display size.
- [`Header`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Header.md) — The item's display text.
- [`ShowSeparator`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/ShowSeparator.md) — Gets or sets whether to display a separator before the item. You can also use the [`ToolbarSeparatorItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarSeparatorItem.md) bar item to insert a separator.

**Events**

- [`Click`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Click.md) — Fires when the item is left-clicked (after the left mouse button is pressed and then released).
- [`Press`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Press.md) — Fires when any mouse button is pressed over the item.

### Regular and Dropdown Buttons (ToolbarButtonItem)

Use [`ToolbarButtonItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarButtonItem.md) to create regular buttons. A click on a regular button invokes a linked command ([`Command`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Command.md)) and events ([`Click`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Click.md) and [`Press`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Press.md)). 

![toolbarbuttonitem](../../images/toolbarbuttonitem.png)

``` xml
xmlns:mxb="https://schemas.eremexcontrols.net/avalonia/bars"

<mxb:ToolbarButtonItem Header="Open" 
 Glyph="{SvgImage 'avares://bars_sample/Images/Toolbars/FileOpen.svg'}" 
 Category="File" Command="{Binding OpenFileCommand}"/>
```

You can associate a dropdown control or menu with a [`ToolbarButtonItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarButtonItem.md) object. In this case, [`ToolbarButtonItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarButtonItem.md) can act as a dropdown button, invoking the specified dropdown control/menu on clicking the item or the built-in down arrow.

![toolbarbuttonitem-dropdowncontrol](../../images/toolbarbuttonitem-dropdowncontrol.png)

``` xml
xmlns:mxb="https://schemas.eremexcontrols.net/avalonia/bars"

<mxb:ToolbarButtonItem Header="Paste"
                       Command="{Binding #textBox.Paste}"
                       IsEnabled="{Binding #textBox.CanPaste}"
                       Glyph="{SvgImage 'avares://bars_sample/Images/Toolbars/EditPaste.svg'}"
                       Category="Edit"
                       DropDownArrowVisibility="ShowArrow" DropDownArrowAlignment="Default"
                       >
    <mxb:ToolbarButtonItem.DropDownControl>
        <mxb:PopupMenu>
            <mxb:ToolbarButtonItem Header="Paste" Command="{Binding #textBox.Paste}" 
             IsEnabled="{Binding #textBox.CanPaste}"/>
            <mxb:ToolbarButtonItem Header="Paste As" Command="{Binding PasteAsCommand}" 
             IsEnabled="{Binding #textBox.CanPaste}"/>
        </mxb:PopupMenu>
    </mxb:ToolbarButtonItem.DropDownControl>
</mxb:ToolbarButtonItem>
```

#### Button's Main Settings

- [`DropDownControl`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarButtonItem/DropDownControl.md) — Gets or sets a dropdown control (an [`Eremex.AvaloniaUI.Controls.Bars.IPopup`](../../API/Eremex.AvaloniaUI.Controls.Bars/IPopup.md) object) associated with the item. The control pops up when a user clicks the item or the built-in down arrow button (see [`DropDownArrowVisibility`](../../API/Eremex.AvaloniaUI.Controls.Bars/DropDownArrowVisibility.md)). The following objects implement the [`Eremex.AvaloniaUI.Controls.Bars.IPopup`](../../API/Eremex.AvaloniaUI.Controls.Bars/IPopup.md) interface, and so they can be displayed as dropdown controls:

    - [`Eremex.AvaloniaUI.Controls.Bars.PopupMenu`](../../API/Eremex.AvaloniaUI.Controls.Bars/PopupMenu.md) — A [popup menu](../toolbars-and-menus/popup-and-context-menus.md). You can add all types of toolbar items to the menu to populate it with content.
    - [`Eremex.AvaloniaUI.Controls.Bars.PopupContainer`](../../API/Eremex.AvaloniaUI.Controls.Bars/PopupContainer.md) — A container of controls. Use [`PopupContainer`](../../API/Eremex.AvaloniaUI.Controls.Bars/PopupContainer.md) to display custom controls in a dropdown.
    
- [`DropDownArrowVisibility`](../../API/Eremex.AvaloniaUI.Controls.Bars/DropDownArrowVisibility.md) — Gets or sets whether the item displays a dropdown arrow used to invoke the associated dropdown control. 

    ![ribbon-items-button-dropdownarrowvisibility](../../images/ribbon-items-button-dropdownarrowvisibility.png)

    - `ShowArrow` — The dropdown arrow is visible. The item and arrow act as a single button. A click on them displays an associated dropdown control.

    - `ShowSplitArrow` or `Default` — The dropdown arrow is visible. It acts as a separate button embedded in the item. A click on the item invokes its command ([`Command`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Command.md)) and events ([`Click`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Click.md) and [`Press`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Press.md)). 

    - `Hide` — The dropdown arrow is hidden. A click on the item invokes the dropdown control.

- [`DropDownArrowAlignment`](../../API/Eremex.AvaloniaUI.Controls.Bars/DropDownArrowAlignment.md) — Gets or sets the position of the dropdown arrow.
- [`DropDownOpenMode`](../../API/Eremex.AvaloniaUI.Controls.Bars/DropDownOpenMode.md) — Gets or sets whether and when the dropdown control is invoked when a user touches the item/dropdown arrow. Supported options include:
    - [`Press`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Press.md) or `Default` — The dropdown is displayed on a mouse press event.
    - [`Click`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Click.md) — The dropdown is displayed after the mouse is pressed and then released over the item.
    - `Never` — The dropdown is not displayed.
- [`DropDownPress`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarButtonItem/DropDownPress.md) — The event that fires when the dropdown arrow is pressed.

See also: [Common Toolbar Item Settings](#common-toolbar-item-settings).

### Check Buttons (ToolbarCheckItem)

[`ToolbarCheckItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem.md) encapsulates a check button, which supports two states - normal and pressed. 

![toolbarcheckitem](../../images/toolbarcheckitem.png)

``` xml
xmlns:mxb="https://schemas.eremexcontrols.net/avalonia/bars"

<mxb:ToolbarCheckItem Header="Bold" 
 IsChecked="{Binding #textBox.FontWeight, 
  Converter={helpers:BoolToFontWeightConverter}, Mode=TwoWay}" 
 Glyph="{SvgImage 'avares://DemoCenter/Images/FontBold.svg'}" Category="Font"/>
```

#### Check Button's Main Settings and Events

- [`IsChecked`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem/IsChecked.md) — Gets or sets the button's check state.
- [`CheckedChanged`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem/CheckedChanged.md) — The event that fires when the check state changes.

- [`CheckBoxStyle`](../../API/Eremex.AvaloniaUI.Controls.Bars/CheckBoxStyle.md) — Gets or sets display mode for a [`ToolbarCheckItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem.md) object. Available options include:

  - [`CheckBoxStyle.CheckButton`](../../API/Eremex.AvaloniaUI.Controls.Bars/CheckBoxStyle.md) — The item is rendered as a check button. When [`IsChecked`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem/IsChecked.md) is `true` the button appears in the pressed state.

    ![bars-checkboxstyle-checkbutton](../../images/bars-checkboxstyle-checkbutton.png)

  - [`CheckBoxStyle.CheckBox`](../../API/Eremex.AvaloniaUI.Controls.Bars/CheckBoxStyle.md) — The item displays a toggle box before its text and glyph. When [`IsChecked`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem/IsChecked.md) is `true` the toggle box has a check mark.

    ![bars-checkboxstyle-checkbox](../../images/bars-checkboxstyle-checkbox.png)
    
  - [`CheckBoxStyle.RadioButton`](../../API/Eremex.AvaloniaUI.Controls.Bars/CheckBoxStyle.md) — The item displays a radio button before its text and glyph. When [`IsChecked`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem/IsChecked.md) is `true` the radio button is rendered as a filled circle.

    You can apply the RadioButton style to [`ToolbarCheckItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem.md) objects combined in a check group ([`ToolbarCheckItemGroup`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItemGroup.md)). In this case, the group appears as a typical radio group.

    ``` xml
    <mxb:ToolbarCheckItemGroup CheckType="Radio">
        <mxb:ToolbarCheckItem Header="E-mail" CheckBoxStyle="RadioButton" />
        <mxb:ToolbarCheckItem Header="Phone" CheckBoxStyle="RadioButton" />
    </mxb:ToolbarCheckItemGroup>
    ```
    
    ![bars-checkboxstyle-radiobutton](../../images/bars-checkboxstyle-radiobutton.png)

- [`CheckBoxAlignment`](../../API/Eremex.AvaloniaUI.Controls.Bars/CheckBoxAlignment.md) — Gets or sets whether the check box (or radio button) are displayed before or after an item's glyph and text. This option is in effect when the [`CheckBoxStyle`](../../API/Eremex.AvaloniaUI.Controls.Bars/CheckBoxStyle.md) property is set to [`CheckBoxStyle.CheckBox`](../../API/Eremex.AvaloniaUI.Controls.Bars/CheckBoxStyle.md) or [`CheckBoxStyle.RadioButton`](../../API/Eremex.AvaloniaUI.Controls.Bars/CheckBoxStyle.md).

    ```xml
    <mxb:ToolbarCheckItem Header="Status bar" CheckBoxAlignment="After"
                        CheckBoxStyle="CheckBox"
                        Hint="Show and hide the status bar"/>
    <mxb:ToolbarSeparatorItem/>
    ```
    
    ![bars-checkboxalignment-after](../../images/bars-checkboxalignment-after.png)

See also: [Common Toolbar Item Settings](#common-toolbar-item-settings).

### Sub-Menus (ToolbarMenuItem)

[`ToolbarMenuItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarMenuItem.md) is an item that displays a sub-menu on a click. 

![toolbarMenuItem](../../images/toolbarMenuItem.png)

To specify a sub-menu's content, define items between the start and end `<ToolbarMenuItem>`  tags in XAML, or add items to the [`ToolbarMenuItem.Items`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarMenuItem/Items.md) collection in code-behind.

``` xml
xmlns:mxb="https://schemas.eremexcontrols.net/avalonia/bars"

<mxb:ToolbarMenuItem Header="File" Category="File">
    <mxb:ToolbarButtonItem Header="New" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=NewDraftAction.svg'}" 
     Category="File" Command="{Binding NewFileCommand}"/>
    <mxb:ToolbarButtonItem Header="Open" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Basic, Icon=Folder Open.svg'}" 
     Category="File" Command="{Binding OpenFileCommand}"/>
    <mxb:ToolbarButtonItem Header="Save" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Basic, Icon=Save.svg'}" 
     Category="File" Command="{Binding SaveFileCommand}"/>
    <mxb:ToolbarButtonItem Header="Print" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Basic, Icon=Print.svg'}" 
     ShowSeparator="True"  Category="File" Command="{Binding PrintFileCommand}"/>
</mxb:ToolbarMenuItem>
```

#### Sub-menu's Main Settings and Events

- [`DropDownOpenMode`](../../API/Eremex.AvaloniaUI.Controls.Bars/DropDownOpenMode.md) — Gets or sets whether and how the sub-menu is invoked when a user touches the item. Supported options include:
    - [`Press`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Press.md) or `Default` — The menu is displayed on a mouse press event.
    - [`Click`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Click.md) — The menu is displayed after the mouse is pressed and then released over the item.
    - `Never` — The menu is not displayed.
- `Items` — A collection of items displayed in the sub-menu.
- `ItemsSource` — A collection of business objects in a View Model from which the sub-menu's items are created. Corresponding data templates should define toolbar items and initialize their settings from underlying business objects.

**Events**

- `Opening` — Fires when the menu is about to be displayed. This event allows you to cancel the display of the menu.
- `Opened` — Fires after the menu is displayed.
- `Closing` — Fires when the menu is about to be closed. This event allows you to cancel closing the menu.
- `Closed` — Fires after the menu is closed.

See also: [Common Toolbar Item Settings](#common-toolbar-item-settings).

### In-place Editors (ToolbarEditorItem)

[`ToolbarEditorItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem.md) allows you to display an in-place editor. 

![ToolbarEditorItem](../../images/ToolbarEditorItem.png)

To specify the in-place editor's type and settings, use the [`ToolbarEditorItem.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/EditorProperties.md) property. You can set [`ToolbarEditorItem.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/EditorProperties.md) to one of the following objects:

- [`ButtonEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditorProperties.md) — Corresponds to a [`ButtonEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md) in-place editor.
- [`CheckEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditorProperties.md) — Corresponds to a [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md) in-place editor.
- `ColorEditorProperties` — Corresponds to a [`ColorEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ColorEditor.md) in-place editor.
- [`ComboBoxEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditorProperties.md) — Corresponds to a [`ComboBoxEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md) in-place editor.
- [`HyperlinkEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/HyperlinkEditorProperties.md) — Corresponds to a [`HyperlinkEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/HyperlinkEditor.md) in-place editor.
- [`PopupColorEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupColorEditorProperties.md) — Corresponds to a [`PopupColorEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupColorEditor.md) in-place editor.
- [`PopupEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditorProperties.md) — Corresponds to a [`PopupEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor.md) in-place editor.
- [`SegmentedEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditorProperties.md) — Corresponds to a [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) in-place editor.
- [`SpinEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditorProperties.md) — Corresponds to a [`SpinEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) in-place editor.
- [`TextEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditorProperties.md) — Corresponds to a [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) in-place editor.
- [`MemoEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/MemoEditorProperties.md) — Corresponds to a [`MemoEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/MemoEditor.md) in-place editor.

In the following example, the _Font_ [`ToolbarEditorItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem.md) object displays a list of fonts using a combobox in-place editor. The [`ToolbarEditorItem.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/EditorProperties.md) property is set to a [`ComboBoxEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditorProperties.md), which corresponds to a [`ComboBoxEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md) control.

``` xml
<mxb:ToolbarEditorItem Header="Font:" EditorWidth="150" Category="Font" 
 EditorValue="{Binding #textBox.FontFamily, Converter={helpers:FontNameToFontFamilyConverter}}">
    <mxb:ToolbarEditorItem.EditorProperties>
        <mxe:ComboBoxEditorProperties 
         ItemsSource="{Binding $parent[view:ToolbarAndMenuPageView].Fonts}"
         IsTextEditable="False" PopupMaxHeight="300"/>
    </mxb:ToolbarEditorItem.EditorProperties>
</mxb:ToolbarEditorItem>      
```

#### In-place Editor's Main Settings and Events

- [`ToolbarEditorItem.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/EditorProperties.md) — Gets or sets the object that specifies the type and settings of the in-place editor.
- [`ToolbarEditorItem.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/EditorValue.md) — Gets or sets the in-place editor's value. Use this property for data binding.
- [`ToolbarEditorItem.SizeMode`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/SizeMode.md) — Gets or sets the item's size mode. This property allows you to stretch the bar item, so it occupues all the available empty space within the bar.
- [`ToolbarEditorItem.EditorWidth`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/EditorWidth.md) — Gets or sets the in-place editor's width.
- [`ToolbarEditorItem.EditorHeight`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/EditorHeight.md) — Gets or sets the in-place editor's height.
- [`ToolbarEditorItem.EditorAlignment`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/EditorAlignment.md) — Gets or sets the editor's alignment relative to the item's header.

- [`ToolbarEditorItem.EditorValueChanged`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/EditorValueChanged.md) — The event that fires after the editor's value is changed.

<!--TODO - `ToolbarEditorItem.Editor` -  

-->

See also: [Common Toolbar Item Settings](#common-toolbar-item-settings).




### Text Labels (ToolbarTextItem)

[`ToolbarTextItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarTextItem.md) displays a text label specified by the [`ToolbarTextItem.Header`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Header.md) property. Use this item to render text that is not editable by users.

![ToolbarTextItem](../../images/ToolbarTextItem.png)

``` xml
<mxb:ToolbarTextItem 
 Header="{Binding #scaleDecorator.Scale, StringFormat={}Zoom: {0:P0}}" 
 ShowBorder="True" Alignment="Far" ShowSeparator="True" Category="Info" 
 CustomizationName="Zoom Info"/>
```

#### Text Label's Main Settings and Events

- [`ToolbarTextItem.SizeMode`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarTextItem/SizeMode.md) — Gets or sets the item's size mode. This property allows you to stretch the item, so it occupues all the available empty space within the bar.
- [`ToolbarTextItem.ShowBorder`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarTextItem/ShowBorder.md) — Gets or sets whether the item's border is visible. You can use the [`ToolbarTextItem.BorderTemplate`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarTextItem/BorderTemplate.md) property to specify a custom template to paint the border.
- [`ToolbarTextItem.BorderTemplate`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarTextItem/BorderTemplate.md) — Gets or sets a custom template to paint the item's border. This template is in effect if the [`ToolbarTextItem.ShowBorder`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarTextItem/ShowBorder.md) option is enabled.

See also: [Common Toolbar Item Settings](#common-toolbar-item-settings).

### Non-Breaking Groups of Items (ToolbarItemGroup)

Use [`ToolbarItemGroup`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItemGroup.md) to create a non-breaking group of toolbar items. A non-breaking group is a container of items that acts as a whole when its parent is resized (the contents of the group cannot be partially hidden; items are always displayed in a single line and do not support wrapping).

![bars-ToolbarItemGroup](../../images/bars-ToolbarItemGroup.png)

To specify the group's contents, define items between the start and end `<ToolbarItemGroup>`  tags, or add items to the [`ToolbarItemGroup.Items`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItemGroup/Items.md) collection in code-behind.

``` xml
<mxb:ToolbarItemGroup CustomizationName="Clipboard" >
    <mxb:ToolbarButtonItem Header="Cut" Command="{Binding #textBox.Cut}" 
     IsEnabled="{Binding #textBox.CanCut}" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=Cut.svg'}" 
     Category="Edit"/>
    <mxb:ToolbarButtonItem Header="Copy" Command="{Binding #textBox.Copy}" 
     IsEnabled="{Binding #textBox.CanCopy}" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=Copy.svg'}" 
     Category="Edit"/>
    <mxb:ToolbarButtonItem Header="Paste" Command="{Binding #textBox.Paste}" 
     IsEnabled="{Binding #textBox.CanPaste}" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=Paste.svg'}" 
     Category="Edit"/>
</mxb:ToolbarItemGroup>
```

#### Group's Main Settings and Events

- [`ToolbarItemGroup.Items`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItemGroup/Items.md) — Allows you to access the group's children.

### Non-Breaking Groups of Check Items (ToolbarCheckItemGroup)

Use [`ToolbarCheckItemGroup`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItemGroup.md) to create a non-breaking group of check items. A non-breaking group is a container of items that acts as a whole when its parent is resized (the contents of the group cannot be partially hidden; items are always displayed in a single line and do not support wrapping).

![bars-ToolbarCheckItemGroup](../../images/bars-ToolbarCheckItemGroup.png)

The [`ToolbarCheckItemGroup`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItemGroup.md) container can control the check state of its child items ([`ToolbarCheckItem` objects](#check-buttons-toolbarcheckitem)). You can use [`ToolbarCheckItemGroup`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItemGroup.md) to create the following group types:

- A group of mutually exclusive items (radio group).
- A group that allows multiple items to be checked at the same time.


To specify the group's content, add [`ToolbarCheckItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem.md) items between the start and end `<ToolbarCheckItemGroup>` tags in XAML, or add items to the [`ToolbarCheckItemGroup.Items`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItemGroup/Items.md) collection in code-behind.

``` xml
<mxb:ToolbarCheckItemGroup CustomizationName="Check group" CheckType="Radio" >
    <mxb:ToolbarCheckItem Header="1" IsChecked="{Binding Option1}"  
     Category="Settings"/>
    <mxb:ToolbarCheckItem Header="2" IsChecked="{Binding Option2}" 
     Category="Settings"/>
    <mxb:ToolbarCheckItem Header="3" IsChecked="{Binding Option3}" 
     Category="Settings"/>
</mxb:ToolbarCheckItemGroup>
```

A [`ToolbarCheckItemGroup`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItemGroup.md) object accepts child items of all supported bar item types. The group, however, only manipilates the check states of nested [`ToolbarCheckItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItem.md) objects.

#### Check Group's Main Settings and Events

- [`ToolbarCheckItemGroup.CheckType`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarCheckItemGroup/CheckType.md) — Gets or sets whether a single or multiple items can be checked in the group at a time. The following options are supported:

    - `Default` or `Multiple` — Multiple items can be checked at a time.
    - `Radio` — A group of mutually exclusive items. A user cannot uncheck an item other than by checking another one.
    - `Single` — A group of mutually exclusive items. A user can uncheck all items within the group.

- [`ToolbarCheckItemGroup.Items`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItemGroup/Items.md) — Allows you to access the group's children.

See also: [Common Toolbar Item Settings](#common-toolbar-item-settings).

### Separators (ToolbarSeparatorItem)

[`ToolbarSeparatorItem`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarSeparatorItem.md) draws a separator.

![bars-toolbarseparatoritem](../../images/bars-toolbarseparatoritem.png)

``` xml
<mxb:ToolbarMenuItem Header="File" Category="File">
    <mxb:ToolbarButtonItem Header="New" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=NewDraftAction.svg'}" 
     Category="File"/>
    <mxb:ToolbarButtonItem Header="Open" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Basic, Icon=Folder Open.svg'}" 
     Category="File"/>
    <mxb:ToolbarButtonItem Header="Save" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Basic, Icon=Save.svg'}" 
     Category="File"/>
    <mxb:ToolbarSeparatorItem/>
    <mxb:ToolbarButtonItem Header="Print" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Basic, Icon=Print.svg'}" 
     Category="File"/>
</mxb:ToolbarMenuItem>
```


## Toolbar Item Categories

You can classify toolbar items into categories to enable item grouping in the Customization Window. A user can select a category in the Customization Window to access related items.

![toolbars-customizationwindow-categories](../../images/toolbars-customizationwindow-categories.png)

Use the [`ToolbarItem.Category`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Category.md) property to assign an item to a category. This property specifies the category name. To assign a group of items to the same category, set their [`ToolbarItem.Category`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Category.md) property to the same category name.

``` xml
<mxb:ToolbarMenuItem Header="Edit" Category="Edit">
    <mxb:ToolbarButtonItem Header="Cut" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=Cut.svg'}" 
     Category="Edit"/>
    <mxb:ToolbarButtonItem Header="Copy" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=Copy.svg'}" 
     Category="Edit"/>
    <mxb:ToolbarButtonItem Header="Paste" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Context Menu, Icon=Paste.svg'}" 
     Category="Edit"/>
    <mxb:ToolbarButtonItem Header="Select All" 
     Command="{Binding #textBox.SelectAll}" Category="Edit" ShowSeparator="True"/>
    <mxb:ToolbarButtonItem Header="Clear all" 
     Command="{Binding #textBox.Clear}" 
     Glyph="{SvgImage 'avares://DemoCenter/Images/Group=Basic, Icon=Clear.svg'}" 
     Category="Edit"/>
</mxb:ToolbarMenuItem>       
```

## Hotkeys

You can use the [`ToolbarItem.HotKey`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/HotKey.md) property to assign hotkeys to items. 

``` xml
<mxb:ToolbarButtonItem 
    Header="Clear" Command="{Binding #textBox.Clear}" HotKey="Ctrl+Q"
    Glyph="{SvgImage 'avares://bars_sample/Images/Toolbars/EditDelete.svg'}"/>
```

A hotkey press activates an item's command provided that focus is within the hotkey scope. The default hotkey scope is the UI region within the [`ToolbarManager`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarManager.md) component's bounds. When the input focus is beyond the hotkey scope, [`ToolbarManager`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarManager.md) is not able to intercept hotkeys.

The [`ToolbarManager.IsWindowManager`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarManager/IsWindowManager.md) property allows you to extend the hotkey scope to the entire window. When you set this property to `true`, the [`ToolbarManager`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarManager.md) component registers item hotkeys in the window. It will be able to intercept and process hotkeys even if focus is outside its client area.

### Displaying Hotkeys

Hotkeys assigned to toolbar items are displayed in the following cases:

- In items when they reside within sub-menus or popup menus.
- In items' tooltips.

![toolbaritem-hotkey-display-in-tooltip](../../images/toolbaritem-hotkey-display-in-tooltip.png)

You can use the [`ToolbarItem.HotKeyDisplayString`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/HotKeyDisplayString.md) property to specify a hotkey display text. This text is displayed even if no hotkey is assigned to the item. This is helpful if a target hotkey is already registered by another object to perform a specific operation, and you want to indicate that the same hotkey is linked to a toolbar item.

For instance, a TextBox registers the _Ctrl+Z_ shortcut to perform an Undo operation. If a toolbar item performs the same Undo operation on the TextBox, do not assign the _Ctrl+Z_ hotkey to the item. Instead, set the item's [`ToolbarItem.HotKeyDisplayString`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/HotKeyDisplayString.md) to "_Ctrl+Z_" to display this shortcut to users in tooltips and sub-menus/popup menus.

``` xml
<mxb:ToolbarButtonItem Header="Undo" HotKeyDisplayString="Ctrl+Z" 
    Command="{Binding $parent[TextBox].Undo}" 
    IsEnabled="{Binding $parent[TextBox].CanUndo}" 
    Glyph="{SvgImage 'avares://bars_sample/Images/Toolbars/EditUndo.svg'}"/>
```

![toolbaritem-hotkeydisplaystring](../../images/toolbaritem-hotkeydisplaystring.png)
