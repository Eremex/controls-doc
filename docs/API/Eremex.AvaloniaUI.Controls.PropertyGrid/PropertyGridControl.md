# PropertyGridControl class

Displays and edits the properties of the selected object.

**Namespace:** [`Eremex.AvaloniaUI.Controls.PropertyGrid`](./index.md)  
**Assembly:** `Eremex.Avalonia.Controls.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Declaration

```csharp
public class PropertyGridControl : TemplatedControl, IPropertyGridEditableNode, 
    IPropertyGridRowsOwner
```

## Public Members

| name | description |
| --- | --- |
| [PropertyGridControl](PropertyGridControl/PropertyGridControl.md)() | Initializes a new instance of the PropertyGridControl class. |
| [ActiveEditor](PropertyGridControl/ActiveEditor.md) { get; } | Gets the editor that is currently active for the focused row. |
| [AllowEditing](PropertyGridControl/AllowEditing.md) { get; set; } | Gets or sets whether users can edit row values. |
| [AllowImmediateEditorValuePosting](PropertyGridControl/AllowImmediateEditorValuePosting.md) { get; set; } | Gets or sets whether editor values are posted immediately as they change. |
| [AllowResizing](PropertyGridControl/AllowResizing.md) { get; set; } | Gets or sets whether users can resize the captions and editors columns. |
| [AutoGenerateRows](PropertyGridControl/AutoGenerateRows.md) { get; set; } | Gets or sets whether rows are generated automatically from the selected object's properties. |
| [CaptionColumnWidth](PropertyGridControl/CaptionColumnWidth.md) { get; set; } | Gets or sets the width of the captions column. |
| [CaptionHorizontalAlignment](PropertyGridControl/CaptionHorizontalAlignment.md) { get; set; } | Gets or sets the horizontal alignment of row captions. |
| [CellTemplate](PropertyGridControl/CellTemplate.md) { get; set; } | Gets or sets the template that displays row values when a row defines no own template. |
| [EditorButtonShowMode](PropertyGridControl/EditorButtonShowMode.md) { get; set; } | Gets or sets when editor buttons are displayed. |
| [EditorColumnWidth](PropertyGridControl/EditorColumnWidth.md) { get; set; } | Gets or sets the width of the editors column. |
| [EditorShowMode](PropertyGridControl/EditorShowMode.md) { get; set; } | Gets or sets the mouse action that activates an editor. |
| [FocusedRow](PropertyGridControl/FocusedRow.md) { get; set; } | Gets or sets the focused row. |
| [IgnoreValidationAttributesOnCommit](PropertyGridControl/IgnoreValidationAttributesOnCommit.md) { get; set; } | Gets or sets whether validation attributes are ignored when an editor value is committed. |
| [IsResizerVisible](PropertyGridControl/IsResizerVisible.md) { get; } | Gets whether the column resizer is displayed. |
| [Rows](PropertyGridControl/Rows.md) { get; } | Gets the collection of rows. |
| [RowsDataTemplates](PropertyGridControl/RowsDataTemplates.md) { get; set; } | Gets or sets the templates used to create rows from RowsSource items. |
| [RowsSource](PropertyGridControl/RowsSource.md) { get; set; } | Gets or sets the collection whose items are used to generate rows. |
| [SearchText](PropertyGridControl/SearchText.md) { get; set; } | Gets or sets the text used to filter rows. |
| [SelectedObject](PropertyGridControl/SelectedObject.md) { get; set; } | Gets or sets the object whose properties are displayed and edited. |
| [SelectedObjects](PropertyGridControl/SelectedObjects.md) { get; set; } | Gets or sets the collection of objects whose properties are displayed and edited. Supports editing multiple objects at once. |
| [ShowDataErrors](PropertyGridControl/ShowDataErrors.md) { get; set; } | Gets or sets whether data validation errors are displayed for rows. |
| [ShowSearchPanel](PropertyGridControl/ShowSearchPanel.md) { get; set; } | Gets or sets whether the search panel is displayed. |
| [ValidateRowValuesOnShowAndUpdate](PropertyGridControl/ValidateRowValuesOnShowAndUpdate.md) { get; set; } | Gets or sets whether row values are validated when displayed and updated instead of when an editor value is committed. |
| event [CellValueChanged](PropertyGridControl/CellValueChanged.md) | Occurs after a row value has been changed. |
| event [CellValueChanging](PropertyGridControl/CellValueChanging.md) | Occurs when a user modifies a row value in an editor, before the change is committed. |
| event [CustomCellTemplateData](PropertyGridControl/CustomCellTemplateData.md) | Occurs when the data for a row's cell template is needed. Set the Data property to provide custom data. |
| event [HiddenEditor](PropertyGridControl/HiddenEditor.md) | Occurs after an editor has been closed. |
| event [InvalidRowValueException](PropertyGridControl/InvalidRowValueException.md) | Occurs when an exception is thrown while a row value is saved to the data object. Set the ErrorContent property to customize the error. |
| event [ShowingEditor](PropertyGridControl/ShowingEditor.md) | Occurs before an editor is activated for a row. Cancel the event to prevent editing. |
| event [UsingComplexDataContext](PropertyGridControl/UsingComplexDataContext.md) | Occurs before a row value of a complex type is used as the DataContext for the cell's content. Cancel the event to bind to the parent object's property instead. |
| event [ValidateRowValue](PropertyGridControl/ValidateRowValue.md) | Occurs when a row value is validated. Set the ErrorContent property to indicate an error. |
| [CloseEditor](PropertyGridControl/CloseEditor.md)() | Saves the active editor's value to the data object and hides the editor. |
| [CollapseAllRows](PropertyGridControl/CollapseAllRows.md)() | Collapses all rows. |
| [ExpandAllRows](PropertyGridControl/ExpandAllRows.md)() | Expands all rows. |
| [HideEditor](PropertyGridControl/HideEditor.md)() | Hides the active editor without posting its value. |
| [PostEditor](PropertyGridControl/PostEditor.md)() | Saves the active editor's value to the data object. |
| [Refresh](PropertyGridControl/Refresh.md)() | Re-reads values from the selected object and updates row values. |
| [RetrieveFields](PropertyGridControl/RetrieveFields.md)() | Regenerates rows from the selected object's properties. |
| [ShowEditor](PropertyGridControl/ShowEditor.md)() | Activates an editor for the focused row and selects its content. |

## See Also

* namespace [Eremex.AvaloniaUI.Controls.PropertyGrid](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->
