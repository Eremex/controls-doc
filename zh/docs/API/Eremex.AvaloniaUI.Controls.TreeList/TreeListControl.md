# TreeListControl 类

显示按节点层次结构排列的项集合。

**命名空间：** [`Eremex.AvaloniaUI.Controls.TreeList`](./index.md)  
**程序集：** `Eremex.Avalonia.Controls.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## 声明

```csharp
public class TreeListControl : TreeListControlBase
```

## 构造函数

| 名称 | 说明 |
| --- | --- |
| [TreeListControl](TreeListControl/TreeListControl.md)() | 默认构造函数。 |

## 属性

| 名称 | 说明 |
| --- | --- |
| [AllowBandResizing](TreeListControl/AllowBandResizing.md) { get; set; } | 获取或设置用户是否可以调整列组的大小。 |
| [AllowBestFit](TreeListControl/AllowBestFit.md) { get; set; } | 获取或设置用户是否可以应用最佳列宽调整。 |
| [AllowColumnFiltering](TreeListControl/AllowColumnFiltering.md) { get; set; } | 获取或设置用户是否可以按列筛选数据。 |
| [AllowColumnMoving](TreeListControl/AllowColumnMoving.md) { get; set; } | 获取或设置用户是否可以通过拖动列标题对列重新排序。 |
| [AllowColumnResizing](TreeListControl/AllowColumnResizing.md) { get; set; } | 获取或设置用户是否可以调整列的大小。 |
| [AllowEditingTotalSummaries](TreeListControl/AllowEditingTotalSummaries.md) { get; set; } | 获取或设置用户是否可以编辑总计汇总。 |
| [AllowHorizontalVirtualization](TreeListControl/AllowHorizontalVirtualization.md) { get; set; } | 获取或设置是否对屏幕外的列进行虚拟化。 |
| [AllowResetColumnWidth](TreeListControl/AllowResetColumnWidth.md) { get; set; } | 获取或设置用户是否可以将列宽重置为默认值。 |
| [AllowSorting](TreeListControl/AllowSorting.md) { get; set; } | 获取或设置用户是否可以对数据进行排序。 |
| [AutoGenerateBands](TreeListControl/AutoGenerateBands.md) { get; set; } | 获取或设置是否自动生成列组。 |
| [AutoGenerateColumns](TreeListControl/AutoGenerateColumns.md) { get; set; } | 获取或设置是否根据数据源自动生成列。 |
| [AutoGenerateServiceColumns](TreeListControl/AutoGenerateServiceColumns.md) { get; set; } | 获取或设置是否自动生成服务列。 |
| [AutoMoveRowFocus](TreeListControl/AutoMoveRowFocus.md) { get; set; } | 获取或设置键盘导航在越过最后一列或第一列时是否将焦点移到下一行或上一行。 |
| [Bands](TreeListControl/Bands.md) { get; } | 获取控件的列组集合。 |
| [BandsSource](TreeListControl/BandsSource.md) { get; set; } | 获取或设置其项用于生成列组的集合。 |
| [BandTemplate](TreeListControl/BandTemplate.md) { get; set; } | 获取或设置用于为 BandsSource 中的每一项创建列组的模板。 |
| [BestFitMode](TreeListControl/BestFitMode.md) { get; set; } | 获取或设置如何计算最佳列宽。 |
| [CellTemplate](TreeListControl/CellTemplate.md) { get; set; } | 获取或设置当列未定义自己的模板时用于显示单元格内容的默认模板。 |
| [ClipboardCopyHeaders](TreeListControl/ClipboardCopyHeaders.md) { get; set; } | 获取或设置是否将列标题与单元格值一起复制到剪贴板。 |
| [ColumnFilterButtonDisplayMode](TreeListControl/ColumnFilterButtonDisplayMode.md) { get; set; } | 获取或设置何时显示列筛选按钮。 |
| [ColumnFilterPopupMode](TreeListControl/ColumnFilterPopupMode.md) { get; set; } | 获取或设置列筛选弹出窗口的类型。 |
| [ColumnMenu](TreeListControl/ColumnMenu.md) { get; set; } | 获取或设置为列标题调用的上下文菜单。 |
| [Columns](TreeListControl/Columns.md) { get; } | 获取控件的列集合。 |
| [ColumnsSource](TreeListControl/ColumnsSource.md) { get; set; } | 获取或设置其项用于生成列的集合。 |
| [ColumnTemplate](TreeListControl/ColumnTemplate.md) { get; set; } | 获取或设置用于为 ColumnsSource 中的每一项创建列的模板。 |
| [ExtendScrollbarToFixedColumns](TreeListControl/ExtendScrollbarToFixedColumns.md) { get; set; } | 获取或设置水平滚动条是否延伸到固定列下方。 |
| [FilterPanelDisplayMode](TreeListControl/FilterPanelDisplayMode.md) { get; set; } | 获取或设置何时显示筛选面板。 |
| [FilterPanelText](TreeListControl/FilterPanelText.md) { get; } | 获取在筛选面板中显示的文本。 |
| [FixedColumnSeparatorWidth](TreeListControl/FixedColumnSeparatorWidth.md) { get; set; } | 获取或设置标记固定列的分隔符的宽度。 |
| [FixedLeftColumnWidth](TreeListControl/FixedLeftColumnWidth.md) { get; } | 获取固定到左边缘的列的总宽度。 |
| [FixedRightColumnWidth](TreeListControl/FixedRightColumnWidth.md) { get; } | 获取固定到右边缘的列的总宽度。 |
| [FocusedColumn](TreeListControl/FocusedColumn.md) { get; set; } | 获取或设置焦点列。 |
| [HeaderDropIndicatorWidth](TreeListControl/HeaderDropIndicatorWidth.md) { get; set; } | 获取或设置拖动列时在标题之间显示的指示器的宽度。 |
| [HeaderPanelMinHeight](TreeListControl/HeaderPanelMinHeight.md) { get; set; } | 获取或设置列标题面板的最小高度。 |
| [IsFilterPanelVisible](TreeListControl/IsFilterPanelVisible.md) { get; } | 获取当前是否显示筛选面板。 |
| [NavigationMode](TreeListControl/NavigationMode.md) { get; set; } | 获取或设置键盘导航是在单元格之间还是在行之间移动焦点。 |
| [RowDragMode](TreeListControl/RowDragMode.md) { get; set; } | 获取或设置是通过行本身还是通过拖动手柄拖动行。 |
| [RowIndicatorWidth](TreeListControl/RowIndicatorWidth.md) { get; set; } | 获取或设置行指示器的宽度。 |
| [SerializationInfo](TreeListControl/SerializationInfo.md) { get; } | 获取存储控件已保存布局的序列化信息。 |
| [ShowAutoFilterRow](TreeListControl/ShowAutoFilterRow.md) { get; set; } | 获取或设置是否显示自动筛选行。 |
| [ShowBands](TreeListControl/ShowBands.md) { get; set; } | 获取或设置是否显示列组标题。 |
| [ShowBandSeparators](TreeListControl/ShowBandSeparators.md) { get; set; } | 获取或设置是否显示列组标题之间的分隔符。 |
| [ShowCheckAllNodesCheckBox](TreeListControl/ShowCheckAllNodesCheckBox.md) { get; set; } | 获取或设置是否显示勾选所有节点的复选框。 |
| [ShowColumnHeaders](TreeListControl/ShowColumnHeaders.md) { get; set; } | 获取或设置是否显示列标题面板。 |
| [ShowColumnMenuFixedItem](TreeListControl/ShowColumnMenuFixedItem.md) { get; set; } | 获取或设置是否在列标题上下文菜单中显示固定列项。 |
| [ShowConditionInAutoFilterRow](TreeListControl/ShowConditionInAutoFilterRow.md) { get; set; } | 获取或设置自动筛选行是否显示所应用的筛选条件。 |
| [ShowHorizontalLines](TreeListControl/ShowHorizontalLines.md) { get; set; } | 获取或设置是否显示水平网格线。 |
| [ShowRowIndicator](TreeListControl/ShowRowIndicator.md) { get; } | 获取是否显示行指示器。 |
| [ShowTotalSummaries](TreeListControl/ShowTotalSummaries.md) { get; set; } | 获取或设置是否显示总计汇总页脚。 |
| [ShowVerticalLines](TreeListControl/ShowVerticalLines.md) { get; set; } | 获取或设置是否显示垂直网格线。 |
| [TotalSummaries](TreeListControl/TotalSummaries.md) { get; } | 获取跨所有行计算的总计汇总项的集合。 |
| [TotalSummaryPanelMinHeight](TreeListControl/TotalSummaryPanelMinHeight.md) { get; set; } | 获取或设置总计汇总页脚面板的最小高度。 |
| [TreeColumnFieldName](TreeListControl/TreeColumnFieldName.md) { get; set; } | 获取或设置显示树层次结构的列的字段名。 |

## 方法

| 名称 | 说明 |
| --- | --- |
| [BestFit](TreeListControl/BestFit.md)(…) | 对指定列应用最佳宽度调整。 |
| [BestFitAllColumns](TreeListControl/BestFitAllColumns.md)() | 对所有可见列应用最佳宽度调整。 |
| [ExportToImages](TreeListControl/ExportToImages.md)(…) | 将控件的可见数据导出为指定目录中的图像文件。 |
| [ExportToPdf](TreeListControl/ExportToPdf.md)(…) | 将控件的可见数据以 PDF 格式导出到指定文件。（2 个重载） |
| [ExportToXlsx](TreeListControl/ExportToXlsx.md)(…) | 将控件的可见数据以 XLSX 格式导出到指定文件。（2 个重载） |
| [GetCellDisplayText](TreeListControl/GetCellDisplayText.md)(…) | 返回指定单元格的显示文本。（2 个重载） |
| [GetCellValue](TreeListControl/GetCellValue.md)(…) | 返回指定单元格的值。（2 个重载） |
| [GetTotalSummaryValue](TreeListControl/GetTotalSummaryValue.md)(…) | 返回为指定汇总项计算的总计汇总值。 |
| [MoveNextCell](TreeListControl/MoveNextCell.md)() | 将焦点移到下一个单元格。 |
| [MovePrevCell](TreeListControl/MovePrevCell.md)() | 将焦点移到上一个单元格。 |
| [PopulateColumns](TreeListControl/PopulateColumns.md)() | 根据数据源字段生成列。 |
| [ResetColumnWidth](TreeListControl/ResetColumnWidth.md)() | 将所有列宽重置为默认值。 |
| [RestoreLayout](TreeListControl/RestoreLayout.md)(…) | 从指定流还原控件的布局。（2 个重载） |
| [SaveLayout](TreeListControl/SaveLayout.md)(…) | 将控件的布局保存到指定流。（2 个重载） |
| [SetCellValue](TreeListControl/SetCellValue.md)(…) | 设置指定单元格的值。（2 个重载） |

## 事件

| 名称 | 说明 |
| --- | --- |
| event [AutoGeneratedColumns](TreeListControl/AutoGeneratedColumns.md) | 在自动生成列之后发生。 |
| event [AutoGeneratingColumn](TreeListControl/AutoGeneratingColumn.md) | 在自动生成列时发生。 |
| event [CellValueChanged](TreeListControl/CellValueChanged.md) | 在单元格值更改后发生。 |
| event [CellValueChanging](TreeListControl/CellValueChanging.md) | 在单元格值正在更改、尚未提交到数据源时发生。 |
| event [CustomColumnDisplayText](TreeListControl/CustomColumnDisplayText.md) | 在需要单元格的显示文本时发生。 |
| event [CustomColumnSort](TreeListControl/CustomColumnSort.md) | 在数据排序期间使用自定义逻辑比较列值时发生。 |
| event [CustomSummary](TreeListControl/CustomSummary.md) | 在计算汇总类型为 Custom 的汇总项时发生。 |
| event [CustomUnboundColumnData](TreeListControl/CustomUnboundColumnData.md) | 在请求或提交未绑定列的单元格值时发生。 |
| event [HiddenEditor](TreeListControl/HiddenEditor.md) | 在就地编辑器关闭后发生。 |
| event [ShowingEditor](TreeListControl/ShowingEditor.md) | 在激活就地编辑器之前发生。 |
| event [ShownEditor](TreeListControl/ShownEditor.md) | 在激活就地编辑器之后发生。 |
| event [ValidateCellValue](TreeListControl/ValidateCellValue.md) | 在验证单元格值时发生。 |

## 另请参阅

* 类 [TreeListControlBase](./TreeListControlBase.md)
* 命名空间 [Eremex.AvaloniaUI.Controls.TreeList](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
