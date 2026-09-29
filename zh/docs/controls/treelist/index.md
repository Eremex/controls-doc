---
title: TreeList 和 TreeView
order: 90000
seealso: []
---

# TreeList 和 TreeView

Eremex Controls 库包含两个用于以树形结构显示层次化数据的数据感知控件 — `TreeListControl` 和 `TreeViewControl`。它们将数据源中的项呈现为节点(行)。如果某个节点拥有子节点,您可以将其展开以显示下一层级的节点结构。

`TreeList` 支持多列显示:

![treelist](../../images/treelist.png)

`TreeView` 是单列控件:

![treeview](../../images/treeview.png)


这两个控件源自同一个基类,因此它们共享许多功能:

- [数据绑定](data-binding/index.md) — 您可以将控件绑定到 Self-Referential(平面)数据源和层次化数据源。
- [非绑定模式](data-binding/unbound-mode.md) — 允许您手动创建节点结构。
- [内置节点复选框](nodes.md#built-in-check-boxes) — 允许选择单个节点。
- [数据排序](sorting.md) — 允许按升序或降序对同级节点进行排序。TreeList 支持基于一个或多个列进行数据排序。
- [节点图标](nodes.md#node-images) — 允许在层次列的单元格值前显示自定义图标。
- [样式](styles.md) — 允许自定义控件元素在各种状态下的外观设置。
- [搜索面板](filter-and-search.md#search-panel-treelist-and-treeview) — 帮助用户根据节点所包含的数据快速定位节点。
- [数据编辑操作](data-editing/index.md) — 如果启用了数据编辑功能,用户可以编辑单元格值。您可以在单元格中嵌入 Eremex 编辑器和自定义编辑器,以特定方式编辑和呈现单元格值。
- [数据验证](data-validation.md) — 验证机制帮助您检查用户输入和数据源的值,并在单元格中显示错误。
- [内置和自定义上下文菜单](context-menus.md)
- [数据注解特性支持](columns.md#use-attributes-to-customize-settings-of-auto-generated-columns) — TreeList 和 TreeView 控件会考虑应用于数据源属性的专用数据注解特性。您可以使用数据注解特性为自动生成的列指定自定义可见性、位置、只读状态和显示名称。
- [节点拖放](node-drag-and-drop.md) — 用户可以在控件内以及拖动节点到另一个控件。
- [大数据量下的高性能](performance-and-data-virtualization.md) — 用于垂直和水平滚动的数据虚拟化机制可在显示大量行和列时提升控件的性能。


TreeList 特有的功能包括:

- [非绑定列](data-binding/unbound-columns.md) — 您可以添加非绑定列(未绑定到数据源字段的列),并通过事件手动为其填充数据。
- [列过滤菜单](filter-and-search.md#column-filters-treelist) — 您可以使用显示列唯一值的下拉菜单来过滤数据。单击任意列标题中的过滤按钮即可访问过滤选项。
- [自动筛选行](filter-and-search.md#auto-filter-row-treelist) — 一种特殊的行,允许用户按列过滤数据。
- [列标题模板](columns.md#column-headers) — 允许在列标题中显示自定义内容,包括图像。
- [多节点选择(高亮)](nodes.md#multiple-node-selection-highlight) — 您可以启用多节点选择模式,允许用户一次选择(高亮)多个节点。
- [列分组条](bands.md) — 允许在一个公共标题下对多个列进行可视化分组。
- [固定列](columns.md#fixed-columns) — 允许特定的列在其他列水平滚动时,始终保持可见并固定在 TreeList 控件的左边缘或右边缘。
- [最佳适应](columns.md#best-fit) — 此功能会将列的宽度调整为能够完整显示列内容(值和标题)而不被截断所需的最小宽度。
- [列的调整大小和移动操作](columns.md#move-columns)
- [导出为 XLSX、PDF、CSV 和图像格式](export.md)

有关更多信息,请参阅以下主题: [TreeList 和 TreeView 控件概述](treelist-and-treeview-overview.md)。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
