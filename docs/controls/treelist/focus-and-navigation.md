---
title: Focus and Navigation
order: 3900
seealso: []
---

# Focus and Navigation


## Cell and Row Navigation Modes

The TreeList control's default behavior allows users to navigate between cells using the keyboard, or focus them using the mouse.
Use the `TreeListControl.NavigationMode` property to switch between Cell Navigation and Row Navigation modes.

**Cell Navigation** (default)

Users can focus any cell using the keyboard or mouse.

![treelist-navigationmode-cell](../../images/treelist-navigationmode-cell.png)

**Row (Node) Navigation**

Users cannot focus individual cells, and cell edit operations are disabled. Clicking a cell highlights the entire node.

``` xml
<mxtl:TreeListControl x:Name="treeList" NavigationMode="Row">
```

![treelist-navigationmode-row](../../images/treelist-navigationmode-row.png)



## Focused Column

Use the `TreeListControl.FocusedColumn` property to obtain the focused column. To move focus to a specific column, assign a corresponding `TreeListColumn` object to the `FocusedColumn` property.

!!! note

    You can only focus a column in [Cell Navigation mode](#cell-and-row-navigation-modes).

## Focused Node (Row)

Use the `TreeListControlBase.FocusedNode` property to access the currently focused node (the node that receives keyboard events). To get the focused node's data (business) object, use the `DataControlBase.FocusedItem` inherited property.

The `TreeListControlBase.FocusedNodeChanged` event allows you to respond to moving focus between nodes.


## Focused Cell

The focused cell is determined by the intersection of the focused node and focused column. To move focus to a specific cell, focus the target [row](#focused-node-row) and [column](#focused-column).

<!-- TODO
Example - focus a specific cell
 -->