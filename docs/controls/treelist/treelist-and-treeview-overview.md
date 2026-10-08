---
title: TreeList and TreeView Controls Overview
order: 20000
seealso: []
---

# TreeList and TreeView Controls Overview

TreeList ([`TreeListControl`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl.md) class) and TreeView ([`TreeViewControl`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl.md) class) controls allow you to display hierarchical data in the form of a tree, where nodes (records) can have other nodes as children.

Both the [`TreeListControl`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl.md) and [`TreeViewControl`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl.md) controls are [`TreeListControlBase`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase.md) descendants, and as such, they have many features in common.
The difference between the controls is that TreeList supports multiple columns of data — each node (row) displays one or more cells. TreeView can only display a single column of data.

## Data Binding

The TreeList and TreeView controls support two types of data sources: self-referential (flat) and hierarchical. They differ in the way how records store the hierarchy information.

Besides bound mode, the controls can function in unbound mode, in which you manually add nodes and thus create the hierarchy.

The TreeList control supports unbound columns, which you can use to display arbitrary data.

See the following topics for more information:

- [Data Binding](data-binding/index.md)
- [Unbound Mode](data-binding/unbound-mode.md)
- [Unbound Columns](data-binding/unbound-columns.md)
- [How to Create a TreeList Control and Bind It to a Hierarchical Data Source](examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)
- [How to Create a TreeView Control and Bind It to a Self Referential Data Source](examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)

## Nodes

TreeList and TreeView controls create nodes once you bind them to a data source. Each node in the TreeView control displays a single value. A TreeList control's node displays values for all columns.

The controls also support unbound mode, in which you can create a node hierarchy manually.

See the following topics for more information: 

- [Nodes](nodes.md)
- [Node Drag-and-Drop](node-drag-and-drop.md)


## Columns (TreeList)

The TreeList control displays data in a tabular form, in which data is arranged in rows (nodes) and columns. Unlike the TreeView control, TreeList supports multiple columns.

See the following topic about column customization options and operations on columns: [Columns](columns.md).

## Column Bands (TreeList)

Column bands provide a way to visually group multiple columns under a common header. Band headers appear in the TreeList as an additional section above columns. You can also create hierarchical bands with an unlimited number of nesting levels.

Learn more: [Bands](bands.md).

## Styles

The Styles mechanism allows you to customize the appearance settings of the controls' visual elements in various states. 

See the following topic for details on the styling mechanism: [Styles](styles.md).

## Data Editing

The TreeView and TreeList controls use in-place Eremex editors to display and edit cell values by default. You can explicitly assign editors to the controls' columns to customize how cell values are rendered and being edited.

See the following topics for more information:

- [Data Editing](data-editing/index.md)
- [Custom Editors in TreeView and TreeList Columns](data-editing/custom-editors.md)

## Data Search and Filtering

The data search and filtering features allow you and your user to locate nodes that contain specific values.

You can find more information in the following topic: [Search and Filtering](filter-and-search.md).

## Sorting

Data sorting allows the TreeList and TreeView controls to arrange sibling nodes in ascending or descending order. TreeList supports data sorting by multiple columns. In addition, users can sort data in the TreeList using the mouse actions and a column header's context menu.

See the following topic for more information: [Data Sorting](sorting.md).

## Context Menus

Popup menus are displayed when a user right-clicks controls. See the following topic to learn how to customize the default popup menus and display custom menus for specific UI elements: [Context Menus](context-menus.md).


## See Also

- [How to Create a TreeList Control and Bind It to a Hierarchical Data Source](examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)
- [How to Create a TreeView Control and Bind It to a Self Referential Data Source](examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)