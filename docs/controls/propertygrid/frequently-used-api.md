---
title: Frequently Used API
order: 100
seealso: []
---

# Frequently Used API

## Properties

Property | Description 
---|---
`ActiveEditor` | Returns the active Eremex cell editor. The property returns `null` if no editor is currently active, or when a non-Eremex editor is active in the focused cell.
`AllowEditing` | Gets or sets whether cell edit operations are enabled.
`AutoGenerateRows` | Gets or sets whether the empty control automatically generates rows for all public properties available in the bound object(s) when the control is initialized. If the control already contains rows, automatic row generation is disabled. To manually populate the control with rows you can use the `PopulateRows` method, or add rows to the `Rows` collection.
`CellTemplate`  | Gets or sets the template to render cell editors in all cells. You can use the `PropertyGridRow.CellTemplate` property to specify the cell editor for specific rows.
`FocusedRow` | Gets or sets the focused row. This property allows you to focus a specific row.
`Rows` | Returns the control's rows displayed at the root level. For category rows (`PropertyGridCategoryRow` objects) stored in this collection you can use the `PropertyGridCategoryRow.Rows` property to access their child rows.
`RowsDataTemplates` | Specifies data templates used to render rows from a row source (the `RowsSource` property).
`RowsSource` | Specifies the data source to generate rows using data templates (`RowsDataTemplates`).
`SelectedObject` | Gets or sets the object whose properties are displayed in the control.
`SelectedObjects` | Gets or sets the list of objects whose properties are displayed in the control.
`UseModernAppearance` | Gets or sets whether the control is painted using the `Modern` or `Classic` style.

## Methods

Method | Description
------|------
`CloseEditor` | Hides the active editor and saves changes made.
`HideEditor` | Hides the active editor and discards changes made.
`PopulateRows` | Generates rows for public properties exposed by the bound object(s) (`SelectedObject` and `SelectedObjects` properties). Existing rows are cleared before the row generation starts.
`PostEditor` | Saves changes made in a cell to the bound object(s).
`ShowEditor` |  Activates the focused row's editor. 

## Events

Event | Description
------|------
`CellValueChanged` | Fires when the cell's value is changed.
`CustomCellTemplateData` | Allows you to supply a custom object as a cell template's value. See the following topic for more information: [Custom Editors](custom-editors.md#dynamically-assign-editors-based-on-row-data-type).
`ShowingEditor` | Fires when a cell editor is activated.

