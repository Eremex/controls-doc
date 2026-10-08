# DataGridControl class

Displays data from a data source as rows and columns with support for sorting, grouping, filtering, and editing.

**Namespace:** [`Eremex.AvaloniaUI.Controls.DataGrid`](./index.md)  
**Assembly:** `Eremex.Avalonia.Controls.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Declaration

```csharp
public class DataGridControl : DataControlBase, IDataControl
```

## Public Members

| name | description |
| --- | --- |
| [DataGridControl](DataGridControl/DataGridControl.md)() | Initializes a new instance of the DataGridControl class. |
| [AllowBandResizing](DataGridControl/AllowBandResizing.md) { get; set; } | Gets or sets whether users can resize bands. |
| [AllowBestFit](DataGridControl/AllowBestFit.md) { get; set; } | Gets or sets whether users can apply best-fit column sizing. |
| [AllowColumnFiltering](DataGridControl/AllowColumnFiltering.md) { get; set; } | Gets or sets whether users can filter data by column. |
| [AllowColumnMoving](DataGridControl/AllowColumnMoving.md) { get; set; } | Gets or sets whether users can reorder columns by dragging their headers. |
| [AllowColumnResizing](DataGridControl/AllowColumnResizing.md) { get; set; } | Gets or sets whether users can resize columns. |
| [AllowDragDrop](DataGridControl/AllowDragDrop.md) { get; set; } | Gets or sets whether row drag-and-drop is enabled. |
| [AllowDragDropSortedRows](DataGridControl/AllowDragDropSortedRows.md) { get; set; } | Gets or sets whether rows can be dragged when the data is sorted. |
| [AllowEditingGroupSummaries](DataGridControl/AllowEditingGroupSummaries.md) { get; set; } | Gets or sets whether users can edit group summaries. |
| [AllowEditingTotalSummaries](DataGridControl/AllowEditingTotalSummaries.md) { get; set; } | Gets or sets whether users can edit total summaries. |
| [AllowGrouping](DataGridControl/AllowGrouping.md) { get; set; } | Gets or sets whether users can group data. |
| [AllowHorizontalVirtualization](DataGridControl/AllowHorizontalVirtualization.md) { get; set; } | Gets or sets whether off-screen columns are virtualized. |
| [AllowResetColumnWidth](DataGridControl/AllowResetColumnWidth.md) { get; set; } | Gets or sets whether users can reset column widths to their default values. |
| [AllowScrollingOnDrag](DataGridControl/AllowScrollingOnDrag.md) { get; set; } | Gets or sets whether the view scrolls automatically when a dragged element approaches its edge. |
| [AllowSorting](DataGridControl/AllowSorting.md) { get; set; } | Gets or sets whether users can sort data. |
| [AutoExpandAllGroups](DataGridControl/AutoExpandAllGroups.md) { get; set; } | Gets or sets whether all groups are expanded automatically. |
| [AutoExpandDelayOnDrag](DataGridControl/AutoExpandDelayOnDrag.md) { get; set; } | Gets or sets the delay before a group is expanded automatically on drag-over. |
| [AutoExpandOnDrag](DataGridControl/AutoExpandOnDrag.md) { get; set; } | Gets or sets whether a collapsed group is expanded automatically when a dragged element hovers over it. |
| [AutoGenerateBands](DataGridControl/AutoGenerateBands.md) { get; set; } | Gets or sets whether bands are generated automatically. |
| [AutoGenerateColumns](DataGridControl/AutoGenerateColumns.md) { get; set; } | Gets or sets whether columns are generated automatically based on the data source. |
| [Bands](DataGridControl/Bands.md) { get; } | Gets the collection of grid bands. |
| [BandsSource](DataGridControl/BandsSource.md) { get; set; } | Gets or sets the collection whose items are used to generate bands. |
| [BandTemplate](DataGridControl/BandTemplate.md) { get; set; } | Gets or sets the template used to create a band for each item in BandsSource. |
| [BestFitMode](DataGridControl/BestFitMode.md) { get; set; } | Gets or sets how the best-fit column width is calculated. |
| [CellTemplate](DataGridControl/CellTemplate.md) { get; set; } | Gets or sets the default template used to display cell content when a column defines no own template. |
| [ClipboardCopyHeaders](DataGridControl/ClipboardCopyHeaders.md) { get; set; } | Gets or sets whether column headers are copied to the clipboard along with cell values. |
| [ColumnFilterButtonDisplayMode](DataGridControl/ColumnFilterButtonDisplayMode.md) { get; set; } | Gets or sets when the column filter buttons are displayed. |
| [ColumnFilterPopupMode](DataGridControl/ColumnFilterPopupMode.md) { get; set; } | Gets or sets the type of the column filter popup. |
| [ColumnMenu](DataGridControl/ColumnMenu.md) { get; set; } | Gets or sets the context menu invoked for column headers. |
| [Columns](DataGridControl/Columns.md) { get; } | Gets the collection of grid columns. |
| [ColumnsSource](DataGridControl/ColumnsSource.md) { get; set; } | Gets or sets the collection whose items are used to generate columns. |
| [ColumnTemplate](DataGridControl/ColumnTemplate.md) { get; set; } | Gets or sets the template used to create a column for each item in ColumnsSource. |
| [Commands](DataGridControl/Commands.md) { get; } | Gets the grid's commands. |
| [ExtendScrollbarToFixedColumns](DataGridControl/ExtendScrollbarToFixedColumns.md) { get; set; } | Gets or sets whether the horizontal scrollbar extends under the fixed columns. |
| [FilterPanelDisplayMode](DataGridControl/FilterPanelDisplayMode.md) { get; set; } | Gets or sets when the filter panel is displayed. |
| [FilterPanelText](DataGridControl/FilterPanelText.md) { get; } | Gets the text displayed in the filter panel. |
| [FixedColumnSeparatorWidth](DataGridControl/FixedColumnSeparatorWidth.md) { get; set; } | Gets or sets the width of the separator marking fixed columns. |
| [FixedLeftColumnWidth](DataGridControl/FixedLeftColumnWidth.md) { get; } | Gets the total width of columns fixed to the left edge. |
| [FixedRightColumnWidth](DataGridControl/FixedRightColumnWidth.md) { get; } | Gets the total width of columns fixed to the right edge. |
| [FocusedColumn](DataGridControl/FocusedColumn.md) { get; set; } | Gets or sets the focused column. |
| [FocusedRowIndex](DataGridControl/FocusedRowIndex.md) { get; set; } | Gets or sets the index of the focused row. |
| [GroupCount](DataGridControl/GroupCount.md) { get; set; } | Gets or sets the number of leading sorted columns used to group data. |
| [GroupSummaries](DataGridControl/GroupSummaries.md) { get; set; } | Gets the collection of group summary items calculated across group rows. |
| [HeaderDropIndicatorWidth](DataGridControl/HeaderDropIndicatorWidth.md) { get; set; } | Gets or sets the width of the indicator shown between headers while a column is dragged. |
| [HeaderPanelMinHeight](DataGridControl/HeaderPanelMinHeight.md) { get; set; } | Gets or sets the minimum height of the column header panel. |
| [IsFilterPanelVisible](DataGridControl/IsFilterPanelVisible.md) { get; } | Gets whether the filter panel is currently displayed. |
| [NavigationMode](DataGridControl/NavigationMode.md) { get; set; } | Gets or sets whether keyboard navigation moves focus between cells or between rows. |
| [RowCellMenu](DataGridControl/RowCellMenu.md) { get; set; } | Gets or sets the context menu invoked for data cells. |
| [RowDragMode](DataGridControl/RowDragMode.md) { get; set; } | Gets or sets whether rows are dragged by the row itself or by a drag handle. |
| [RowIndicatorWidth](DataGridControl/RowIndicatorWidth.md) { get; set; } | Gets or sets the width of the row indicator. |
| [SerializationInfo](DataGridControl/SerializationInfo.md) { get; } | Gets the serialization information for the grid. |
| [ShowAutoFilterRow](DataGridControl/ShowAutoFilterRow.md) { get; set; } | Gets or sets whether the auto-filter row is displayed. |
| [ShowBands](DataGridControl/ShowBands.md) { get; set; } | Gets or sets whether band headers are displayed. |
| [ShowBandSeparators](DataGridControl/ShowBandSeparators.md) { get; set; } | Gets or sets whether separators between band headers are displayed. |
| [ShowColumnHeaders](DataGridControl/ShowColumnHeaders.md) { get; set; } | Gets or sets whether the column header panel is displayed. |
| [ShowColumnMenuFixedItem](DataGridControl/ShowColumnMenuFixedItem.md) { get; set; } | Gets or sets whether the fixed-column item is displayed in the column header context menu. |
| [ShowConditionInAutoFilterRow](DataGridControl/ShowConditionInAutoFilterRow.md) { get; set; } | Gets or sets whether the auto-filter row displays the applied filter condition. |
| [ShowGroupedColumns](DataGridControl/ShowGroupedColumns.md) { get; set; } | Gets or sets whether grouped columns remain visible among the data columns. |
| [ShowGroupPanel](DataGridControl/ShowGroupPanel.md) { get; set; } | Gets or sets whether the group panel is displayed. |
| [ShowGroupSummaries](DataGridControl/ShowGroupSummaries.md) { get; set; } | Gets or sets whether group footer rows that display group summaries are displayed. |
| [ShowHorizontalLines](DataGridControl/ShowHorizontalLines.md) { get; set; } | Gets or sets whether horizontal grid lines are displayed. |
| [ShowRowIndicator](DataGridControl/ShowRowIndicator.md) { get; } | Gets whether the row indicator is displayed. |
| [ShowTotalSummaries](DataGridControl/ShowTotalSummaries.md) { get; set; } | Gets or sets whether the total summary footer is displayed. |
| [ShowVerticalLines](DataGridControl/ShowVerticalLines.md) { get; set; } | Gets or sets whether vertical grid lines are displayed. |
| [TotalSummaries](DataGridControl/TotalSummaries.md) { get; } | Gets the collection of total summary items calculated across all rows. |
| [UsePlatformRowDragDrop](DataGridControl/UsePlatformRowDragDrop.md) { get; set; } | Gets or sets whether the platform drag-and-drop is used when dragging rows. |
| [VisibleRowCount](DataGridControl/VisibleRowCount.md) { get; } | Gets the number of currently visible rows. |
| event [AutoGeneratedColumns](DataGridControl/AutoGeneratedColumns.md) | Occurs after columns are generated automatically from the data source. |
| event [AutoGeneratingColumn](DataGridControl/AutoGeneratingColumn.md) | Occurs when a column is about to be generated automatically. Cancel the event to prevent the column from being generated. |
| event [CellValueChanged](DataGridControl/CellValueChanged.md) | Occurs after a cell value has been changed. |
| event [CellValueChanging](DataGridControl/CellValueChanging.md) | Occurs when a user modifies a cell value in an editor, before the change is committed. |
| event [CompleteDragDrop](DataGridControl/CompleteDragDrop.md) | Occurs after a drag-and-drop operation is completed. |
| event [CustomColumnDisplayText](DataGridControl/CustomColumnDisplayText.md) | Occurs when the display text of a cell is needed. Set the DisplayText property to customize the text. |
| event [CustomColumnGroup](DataGridControl/CustomColumnGroup.md) | Occurs when two rows are compared during grouping. Set the Result property to indicate whether the rows belong to the same group. |
| event [CustomColumnSort](DataGridControl/CustomColumnSort.md) | Occurs when two rows are compared during sorting. Set the Result property to implement custom sorting. |
| event [CustomGroupValueDisplayText](DataGridControl/CustomGroupValueDisplayText.md) | Occurs when the display text of a group row value is needed. Set the DisplayText property to customize the text. |
| event [CustomRowFilter](DataGridControl/CustomRowFilter.md) | Occurs when a row is filtered. Set the Visible property to show or hide the row. |
| event [CustomSummary](DataGridControl/CustomSummary.md) | Occurs when a summary value is calculated. Set the SummaryValue property to implement a custom summary. |
| event [CustomUnboundColumnData](DataGridControl/CustomUnboundColumnData.md) | Occurs when the value of an unbound column cell is requested or committed. Set the Value property to provide the value. |
| event [DragOver](DataGridControl/DragOver.md) | Occurs while a dragged row is over the grid. Set the Effects and DropPosition properties to customize the drop operation. |
| event [Drop](DataGridControl/Drop.md) | Occurs when a dragged row is dropped over the grid. Handle the event to perform a custom drop operation. |
| event [HiddenEditor](DataGridControl/HiddenEditor.md) | Occurs after an editor has been closed. |
| event [RowClick](DataGridControl/RowClick.md) | Occurs when a row is clicked. |
| event [SelectionChanged](DataGridControl/SelectionChanged.md) | Occurs when the row selection changes. |
| event [ShowingEditor](DataGridControl/ShowingEditor.md) | Occurs before an editor is activated for a cell. Cancel the event to prevent editing. |
| event [ShownEditor](DataGridControl/ShownEditor.md) | Occurs after an editor has been activated for a cell. |
| event [StartDrag](DataGridControl/StartDrag.md) | Occurs when a row drag operation starts. Set the Effects and Data properties to customize the drag operation. |
| event [ValidateCellValue](DataGridControl/ValidateCellValue.md) | Occurs when a cell value is validated. Set the ErrorContent property to indicate an error. |
| override [BeginDataUpdate](DataGridControl/BeginDataUpdate.md)() |  |
| [BestFit](DataGridControl/BestFit.md)(…) | Sets the width of the specified column to best fit its content. |
| [BestFitAllColumns](DataGridControl/BestFitAllColumns.md)() | Sets the widths of all columns to best fit their content. |
| [CollapseAllGroups](DataGridControl/CollapseAllGroups.md)() | Collapses all group rows. |
| [CollapseGroupRow](DataGridControl/CollapseGroupRow.md)(…) | Collapses the group row at the specified index. |
| override [CommitEditing](DataGridControl/CommitEditing.md)() |  |
| [ExpandAllGroups](DataGridControl/ExpandAllGroups.md)() | Expands all group rows. |
| [ExpandGroupRow](DataGridControl/ExpandGroupRow.md)(…) | Expands the group row at the specified index. |
| [ExportToImages](DataGridControl/ExportToImages.md)(…) | Exports the grid to image files saved in the specified directory. |
| [ExportToPdf](DataGridControl/ExportToPdf.md)(…) | Exports the grid to the specified file in PDF format. (2 methods) |
| [ExportToXlsx](DataGridControl/ExportToXlsx.md)(…) | Exports the grid to the specified file in XLSX format. (2 methods) |
| [FindRowByDisplayText](DataGridControl/FindRowByDisplayText.md)(…) | Finds the first row whose cell display text in the specified field equals the specified text. Returns InvalidRowIndex if no row is found. (2 methods) |
| [FindRowByItem](DataGridControl/FindRowByItem.md)(…) | Finds the row that corresponds to the specified data source item. Returns InvalidRowIndex if the item is not found. |
| [FindRowByValue](DataGridControl/FindRowByValue.md)(…) | Finds the first row whose cell value in the specified field equals the specified value. Returns InvalidRowIndex if no row is found. (2 methods) |
| [GetCellDisplayText](DataGridControl/GetCellDisplayText.md)(…) | Gets the display text of the cell at the intersection of the specified row and the column bound to the specified field. (2 methods) |
| [GetCellValue](DataGridControl/GetCellValue.md)(…) | Gets the value of the cell at the intersection of the specified row and column. (2 methods) |
| [GetGroupChildRowCount](DataGridControl/GetGroupChildRowCount.md)() | Gets the number of top-level group rows. |
| [GetGroupChildRowCount](DataGridControl/GetGroupChildRowCount.md)(…) | Gets the number of child rows of the group row at the specified index. |
| [GetGroupChildRowIndex](DataGridControl/GetGroupChildRowIndex.md)(…) | Gets the index of the child row at the specified position within the group row at the specified index. (2 methods) |
| [GetGroupRowValue](DataGridControl/GetGroupRowValue.md)(…) | Gets the value of the group row at the specified index. |
| [GetGroupSummaryValue](DataGridControl/GetGroupSummaryValue.md)(…) |  |
| [GetParentRowIndex](DataGridControl/GetParentRowIndex.md)(…) | Gets the index of the parent group row of the row at the specified index. |
| [GetRowIndexBySourceItemIndex](DataGridControl/GetRowIndexBySourceItemIndex.md)(…) | Gets the index of the row that corresponds to the data source item at the specified index. |
| [GetRowIndexByVisibleRowIndex](DataGridControl/GetRowIndexByVisibleRowIndex.md)(…) | Gets the index of the row at the specified visible index. |
| [GetRowLevel](DataGridControl/GetRowLevel.md)(…) | Gets the nesting level of the row at the specified index. |
| [GetSelectedRowIndexes](DataGridControl/GetSelectedRowIndexes.md)() | Gets the indexes of the selected rows. |
| [GetSourceItem](DataGridControl/GetSourceItem.md)(…) | Gets the item from the data source at the specified index. |
| [GetSourceItemByRowIndex](DataGridControl/GetSourceItemByRowIndex.md)(…) | Gets the data source item that corresponds to the row at the specified index. |
| [GetSourceItemByVisibleRowIndex](DataGridControl/GetSourceItemByVisibleRowIndex.md)(…) | Gets the data source item that corresponds to the row at the specified visible index. |
| [GetSourceItemIndexByRowIndex](DataGridControl/GetSourceItemIndexByRowIndex.md)(…) | Gets the data source index of the row at the specified index. |
| [GetSourceItemIndexByVisibleRowIndex](DataGridControl/GetSourceItemIndexByVisibleRowIndex.md)(…) | Gets the data source index of the row at the specified visible index. |
| [GetSourceItemValue](DataGridControl/GetSourceItemValue.md)(…) | Gets the value of the specified column's field for the data source item at the specified index. (2 methods) |
| [GetTotalSummaryValue](DataGridControl/GetTotalSummaryValue.md)(…) | Gets the calculated value of the specified total summary. |
| [GetVisibleRowIndexByRowIndex](DataGridControl/GetVisibleRowIndexByRowIndex.md)(…) | Gets the visible index of the row at the specified index. |
| [GetVisibleRowIndexBySourceItemIndex](DataGridControl/GetVisibleRowIndexBySourceItemIndex.md)(…) | Gets the visible index of the row that corresponds to the data source item at the specified index. |
| [IsGroupFooterRow](DataGridControl/IsGroupFooterRow.md)(…) | Determines whether the row at the specified index is a group footer row. |
| [IsGroupRow](DataGridControl/IsGroupRow.md)(…) | Determines whether the row at the specified index is a group row. |
| [IsGroupRowExpanded](DataGridControl/IsGroupRowExpanded.md)(…) | Determines whether the group row at the specified index is expanded. |
| [IsRowSelected](DataGridControl/IsRowSelected.md)(…) | Determines whether the row at the specified index is selected. |
| [MoveNextCell](DataGridControl/MoveNextCell.md)() | Moves focus to the next cell. |
| [MoveNextRow](DataGridControl/MoveNextRow.md)() | Moves focus to the next row. |
| [MovePrevCell](DataGridControl/MovePrevCell.md)() | Moves focus to the previous cell. |
| [MovePrevRow](DataGridControl/MovePrevRow.md)(…) | Moves focus to the previous row, optionally allowing focus to move to the auto-filter row. |
| [PopulateColumns](DataGridControl/PopulateColumns.md)() | Creates columns based on the data source. |
| [RefreshData](DataGridControl/RefreshData.md)() | Re-reads the data source and refreshes the grid's content. |
| [RefreshRow](DataGridControl/RefreshRow.md)(…) | Refreshes the visible cells of the row at the specified index. |
| [ResetColumnWidth](DataGridControl/ResetColumnWidth.md)() | Resets the widths of all columns to their default values. |
| [RestoreLayout](DataGridControl/RestoreLayout.md)(…) | Restores the grid's layout from the specified stream. (2 methods) |
| [SaveLayout](DataGridControl/SaveLayout.md)(…) | Saves the grid's layout to the specified stream. (2 methods) |
| [SelectRange](DataGridControl/SelectRange.md)(…) | Selects all rows between the specified start and end row indexes. |
| [SelectRow](DataGridControl/SelectRow.md)(…) | Selects the row at the specified index. |
| [SetCellValue](DataGridControl/SetCellValue.md)(…) | Sets the value of the cell at the intersection of the specified row and column. (2 methods) |
| [UnselectRow](DataGridControl/UnselectRow.md)(…) | Removes the selection from the row at the specified index. |
| const [InvalidRowIndex](DataGridControl/InvalidRowIndex.md) | Represents an invalid row index. |

## See Also

* class [DataControlBase](../Eremex.AvaloniaUI.Controls.DataControl/DataControlBase.md)
* namespace [Eremex.AvaloniaUI.Controls.DataGrid](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->
