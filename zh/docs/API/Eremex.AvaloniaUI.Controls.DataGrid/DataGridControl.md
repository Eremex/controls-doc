# DataGridControl 类

将数据源中的数据显示为行和列，支持排序、分组、筛选和编辑。

**命名空间：** [`Eremex.AvaloniaUI.Controls.DataGrid`](./index.md)  
**程序集：** `Eremex.Avalonia.Controls.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## 声明

```csharp
public class DataGridControl : DataControlBase, IDataControl
```

## 构造函数

| 名称 | 说明 |
| --- | --- |
| [DataGridControl](DataGridControl/DataGridControl.md)() | 初始化 DataGridControl 类的新实例。 |

## 属性

| 名称 | 说明 |
| --- | --- |
| [AllowBandResizing](DataGridControl/AllowBandResizing.md) { get; set; } | 获取或设置用户是否可以调整列组的大小。 |
| [AllowBestFit](DataGridControl/AllowBestFit.md) { get; set; } | 获取或设置用户是否可以应用最佳列宽调整。 |
| [AllowColumnFiltering](DataGridControl/AllowColumnFiltering.md) { get; set; } | 获取或设置用户是否可以按列筛选数据。 |
| [AllowColumnMoving](DataGridControl/AllowColumnMoving.md) { get; set; } | 获取或设置用户是否可以通过拖动列标题对列重新排序。 |
| [AllowColumnResizing](DataGridControl/AllowColumnResizing.md) { get; set; } | 获取或设置用户是否可以调整列的大小。 |
| [AllowDragDrop](DataGridControl/AllowDragDrop.md) { get; set; } | 获取或设置是否启用行拖放。 |
| [AllowDragDropSortedRows](DataGridControl/AllowDragDropSortedRows.md) { get; set; } | 获取或设置数据排序时是否可以拖动行。 |
| [AllowEditingGroupSummaries](DataGridControl/AllowEditingGroupSummaries.md) { get; set; } | 获取或设置用户是否可以编辑分组汇总。 |
| [AllowEditingTotalSummaries](DataGridControl/AllowEditingTotalSummaries.md) { get; set; } | 获取或设置用户是否可以编辑总计汇总。 |
| [AllowGrouping](DataGridControl/AllowGrouping.md) { get; set; } | 获取或设置用户是否可以对数据进行分组。 |
| [AllowHorizontalVirtualization](DataGridControl/AllowHorizontalVirtualization.md) { get; set; } | 获取或设置是否对屏幕外的列进行虚拟化。 |
| [AllowResetColumnWidth](DataGridControl/AllowResetColumnWidth.md) { get; set; } | 获取或设置用户是否可以将列宽重置为默认值。 |
| [AllowScrollingOnDrag](DataGridControl/AllowScrollingOnDrag.md) { get; set; } | 获取或设置当拖动的元素接近视图边缘时视图是否自动滚动。 |
| [AllowSorting](DataGridControl/AllowSorting.md) { get; set; } | 获取或设置用户是否可以对数据进行排序。 |
| [AutoExpandAllGroups](DataGridControl/AutoExpandAllGroups.md) { get; set; } | 获取或设置是否自动展开所有分组。 |
| [AutoExpandDelayOnDrag](DataGridControl/AutoExpandDelayOnDrag.md) { get; set; } | 获取或设置拖动经过时分组自动展开之前的延迟。 |
| [AutoExpandOnDrag](DataGridControl/AutoExpandOnDrag.md) { get; set; } | 获取或设置当拖动的元素悬停在折叠的分组上方时，该分组是否自动展开。 |
| [AutoGenerateBands](DataGridControl/AutoGenerateBands.md) { get; set; } | 获取或设置是否自动生成列组。 |
| [AutoGenerateColumns](DataGridControl/AutoGenerateColumns.md) { get; set; } | 获取或设置是否根据数据源自动生成列。 |
| [Bands](DataGridControl/Bands.md) { get; } | 获取网格列组的集合。 |
| [BandsSource](DataGridControl/BandsSource.md) { get; set; } | 获取或设置其项用于生成列组的集合。 |
| [BandTemplate](DataGridControl/BandTemplate.md) { get; set; } | 获取或设置用于为 BandsSource 中的每一项创建列组的模板。 |
| [BestFitMode](DataGridControl/BestFitMode.md) { get; set; } | 获取或设置如何计算最佳列宽。 |
| [CellTemplate](DataGridControl/CellTemplate.md) { get; set; } | 获取或设置当列未定义自己的模板时用于显示单元格内容的默认模板。 |
| [ClipboardCopyHeaders](DataGridControl/ClipboardCopyHeaders.md) { get; set; } | 获取或设置是否将列标题与单元格值一起复制到剪贴板。 |
| [ColumnFilterButtonDisplayMode](DataGridControl/ColumnFilterButtonDisplayMode.md) { get; set; } | 获取或设置何时显示列筛选按钮。 |
| [ColumnFilterPopupMode](DataGridControl/ColumnFilterPopupMode.md) { get; set; } | 获取或设置列筛选弹出窗口的类型。 |
| [ColumnMenu](DataGridControl/ColumnMenu.md) { get; set; } | 获取或设置为列标题调用的上下文菜单。 |
| [Columns](DataGridControl/Columns.md) { get; } | 获取网格列的集合。 |
| [ColumnsSource](DataGridControl/ColumnsSource.md) { get; set; } | 获取或设置其项用于生成列的集合。 |
| [ColumnTemplate](DataGridControl/ColumnTemplate.md) { get; set; } | 获取或设置用于为 ColumnsSource 中的每一项创建列的模板。 |
| [Commands](DataGridControl/Commands.md) { get; } | 获取网格的命令。 |
| [ExtendScrollbarToFixedColumns](DataGridControl/ExtendScrollbarToFixedColumns.md) { get; set; } | 获取或设置水平滚动条是否延伸到固定列下方。 |
| [FilterPanelDisplayMode](DataGridControl/FilterPanelDisplayMode.md) { get; set; } | 获取或设置何时显示筛选面板。 |
| [FilterPanelText](DataGridControl/FilterPanelText.md) { get; } | 获取在筛选面板中显示的文本。 |
| [FixedColumnSeparatorWidth](DataGridControl/FixedColumnSeparatorWidth.md) { get; set; } | 获取或设置标记固定列的分隔符的宽度。 |
| [FixedLeftColumnWidth](DataGridControl/FixedLeftColumnWidth.md) { get; } | 获取固定到左边缘的列的总宽度。 |
| [FixedRightColumnWidth](DataGridControl/FixedRightColumnWidth.md) { get; } | 获取固定到右边缘的列的总宽度。 |
| [FocusedColumn](DataGridControl/FocusedColumn.md) { get; set; } | 获取或设置焦点列。 |
| [FocusedRowIndex](DataGridControl/FocusedRowIndex.md) { get; set; } | 获取或设置焦点行的索引。 |
| [GroupCount](DataGridControl/GroupCount.md) { get; set; } | 获取或设置用于对数据分组的前导排序列的数量。 |
| [GroupSummaries](DataGridControl/GroupSummaries.md) { get; set; } | 获取跨分组行计算的分组汇总项的集合。 |
| [GroupSummaryRowMinHeight](DataGridControl/GroupSummaryRowMinHeight.md) { get; set; } | 获取或设置显示分组汇总的分组页脚行的最小高度。 |
| [HeaderDropIndicatorWidth](DataGridControl/HeaderDropIndicatorWidth.md) { get; set; } | 获取或设置拖动列时在标题之间显示的指示器的宽度。 |
| [HeaderPanelMinHeight](DataGridControl/HeaderPanelMinHeight.md) { get; set; } | 获取或设置列标题面板的最小高度。 |
| [IsFilterPanelVisible](DataGridControl/IsFilterPanelVisible.md) { get; } | 获取当前是否显示筛选面板。 |
| [NavigationMode](DataGridControl/NavigationMode.md) { get; set; } | 获取或设置键盘导航是在单元格之间还是在行之间移动焦点。 |
| [RowCellMenu](DataGridControl/RowCellMenu.md) { get; set; } | 获取或设置为数据单元格调用的上下文菜单。 |
| [RowDragMode](DataGridControl/RowDragMode.md) { get; set; } | 获取或设置是通过行本身还是通过拖动手柄拖动行。 |
| [RowIndicatorWidth](DataGridControl/RowIndicatorWidth.md) { get; set; } | 获取或设置行指示器的宽度。 |
| [SerializationInfo](DataGridControl/SerializationInfo.md) { get; } | 获取网格的序列化信息。 |
| [ShowAutoFilterRow](DataGridControl/ShowAutoFilterRow.md) { get; set; } | 获取或设置是否显示自动筛选行。 |
| [ShowBands](DataGridControl/ShowBands.md) { get; set; } | 获取或设置是否显示列组标题。 |
| [ShowBandSeparators](DataGridControl/ShowBandSeparators.md) { get; set; } | 获取或设置是否显示列组标题之间的分隔符。 |
| [ShowColumnHeaders](DataGridControl/ShowColumnHeaders.md) { get; set; } | 获取或设置是否显示列标题面板。 |
| [ShowColumnMenuFixedItem](DataGridControl/ShowColumnMenuFixedItem.md) { get; set; } | 获取或设置是否在列标题上下文菜单中显示固定列项。 |
| [ShowConditionInAutoFilterRow](DataGridControl/ShowConditionInAutoFilterRow.md) { get; set; } | 获取或设置自动筛选行是否显示所应用的筛选条件。 |
| [ShowGroupedColumns](DataGridControl/ShowGroupedColumns.md) { get; set; } | 获取或设置已分组的列是否在数据列中保持可见。 |
| [ShowGroupPanel](DataGridControl/ShowGroupPanel.md) { get; set; } | 获取或设置是否显示分组面板。 |
| [ShowGroupSummaries](DataGridControl/ShowGroupSummaries.md) { get; set; } | 获取或设置是否显示显示分组汇总的分组页脚行。 |
| [ShowHorizontalLines](DataGridControl/ShowHorizontalLines.md) { get; set; } | 获取或设置是否显示水平网格线。 |
| [ShowRowIndicator](DataGridControl/ShowRowIndicator.md) { get; } | 获取是否显示行指示器。 |
| [ShowTotalSummaries](DataGridControl/ShowTotalSummaries.md) { get; set; } | 获取或设置是否显示总计汇总页脚。 |
| [ShowVerticalLines](DataGridControl/ShowVerticalLines.md) { get; set; } | 获取或设置是否显示垂直网格线。 |
| [TotalSummaries](DataGridControl/TotalSummaries.md) { get; } | 获取跨所有行计算的总计汇总项的集合。 |
| [TotalSummaryPanelMinHeight](DataGridControl/TotalSummaryPanelMinHeight.md) { get; set; } | 获取或设置总计汇总页脚面板的最小高度。 |
| [UsePlatformRowDragDrop](DataGridControl/UsePlatformRowDragDrop.md) { get; set; } | 获取或设置拖动行时是否使用平台拖放。 |
| [VisibleRowCount](DataGridControl/VisibleRowCount.md) { get; } | 获取当前可见行的数量。 |

## 方法

| 名称 | 说明 |
| --- | --- |
| override [BeginDataUpdate](DataGridControl/BeginDataUpdate.md)() |  |
| [BestFit](DataGridControl/BestFit.md)(…) | 设置指定列的宽度以最佳适应其内容。 |
| [BestFitAllColumns](DataGridControl/BestFitAllColumns.md)() | 设置所有列的宽度以最佳适应其内容。 |
| [CollapseAllGroups](DataGridControl/CollapseAllGroups.md)() | 折叠所有分组行。 |
| [CollapseGroupRow](DataGridControl/CollapseGroupRow.md)(…) | 折叠指定索引处的分组行。 |
| override [CommitEditing](DataGridControl/CommitEditing.md)() |  |
| [ExpandAllGroups](DataGridControl/ExpandAllGroups.md)() | 展开所有分组行。 |
| [ExpandGroupRow](DataGridControl/ExpandGroupRow.md)(…) | 展开指定索引处的分组行。 |
| [ExportToImages](DataGridControl/ExportToImages.md)(…) | 将网格导出为保存在指定目录中的图像文件。 |
| [ExportToPdf](DataGridControl/ExportToPdf.md)(…) | 将网格以 PDF 格式导出到指定文件。（2 个重载） |
| [ExportToXlsx](DataGridControl/ExportToXlsx.md)(…) | 将网格以 XLSX 格式导出到指定文件。（2 个重载） |
| [FindRowByDisplayText](DataGridControl/FindRowByDisplayText.md)(…) | 查找指定字段中单元格显示文本等于指定文本的第一行。如果未找到任何行，则返回 InvalidRowIndex。（2 个重载） |
| [FindRowByItem](DataGridControl/FindRowByItem.md)(…) | 查找与指定数据源项对应的行。如果未找到该项，则返回 InvalidRowIndex。 |
| [FindRowByValue](DataGridControl/FindRowByValue.md)(…) | 查找指定字段中单元格值等于指定值的第一行。如果未找到任何行，则返回 InvalidRowIndex。（2 个重载） |
| [GetCellDisplayText](DataGridControl/GetCellDisplayText.md)(…) | 获取指定行与绑定到指定字段的列交叉处单元格的显示文本。（2 个重载） |
| [GetCellValue](DataGridControl/GetCellValue.md)(…) | 获取指定行与指定列交叉处单元格的值。（2 个重载） |
| [GetGroupChildRowCount](DataGridControl/GetGroupChildRowCount.md)() | 获取顶级分组行的数量。 |
| [GetGroupChildRowCount](DataGridControl/GetGroupChildRowCount.md)(…) | 获取指定索引处分组行的子行数量。 |
| [GetGroupChildRowIndex](DataGridControl/GetGroupChildRowIndex.md)(…) | 获取指定索引处分组行内指定位置处子行的索引。（2 个重载） |
| [GetGroupRowValue](DataGridControl/GetGroupRowValue.md)(…) | 获取指定索引处分组行的值。 |
| [GetGroupSummaryValue](DataGridControl/GetGroupSummaryValue.md)(…) |  |
| [GetParentRowIndex](DataGridControl/GetParentRowIndex.md)(…) | 获取指定索引处行的父分组行的索引。 |
| [GetRowIndexBySourceItemIndex](DataGridControl/GetRowIndexBySourceItemIndex.md)(…) | 获取与指定索引处数据源项对应的行的索引。 |
| [GetRowIndexByVisibleRowIndex](DataGridControl/GetRowIndexByVisibleRowIndex.md)(…) | 获取指定可见索引处行的索引。 |
| [GetRowLevel](DataGridControl/GetRowLevel.md)(…) | 获取指定索引处行的嵌套级别。 |
| [GetSelectedRowIndexes](DataGridControl/GetSelectedRowIndexes.md)() | 获取所选行的索引。 |
| [GetSourceItem](DataGridControl/GetSourceItem.md)(…) | 获取数据源中指定索引处的项。 |
| [GetSourceItemByRowIndex](DataGridControl/GetSourceItemByRowIndex.md)(…) | 获取与指定索引处的行对应的数据源项。 |
| [GetSourceItemByVisibleRowIndex](DataGridControl/GetSourceItemByVisibleRowIndex.md)(…) | 获取与指定可见索引处的行对应的数据源项。 |
| [GetSourceItemIndexByRowIndex](DataGridControl/GetSourceItemIndexByRowIndex.md)(…) | 获取指定索引处行的数据源索引。 |
| [GetSourceItemIndexByVisibleRowIndex](DataGridControl/GetSourceItemIndexByVisibleRowIndex.md)(…) | 获取指定可见索引处行的数据源索引。 |
| [GetSourceItemValue](DataGridControl/GetSourceItemValue.md)(…) | 获取指定索引处数据源项中指定列字段的值。（2 个重载） |
| [GetTotalSummaryValue](DataGridControl/GetTotalSummaryValue.md)(…) | 获取指定总计汇总的计算值。 |
| [GetVisibleRowIndexByRowIndex](DataGridControl/GetVisibleRowIndexByRowIndex.md)(…) | 获取指定索引处行的可见索引。 |
| [GetVisibleRowIndexBySourceItemIndex](DataGridControl/GetVisibleRowIndexBySourceItemIndex.md)(…) | 获取与指定索引处数据源项对应的行的可见索引。 |
| [IsGroupFooterRow](DataGridControl/IsGroupFooterRow.md)(…) | 确定指定索引处的行是否为分组页脚行。 |
| [IsGroupRow](DataGridControl/IsGroupRow.md)(…) | 确定指定索引处的行是否为分组行。 |
| [IsGroupRowExpanded](DataGridControl/IsGroupRowExpanded.md)(…) | 确定指定索引处的分组行是否已展开。 |
| [IsRowSelected](DataGridControl/IsRowSelected.md)(…) | 确定指定索引处的行是否被选中。 |
| [MoveNextCell](DataGridControl/MoveNextCell.md)() | 将焦点移到下一个单元格。 |
| [MoveNextRow](DataGridControl/MoveNextRow.md)() | 将焦点移到下一行。 |
| [MovePrevCell](DataGridControl/MovePrevCell.md)() | 将焦点移到上一个单元格。 |
| [MovePrevRow](DataGridControl/MovePrevRow.md)(…) | 将焦点移到上一行，并可选择允许焦点移到自动筛选行。 |
| [PopulateColumns](DataGridControl/PopulateColumns.md)() | 根据数据源创建列。 |
| [RefreshData](DataGridControl/RefreshData.md)() | 重新读取数据源并刷新网格的内容。 |
| [RefreshRow](DataGridControl/RefreshRow.md)(…) | 刷新指定索引处行的可见单元格。 |
| [ResetColumnWidth](DataGridControl/ResetColumnWidth.md)() | 将所有列的宽度重置为默认值。 |
| [RestoreLayout](DataGridControl/RestoreLayout.md)(…) | 从指定流还原网格的布局。（2 个重载） |
| [SaveLayout](DataGridControl/SaveLayout.md)(…) | 将网格的布局保存到指定流。（2 个重载） |
| [SelectRange](DataGridControl/SelectRange.md)(…) | 选择指定起始行索引和结束行索引之间的所有行。 |
| [SelectRow](DataGridControl/SelectRow.md)(…) | 选择指定索引处的行。 |
| [SetCellValue](DataGridControl/SetCellValue.md)(…) | 设置指定行与指定列交叉处单元格的值。（2 个重载） |
| [UnselectRow](DataGridControl/UnselectRow.md)(…) | 取消选择指定索引处的行。 |

## 事件

| 名称 | 说明 |
| --- | --- |
| event [AutoGeneratedColumns](DataGridControl/AutoGeneratedColumns.md) | 在根据数据源自动生成列之后发生。 |
| event [AutoGeneratingColumn](DataGridControl/AutoGeneratingColumn.md) | 在即将自动生成列时发生。取消该事件可阻止生成该列。 |
| event [CellValueChanged](DataGridControl/CellValueChanged.md) | 在单元格值更改后发生。 |
| event [CellValueChanging](DataGridControl/CellValueChanging.md) | 在用户于编辑器中修改单元格值、更改提交之前发生。 |
| event [CompleteDragDrop](DataGridControl/CompleteDragDrop.md) | 在拖放操作完成后发生。 |
| event [CustomColumnDisplayText](DataGridControl/CustomColumnDisplayText.md) | 在需要单元格的显示文本时发生。设置 DisplayText 属性可自定义文本。 |
| event [CustomColumnGroup](DataGridControl/CustomColumnGroup.md) | 在分组期间比较两行时发生。设置 Result 属性可指示这两行是否属于同一分组。 |
| event [CustomColumnSort](DataGridControl/CustomColumnSort.md) | 在排序期间比较两行时发生。设置 Result 属性可实现自定义排序。 |
| event [CustomGroupValueDisplayText](DataGridControl/CustomGroupValueDisplayText.md) | 在需要分组行值的显示文本时发生。设置 DisplayText 属性可自定义文本。 |
| event [CustomRowFilter](DataGridControl/CustomRowFilter.md) | 在筛选行时发生。设置 Visible 属性可显示或隐藏该行。 |
| event [CustomSummary](DataGridControl/CustomSummary.md) | 在计算汇总值时发生。设置 SummaryValue 属性可实现自定义汇总。 |
| event [CustomUnboundColumnData](DataGridControl/CustomUnboundColumnData.md) | 在请求或提交未绑定列单元格的值时发生。设置 Value 属性可提供该值。 |
| event [DragOver](DataGridControl/DragOver.md) | 在拖动的行位于网格上方时发生。设置 Effects 和 DropPosition 属性可自定义放置操作。 |
| event [Drop](DataGridControl/Drop.md) | 在将拖动的行放置到网格上时发生。处理该事件可执行自定义放置操作。 |
| event [HiddenEditor](DataGridControl/HiddenEditor.md) | 在编辑器关闭后发生。 |
| event [RowClick](DataGridControl/RowClick.md) | 在单击行时发生。 |
| event [SelectionChanged](DataGridControl/SelectionChanged.md) | 在行选择更改时发生。 |
| event [ShowingEditor](DataGridControl/ShowingEditor.md) | 在为单元格激活编辑器之前发生。取消该事件可阻止编辑。 |
| event [ShownEditor](DataGridControl/ShownEditor.md) | 在为单元格激活编辑器之后发生。 |
| event [StartDrag](DataGridControl/StartDrag.md) | 在行拖动操作开始时发生。设置 Effects 和 Data 属性可自定义拖动操作。 |
| event [ValidateCellValue](DataGridControl/ValidateCellValue.md) | 在验证单元格值时发生。设置 ErrorContent 属性可指示错误。 |

## 字段

| 名称 | 说明 |
| --- | --- |
| const [InvalidRowIndex](DataGridControl/InvalidRowIndex.md) | 表示无效的行索引。 |

## 另请参阅

* 类 [DataControlBase](../Eremex.AvaloniaUI.Controls.DataControl/DataControlBase.md)
* 命名空间 [Eremex.AvaloniaUI.Controls.DataGrid](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
