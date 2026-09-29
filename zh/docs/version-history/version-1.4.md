---
title: 1.4版本
order: 14
seealso: []
---

# 版本 1.4


## 1.4.34

### Avalonia 12 支持

此版本为 Eremex Controls 库带来了对 Avalonia 12 的全面支持。 Avalonia 12 在性能、稳定性和平台可靠性方面实现了显着改进。此更新确保 Eremex Controls 套件与新版本 Avalonia 框架中引入的更改顺利集成。

有关 Avalonia 12 中重大更改的详细信息，请参阅：
[https://docs.avaloniaui.net/docs/avalonia12-breaking-changes](https://docs.avaloniaui.net/docs/avalonia12-breaking-changes)。




### DataGrid 和 TreeList

#### 行拖放增强功能

##### 行预览


DataGrid 和 TreeList 现在在[拖放操作](../controls/datagrid/row-drag-and-drop.md)期间显示行预览，在您重新排序或移动数据时为您提供视觉反馈。

![grid-dragdrop-row-previews-wn14](../images/grid-dragdrop-row-previews-wn14.png)

当您拖动多行时，行预览会显示正在拖动的对象的数量。

![grid-dragdrop-multiple-row-previews-wn14](../images/grid-dragdrop-multiple-row-previews-wn14.png)

##### 行拖动手柄

该版本添加了新的拖动模式，其中使用特殊的拖动手柄来拖动行。拖动手柄显示在行左侧的行指示器区域中。

![grid-dragdrop-drag-handle](../images/grid-draganddrop-draghandle-mode.gif)

当启用拖放功能时，拖动手柄可简化单元格编辑器的激活。以前，用户通过单击并拖动任何行单元格来启动行拖放。然而，这种行为与在单元格内按下鼠标时激活单元格编辑器的要求（许多人表示）相矛盾。新的基于拖动手柄的模式解决了这个问题：

- 默认情况下，单击单元格即可激活单元格编辑器。
- 要拖动行，请使用专用的行拖动手柄。

######相关API

- `DataGridControl.RowDragMode`
- `DataGridControl.RowIndicatorWidth`
- `TreeListControl.RowDragMode`
- `TreeListControl.RowIndicatorWidth`

##### 重大更改 - 在应用程序之间拖动行

从版本 1.4 开始，要允许在应用程序之间拖动行，请为开始拖放操作的控件启用新的 `UsePlatformRowDragDrop` 属性。请注意，在基于平台的行拖动操作期间不会显示行预览。

v1.4 之前的版本不需要任何额外的选项即可在应用程序之间启用行拖放。

##### 文档

- [Data Grid - Row Drag-and-Drop](../controls/datagrid/row-drag-and-drop.md)
- [Tree List - Node Drag-and-Drop](../controls/treelist/node-drag-and-drop.md)

#### 列标题拖动视觉增强

要隐藏列，用户可以将其列标头拖离标头面板一小段距离并将其放置在那里。为了提供有关此操作的清晰视觉提示，”隐藏列”提示现在显示在拖动的列标题上方。

![grid-column-drag-hidecolumn-hint](../images/grid-column-drag-hidecolumn-hint.png)

此外，在拖动操作期间，列标头的预览现在显示为半透明并带有阴影效果。

![grid-column-drag-shadow-effect](../images/grid-column-drag-shadow-effect.png)

#### 最适合

DataGrid 和 TreeList 控件现在支持最佳适配功能。此功能允许用户自动将列大小调整到理想的最小宽度，以完整显示单元格内容。

![bestfit-feature](../images/bestfit-feature.png)

要应用最佳拟合，用户可以双击列标题的右边缘或从列的上下文菜单中选择”最佳拟合”命令。用户还可以一次将”最佳适合”应用到所有列，以确保所有内容保持完全可见。

![bestfit-feature-bestfitall](../images/bestfit-feature-bestfitall.png)

控件包括 `BestFitMode` 属性，用于指定在最佳拟合操作期间测量哪些行值：

- `Fast` 模式 – 测量唯一行值的宽度。这可以提高大多数标准场景中的最佳拟合性能。

- `Full` 模式 – 测量所有行值的宽度，包括重复值。此模式比”快速”慢，但在使用单元模板或验证错误时可以正确计算列宽度。

#####相关API

- `DataGridControl.AllowBestFit`
- `DataGridControl.BestFitMode`
- `DataGridControl.BestFitMode`
- `DataGridControl.BestFit`
- `DataGridControl.BestFitAllColumns`
- `GridColumn.AllowBestFit`
- `GridColumn.BestFitMode`
- `GridColumn.BestFitMode`
- `TreeListControl.AllowBestFit`
- `TreeListControl.BestFitMode`
- `TreeListControl.BestFitMode`
- `TreeListControl.BestFit`
- `TreeListControl.BestFitAllColumns`
- `TreeListColumn.AllowBestFit`
- `TreeListColumn.BestFitMode`
- `TreeListColumn.BestFitMode`

##### 文档

- [Data Grid - Best Fit](../controls/datagrid/columns.md#best-fit)
- [Tree List - Best Fit](../controls/treelist/columns.md#best-fit)

#### 重置用户对列宽的更改

用户更改列宽度（通过拖动或使用”最佳拟合”）后，_重置列宽_命令将出现在列上下文菜单中。此命令重置用户对列宽度所做的更改，恢复用户修改之前应用于 XAML 或代码隐藏中的列的原始宽度。

![columns-resetcolumnwidthmenu](../images/columns-resetcolumnwidthmenu.png)

#####相关API

- `DataGridControl.AllowResetColumnWidth`
- `DataGridControl.ResetColumnWidth`
- `TreeListControl.AllowResetColumnWidth`
- `TreeListControl.ResetColumnWidth`

#### 已修复的问题

- TreeList - 如果 `ExpandNodesOnFiltering` 为 `true`，则在过滤数据时引发 `StackOverflowException`。
- TreeList - 当节点集合更改时，自动筛选行中的活动编辑器将关闭。
- DataGrid 和 TreeList - `Cmd+A` 快捷键不适用于 Mac。

### Cartesian Chart - 十字准线增强

Cartesian Chart 控件扩展了其公共 API，让您能够对十字准线标签的行为和外观进行更精细的控制。

#### 新的十字准线标签显示模式

`CrosshairOptions.SeriesLabelMode` 属性指定是否以及如何组合多个十字准线标签。该属性的默认值现在是 `Smart`：

- `Smart` 模式 — 每个系列都显示自己的十字准线标签。当标签重叠时，它们会合并为一个标签。
  
![chart-CrosshairSeriesLabelMode-smart](../images/chart-CrosshairSeriesLabelMode-smart.png)

#### 十字线系列排序

当多个系列组合在单个十字线标签中时，您可以使用新的 `CrosshairOptions.SeriesLabelItemSortMode` 属性来指定标签中系列的显示顺序：

- `By Series` 顺序 — 按系列添加到 `CartesianChart.Series` 集合中的顺序对系列进行排序。

![chart-CrosshairSeriesLabelItemSortMode-BySeries](../images/chart-CrosshairSeriesLabelItemSortMode-BySeries.png)

- `By Value` 顺序 — 按 _Y_ 值对系列进行排序。

![chart-CrosshairSeriesLabelItemSortMode-ByValue](../images/chart-CrosshairSeriesLabelItemSortMode-ByValue.png)

#### 仅包含光标附近的系列

以下属性允许您仅显示光标附近数据点的十字准线标签。

- `CrosshairOptions.MaxPickDistance` — 指定搜索要包含在十字准线标签中的数据点的范围。

![chart-Crosshair-MaxPickDistance](../images/chart-Crosshair-MaxPickDistance.png)

#### 十字线显示延迟

- `CrosshairOptions.SeriesLabelShowDelay` — 指定显示十字线系列标签之前的延迟（以毫秒为单位）。


#### 显示和隐藏十字线 API

- `ShowCrosshair(Point position)`
- `HideCrosshair()`

#### 更新的十字准线模板

图表控件的十字准线模板进行了改造，优化了结构，支持新的系列排序功能，并在不同场景下实现一致的视觉外观。

![chart-crosshairtemplate-changes-v14](../images/chart-crosshairtemplate-changes-v14.png)

模板更改包括：

- `CrosshairAllSeriesLabelControlData` 类现在包含 `ObservableCollection<CrosshairSeriesLabelItem> SeriesItems` 集合，而不是 `CrosshairAllSeriesLabelGroup` 集合。
- `CrosshairAllSeriesLabelGroup` 类别已被删除。
- `CrosshairAllSeriesLabelSeriesItem` 类别已重命名为 `CrosshairSeriesLabelItem`。此类包含有关系列参数和参数前缀的信息。
- `CrosshairAllSeriesLabelSeriesValueItem` 类别已重命名为 `CrosshairSeriesLabelSeriesValueItem`。
- `CrosshairSingleSeriesLabelControlData` 类不再继承自 `CrosshairAllSeriesLabelSeriesValueItem`。 `CrosshairSingleSeriesLabelControlData` 现在公开 `CrosshairSeriesLabelItem` 类型的 `SeriesItem` 属性。

#### 文档

- [Crosshair](../controls/charts/crosshair.md)


### Docking UI

#### 已修复的问题

- 在某些情况下，浮动面板停靠时会引发异常。
- 当显示启用了 `OverlayDismissEventPassThrough` 属性的菜单时，不会激活 dock item。

### 重大变化

- 对 `CommunityToolkit.Mvvm ` 包的依赖已被删除。如果您的项目需要此包，请显式添加对 `CommunityToolkit.Mvvm` 的引用。
- `DataControlCommands`、`DataGridControlCommands`、`TreeListCommands` 和编辑器命令现在包含 `ICommand`，而不是 CommunityToolkit 的 `IRelayCommand`。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
