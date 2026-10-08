# TreeListControl class

Displays a collection of items arranged in a hierarchy of nodes.

**Namespace:** [`Eremex.AvaloniaUI.Controls.TreeList`](./index.md)  
**Assembly:** `Eremex.Avalonia.Controls.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Declaration

```csharp
public class TreeListControl : TreeListControlBase
```

## Public Members

| name | description |
| --- | --- |
| [TreeListControl](TreeListControl/TreeListControl.md)() | The default constructor. |
| [AllowBandResizing](TreeListControl/AllowBandResizing.md) { get; set; } | Gets or sets whether users can resize bands. |
| [AllowBestFit](TreeListControl/AllowBestFit.md) { get; set; } | Gets or sets whether users can apply best-fit column sizing. |
| [AllowColumnFiltering](TreeListControl/AllowColumnFiltering.md) { get; set; } | Gets or sets whether users can filter data by column. |
| [AllowColumnMoving](TreeListControl/AllowColumnMoving.md) { get; set; } | Gets or sets whether users can reorder columns by dragging their headers. |
| [AllowColumnResizing](TreeListControl/AllowColumnResizing.md) { get; set; } | Gets or sets whether users can resize columns. |
| [AllowEditingTotalSummaries](TreeListControl/AllowEditingTotalSummaries.md) { get; set; } | Gets or sets whether users can edit total summaries. |
| [AllowHorizontalVirtualization](TreeListControl/AllowHorizontalVirtualization.md) { get; set; } | Gets or sets whether off-screen columns are virtualized. |
| [AllowResetColumnWidth](TreeListControl/AllowResetColumnWidth.md) { get; set; } | Gets or sets whether users can reset column widths to their default values. |
| [AllowSorting](TreeListControl/AllowSorting.md) { get; set; } | Gets or sets whether users can sort data. |
| [AutoGenerateBands](TreeListControl/AutoGenerateBands.md) { get; set; } | Gets or sets whether bands are generated automatically. |
| [AutoGenerateColumns](TreeListControl/AutoGenerateColumns.md) { get; set; } | Gets or sets whether columns are generated automatically based on the data source. |
| [AutoGenerateServiceColumns](TreeListControl/AutoGenerateServiceColumns.md) { get; set; } | Gets or sets whether service columns are generated automatically. |
| [AutoMoveRowFocus](TreeListControl/AutoMoveRowFocus.md) { get; set; } | Gets or sets whether keyboard navigation moves focus to the next or previous row when passing the last or first column. |
| [Bands](TreeListControl/Bands.md) { get; } | Gets the control's band collection. |
| [BandsSource](TreeListControl/BandsSource.md) { get; set; } | Gets or sets the collection whose items are used to generate bands. |
| [BandTemplate](TreeListControl/BandTemplate.md) { get; set; } | Gets or sets the template used to create a band for each item in BandsSource. |
| [BestFitMode](TreeListControl/BestFitMode.md) { get; set; } | Gets or sets how the best-fit column width is calculated. |
| [CellTemplate](TreeListControl/CellTemplate.md) { get; set; } | Gets or sets the default template used to display cell content when a column defines no own template. |
| [ClipboardCopyHeaders](TreeListControl/ClipboardCopyHeaders.md) { get; set; } | Gets or sets whether column headers are copied to the clipboard along with cell values. |
| [ColumnFilterButtonDisplayMode](TreeListControl/ColumnFilterButtonDisplayMode.md) { get; set; } | Gets or sets when the column filter buttons are displayed. |
| [ColumnFilterPopupMode](TreeListControl/ColumnFilterPopupMode.md) { get; set; } | Gets or sets the type of the column filter popup. |
| [ColumnMenu](TreeListControl/ColumnMenu.md) { get; set; } | Gets or sets the context menu invoked for column headers. |
| [Columns](TreeListControl/Columns.md) { get; } | Gets the control's column collection. |
| [ColumnsSource](TreeListControl/ColumnsSource.md) { get; set; } | Gets or sets the collection whose items are used to generate columns. |
| [ColumnTemplate](TreeListControl/ColumnTemplate.md) { get; set; } | Gets or sets the template used to create a column for each item in ColumnsSource. |
| [ExtendScrollbarToFixedColumns](TreeListControl/ExtendScrollbarToFixedColumns.md) { get; set; } | Gets or sets whether the horizontal scrollbar extends under the fixed columns. |
| [FilterPanelDisplayMode](TreeListControl/FilterPanelDisplayMode.md) { get; set; } | Gets or sets when the filter panel is displayed. |
| [FilterPanelText](TreeListControl/FilterPanelText.md) { get; } | Gets the text displayed in the filter panel. |
| [FixedColumnSeparatorWidth](TreeListControl/FixedColumnSeparatorWidth.md) { get; set; } | Gets or sets the width of the separator marking fixed columns. |
| [FixedLeftColumnWidth](TreeListControl/FixedLeftColumnWidth.md) { get; } | Gets the total width of columns fixed to the left edge. |
| [FixedRightColumnWidth](TreeListControl/FixedRightColumnWidth.md) { get; } | Gets the total width of columns fixed to the right edge. |
| [FocusedColumn](TreeListControl/FocusedColumn.md) { get; set; } | Gets or sets the focused column. |
| [HeaderDropIndicatorWidth](TreeListControl/HeaderDropIndicatorWidth.md) { get; set; } | Gets or sets the width of the indicator shown between headers while a column is dragged. |
| [HeaderPanelMinHeight](TreeListControl/HeaderPanelMinHeight.md) { get; set; } | Gets or sets the minimum height of the column header panel. |
| [IsFilterPanelVisible](TreeListControl/IsFilterPanelVisible.md) { get; } | Gets whether the filter panel is currently displayed. |
| [NavigationMode](TreeListControl/NavigationMode.md) { get; set; } | Gets or sets whether keyboard navigation moves focus between cells or between rows. |
| [RowDragMode](TreeListControl/RowDragMode.md) { get; set; } | Gets or sets whether rows are dragged by the row itself or by a drag handle. |
| [RowIndicatorWidth](TreeListControl/RowIndicatorWidth.md) { get; set; } | Gets or sets the width of the row indicator. |
| [SerializationInfo](TreeListControl/SerializationInfo.md) { get; } | Gets the serialization info that stores the control's saved layout. |
| [ShowAutoFilterRow](TreeListControl/ShowAutoFilterRow.md) { get; set; } | Gets or sets whether the auto-filter row is displayed. |
| [ShowBands](TreeListControl/ShowBands.md) { get; set; } | Gets or sets whether band headers are displayed. |
| [ShowBandSeparators](TreeListControl/ShowBandSeparators.md) { get; set; } | Gets or sets whether separators between band headers are displayed. |
| [ShowCheckAllNodesCheckBox](TreeListControl/ShowCheckAllNodesCheckBox.md) { get; set; } | Gets or sets whether the check box that checks all nodes is displayed. |
| [ShowColumnHeaders](TreeListControl/ShowColumnHeaders.md) { get; set; } | Gets or sets whether the column header panel is displayed. |
| [ShowColumnMenuFixedItem](TreeListControl/ShowColumnMenuFixedItem.md) { get; set; } | Gets or sets whether the fixed-column item is displayed in the column header context menu. |
| [ShowConditionInAutoFilterRow](TreeListControl/ShowConditionInAutoFilterRow.md) { get; set; } | Gets or sets whether the auto-filter row displays the applied filter condition. |
| [ShowHorizontalLines](TreeListControl/ShowHorizontalLines.md) { get; set; } | Gets or sets whether horizontal grid lines are displayed. |
| [ShowRowIndicator](TreeListControl/ShowRowIndicator.md) { get; } | Gets whether the row indicator is displayed. |
| [ShowTotalSummaries](TreeListControl/ShowTotalSummaries.md) { get; set; } | Gets or sets whether the total summary footer is displayed. |
| [ShowVerticalLines](TreeListControl/ShowVerticalLines.md) { get; set; } | Gets or sets whether vertical grid lines are displayed. |
| [TotalSummaries](TreeListControl/TotalSummaries.md) { get; } | Gets the collection of total summary items calculated across all rows. |
| [TreeColumnFieldName](TreeListControl/TreeColumnFieldName.md) { get; set; } | Gets or sets the field name of the column that displays the tree hierarchy. |
| event [AutoGeneratedColumns](TreeListControl/AutoGeneratedColumns.md) | Occurs after columns are generated automatically. |
| event [AutoGeneratingColumn](TreeListControl/AutoGeneratingColumn.md) | Occurs when a column is generated automatically. |
| event [CellValueChanged](TreeListControl/CellValueChanged.md) | Occurs when a cell value has been changed. |
| event [CellValueChanging](TreeListControl/CellValueChanging.md) | Occurs while a cell value is being changed before it is posted to the data source. |
| event [CustomColumnDisplayText](TreeListControl/CustomColumnDisplayText.md) | Occurs when the display text of a cell is required. |
| event [CustomColumnSort](TreeListControl/CustomColumnSort.md) | Occurs when column values are compared with custom logic during data sorting. |
| event [CustomSummary](TreeListControl/CustomSummary.md) | Occurs when a summary item with the Custom summary type is calculated. |
| event [CustomUnboundColumnData](TreeListControl/CustomUnboundColumnData.md) | Occurs when a cell value of an unbound column is requested or posted. |
| event [HiddenEditor](TreeListControl/HiddenEditor.md) | Occurs after an in-place editor is closed. |
| event [ShowingEditor](TreeListControl/ShowingEditor.md) | Occurs before an in-place editor is activated. |
| event [ShownEditor](TreeListControl/ShownEditor.md) | Occurs after an in-place editor is activated. |
| event [ValidateCellValue](TreeListControl/ValidateCellValue.md) | Occurs when a cell value is validated. |
| [BestFit](TreeListControl/BestFit.md)(…) | Applies best-fit sizing to the specified column. |
| [BestFitAllColumns](TreeListControl/BestFitAllColumns.md)() | Applies best-fit sizing to all visible columns. |
| [ExportToImages](TreeListControl/ExportToImages.md)(…) | Exports the control's visible data to image files in the specified directory. |
| [ExportToPdf](TreeListControl/ExportToPdf.md)(…) | Exports the control's visible data to the specified file in PDF format. (2 methods) |
| [ExportToXlsx](TreeListControl/ExportToXlsx.md)(…) | Exports the control's visible data to the specified file in XLSX format. (2 methods) |
| [GetCellDisplayText](TreeListControl/GetCellDisplayText.md)(…) | Returns the display text of the specified cell. (2 methods) |
| [GetCellValue](TreeListControl/GetCellValue.md)(…) | Returns the value of the specified cell. (2 methods) |
| [GetTotalSummaryValue](TreeListControl/GetTotalSummaryValue.md)(…) | Returns the total summary value calculated for the specified summary item. |
| [MoveNextCell](TreeListControl/MoveNextCell.md)() | Moves focus to the next cell. |
| [MovePrevCell](TreeListControl/MovePrevCell.md)() | Moves focus to the previous cell. |
| [PopulateColumns](TreeListControl/PopulateColumns.md)() | Generates columns based on the data source fields. |
| [ResetColumnWidth](TreeListControl/ResetColumnWidth.md)() | Resets all column widths to their default values. |
| [RestoreLayout](TreeListControl/RestoreLayout.md)(…) | Restores the control's layout from the specified stream. (2 methods) |
| [SaveLayout](TreeListControl/SaveLayout.md)(…) | Saves the control's layout to the specified stream. (2 methods) |
| [SetCellValue](TreeListControl/SetCellValue.md)(…) | Sets the value of the specified cell. (2 methods) |

## See Also

* class [TreeListControlBase](./TreeListControlBase.md)
* namespace [Eremex.AvaloniaUI.Controls.TreeList](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->
