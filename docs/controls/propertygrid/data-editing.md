---
title: Data Editing
order: 700
seealso: []
---

# Data Editing

## Default In-place Eremex Editors

If you do not explicitly specify in-place editors for rows, the PropertyGrid control uses in-place Eremex editors to display and edit row values of common data types.

![propertygrid-inplaceeditors](../../images/propertygrid-inplaceeditors.png)

The following list shows Eremex editors associated with common data types:

- Boolean values — [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md)
- Double values — [`SpinEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md)
- Enumeration values — [`ComboBoxEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md)
- Properties with a `TypeConverter` attribute whose `TypeConverter.GetStandardValuesSupported` method returns `true` — [`ComboBoxEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md)
- Other values — [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md)

You can dynamically access and modify instances of in-place Eremex editors when these editors are activated. See the [Access the Active In-place Eremex Editor](#access-the-active-in-place-eremex-editor) section for more details.

## Assign In-place Eremex Editors

You can explicitly assign in-place Eremex editors to rows if you need to override the default editor assignment, or to customize row editors in XAML or code-behind. 

Use the [`PropertyGridRow.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridRow/EditorProperties.md) property for this purpose, as follows:

1. Create and customize an instance of a helper `...EditorProperties` class that stores settings specific to the required in-place editor. These helper classes are all [`BaseEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditorProperties.md) descendants: 
    - [`ButtonEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditorProperties.md) — Contains settings specific to the [`ButtonEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md) control.
    - [`CheckEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditorProperties.md) — Contains settings specific to the [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md) control.
    - `ColorEditorProperties` — Contains settings specific to the [`ColorEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ColorEditor.md) control.
    - [`ComboBoxEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditorProperties.md) — Contains settings specific to the [`ComboBoxEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md) control.
    - [`HyperlinkEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/HyperlinkEditorProperties.md) — Contains settings specific to the [`HyperlinkEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/HyperlinkEditor.md) control.
    - [`PopupColorEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupColorEditorProperties.md) — Contains settings specific to the [`PopupColorEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupColorEditor.md) control.
    - [`PopupEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditorProperties.md) — Contains settings specific to the [`PopupEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor.md) control.
    - [`SegmentedEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditorProperties.md) — Contains settings specific to the [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) control.
    - [`SpinEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditorProperties.md) — Contains settings specific to the [`SpinEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) control.
    - [`TextEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditorProperties.md) — Contains settings specific to the [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) control.
    
2. Set the [`PropertyGridRow.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridRow/EditorProperties.md) property to the created `...EditorProperties` instance.

``` xml
xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxpg:PropertyGridRow FieldName="OrderNo">
    <mxpg:PropertyGridRow.EditorProperties >
        <mxe:ButtonEditorProperties TextWrapping="Wrap" />
    </mxpg:PropertyGridRow.EditorProperties>
</mxpg:PropertyGridRow>
```

The [`PropertyGridRow.CellTemplate`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridRow/CellTemplate.md) property is another way to assign an Eremex editor to a row. Ensure that the Eremex editor has the `x:Name` property set to **"PART_Editor"**. In this case, PropertyGrid automatically binds the editor's [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) property to the row's bound field. Additionally, PropertyGrid starts to maintain the in-place editor's appearance settings (the borders' visibility and foreground colors in the active and inactive states).

``` xml
xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
...
<mxpg:PropertyGridRow FieldName="Caption">
    <mxpg:PropertyGridRow.CellTemplate>
        <DataTemplate>
            <mxe:ButtonEditor x:Name="PART_Editor">
                <mxe:ButtonEditor.Buttons>
                    <mxe:ButtonSettings Content="..."/>
                </mxe:ButtonEditor.Buttons>
            </mxe:ButtonEditor>
        </DataTemplate>
    </mxpg:PropertyGridRow.CellTemplate>
</mxpg:PropertyGridRow>
```


## Custom Editors
PropertyGrid allows you to specify custom editors for row cells. You can assign an editor directly to a specific row, or dynamically assign editors to rows based on the data type of the row's underlying object.
See the following topic for more information: [Custom Editors](custom-editors.md).

<!--TODO ## Get and Set Cell values

-->

## Access the Active In-place Eremex Editor

- [`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) property — Returns the active in-place editor. 
  
  To improve the control's performance, PropertyGrid uses light-weight versions of in-place Eremex editors when it renders cell values in display mode (when text editing is not active). When a text edit operation starts in a cell, the in-place editor switches from its lightweight version to a fully-functioning version. In this case, you can use the [`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) property to access the Eremex editor instance. When a row cell loses focus, the editor switches back to its lightweight version, and the [`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) property returns `null`.

- [`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md) event — Allows you to receive notifications when edit operations start in row cells. You can safely access the [`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) property in a [`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md) event handler.

## Show a Cell Editor

- [`ShowEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowEditor.md) method — Activates a cell editor in the focused row.
- [`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md) event — Allows you to prevent a cell editor from being activated by users in specific cases. While handling the [`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md) event, set the `Cancel` event parameter to `true` to disable an editor activation.

## Close the Active In-place Editor

- [`CloseEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CloseEditor.md) method — Saves changes made in the cell editor and closes the editor.
- [`HideEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/HideEditor.md) method — Closes the cell editor without saving any changes.

- [`HiddenEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/HiddenEditor.md) event — Fires after the active cell editor is closed.


## Save the Changes Made in an In-place Editor

- [`CloseEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CloseEditor.md) method — Saves changes made in the cell editor and closes the editor.
- [`PostEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/PostEditor.md) method — Saves changes made in the active cell editor without closing the editor.