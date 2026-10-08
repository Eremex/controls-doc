---
title: Data Editing
order: 6000
seealso: []
---

# Data Editing

## Default In-place Eremex Editors

The default behavior of the TreeList and TreeView controls is to use in-place Eremex editors to display and edit cell values of common data types:
If you do not explicitly specify cell editors, the TreeList and TreeView controls use in-place Eremex editors to display and edit cell values of these data types:

- Boolean values — [`CheckEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md)
- Double values — [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md)
- Enumeration values — [`ComboBoxEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md)
- Properties with a `TypeConverter` attribute whose `TypeConverter.GetStandardValuesSupported` method returns `true` — [`ComboBoxEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md)
- Other values — [`TextEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md)

You can explicitly specify cell editors for columns to override the default editor assignment, and to customize settings of in-place editors. The current topic provides more details about editor assignment.

When an edit operation starts in a cell, you can access and modify the active in-place editor. See the [Access the Active In-place Eremex Editor](#access-the-active-in-place-eremex-editor) section for more information.

## Assign In-place Eremex Editors

The TreeList and TreeView controls allow you to explicitly assign in-place Eremex editors to cells (columns) to override the default editor assignment, or to customize cell editors in XAML or code-behind. Use the following properties for this purpose:

- TreeView control : [`TreeViewControl.EditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/EditorProperties.md) 

  The TreeView control displays a single column of data. Thus, the [`TreeViewControl.EditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/EditorProperties.md) property specifies the in-place editor used to edit this column's cells. 

- TreeList control: [`TreeListColumn.EditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md)
  
  Each column in the TreeList control can have its own in-place editor. Create a TreeList column (a [`TreeListColumn`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListColumn.md) object) in the [`TreeListControl.Columns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/Columns.md) collection and set the column's editor using the [`TreeListColumn.EditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md) property.

You can set the `EditorProperties` property to the following objects that specify the in-place editor type (all of these objects are [`BaseEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditorProperties.md) descendants):

- [`ButtonEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditorProperties.md) — Contains settings specific to the [`ButtonEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md) control.
- [`CheckEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditorProperties.md) — Contains settings specific to the [`CheckEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md) control.
- [`ComboBoxEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditorProperties.md) — Contains settings specific to the [`ComboBoxEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md) control.
- [`DateEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditorProperties.md) — Contains settings specific to the [`DateEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md) control.
- [`HyperlinkEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/HyperlinkEditorProperties.md) — Contains settings specific to the [`HyperlinkEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/HyperlinkEditor.md) control.
- [`MemoEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/MemoEditorProperties.md) — Contains settings specific to the [`MemoEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/MemoEditor.md) control.
- [`PopupColorEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupColorEditorProperties.md) — Contains settings specific to the [`PopupColorEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupColorEditor.md) control.
- [`SegmentedEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditorProperties.md) — Contains settings specific to the [`SegmentedEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) control.
- [`SpinEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditorProperties.md) — Contains settings specific to the [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) control.
- [`TextEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditorProperties.md) — Contains settings specific to the [`TextEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) control.
    
Assume that you set the `EditorProperties` property to a [`SpinEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditorProperties.md) object. In display mode (cell editing is not active), the TreeList/TreeView control emulates a [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) in the target column's cells, using the settings of the [`SpinEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditorProperties.md) object. No real [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) is created until an edit operation starts in a cell. When a user starts cell editing, the TreeList/TreeView control creates a real [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) in-place editor in the focused cell. After the edit operation is complete, the control destroys the real [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) and starts emulating a [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) in this cell. See [Access the Active In-place Eremex Editor](#access-the-active-in-place-eremex-editor) to learn how to access the real cell editor.

### Example - How to use ButtonEditor as an in-place editor in a treelist column

The following code assigns a [`ButtonEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md) in-place editor to a TreeList column. 

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

The following code assigns a [`ComboBoxEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md) in-place editor to a TreeView.

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

- [`TreeListColumn.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md)
- [`TreeViewControl.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/CellTemplate.md)

Set the `x:Name` property to **"PART_Editor"** for the Eremex editor defined in a template. This ensures automatic binding of the editor's value ([`BaseEditor.EditorValue`](../../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md)) to the column's field. Additionally, 
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

- [`TreeListControl.GetCellDisplayText`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/GetCellDisplayText.md)
- [`TreeListControl.GetCellValue`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/GetCellValue.md)
- [`TreeListControl.SetCellValue`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/SetCellValue.md)
- [`TreeViewControl.GetCellDisplayText`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/GetCellDisplayText.md)
- [`TreeViewControl.GetCellValue`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/GetCellValue.md)
- [`TreeViewControl.SetCellValue`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/SetCellValue.md)



## Access the Active In-place Eremex Editor

- [`ActiveEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ActiveEditor.md) property — Returns the active in-place editor. 
  
  When an in-place Eremex editor is assigned to a TreeList/TreeView column (implicitly, or explicitly using the `EditorSettings` property and templates), the control emulates the specified in-place editor in this column's cells in display mode (when cell editing is not active). No real in-place editor exists at this moment. The emulation of cell editors in display mode improves application performance.

  When a user starts editing a cell, the control creates a real in-place editor. At this moment, you can use the control's [`ActiveEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ActiveEditor.md) property to access the real Eremex editor instance. When a cell loses focus, the real editor is destroyed, and the [`ActiveEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ActiveEditor.md) property returns `null`.

- [`ShownEditor`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShownEditor.md) event — Raised after an in-place editor has been created for a cell and edit operation has started. You can access the active editor using the event's [`Editor`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewEditorEventArgs/Editor.md) parameter or the control's [`ActiveEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ActiveEditor.md) property.

## Show Cell Editors

- [`ShowEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ShowEditor.md) method — Activates a cell editor in the focused cell.
- [`ShowingEditor`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowingEditor.md) event — Allows you to prevent a cell editor from being activated by users in specific cases. While handling the [`ShowingEditor`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowingEditor.md) event, set the [`Cancel`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewShowingEditorEventArgs/Cancel.md) event parameter to `true` to disable an editor activation.


### Show Cell Editors by Users

When cell editing is enabled, a click on a node cell activates a cell editor. Use the [`DataControlBase.EditorShowMode`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/EditorShowMode.md) property to specify which mouse action triggers the editor. You can set this property to the following values:

- [`EditorShowMode.PointerPressed`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md) (default) — A cell editor is activated when the mouse button is pressed.

    When [node drag-and-drop](../node-drag-and-drop.md) is enabled and [`RowDragMode`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/RowDragMode.md) is set to [`RowDragMode.Row`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/RowDragMode.md), the [`EditorShowMode.PointerPressed`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md) mode is not supported. In this configuration, the default mode is [`EditorShowMode.PointerPressedInFocusedCell`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md).

- [`EditorShowMode.PointerPressedInFocusedCell`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md) — A cell editor is activated when the mouse button is pressed in the focused cell.

    This mode is the default if node drag-and-drop is active and the control's [`RowDragMode`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/RowDragMode.md) property is set to [`RowDragMode.Row`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/RowDragMode.md).

- [`EditorShowMode.PointerReleased`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md) — A cell editor is activated when the mouse button is released.
- [`EditorShowMode.PointerReleasedInFocusedCell`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md) — A cell editor is activated when the mouse button is released in the focused cell.

## Close the Active In-place Editor

- [`CloseEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/CloseEditor.md) method — Saves changes made in the cell editor and closes the editor.
- [`HideEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/HideEditor.md) method — Closes the cell editor without saving any changes.

- [`HiddenEditor`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/HiddenEditor.md) event — Fires after the active cell editor is closed.


## Save the Changes Made in an In-place Editor

- [`CloseEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/CloseEditor.md) method — Saves changes made in the cell editor and closes the editor.
- [`PostEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/PostEditor.md) method — Saves changes made in the active cell editor without closing the editor.
