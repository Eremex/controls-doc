---
title: Data Editing
order: 6000
seealso: []
---

# Data Editing

## Default In-place Eremex Editors

The default behavior of the TreeList and TreeView controls is to use in-place Eremex editors to display and edit cell values of common data types:
If you do not explicitly specify cell editors, the TreeList and TreeView controls use in-place Eremex editors to display and edit cell values of these data types:

- Boolean values — `CheckEditor`
- Double values — `SpinEditor`
- Enumeration values — `ComboBoxEditor`
- Properties with a `TypeConverter` attribute whose `TypeConverter.GetStandardValuesSupported` method returns `true` — `ComboBoxEditor`
- Other values — `TextEditor`

You can explicitly specify cell editors for columns to override the default editor assignment, and to customize settings of in-place editors. The current topic provides more details about editor assignment.

When an edit operation starts in a cell, you can access and modify the active in-place editor. See the [Access the Active In-place Eremex Editor](#access-the-active-in-place-eremex-editor) section for more information.

## Assign In-place Eremex Editors

The TreeList and TreeView controls allow you to explicitly assign in-place Eremex editors to cells (columns) to override the default editor assignment, or to customize cell editors in XAML or code-behind. Use the following properties for this purpose:

- TreeView control : `TreeViewControl.EditorProperties` 

  The TreeView control displays a single column of data. Thus, the `TreeViewControl.EditorProperties` property specifies the in-place editor used to edit this column's cells. 

- TreeList control: `TreeListColumn.EditorProperties`
  
  Each column in the TreeList control can have its own in-place editor. Create a TreeList column (a `TreeListColumn` object) in the `TreeListControl.Columns` collection and set the column's editor using the `TreeListColumn.EditorProperties` property.

You can set the `EditorProperties` property to the following objects that specify the in-place editor type (all of these objects are `BaseEditorProperties` descendants):

- `ButtonEditorProperties` — Contains settings specific to the `ButtonEditor` control.
- `CheckEditorProperties` — Contains settings specific to the `CheckEditor` control.
- `ComboBoxEditorProperties` — Contains settings specific to the `ComboBoxEditor` control.
- `DateEditorProperties` — Contains settings specific to the `DateEditor` control.
- `HyperlinkEditorProperties` — Contains settings specific to the `HyperlinkEditor` control.
- `MemoEditorProperties` — Contains settings specific to the `MemoEditor` control.
- `PopupColorEditorProperties` — Contains settings specific to the `PopupColorEditor` control.
- `SegmentedEditorProperties` — Contains settings specific to the `SegmentedEditor` control.
- `SpinEditorProperties` — Contains settings specific to the `SpinEditor` control.
- `TextEditorProperties` — Contains settings specific to the `TextEditor` control.
    
Assume that you set the `EditorProperties` property to a `SpinEditorProperties` object. In display mode (cell editing is not active), the TreeList/TreeView control emulates a `SpinEditor` in the target column's cells, using the settings of the `SpinEditorProperties` object. No real `SpinEditor` is created until an edit operation starts in a cell. When a user starts cell editing, the TreeList/TreeView control creates a real `SpinEditor` in-place editor in the focused cell. After the edit operation is complete, the control destroys the real `SpinEditor` and starts emulating a `SpinEditor` in this cell. See [Access the Active In-place Eremex Editor](#access-the-active-in-place-eremex-editor) to learn how to access the real cell editor.

### Example - How to use ButtonEditor as an in-place editor in a treelist column

The following code assigns a `ButtonEditor` in-place editor to a TreeList column. 

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist" 
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxtl:TreeListControl.Columns>
    <mxtl:TreeListColumn Header="Name" FieldName="Name">
        <mxtl:TreeListColumn.EditorProperties>
            <mxe:ButtonEditorProperties>
                <mxe:ButtonEditorProperties.Buttons>
                    <mxe:ButtonSettings Content="Clear" 
                     Command="{Binding $parent[mxtl:CellControl].DataControl.
                               DataContext.ClearValueCommand}"/>
                </mxe:ButtonEditorProperties.Buttons>
            </mxe:ButtonEditorProperties>
        </mxtl:TreeListColumn.EditorProperties>
    </mxtl:TreeListColumn>
</mxtl:TreeListControl.Columns>
```

### Example - How to use ComboBoxEditor as an in-place editor in treeview

The following code assigns a `ComboBoxEditor` in-place editor to a TreeView.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist" 
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxtl:TreeViewControl.EditorProperties>
    <mxe:ComboBoxEditorProperties ItemsSource="{Binding Families}"/>
</mxtl:TreeViewControl.EditorProperties>
```

## Assign In-place Eremex Editors Using Templates

You can use templates to assign Eremex editors to TreeList and TreeView columns. Cell templates allow you to supply different editors for different rows in the same column.

!!! Note 

    Using templates has the following limitations:

    - Display text provided via cell templates is not used for sorting, grouping, and filtering data.
    - Cell templates are not [exported](../export.md).


To supply an in-place editor for a column in a cell template, use the following properties:

- `TreeListColumn.CellTemplate`
- `TreeViewControl.CellTemplate`

Set the `x:Name` property to **"PART_Editor"** for the Eremex editor defined in a template. This ensures automatic binding of the editor's value (`BaseEditor.EditorValue`) to the column's field. Additionally, 
the editor's appearance settings (border visibility and foreground colors in the active and inactive states) will be managed by the TreeList/TreeView control.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
...
<mxtl:TreeListColumn Header="Phone" FieldName="Phone">
    <mxtl:TreeListColumn.CellTemplate>
        <DataTemplate>
            <mxe:ButtonEditor x:Name="PART_Editor">
                <mxe:ButtonEditor.Buttons>
                    <mxe:ButtonSettings Content="..."/>
                </mxe:ButtonEditor.Buttons>
            </mxe:ButtonEditor>
        </DataTemplate>
    </mxtl:TreeListColumn.CellTemplate>
</mxtl:TreeListColumn>
```


## Custom Editors

You can use cell templates to embed custom editors in TreeList and TreeView columns. The following approaches are available:

- Assign an editor directly to a specific column.
- Dynamically assign editors to columns based on the data type of the column's underlying object. This technique is applicable to the TreeList control.

See the [Custom Editors](custom-editors.md) topic for more information.



## Get and Set Cell Values

The TreeList and TreeView controls expose the following API to obtain and set cell values:

- `TreeListControl.GetCellDisplayText`
- `TreeListControl.GetCellValue`
- `TreeListControl.SetCellValue`
- `TreeViewControl.GetCellDisplayText`
- `TreeViewControl.GetCellValue`
- `TreeViewControl.SetCellValue`



## Access the Active In-place Eremex Editor

- `ActiveEditor` property — Returns the active in-place editor. 
  
  When an in-place Eremex editor is assigned to a TreeList/TreeView column (implicitly, or explicitly using the `EditorSettings` property and templates), the control emulates the specified in-place editor in this column's cells in display mode (when cell editing is not active). No real in-place editor exists at this moment. The emulation of cell editors in display mode improves application performance.

  When a user starts editing a cell, the control creates a real in-place editor. At this moment, you can use the control's `ActiveEditor` property to access the real Eremex editor instance. When a cell loses focus, the real editor is destroyed, and the `ActiveEditor` property returns `null`.

- `ShownEditor` event — Raised after an in-place editor has been created for a cell and edit operation has started. You can access the active editor using the event's `Editor` parameter or the control's `ActiveEditor` property.

## Show Cell Editors

- `ShowEditor` method — Activates a cell editor in the focused cell.
- `ShowingEditor` event — Allows you to prevent a cell editor from being activated by users in specific cases. While handling the `ShowingEditor` event, set the `Cancel` event parameter to `true` to disable an editor activation.


### Show Cell Editors by Users

When cell editing is enabled, a click on a node cell activates a cell editor. Use the `DataControlBase.EditorShowMode` property to specify which mouse action triggers the editor. You can set this property to the following values:

- `EditorShowMode.PointerPressed` (default) — A cell editor is activated when the mouse button is pressed.

    When [node drag-and-drop](../node-drag-and-drop.md) is enabled and `RowDragMode` is set to `RowDragMode.Row`, the `EditorShowMode.PointerPressed` mode is not supported. In this configuration, the default mode is `EditorShowMode.PointerPressedInFocusedCell`.

- `EditorShowMode.PointerPressedInFocusedCell` — A cell editor is activated when the mouse button is pressed in the focused cell.

    This mode is the default if node drag-and-drop is active and the control's `RowDragMode` property is set to `RowDragMode.Row`.

- `EditorShowMode.PointerReleased` — A cell editor is activated when the mouse button is released.
- `EditorShowMode.PointerReleasedInFocusedCell` — A cell editor is activated when the mouse button is released in the focused cell.

## Close the Active In-place Editor

- `CloseEditor` method — Saves changes made in the cell editor and closes the editor.
- `HideEditor` method — Closes the cell editor without saving any changes.

- `HiddenEditor` event — Fires after the active cell editor is closed.


## Save the Changes Made in an In-place Editor

- `CloseEditor` method — Saves changes made in the cell editor and closes the editor.
- `PostEditor` method — Saves changes made in the active cell editor without closing the editor.
