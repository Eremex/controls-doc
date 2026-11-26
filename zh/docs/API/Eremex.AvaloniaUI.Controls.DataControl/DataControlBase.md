# DataControlBase 类

为以行形式显示项集合的数据控件提供基类。

**命名空间：** [`Eremex.AvaloniaUI.Controls.DataControl`](./index.md)  
**程序集：** `Eremex.Avalonia.Controls.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## 声明

```csharp
public abstract class DataControlBase : TemplatedControl, IBandsOwner, ISortedInfoCollectionOwner
```

## 属性

| 名称 | 说明 |
| --- | --- |
| [ActiveEditor](DataControlBase/ActiveEditor.md) { get; } | 获取当前活动的就地编辑器。 |
| [AllowEditing](DataControlBase/AllowEditing.md) { get; set; } | 获取或设置用户是否可以编辑单元格值。 |
| [AllowImmediateEditorValuePosting](DataControlBase/AllowImmediateEditorValuePosting.md) { get; set; } | 获取或设置编辑器值在更改时是否立即提交。 |
| [AutoScrollToFocusedRow](DataControlBase/AutoScrollToFocusedRow.md) { get; set; } | 获取或设置视图是否自动滚动以使焦点行保持可见。 |
| [EditorButtonShowMode](DataControlBase/EditorButtonShowMode.md) { get; set; } | 获取或设置何时显示编辑器按钮。 |
| [EditorShowMode](DataControlBase/EditorShowMode.md) { get; set; } | 获取或设置何时激活就地编辑器。 |
| [FilterString](DataControlBase/FilterString.md) { get; set; } | 获取或设置应用于数据的筛选条件字符串。 |
| [FocusedItem](DataControlBase/FocusedItem.md) { get; set; } | 获取或设置焦点数据项。 |
| virtual [HeaderDropIndex](DataControlBase/HeaderDropIndex.md) { get; set; } | 获取或设置拖动的列标题放置到的索引。 |
| [IgnoreValidationAttributesOnCommit](DataControlBase/IgnoreValidationAttributesOnCommit.md) { get; set; } | 获取或设置在提交单元格值时是否忽略验证特性。 |
| [IsColumnChooserVisible](DataControlBase/IsColumnChooserVisible.md) { get; set; } | 获取或设置是否显示列选择器。 |
| [IsFilterEnabled](DataControlBase/IsFilterEnabled.md) { get; set; } | 获取或设置是否启用筛选。 |
| [IsSearchPanelVisible](DataControlBase/IsSearchPanelVisible.md) { get; set; } | 获取或设置搜索面板是否可见。 |
| [ItemsSource](DataControlBase/ItemsSource.md) { get; set; } | 获取或设置其项由控件以行形式显示的数据源。 |
| [KeepSelectedOnClick](DataControlBase/KeepSelectedOnClick.md) { get; set; } | 获取或设置再次单击时所选行是否保持选中状态。 |
| [RowLevelIndent](DataControlBase/RowLevelIndent.md) { get; set; } | 获取或设置每个行嵌套级别应用的缩进。 |
| [RowMinHeight](DataControlBase/RowMinHeight.md) { get; set; } | 获取或设置行的最小高度。 |
| [SearchPanelDisplayMode](DataControlBase/SearchPanelDisplayMode.md) { get; set; } | 获取或设置何时显示搜索面板。 |
| [SearchPanelHighlightResults](DataControlBase/SearchPanelHighlightResults.md) { get; set; } | 获取或设置是否突出显示搜索结果。 |
| [SearchText](DataControlBase/SearchText.md) { get; set; } | 获取或设置在搜索面板中输入的搜索文本。 |
| [SelectedItems](DataControlBase/SelectedItems.md) { get; set; } | 获取或设置所选数据项的集合。 |
| [SelectionMode](DataControlBase/SelectionMode.md) { get; set; } | 获取或设置用户可以选择单行还是多行。 |
| [ShowItemsSourceErrors](DataControlBase/ShowItemsSourceErrors.md) { get; set; } | 获取或设置是否显示源项的验证错误。 |
| [ShowSearchPanelCloseButton](DataControlBase/ShowSearchPanelCloseButton.md) { get; set; } | 获取或设置搜索面板是否显示关闭按钮。 |
| [TextSortMode](DataControlBase/TextSortMode.md) { get; set; } | 获取或设置排序时如何比较文本值。 |
| [ValidateCellValuesOnShowAndUpdate](DataControlBase/ValidateCellValuesOnShowAndUpdate.md) { get; set; } | 获取或设置在显示和更新时是否验证单元格值。 |

## 方法

| 名称 | 说明 |
| --- | --- |
| virtual [BeginDataUpdate](DataControlBase/BeginDataUpdate.md)() | 阻止控件更新其数据，直到调用 EndDataUpdate 或 CancelDataUpdate。 |
| [BeginSelection](DataControlBase/BeginSelection.md)() | 阻止选择更新，直到调用 EndSelection。 |
| [CancelDataUpdate](DataControlBase/CancelDataUpdate.md)() | 在 BeginDataUpdate 之后恢复数据更新，但不刷新控件的数据。 |
| [ClearAllColumnsFilter](DataControlBase/ClearAllColumnsFilter.md)() | 清除所有列应用的筛选条件。 |
| [ClearSelection](DataControlBase/ClearSelection.md)() | 清除当前选择。 |
| [ClearSorting](DataControlBase/ClearSorting.md)() | 移除应用于所有列的排序。 |
| [CloseEditor](DataControlBase/CloseEditor.md)() | 关闭活动的就地编辑器。 |
| virtual [CommitEditing](DataControlBase/CommitEditing.md)() | 通过关闭活动的就地编辑器来完成当前编辑会话。 |
| [CopyToClipboardAsync](DataControlBase/CopyToClipboardAsync.md)() | 将列标题和所选行复制到剪贴板。 |
| virtual [EndDataUpdate](DataControlBase/EndDataUpdate.md)() | 在 BeginDataUpdate 之后恢复数据更新并刷新控件的数据。 |
| [EndSelection](DataControlBase/EndSelection.md)() | 应用自 BeginSelection 以来所做的选择更改。 |
| [ExportToCsv](DataControlBase/ExportToCsv.md)(…) | 将控件的可见数据以 CSV 格式导出到指定文件。（2 个重载） |
| [HideColumnChooser](DataControlBase/HideColumnChooser.md)() | 隐藏列选择器。 |
| [HideEditor](DataControlBase/HideEditor.md)() | 隐藏活动的就地编辑器。 |
| [MoveNextPage](DataControlBase/MoveNextPage.md)() | 将焦点移到下一页的第一行。 |
| [MovePrevPage](DataControlBase/MovePrevPage.md)() | 将焦点移到上一页的最后一行。 |
| [PostEditor](DataControlBase/PostEditor.md)() | 将编辑后的值提交到数据源。 |
| [ResizeBand](DataControlBase/ResizeBand.md)(…) | 为指定列组中显示的所有列设置相同的宽度。 |
| [ResizeColumn](DataControlBase/ResizeColumn.md)(…) | 设置指定列的宽度。 |
| [SelectAll](DataControlBase/SelectAll.md)() | 选择所有行。 |
| [ShowColumnChooser](DataControlBase/ShowColumnChooser.md)() | 显示列选择器。 |
| [ShowEditor](DataControlBase/ShowEditor.md)() | 为焦点单元格激活就地编辑器并选择其内容。 |
| static [GetIsFocusWithin](DataControlBase/GetIsFocusWithin.md)(…) | 获取键盘焦点是否位于指定元素内。 |

## 事件

| 名称 | 说明 |
| --- | --- |
| event [EndSorting](DataControlBase/EndSorting.md) | 在数据排序完成后发生。 |
| event [FilterChanged](DataControlBase/FilterChanged.md) | 在数据筛选器更改时发生。 |
| event [InvalidCellValueException](DataControlBase/InvalidCellValueException.md) | 在提交无效单元格值的过程中引发异常时发生。 |
| event [StartSorting](DataControlBase/StartSorting.md) | 在数据排序开始之前发生。 |

## 字段

| 名称 | 说明 |
| --- | --- |
| const [AutoFilterRowIndex](DataControlBase/AutoFilterRowIndex.md) | 表示标识自动筛选行的可见索引。 |

## 另请参阅

* 命名空间 [Eremex.AvaloniaUI.Controls.DataControl](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
