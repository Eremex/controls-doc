# DataControlBase class

Provides a base class for data controls that display a collection of items as rows.

**Namespace:** [`Eremex.AvaloniaUI.Controls.DataControl`](./index.md)  
**Assembly:** `Eremex.Avalonia.Controls.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Declaration

```csharp
public abstract class DataControlBase : TemplatedControl, IBandsOwner, ISortedInfoCollectionOwner
```

## Public Members

| name | description |
| --- | --- |
| [ActiveEditor](DataControlBase/ActiveEditor.md) { get; } | Gets the currently active in-place editor. |
| [AllowEditing](DataControlBase/AllowEditing.md) { get; set; } | Gets or sets whether users can edit cell values. |
| [AllowImmediateEditorValuePosting](DataControlBase/AllowImmediateEditorValuePosting.md) { get; set; } | Gets or sets whether editor values are posted immediately as they change. |
| [AutoScrollToFocusedRow](DataControlBase/AutoScrollToFocusedRow.md) { get; set; } | Gets or sets whether the view scrolls automatically to keep the focused row visible. |
| [EditorButtonShowMode](DataControlBase/EditorButtonShowMode.md) { get; set; } | Gets or sets when editor buttons are displayed. |
| [EditorShowMode](DataControlBase/EditorShowMode.md) { get; set; } | Gets or sets when in-place editors are activated. |
| [FilterString](DataControlBase/FilterString.md) { get; set; } | Gets or sets the filter criteria string applied to the data. |
| [FocusedItem](DataControlBase/FocusedItem.md) { get; set; } | Gets or sets the focused data item. |
| virtual [HeaderDropIndex](DataControlBase/HeaderDropIndex.md) { get; set; } | Gets or sets the index at which a dragged column header is dropped. |
| [IgnoreValidationAttributesOnCommit](DataControlBase/IgnoreValidationAttributesOnCommit.md) { get; set; } | Gets or sets whether validation attributes are ignored when committing cell values. |
| [IsColumnChooserVisible](DataControlBase/IsColumnChooserVisible.md) { get; set; } | Gets or sets whether the column chooser is displayed. |
| [IsFilterEnabled](DataControlBase/IsFilterEnabled.md) { get; set; } | Gets or sets whether filtering is enabled. |
| [IsSearchPanelVisible](DataControlBase/IsSearchPanelVisible.md) { get; set; } | Gets or sets whether the search panel is visible. |
| [ItemsSource](DataControlBase/ItemsSource.md) { get; set; } | Gets or sets the data source whose items are displayed by the control as rows. |
| [KeepSelectedOnClick](DataControlBase/KeepSelectedOnClick.md) { get; set; } | Gets or sets whether the selected row remains selected when clicked again. |
| [RowLevelIndent](DataControlBase/RowLevelIndent.md) { get; set; } | Gets or sets the indent applied per row nesting level. |
| [RowMinHeight](DataControlBase/RowMinHeight.md) { get; set; } | Gets or sets the minimum height of rows. |
| [SearchPanelDisplayMode](DataControlBase/SearchPanelDisplayMode.md) { get; set; } | Gets or sets when the search panel is displayed. |
| [SearchPanelHighlightResults](DataControlBase/SearchPanelHighlightResults.md) { get; set; } | Gets or sets whether search results are highlighted. |
| [SearchText](DataControlBase/SearchText.md) { get; set; } | Gets or sets the search text entered in the search panel. |
| [SelectedItems](DataControlBase/SelectedItems.md) { get; set; } | Gets or sets the collection of selected data items. |
| [SelectionMode](DataControlBase/SelectionMode.md) { get; set; } | Gets or sets whether users can select a single row or multiple rows. |
| [ShowItemsSourceErrors](DataControlBase/ShowItemsSourceErrors.md) { get; set; } | Gets or sets whether validation errors of the source items are displayed. |
| [ShowSearchPanelCloseButton](DataControlBase/ShowSearchPanelCloseButton.md) { get; set; } | Gets or sets whether the search panel shows a close button. |
| [TextSortMode](DataControlBase/TextSortMode.md) { get; set; } | Gets or sets how text values are compared when sorting. |
| [ValidateCellValuesOnShowAndUpdate](DataControlBase/ValidateCellValuesOnShowAndUpdate.md) { get; set; } | Gets or sets whether cell values are validated when shown and updated. |
| event [EndSorting](DataControlBase/EndSorting.md) | Occurs after data sorting is completed. |
| event [FilterChanged](DataControlBase/FilterChanged.md) | Occurs when the data filter is changed. |
| event [InvalidCellValueException](DataControlBase/InvalidCellValueException.md) | Occurs when an exception is thrown while posting an invalid cell value. |
| event [StartSorting](DataControlBase/StartSorting.md) | Occurs before data sorting is started. |
| virtual [BeginDataUpdate](DataControlBase/BeginDataUpdate.md)() | Prevents the control from updating its data until EndDataUpdate or CancelDataUpdate is called. |
| [BeginSelection](DataControlBase/BeginSelection.md)() | Prevents selection updates until EndSelection is called. |
| [CancelDataUpdate](DataControlBase/CancelDataUpdate.md)() | Resumes data updates after BeginDataUpdate without refreshing the control's data. |
| [ClearAllColumnsFilter](DataControlBase/ClearAllColumnsFilter.md)() | Clears filter conditions applied by all columns. |
| [ClearSelection](DataControlBase/ClearSelection.md)() | Clears the current selection. |
| [ClearSorting](DataControlBase/ClearSorting.md)() | Removes sorting applied to all columns. |
| [CloseEditor](DataControlBase/CloseEditor.md)() | Closes the active in-place editor. |
| virtual [CommitEditing](DataControlBase/CommitEditing.md)() | Completes the current edit session by closing the active in-place editor. |
| [CopyToClipboardAsync](DataControlBase/CopyToClipboardAsync.md)() | Copies column captions and selected rows to the clipboard. |
| virtual [EndDataUpdate](DataControlBase/EndDataUpdate.md)() | Resumes data updates after BeginDataUpdate and refreshes the control's data. |
| [EndSelection](DataControlBase/EndSelection.md)() | Applies the selection changes made since BeginSelection. |
| [ExportToCsv](DataControlBase/ExportToCsv.md)(…) | Exports the control's visible data to the specified file in CSV format. (2 methods) |
| [HideColumnChooser](DataControlBase/HideColumnChooser.md)() | Hides the column chooser. |
| [HideEditor](DataControlBase/HideEditor.md)() | Hides the active in-place editor. |
| [MoveNextPage](DataControlBase/MoveNextPage.md)() | Moves focus to the first row of the next page. |
| [MovePrevPage](DataControlBase/MovePrevPage.md)() | Moves focus to the last row of the previous page. |
| [PostEditor](DataControlBase/PostEditor.md)() | Posts the edited value to the data source. |
| [ResizeBand](DataControlBase/ResizeBand.md)(…) | Sets the same width for all columns displayed within the specified band. |
| [ResizeColumn](DataControlBase/ResizeColumn.md)(…) | Sets the width of the specified column. |
| [SelectAll](DataControlBase/SelectAll.md)() | Selects all rows. |
| [ShowColumnChooser](DataControlBase/ShowColumnChooser.md)() | Displays the column chooser. |
| [ShowEditor](DataControlBase/ShowEditor.md)() | Activates the in-place editor for the focused cell and selects its content. |
| const [AutoFilterRowIndex](DataControlBase/AutoFilterRowIndex.md) | Represents the visible index that identifies the auto-filter row. |
| static [GetIsFocusWithin](DataControlBase/GetIsFocusWithin.md)(…) | Gets whether keyboard focus is within the specified element. |

## See Also

* namespace [Eremex.AvaloniaUI.Controls.DataControl](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->
