---
title: Data Binding
order: 10000
seealso: []
---

# Data Binding

Once a TreeList/TreeView control is bound to a data source, it creates nodes ([`TreeListNode`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode.md) objects) for data source records. Nodes are initially empty. You need to specify data record properties (data source fields) whose values are displayed in nodes.

To display values in TreeList nodes, create bound or unbound columns in the [`TreeListControl.Columns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/Columns.md) collection. Enable the [`TreeListControl.AutoGenerateColumns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AutoGenerateColumns.md) option to automatically generate missing columns for all data source properties/fields once you bind the control. See the [Columns](../columns.md) and [Unbound Columns](unbound-columns.md) topics for more information.

The TreeView control is a single-column version of the TreeList. Use the [`TreeViewControl.DataFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/DataFieldName.md) property to specify which values to display in its nodes in bound mode. This member determines the name of the property/field in the data source whose data is displayed by the control.

The [`ItemsSource`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ItemsSource.md) property allows you to bind the TreeList/TreeView control to a data source that contains information on parent-child relationships between records. The controls support two data source types, which differ in the way they encode the hierarchy information:

- Self-referential (flat) data source.
- Hierarchical data source

## Self-Referential (Flat) Data Source

A self-referential data source is a flat table, collection, or list, in which records have two service properties/fields used to create parent-child relationships between records:

- A Key field — A record's unique identifier.
- A Parent Key field — Stores the Key field value of the record's parent.

Typically, both the Key field and Parent Key field are of the Integer data type. Parent and child data objects are always of the same data type.

See the following topics for more information:

- [Binding to Self-Referential Data Source](binding-to-self-referential-data-source.md)
- [How to Create a TreeView Control and Bind It to a Self Referential Data Source](../examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)

### Common API
- [`ItemsSource`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ItemsSource.md) — The control's data source.
- [`KeyFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/KeyFieldName.md) —  The name of the field that stores unique record identifiers (Key field values).
- [`ParentFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ParentFieldName.md) — The name of the field that stores the identifier (Key field value) of a record's parent.
- [`RootValue`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/RootValue.md) — A root node's parent Key Field value. 

### TreeList's API

- [`Columns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/Columns.md) — A collection of bound and unbound TreeList columns.
- [`AutoGenerateColumns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AutoGenerateColumns.md) — Specifies whether TreeList automatically generates missing columns for public properties/fields exposed by the data source at runtime. If the control's [`Columns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/Columns.md) collection already contains a column bound to a specific property/field, no extra column bound to the same property/field is auto-generated.
- [`AutoGenerateServiceColumns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AutoGenerateServiceColumns.md) — Specifies whether the TreeList automatically generates columns bound to the Key field and Parent key field. This property is in effect if the [`AutoGenerateColumns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AutoGenerateColumns.md) option is enabled.

### TreeView's API

- [`DataFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/DataFieldName.md) — The name of the field whose data is displayed in the control.

## Hierarchical Data Source

In a hierarchical data source, a business object (record) has a property that stores a collection of child data objects. Parent and child data objects can be of different types, but they should share a set of properties that the TreeView/TreeList controls display as columns.

### Dynamic Data Load

When bound to a hierarchical data source, TreeList and TreeView controls load nodes on demand: child nodes are dynamically loaded when a parent node is expanded. This applies restrictions to the node checking and filter/search/summary functionalities.

Set the [`AllowDynamicDataLoading`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/AllowDynamicDataLoading.md) property to `false` to load all nodes at the same time once you bind the control to the data source.

See the following topics for more information:

- [Binding to Hierarchical Data](binding-to-hierarchical-data.md)
- [How to Create a TreeList Control and Bind It to a Hierarchical Data Source](../examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)

### Common API

- [`ItemsSource`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ItemsSource.md) — Set this property to the object that contains data (for example, a collection of root objects) used to create root nodes.
- [`ChildrenSelector`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenSelector.md) —  A selector that returns child objects for each business object (record). Use either [`ChildrenSelector`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenSelector.md), or [`ChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenFieldName.md).
- [`ChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenFieldName.md) — The name of the property (field) that stores child objects for each business object. Use either [`ChildrenSelector`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenSelector.md), or [`ChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenFieldName.md).
- [`HasChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/HasChildrenFieldName.md) — The name of the Boolean property that returns `true` if an object has child objects. The [`HasChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/HasChildrenFieldName.md) property allows the control to dynamically determine the visibility of expand ('+') buttons. Use [`HasChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/HasChildrenFieldName.md) together with the [`ChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenFieldName.md) property. 

### TreeView's API

- [`DataFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/DataFieldName.md) — The name of the field whose data is displayed in the control.

# See Also
- [Binding to Hierarchical Data](binding-to-hierarchical-data.md)
- [Binding to Self-Referential Data Source](binding-to-self-referential-data-source.md)
- [Unbound Columns](unbound-columns.md)
- [Unbound Mode](unbound-mode.md)
- [How to Create a TreeView Control and Bind It to a Self Referential Data Source](../examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)
- [How to Create a TreeList Control and Bind It to a Hierarchical Data Source](../examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)