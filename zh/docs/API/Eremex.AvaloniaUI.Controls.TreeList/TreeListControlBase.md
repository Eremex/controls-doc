# TreeListControlBase 类

为显示按节点层次结构排列的项集合的数据控件提供基类。

**命名空间：** [`Eremex.AvaloniaUI.Controls.TreeList`](./index.md)  
**程序集：** `Eremex.Avalonia.Controls.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## 声明

```csharp
public abstract class TreeListControlBase : DataControlBase
```

## 属性

| 名称 | 说明 |
| --- | --- |
| [AllowDragDrop](TreeListControlBase/AllowDragDrop.md) { get; set; } | 获取或设置是否启用节点拖放。 |
| [AllowDragDropSortedNodes](TreeListControlBase/AllowDragDropSortedNodes.md) { get; set; } | 获取或设置数据排序时是否可以拖动节点。 |
| [AllowDropInsideNode](TreeListControlBase/AllowDropInsideNode.md) { get; set; } | 获取或设置节点是否可以在其内部接受拖动的节点。 |
| [AllowDynamicDataLoading](TreeListControlBase/AllowDynamicDataLoading.md) { get; set; } | 获取或设置展开父节点时是否按需加载子节点。 |
| [AllowIndeterminateCheckState](TreeListControlBase/AllowIndeterminateCheckState.md) { get; set; } | 获取或设置父节点复选框是否可以处于不确定状态。 |
| [AllowRecursiveNodeChecking](TreeListControlBase/AllowRecursiveNodeChecking.md) { get; set; } | 获取或设置勾选节点时是否勾选其所有后代节点。 |
| [AllowScrollingOnDrag](TreeListControlBase/AllowScrollingOnDrag.md) { get; set; } | 获取或设置当拖动的元素接近视图边缘时视图是否自动滚动。 |
| [AutoExpandAllNodes](TreeListControlBase/AutoExpandAllNodes.md) { get; set; } | 获取或设置是否自动展开所有节点。 |
| [AutoExpandDelayOnDrag](TreeListControlBase/AutoExpandDelayOnDrag.md) { get; set; } | 获取或设置拖动经过时节点自动展开之前的延迟。 |
| [AutoExpandOnDrag](TreeListControlBase/AutoExpandOnDrag.md) { get; set; } | 获取或设置当拖动的元素悬停在折叠的节点上方时，该节点是否自动展开。 |
| [AutoScrollOnSorting](TreeListControlBase/AutoScrollOnSorting.md) { get; set; } | 获取或设置排序后视图是否滚动到焦点节点。 |
| [CheckBoxFieldName](TreeListControlBase/CheckBoxFieldName.md) { get; set; } | 获取或设置存储节点勾选状态的字段。 |
| [ChildrenFieldName](TreeListControlBase/ChildrenFieldName.md) { get; set; } | 获取或设置包含节点子项的字段。 |
| [ChildrenSelector](TreeListControlBase/ChildrenSelector.md) { get; set; } | 获取或设置为节点提供子项的对象。 |
| [Commands](TreeListControlBase/Commands.md) { get; } | 获取树的命令。 |
| [ExpandNodesOnFiltering](TreeListControlBase/ExpandNodesOnFiltering.md) { get; set; } | 获取或设置应用筛选器时是否自动展开节点。 |
| [ExpandStateFieldName](TreeListControlBase/ExpandStateFieldName.md) { get; set; } | 获取或设置存储节点展开状态的字段。 |
| [FilterMode](TreeListControlBase/FilterMode.md) { get; set; } | 获取或设置应用筛选器时显示哪些节点。 |
| [FocusedNode](TreeListControlBase/FocusedNode.md) { get; set; } | 获取或设置焦点节点。 |
| [HasChildrenFieldName](TreeListControlBase/HasChildrenFieldName.md) { get; set; } | 获取或设置指示节点是否具有子节点的字段。 |
| [KeyFieldName](TreeListControlBase/KeyFieldName.md) { get; set; } | 获取或设置在自引用数据中唯一标识节点的字段。 |
| [NodeImageFieldName](TreeListControlBase/NodeImageFieldName.md) { get; set; } | 获取或设置包含节点图像的字段。 |
| [NodeImageSelector](TreeListControlBase/NodeImageSelector.md) { get; set; } | 获取或设置为节点提供图像的对象。 |
| [Nodes](TreeListControlBase/Nodes.md) { get; } | 获取节点的根集合。 |
| [ParentFieldName](TreeListControlBase/ParentFieldName.md) { get; set; } | 获取或设置在自引用数据中引用父节点键的字段。 |
| [RestoreStateKeyFieldName](TreeListControlBase/RestoreStateKeyFieldName.md) { get; set; } | 获取或设置在还原已保存的控件状态时其值用于标识节点的字段。 |
| [RootValue](TreeListControlBase/RootValue.md) { get; set; } | 获取或设置在自引用数据中标识根节点的父键值。 |
| [RowCellMenu](TreeListControlBase/RowCellMenu.md) { get; set; } | 获取或设置为数据单元格调用的上下文菜单。 |
| [ShowExpandButtons](TreeListControlBase/ShowExpandButtons.md) { get; set; } | 获取或设置是否显示展开按钮。 |
| [ShowNodeCheckBoxes](TreeListControlBase/ShowNodeCheckBoxes.md) { get; set; } | 获取或设置是否显示节点复选框。 |
| [ShowNodeImages](TreeListControlBase/ShowNodeImages.md) { get; set; } | 获取或设置是否显示节点图像。 |
| [ShowRootIndent](TreeListControlBase/ShowRootIndent.md) { get; set; } | 获取或设置是否显示根级缩进。 |
| [UsePlatformRowDragDrop](TreeListControlBase/UsePlatformRowDragDrop.md) { get; set; } | 获取或设置拖动节点时是否使用平台拖放。 |
| [VisibleNodeCount](TreeListControlBase/VisibleNodeCount.md) { get; } | 获取当前可见节点的数量。 |

## 方法

| 名称 | 说明 |
| --- | --- |
| [CheckAllNodes](TreeListControlBase/CheckAllNodes.md)() | 勾选所有可见节点。 |
| [CollapseAllNodes](TreeListControlBase/CollapseAllNodes.md)() | 折叠所有节点。 |
| override [CommitEditing](TreeListControlBase/CommitEditing.md)() |  |
| [ExpandAllNodes](TreeListControlBase/ExpandAllNodes.md)() | 展开所有节点。 |
| [FindNode](TreeListControlBase/FindNode.md)(…) | 返回满足指定条件的第一个节点。 |
| [GetAllCheckedNodes](TreeListControlBase/GetAllCheckedNodes.md)() | 返回所有已勾选节点的列表。 |
| [GetNodeByVisibleIndex](TreeListControlBase/GetNodeByVisibleIndex.md)(…) | 返回显示在指定可见索引处的节点。 |
| [GetSelectedNodes](TreeListControlBase/GetSelectedNodes.md)() | 返回所选节点的列表。 |
| [GetVisibleIndexByNode](TreeListControlBase/GetVisibleIndexByNode.md)(…) | 返回指定节点的可见索引。 |
| [IsNodeSelected](TreeListControlBase/IsNodeSelected.md)(…) | 获取指定节点是否被选中。 |
| [MoveFirstNode](TreeListControlBase/MoveFirstNode.md)() | 将焦点移到第一个节点。 |
| [MoveLastNode](TreeListControlBase/MoveLastNode.md)() | 将焦点移到最后一个节点。 |
| [MoveNextNode](TreeListControlBase/MoveNextNode.md)() | 将焦点移到下一个节点。 |
| [MovePrevNode](TreeListControlBase/MovePrevNode.md)(…) | 将焦点移到上一个节点。 |
| [RefreshData](TreeListControlBase/RefreshData.md)() | 刷新控件的数据。 |
| [RefreshNode](TreeListControlBase/RefreshNode.md)(…) | 刷新指定节点的显示数据。 |
| [RefreshNodeChildren](TreeListControlBase/RefreshNodeChildren.md)(…) | 刷新指定节点的子节点。 |
| [ScrollIntoView](TreeListControlBase/ScrollIntoView.md)(…) | 滚动视图以使指定节点可见。 |
| [SelectNode](TreeListControlBase/SelectNode.md)(…) | 选择指定节点。 |
| [SelectRange](TreeListControlBase/SelectRange.md)(…) | 选择指定起始节点和结束节点之间的所有节点。 |
| [UncheckAllNodes](TreeListControlBase/UncheckAllNodes.md)() | 取消勾选所有可见节点。 |
| [UnselectNode](TreeListControlBase/UnselectNode.md)(…) | 取消选择指定节点。 |

## 事件

| 名称 | 说明 |
| --- | --- |
| event [CompleteDragDrop](TreeListControlBase/CompleteDragDrop.md) | 在拖放操作完成后发生。 |
| event [CustomNodeFilter](TreeListControlBase/CustomNodeFilter.md) | 在对节点应用自定义筛选时发生。 |
| event [DragOver](TreeListControlBase/DragOver.md) | 在拖动的元素位于控件上方时发生。 |
| event [Drop](TreeListControlBase/Drop.md) | 在将拖动的元素放置到控件上时发生。 |
| event [FocusedColumnChanged](TreeListControlBase/FocusedColumnChanged.md) | 在焦点列更改时发生。 |
| event [FocusedNodeChanged](TreeListControlBase/FocusedNodeChanged.md) | 在焦点节点更改时发生。 |
| event [NodeChanged](TreeListControlBase/NodeChanged.md) | 在节点的数据或状态更改时发生。 |
| event [NodeCheckStateChanged](TreeListControlBase/NodeCheckStateChanged.md) | 在节点的勾选状态更改时发生。 |
| event [NodeClick](TreeListControlBase/NodeClick.md) | 在单击节点时发生。 |
| event [NodeCollapsed](TreeListControlBase/NodeCollapsed.md) | 在节点折叠后发生。 |
| event [NodeCollapsing](TreeListControlBase/NodeCollapsing.md) | 在节点折叠之前发生。 |
| event [NodeExpanded](TreeListControlBase/NodeExpanded.md) | 在节点展开后发生。 |
| event [NodeExpanding](TreeListControlBase/NodeExpanding.md) | 在节点展开之前发生。 |
| event [SelectionChanged](TreeListControlBase/SelectionChanged.md) | 在节点选择更改时发生。 |
| event [StartDrag](TreeListControlBase/StartDrag.md) | 在开始拖动节点时发生。 |

## 另请参阅

* 类 [DataControlBase](../Eremex.AvaloniaUI.Controls.DataControl/DataControlBase.md)
* 命名空间 [Eremex.AvaloniaUI.Controls.TreeList](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
