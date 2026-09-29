---
title: How to Create a TreeList Control and Bind It to a Hierarchical Data Source
order: 10000
seealso: []
---

# How to Create a TreeList Control and Bind It to a Hierarchical Data Source

This example creates the following controls:

- A `TreeListControl` control that displays a hierarchical list of _Employee_ objects. Multiple node selection is enabled, which allows you to select (highlight) multiple nodes at one time.
- A text editor that displays the name of the employee currently focused in the TreeList.
- A list box control that displays names of employees that are selected (highlighted) in the TreeList.

The TreeList is bound to an _Employee_ business object, which represents a [hierarchical data source](../data-binding/binding-to-hierarchical-data.md). It contains the _Subordinates_ collection, whose contents should be displayed as child nodes.

In the example the following main properties are used to set up the `TreeListControl`:

- `DataControlBase.ItemsSource` — Specifies the control's data source.
- `TreeListControl.Columns` — Specifies the collection of TreeList columns bound to the data source's properties.
- `TreeListControlBase.ChildrenFieldName` — Specifies the name of the field (property) that stores child data in the underlying business object.
- `TreeListControlBase.HasChildrenFieldName` — Specifies the name of the field (property) that returns `true` if a business object has child data, and `false`, otherwise.
- `TreeListControlBase.SelectionMode` — Enables multiple node selection.

In multiple node selection mode, a user can select (highlight) multiple nodes using the mouse and keyboard. For instance, a user can hold the CTRL key down and click individual nodes to select them. TreeList allows you to access currently selected nodes from the `DataControlBase.SelectedItems` collection. 

The following two controls are used to display information on the currently focused and selected TreeList nodes:

- The text editor displays the name of the focused node's _Employee_ object. The control is bound to the TreeList's `FocusedItem` property.
- The list box displays the names of _Employee_ objects that correspond to the TreeList's selected nodes.

The example locates two TreeList nodes by names, and selects them at application startup.

``` xml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:vm="using:TreeControls"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
        xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
        xmlns:sys="clr-namespace:System;assembly=mscorlib"
        x:Class="TreeControls.MainWindow"
        Title="TreeControls">
    <Grid ColumnDefinitions="*, 200">
        <mxtl:TreeListControl
            Grid.Column="0"
            Name="treeList1"
            ItemsSource="{Binding Employees}"
            ChildrenFieldName="Subordinates"
            HasChildrenFieldName="HasChildren"
            SelectionMode="Multiple"
            SelectedItems="{Binding SelectedEmployees}"
            >
            <mxtl:TreeListControl.Columns>
                <mxtl:TreeListColumn Name="colName" FieldName="Name" Header="Name" />
                <mxtl:TreeListColumn Name="colBirthdate" FieldName="Birthdate" Header="Birthdate"/>
            </mxtl:TreeListControl.Columns>
        </mxtl:TreeListControl>

        <StackPanel Orientation="Vertical" Grid.Column="1" >
            <Label Content="Focused Item:"></Label>
            
            <mxe:TextEditor 
                ReadOnly="True"
                EditorValue="{Binding #treeList1.FocusedItem.Name}"
            >
            </mxe:TextEditor>
            <Label Content="Selected Items:" Margin="0,20,0,0"></Label>
            <ListBox Name="listBox"
                     Margin="6"
                     ItemsSource="{Binding SelectedEmployees}"
                 >
                <ListBox.ItemTemplate>
                    <DataTemplate>
                        <TextBlock Text="{Binding Name}" />
                    </DataTemplate>
                </ListBox.ItemTemplate>
            </ListBox>
        </StackPanel>
    </Grid>
</Window>
```

``` cs
using Avalonia.Controls;
using CommunityToolkit.Mvvm.ComponentModel;
using Eremex.AvaloniaUI.Controls.TreeList;
using System;
using System.Collections.ObjectModel;
using Eremex.AvaloniaUI.Controls.DataControl;

namespace TreeControls;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        MyViewModel viewModel = new MyViewModel();
        this.DataContext = viewModel;

        InitializeComponent();

        treeList1.SelectionMode = RowSelectionMode.Multiple;
        treeList1.ExpandAllNodes();
        TreeListNode node1 = treeList1.FindNode(node => 
            (node.Content as Employee).Name.Contains("Sam"));
        TreeListNode node2 = treeList1.FindNode(node => 
            (node.Content as Employee).Name.Contains("Dan"));
        treeList1.BeginSelection();
        treeList1.ClearSelection();
        treeList1.SelectNode(node1);
        treeList1.SelectNode(node2);
        treeList1.EndSelection();
    }
}

public partial class MyViewModel : ObservableObject
{
    public MyViewModel()
    {
        Employee p1 = new Employee() { 
            Name = "Mark Douglas", Birthdate = new DateTime(1990, 01, 5) };
        Employee p2 = new Employee() { 
            Name = "Mary Watson", Birthdate = new DateTime(1985, 12, 17) };
        Employee p3 = new Employee() { 
            Name = "Alex Wude", Birthdate = new DateTime(2000, 10, 7) };
        Employee p4 = new Employee() { 
            Name = "Sam Louis", Birthdate = new DateTime(1975, 8, 27) };
        Employee p5 = new Employee() { 
            Name = "Dan Miller", Birthdate = new DateTime(1981, 3, 6) };
        p1.Subordinates.Add(p2);
        p1.Subordinates.Add(p3);
        p2.Subordinates.Add(p4);
        p3.Subordinates.Add(p5);

        Employees = new ObservableCollection<Employee>() { p1 };

        SelectedEmployees = new();
    }

    public ObservableCollection<Employee> Employees { get; set; }

    public ObservableCollection<Employee>? SelectedEmployees { get; set; }
}

public partial class Employee : ObservableObject
{
    [ObservableProperty]
    public string name = "";

    [ObservableProperty]
    public DateTime? birthdate = null;

    public ObservableCollection<Employee> Subordinates { get; } = new();

    public bool HasChildren { get { return Subordinates.Count > 0; } }
}
```