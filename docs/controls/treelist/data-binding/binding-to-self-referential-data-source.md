---
title: Binding to Self-Referential Data Source
order: 90000
seealso: []
---

# Binding to Self-Referential Data Source

You can use a self-referential data source to encode hierarchy relationships between records. A self-referential data source is a flat list or collection of records. Its records have two service properties that specify parent-child relationships:

- _Key field_ — A unique record identifier (of a simple data type; for example, Integer).
- _Parent key field_ — A parent record's _Key field_.

The following image demonstrates an example of a self-referential data table, and a TreeList control that displays this data once the control's dedicated settings are set up.

![TreeList - Key and Parent Key fields](../../../images/treelist-key-parent-relations.png)

All records that are going to be displayed as root nodes (at the root level) should have the _Parent key field_ set to the same root value. The root value must be unique — it must not match any key field in the data source.

To bind a TreeList/TreeView control to a self-referential data source, do the following:

- Ensure that data source records have two public properties that specify the Key field and _Parent key field_.
- Set the control's `TreeListControlBase.KeyFieldName` property to the Key field name.
- Set the control's `TreeListControlBase.ParentFieldName` property to the _Parent key field_ name.
- Set the control's `TreeListControlBase.RootValue` property to the root value defined for root records in the data source.

## Visibility of Service Columns

TreeList does not create columns bound to service key fields by default. To allow the control to automatically create columns bound to the specified _Key field_ and _Parent key field_, set the `AutoGenerateColumns` and `AutoGenerateServiceColumns` properties to `true`.

## Example

The following example binds a TreeList control to a self-referential data source (a collection of _Employee_ records). The Employee class defines two properties (_ID_ and _ParentID_) that specify a record's _Key field_ and _Parent key field_, respectively. Root records have the _Parent key field_ set to **-1**, so the control's `RootValue` property is set to this value.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
...
<mxtl:TreeListControl Grid.Column="0" Name="treeList2">                
    <mxtl:TreeListControl.Columns>
        <mxtl:TreeListColumn Name="colName1" FieldName="Name" />
        <mxtl:TreeListColumn Name="colBirthdate1" FieldName="Birthdate" >
            <mxtl:TreeListColumn.EditorProperties>
                <mxe:TextEditorProperties DisplayFormatString="yyyy-MM-dd"/>
            </mxtl:TreeListColumn.EditorProperties>
                        
        </mxtl:TreeListColumn>
    </mxtl:TreeListControl.Columns>
</mxtl:TreeListControl>
```
``` cs
using CommunityToolkit.Mvvm.ComponentModel;

ObservableCollection<Employee> employees = new ObservableCollection<Employee>();
employees.Add(new Employee() { 
    ID = 0, ParentID = -1, Name = "Serge Smolin", Birthdate = new DateTime(1990, 01, 5)});
employees.Add(new Employee() { 
    ID = 1, ParentID = 0, Name = "Alex Douglas", Birthdate = new DateTime(1975, 8, 27)});
employees.Add(new Employee() { 
    ID = 2, ParentID = 0, Name = "Dennis Parker", Birthdate = new DateTime(1985, 12, 17)});
employees.Add(new Employee() { 
    ID = 3, ParentID = 1, Name = "Pavel Morris", Birthdate = new DateTime(1987, 10, 15)});
employees.Add(new Employee() { 
    ID = 4, ParentID = 2, Name = "Mary Thompson", Birthdate = new DateTime(1991, 03, 16)});
employees.Add(new Employee() { 
    ID = 5, ParentID = 3, Name = "Vera Liskina", Birthdate = new DateTime(1991, 04, 16)});

treeList2.KeyFieldName = "ID";
treeList2.ParentFieldName = "ParentID";
treeList2.RootValue = -1;

treeList2.ItemsSource = employees;

public partial class Employee : ObservableObject
{
    [ObservableProperty]
    public string name = "";

    [ObservableProperty]
    public DateTime? birthdate = null;

    public int ID { get; set; }

    public int ParentID { get; set; }

}
```

# See Also
- [Data Binding](./index.md)
- [Binding to Hierarchical Data](binding-to-hierarchical-data.md)
- [Columns](../columns.md)
- [How to Create a TreeView Control and Bind It to a Self Referential Data Source](../examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)