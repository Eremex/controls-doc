---
title: TreeList 和 TreeView 控制概述
order: 20000
seealso: []
---

# TreeList 和 TreeView 控制概述

TreeList（`TreeListControl` 类）和 TreeView（`TreeViewControl` 类） controls 允许您以树的形式显示分层数据，其中节点（记录）可以将其他节点作为子节点。

`TreeListControl` 和 `TreeViewControl` controls 都是 `TreeListControlBase` 的后代，因此，它们具有许多共同点。
与controls的区别在于TreeList支持多列数据——每个节点（行）显示一个或多个单元格。 TreeView只能显示单个column的数据。

## 数据绑定

TreeList 和 TreeView controls 支持两种类型的数据源：自引用（平面）和分层。它们的不同之处在于记录存储层次结构信息的方式。

除了绑定模式外，controls 还可以在非绑定模式下工作，在该模式下，您可以手动添加节点，从而创建层次结构。

TreeList control 支持未绑定列，您可以使用它来显示任意数据。

请参阅以下主题以获取更多信息：

- [Data Binding](data-binding/index.md)
- [Unbound Mode](data-binding/unbound-mode.md)
- [Unbound Columns](data-binding/unbound-columns.md)
- [How to Create a TreeList Control and Bind It to a Hierarchical Data Source](examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)
- [How to Create a TreeView Control and Bind It to a Self Referential Data Source](examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)

## 节点

将 TreeList 和 TreeView controls 绑定到数据源后，它们将创建节点。 TreeView control 中的每个节点显示一个值。 TreeList control 的节点显示所有列的值。

controls还支持非绑定模式，您可以在该模式下手动创建节点层次结构。

请参阅以下主题以获取更多信息：

- [Nodes](nodes.md)
- [Node Drag-and-Drop](node-drag-and-drop.md)


## 列 (TreeList)

TreeList control 以表格形式显示数据，其中数据按行（节点）和列排列。与 TreeView control 不同，TreeList 支持多列。

请参阅以下有关 column 自定义选项和色谱柱操作的主题：[Columns](columns.md)。

## 列组 (TreeList)

列组提供了一种在公共标题下直观地对多个列进行分组的方法。频段标题显示在 TreeList 中，作为列上方的附加部分。您还可以创建具有无限数量嵌套级别的分层带。

了解更多：[Bands](bands.md)。

## 风格

样式机制允许您自定义controls视觉元素在各种状态下的外观设置。

有关样式机制的详细信息，请参阅以下主题：[Styles](styles.md)。

## 数据编辑

TreeView 和 TreeList controls 默认使用 in-place Eremex 编辑器来显示和编辑单元格值。您可以将编辑器显式分配给 controls' 列，以自定义单元格值的呈现和编辑方式。

请参阅以下主题以获取更多信息：

- [Data Editing](data-editing/index.md)
- [Custom Editors in TreeView and TreeList Columns](data-editing/custom-editors.md)

## 数据搜索和过滤

数据搜索和过滤功能允许您和您的用户找到包含特定值的 locate 节点。

您可以在以下主题中找到更多信息：[Search and Filtering](filter-and-search.md)。

## 排序

数据排序允许 TreeList 和 TreeView controls 至 arrange sibling 节点按升序或降序排列。 TreeList支持多列数据排序。此外，用户还可以使用鼠标操作和 column 标题的上下文菜单对 TreeList 中的数据进行排序。

有关详细信息，请参阅以下主题：[Data Sorting](sorting.md)。

## 上下文菜单

当用户右键单击控件时，将显示弹出菜单。请参阅以下主题，了解如何自定义默认弹出菜单并显示特定 UI 元素的自定义菜单：[Context Menus](context-menus.md)。


## 另请参阅

- [How to Create a TreeList Control and Bind It to a Hierarchical Data Source](examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)
- [How to Create a TreeView Control and Bind It to a Self Referential Data Source](examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
