# TreeListControlBase class

Provides a base class for data controls that display a collection of items arranged in a hierarchy of nodes.

**Namespace:** [`Eremex.AvaloniaUI.Controls.TreeList`](./index.md)  
**Assembly:** `Eremex.Avalonia.Controls.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Declaration

```csharp
public abstract class TreeListControlBase : DataControlBase
```

## Public Members

| name | description |
| --- | --- |
| [AllowDragDrop](TreeListControlBase/AllowDragDrop.md) { get; set; } | Gets or sets whether node drag-and-drop is enabled. |
| [AllowDragDropSortedNodes](TreeListControlBase/AllowDragDropSortedNodes.md) { get; set; } | Gets or sets whether nodes can be dragged when the data is sorted. |
| [AllowDropInsideNode](TreeListControlBase/AllowDropInsideNode.md) { get; set; } | Gets or sets whether a node can accept dragged nodes inside it. |
| [AllowDynamicDataLoading](TreeListControlBase/AllowDynamicDataLoading.md) { get; set; } | Gets or sets whether child nodes are loaded on demand when their parent is expanded. |
| [AllowIndeterminateCheckState](TreeListControlBase/AllowIndeterminateCheckState.md) { get; set; } | Gets or sets whether parent check boxes can be in the indeterminate state. |
| [AllowRecursiveNodeChecking](TreeListControlBase/AllowRecursiveNodeChecking.md) { get; set; } | Gets or sets whether checking a node checks all its descendants. |
| [AllowScrollingOnDrag](TreeListControlBase/AllowScrollingOnDrag.md) { get; set; } | Gets or sets whether the view scrolls automatically when a dragged element approaches its edge. |
| [AutoExpandAllNodes](TreeListControlBase/AutoExpandAllNodes.md) { get; set; } | Gets or sets whether all nodes are expanded automatically. |
| [AutoExpandDelayOnDrag](TreeListControlBase/AutoExpandDelayOnDrag.md) { get; set; } | Gets or sets the delay before a node is expanded automatically on drag-over. |
| [AutoExpandOnDrag](TreeListControlBase/AutoExpandOnDrag.md) { get; set; } | Gets or sets whether a collapsed node is expanded automatically when a dragged element hovers over it. |
| [AutoScrollOnSorting](TreeListControlBase/AutoScrollOnSorting.md) { get; set; } | Gets or sets whether the view scrolls to the focused node after sorting. |
| [CheckBoxFieldName](TreeListControlBase/CheckBoxFieldName.md) { get; set; } | Gets or sets the field that stores node check states. |
| [ChildrenFieldName](TreeListControlBase/ChildrenFieldName.md) { get; set; } | Gets or sets the field that contains a node's child items. |
| [ChildrenSelector](TreeListControlBase/ChildrenSelector.md) { get; set; } | Gets or sets the object that supplies child items for nodes. |
| [Commands](TreeListControlBase/Commands.md) { get; } | Gets the tree's commands. |
| [ExpandNodesOnFiltering](TreeListControlBase/ExpandNodesOnFiltering.md) { get; set; } | Gets or sets whether nodes are expanded automatically when a filter is applied. |
| [ExpandStateFieldName](TreeListControlBase/ExpandStateFieldName.md) { get; set; } | Gets or sets the field that stores the expanded state of nodes. |
| [FilterMode](TreeListControlBase/FilterMode.md) { get; set; } | Gets or sets which nodes are displayed when a filter is applied. |
| [FocusedNode](TreeListControlBase/FocusedNode.md) { get; set; } | Gets or sets the focused node. |
| [HasChildrenFieldName](TreeListControlBase/HasChildrenFieldName.md) { get; set; } | Gets or sets the field that indicates whether a node has children. |
| [KeyFieldName](TreeListControlBase/KeyFieldName.md) { get; set; } | Gets or sets the field that uniquely identifies nodes in self-referential data. |
| [NodeImageFieldName](TreeListControlBase/NodeImageFieldName.md) { get; set; } | Gets or sets the field that contains node images. |
| [NodeImageSelector](TreeListControlBase/NodeImageSelector.md) { get; set; } | Gets or sets the object that provides images for nodes. |
| [Nodes](TreeListControlBase/Nodes.md) { get; } | Gets the root collection of nodes. |
| [ParentFieldName](TreeListControlBase/ParentFieldName.md) { get; set; } | Gets or sets the field that references the parent node key in self-referential data. |
| [RestoreStateKeyFieldName](TreeListControlBase/RestoreStateKeyFieldName.md) { get; set; } | Gets or sets the field whose values identify nodes when restoring the saved control state. |
| [RootValue](TreeListControlBase/RootValue.md) { get; set; } | Gets or sets the parent key value that identifies root nodes in self-referential data. |
| [RowCellMenu](TreeListControlBase/RowCellMenu.md) { get; set; } | Gets or sets the context menu invoked for data cells. |
| [ShowExpandButtons](TreeListControlBase/ShowExpandButtons.md) { get; set; } | Gets or sets whether expand buttons are displayed. |
| [ShowNodeCheckBoxes](TreeListControlBase/ShowNodeCheckBoxes.md) { get; set; } | Gets or sets whether node check boxes are displayed. |
| [ShowNodeImages](TreeListControlBase/ShowNodeImages.md) { get; set; } | Gets or sets whether node images are displayed. |
| [ShowRootIndent](TreeListControlBase/ShowRootIndent.md) { get; set; } | Gets or sets whether the root level indent is displayed. |
| [UsePlatformRowDragDrop](TreeListControlBase/UsePlatformRowDragDrop.md) { get; set; } | Gets or sets whether the platform drag-and-drop is used when dragging nodes. |
| [VisibleNodeCount](TreeListControlBase/VisibleNodeCount.md) { get; } | Gets the number of currently visible nodes. |
| event [CompleteDragDrop](TreeListControlBase/CompleteDragDrop.md) | Occurs after the drag-and-drop operation is completed. |
| event [CustomNodeFilter](TreeListControlBase/CustomNodeFilter.md) | Occurs when custom filtering is applied to nodes. |
| event [DragOver](TreeListControlBase/DragOver.md) | Occurs when a dragged element is over the control. |
| event [Drop](TreeListControlBase/Drop.md) | Occurs when a dragged element is dropped onto the control. |
| event [FocusedColumnChanged](TreeListControlBase/FocusedColumnChanged.md) | Occurs when the focused column is changed. |
| event [FocusedNodeChanged](TreeListControlBase/FocusedNodeChanged.md) | Occurs when the focused node is changed. |
| event [NodeChanged](TreeListControlBase/NodeChanged.md) | Occurs when a node's data or state is changed. |
| event [NodeCheckStateChanged](TreeListControlBase/NodeCheckStateChanged.md) | Occurs when a node's check state is changed. |
| event [NodeClick](TreeListControlBase/NodeClick.md) | Occurs when a node is clicked. |
| event [NodeCollapsed](TreeListControlBase/NodeCollapsed.md) | Occurs after a node is collapsed. |
| event [NodeCollapsing](TreeListControlBase/NodeCollapsing.md) | Occurs before a node is collapsed. |
| event [NodeExpanded](TreeListControlBase/NodeExpanded.md) | Occurs after a node is expanded. |
| event [NodeExpanding](TreeListControlBase/NodeExpanding.md) | Occurs before a node is expanded. |
| event [SelectionChanged](TreeListControlBase/SelectionChanged.md) | Occurs when the node selection is changed. |
| event [StartDrag](TreeListControlBase/StartDrag.md) | Occurs when node dragging is started. |
| [CheckAllNodes](TreeListControlBase/CheckAllNodes.md)() | Checks all visible nodes. |
| [CollapseAllNodes](TreeListControlBase/CollapseAllNodes.md)() | Collapses all nodes. |
| override [CommitEditing](TreeListControlBase/CommitEditing.md)() |  |
| [ExpandAllNodes](TreeListControlBase/ExpandAllNodes.md)() | Expands all nodes. |
| [FindNode](TreeListControlBase/FindNode.md)(…) | Returns the first node that satisfies the specified condition. |
| [GetAllCheckedNodes](TreeListControlBase/GetAllCheckedNodes.md)() | Returns the list of all checked nodes. |
| [GetNodeByVisibleIndex](TreeListControlBase/GetNodeByVisibleIndex.md)(…) | Returns the node displayed at the specified visible index. |
| [GetSelectedNodes](TreeListControlBase/GetSelectedNodes.md)() | Returns the list of selected nodes. |
| [GetVisibleIndexByNode](TreeListControlBase/GetVisibleIndexByNode.md)(…) | Returns the visible index of the specified node. |
| [IsNodeSelected](TreeListControlBase/IsNodeSelected.md)(…) | Gets whether the specified node is selected. |
| [MoveFirstNode](TreeListControlBase/MoveFirstNode.md)() | Moves focus to the first node. |
| [MoveLastNode](TreeListControlBase/MoveLastNode.md)() | Moves focus to the last node. |
| [MoveNextNode](TreeListControlBase/MoveNextNode.md)() | Moves focus to the next node. |
| [MovePrevNode](TreeListControlBase/MovePrevNode.md)(…) | Moves focus to the previous node. |
| [RefreshData](TreeListControlBase/RefreshData.md)() | Refreshes the control's data. |
| [RefreshNode](TreeListControlBase/RefreshNode.md)(…) | Refreshes the specified node's displayed data. |
| [RefreshNodeChildren](TreeListControlBase/RefreshNodeChildren.md)(…) | Refreshes the specified node's child nodes. |
| [ScrollIntoView](TreeListControlBase/ScrollIntoView.md)(…) | Scrolls the view to make the specified node visible. |
| [SelectNode](TreeListControlBase/SelectNode.md)(…) | Selects the specified node. |
| [SelectRange](TreeListControlBase/SelectRange.md)(…) | Selects all nodes between the specified start and end nodes. |
| [UncheckAllNodes](TreeListControlBase/UncheckAllNodes.md)() | Unchecks all visible nodes. |
| [UnselectNode](TreeListControlBase/UnselectNode.md)(…) | Removes the selection from the specified node. |

## See Also

* class [DataControlBase](../Eremex.AvaloniaUI.Controls.DataControl/DataControlBase.md)
* namespace [Eremex.AvaloniaUI.Controls.TreeList](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->
