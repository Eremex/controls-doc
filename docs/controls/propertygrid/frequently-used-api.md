---
title: Frequently Used API
order: 100
seealso: []
---

# Frequently Used API

## Properties

Property | Description 
---|---
[`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) | Returns the active Eremex cell editor. The property returns `null` if no editor is currently active, or when a non-Eremex editor is active in the focused cell.
[`AllowEditing`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/AllowEditing.md) | Gets or sets whether cell edit operations are enabled.
[`AutoGenerateRows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/AutoGenerateRows.md) | Gets or sets whether the empty control automatically generates rows for all public properties available in the bound object(s) when the control is initialized. If the control already contains rows, automatic row generation is disabled. To manually populate the control with rows you can use the `PopulateRows` method, or add rows to the [`Rows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/Rows.md) collection.
[`CellTemplate`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CellTemplate.md)  | Gets or sets the template to render cell editors in all cells. You can use the [`PropertyGridRow.CellTemplate`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridRow/CellTemplate.md) property to specify the cell editor for specific rows.
[`FocusedRow`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/FocusedRow.md) | Gets or sets the focused row. This property allows you to focus a specific row.
[`Rows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/Rows.md) | Returns the control's rows displayed at the root level. For category rows ([`PropertyGridCategoryRow`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridCategoryRow.md) objects) stored in this collection you can use the [`PropertyGridCategoryRow.Rows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridCategoryRow/Rows.md) property to access their child rows.
[`RowsDataTemplates`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/RowsDataTemplates.md) | Specifies data templates used to render rows from a row source (the [`RowsSource`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridExpandableRowBase/RowsSource.md) property).
[`RowsSource`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridExpandableRowBase/RowsSource.md) | Specifies the data source to generate rows using data templates ([`RowsDataTemplates`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/RowsDataTemplates.md)).
[`SelectedObject`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObject.md) | Gets or sets the object whose properties are displayed in the control.
[`SelectedObjects`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObjects.md) | Gets or sets the list of objects whose properties are displayed in the control.
`UseModernAppearance` | Gets or sets whether the control is painted using the `Modern` or `Classic` style.

## Methods

Method | Description
------|------
[`CloseEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CloseEditor.md) | Hides the active editor and saves changes made.
[`HideEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/HideEditor.md) | Hides the active editor and discards changes made.
`PopulateRows` | Generates rows for public properties exposed by the bound object(s) ([`SelectedObject`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObject.md) and [`SelectedObjects`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObjects.md) properties). Existing rows are cleared before the row generation starts.
[`PostEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/PostEditor.md) | Saves changes made in a cell to the bound object(s).
[`ShowEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowEditor.md) |  Activates the focused row's editor. 

## Events

Event | Description
------|------
[`CellValueChanged`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CellValueChanged.md) | Fires when the cell's value is changed.
[`CustomCellTemplateData`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CustomCellTemplateData.md) | Allows you to supply a custom object as a cell template's value. See the following topic for more information: [Custom Editors](custom-editors.md#dynamically-assign-editors-based-on-row-data-type).
[`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md) | Fires when a cell editor is activated.

