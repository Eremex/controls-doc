---
title: Performance and Data Virtualization
order: 600
seealso: []
---

# Performance and Data Virtualization

Tree List and Data Grid controls support data virtualization to improve performance (load times) for large datasets. 
When data virtualization is enabled (default), the control generates visual elements (cells, column headers, etc.) only for the visible viewport. Otherwise, the control creates and stores visual elements in memory for all items, including those hidden outside the viewport.

## Vertical and Horizontal Virtualization

Vertical virtualization (when scrolling through rows) is always active.

Horizontal virtualization (when scrolling through columns) is enabled by default. 

##### Related API

- [`TreeListControl.AllowHorizontalVirtualization`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AllowHorizontalVirtualization.md) property — Gets or sets whether horizontal virtualization is enabled.


You may need to disable horizontal virtualization when rows/nodes have different heights (when a row height is calculated based on cell contents). See [Node Auto-Height](nodes.md#node-auto-height).

When horizontal virtualization is enabled, automatic row heights are calculated according to the contents of the currently visible cells. Cells outside the viewport do not affect row height calculation. When you scroll to the cells with different content heights, the row height is adjusted dynamically. To prevent dynamic row height changes during horizontal scrolling, disable horizontal virtualization.

``` xml
<mxtl:TreeListControl x:Name="treeList" AllowHorizontalVirtualization="False">
```