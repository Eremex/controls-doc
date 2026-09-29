---
title: 数据绑定
order: 10000
seealso: []
---

# 数据绑定

将 TreeList/TreeView 控件绑定到数据源后,它会为数据源中的记录创建节点(`TreeListNode` 对象)。节点最初是空的。您需要指定数据记录的属性(数据源字段),其值将显示在节点中。

要在 TreeList 节点中显示值,请在 `TreeListControl.Columns` 集合中创建绑定列或非绑定列。启用 `TreeListControl.AutoGenerateColumns` 选项,可以在绑定控件后自动为数据源的所有属性/字段生成缺失的列。有关更多信息,请参阅[列](../columns.md)和[非绑定列](unbound-columns.md)主题。

TreeView 控件是 TreeList 的单列版本。使用 `TreeViewControl.DataFieldName` 属性可以指定在绑定模式下其节点中显示哪些值。该成员确定数据源中属性/字段的名称,该属性/字段的数据将由控件显示。

`ItemsSource` 属性允许您将 TreeList/TreeView 控件绑定到包含记录之间父子关系信息的数据源。这些控件支持两种数据源类型,它们在编码层级信息的方式上有所不同:

- 自引用（扁平）数据源。
- 层级数据源

## 自引用（扁平）数据源

自引用数据源是一个扁平的表、集合或列表,其中记录具有两个用于建立记录间父子关系的服务属性/字段:

- 键(Key)字段 — 记录的唯一标识符。
- 父键(Parent Key)字段 — 存储记录父项的 Key 字段值。

通常,Key 字段和 Parent Key 字段都是整数数据类型。父数据对象和子数据对象始终属于相同的数据类型。

有关更多信息,请参阅以下主题:

- [绑定到自引用数据源](binding-to-self-referential-data-source.md)
- [如何创建 TreeView 控件并将其绑定到自引用数据源](../examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)

### 通用 API
- `ItemsSource` — 控件的数据源。
- `KeyFieldName` — 存储记录唯一标识符(Key 字段值)的字段名称。
- `ParentFieldName` — 存储记录父项标识符(Key 字段值)的字段名称。
- `RootValue` — 根节点的父 Key 字段值。

### TreeList 的 API

- `Columns` — TreeList 绑定列和非绑定列的集合。
- `AutoGenerateColumns` — 指定 TreeList 是否在运行时为数据源公开的公共属性/字段自动生成缺失的列。如果控件的 `Columns` 集合中已包含绑定到特定属性/字段的列,则不会为同一属性/字段自动生成额外的列。
- `AutoGenerateServiceColumns` — 指定 TreeList 是否自动生成绑定到 Key 字段和 Parent Key 字段的列。此属性仅在启用 `AutoGenerateColumns` 选项时生效。

### TreeView 的 API

- `DataFieldName` — 其数据显示在控件中的字段名称。

## 层级数据源

在层级数据源中,业务对象(记录)具有一个属性,用于存储子数据对象的集合。父数据对象和子数据对象可以是不同的类型,但它们必须共享一组属性,TreeView/TreeList 控件将这些属性显示为列。

绑定到层级数据源时,TreeList 和 TreeView 控件会按需加载节点:展开父节点时会动态加载子节点。这会对节点选中及筛选/搜索功能施加限制。

将 `AllowDynamicDataLoading` 属性设置为 `false`,可以在控件绑定到数据源后同时加载所有节点。

有关更多信息,请参阅以下主题:

- [绑定到层级数据](binding-to-hierarchical-data.md)
- [如何创建 TreeList 控件并将其绑定到层级数据源](../examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)

### 通用 API

- `ItemsSource` — 将此属性设置为包含数据(例如根对象的集合)的对象,用于创建根节点。
- `ChildrenSelector` — 一个选择器,为每个业务对象(记录)返回子对象。请使用 `ChildrenSelector` 或 `ChildrenFieldName` 二者之一。
- `ChildrenFieldName` — 存储每个业务对象的子对象的属性(字段)名称。请使用 `ChildrenSelector` 或 `ChildrenFieldName` 二者之一。
- `HasChildrenFieldName` — 布尔属性的名称,如果对象具有子对象则返回 `true`。`HasChildrenFieldName` 属性使控件能够动态确定展开按钮('+')的可见性。请将 `HasChildrenFieldName` 与 `ChildrenFieldName` 属性一起使用。

### TreeView 的 API

- `DataFieldName` — 其数据显示在控件中的字段名称。

# 另请参阅
- [绑定到层级数据](binding-to-hierarchical-data.md)
- [绑定到自引用数据源](binding-to-self-referential-data-source.md)
- [非绑定列](unbound-columns.md)
- [非绑定模式](unbound-mode.md)
- [如何创建 TreeView 控件并将其绑定到自引用数据源](../examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)
- [如何创建 TreeList 控件并将其绑定到层级数据源](../examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
