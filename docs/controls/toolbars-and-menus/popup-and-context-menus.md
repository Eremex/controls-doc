---
title: Popup and Context Menus
order: 70000
seealso: []
---

# Popup and Context Menus

The Toolbar&Menu library contains the `PopupMenu` component that allows you to create popup and context menus for controls.

## Context Menus

To specify a context menu, set the `ToolbarManager.ContextPopup` attached property for the target control to a `PopupMenu` object.

![toolbars-contextmenu](../../images/toolbars-contextmenu.png)

You can add all types of [toolbar items](toolbar-items.md) to a context menu. Define items between the start and end `<PopupMenu>` tags in XAML, or add the items to the `PopupMenu.Items` collection in code-behind.

``` xml
xmlns:mxb="https://schemas.eremexcontrols.net/avalonia/bars"

<TextBox x:Name="textBox"  Text="Text Editor" AcceptsReturn="True" 
 CornerRadius="0" FontFamily="Arial" FontSize="20" Height="200">
    <mxb:ToolbarManager.ContextPopup>
        <mxb:PopupMenu ShowIconStrip="True">
            <mxb:ToolbarButtonItem Header="Undo" HotKeyDisplayString="Ctrl+Z" 
             Command="{Binding $parent[TextBox].Undo}" 
             IsEnabled="{Binding $parent[TextBox].CanUndo}"
             Glyph="{SvgImage 'avares://bars_sample/Images/Toolbars/EditUndo.svg'}"/>
            <mxb:ToolbarButtonItem Header="Redo" HotKeyDisplayString="Ctrl+Y"  
             Command="{Binding $parent[TextBox].Redo}" 
             IsEnabled="{Binding $parent[TextBox].CanRedo}"
             Glyph="{SvgImage 'avares://bars_sample/Images/Toolbars/EditRedo.svg'}"/>
            <mxb:ToolbarSeparatorItem/>
            <mxb:ToolbarButtonItem Header="Clear" 
             Command="{Binding $parent[TextBox].Clear}" HotKey="Ctrl+Q"
             Glyph="{SvgImage 'avares://bars_sample/Images/Toolbars/EditDelete.svg'}"/>
        </mxb:PopupMenu>
    </mxb:ToolbarManager.ContextPopup>
</TextBox>
```

## PopupMenu's Main Settings and Events

- `ShowIconStrip` — Gets or sets whether to display a vertical strip of icons for menu items.
- `Header` — Allows you to specify a header for the menu.
- `ShowHeader` — Gets or sets whether the menu header is visible.
- `ContentRightIndent` — Specifies the width of the empty space to the right of menu items' text.

**Events**

- `Opening` — Fires when the menu is about to be displayed. This event allows you to cancel the display of the menu.
- `Opened` — Fires after the menu is displayed.
- `Closing` — Fires when the menu is about to be closed. This event allows you to cancel closing the menu.
- `Closed` — Fires after the menu is closed.

## Example - How to assign context menus to controls of a specific type

You can define a menu in the `Styles` collection if you need to specify one context menu for multiple controls of the same type. The following example sets the `ToolbarManager.ContextPopup` attached property for `TextBox` controls that reside within a UserControl.

![toolbars-contextmenu-styles](../../images/toolbars-contextmenu-styles.png)

``` xml
xmlns:mxb="https://schemas.eremexcontrols.net/avalonia/bars"

<UserControl.Styles>
    <Style Selector="TextBox">
        <Setter Property="mxb:ToolbarManager.ContextPopup">
            <Setter.Value>
                <Template>
                    <mxb:PopupMenu Focusable="False">
                        <mxb:ToolbarButtonItem Header="Cut" HotKeyDisplayString="Ctrl+X" 
                         Command="{Binding $parent[TextBox].Cut}" 
                         IsEnabled="{Binding $parent[TextBox].CanCut}"
                         Glyph="{SvgImage 
                         'avares://DemoCenter/Images/Group=Context Menu, Icon=Cut.svg'}"/>
                        <mxb:ToolbarButtonItem Header="Copy" HotKeyDisplayString="Ctrl+C" 
                         Command="{Binding $parent[TextBox].Copy}" 
                         IsEnabled="{Binding $parent[TextBox].CanCopy}"
                         Glyph="{SvgImage 
                         'avares://DemoCenter/Images/Group=Context Menu, Icon=Copy.svg'}"/>
                        <mxb:ToolbarButtonItem Header="Paste" HotKeyDisplayString="Ctrl+V" 
                         Command="{Binding $parent[TextBox].Paste}" 
                         IsEnabled="{Binding $parent[TextBox].CanPaste}"
                         Glyph="{SvgImage 
                         'avares://DemoCenter/Images/Group=Context Menu, Icon=Paste.svg'}"/>
                        <mxb:ToolbarSeparatorItem/>
                        <mxb:ToolbarButtonItem Header="Undo" HotKeyDisplayString="Ctrl+Z" 
                         Command="{Binding $parent[TextBox].Undo}" 
                         IsEnabled="{Binding $parent[TextBox].CanUndo}"
                         Glyph="{SvgImage 
                         'avares://DemoCenter/Images/Group=Basic, Icon=Undo.svg'}"/>
                        <mxb:ToolbarButtonItem Header="Redo" HotKeyDisplayString="Ctrl+Y" 
                         Command="{Binding $parent[TextBox].Redo}" 
                         IsEnabled="{Binding $parent[TextBox].CanRedo}"
                         Glyph="{SvgImage 
                         'avares://DemoCenter/Images/Group=Basic, Icon=Redo.svg'}"/>
                        <mxb:ToolbarSeparatorItem/>
                        <mxb:ToolbarButtonItem Header="Select All" HotKeyDisplayString="Ctrl+A" 
                         Command="{Binding $parent[TextBox].SelectAll}"/>
                        <mxb:ToolbarButtonItem Header="Clear" 
                         Command="{Binding $parent[TextBox].Clear}"
                         Glyph="{SvgImage 
                         'avares://DemoCenter/Images/Group=Context Menu, Icon=Delete.svg'}"/>
                    </mxb:PopupMenu>
                </Template>
            </Setter.Value>
        </Setter>
    </Style>
</UserControl.Styles>
```