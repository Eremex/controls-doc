---
title: How to Create a TreeView Control and Bind It to a Self Referential Data Source
order: 9900
seealso: []
---

# How to Create a TreeView Control and Bind It to a Self Referential Data Source

This example creates a `TreeViewControl` control that displays a hierarchical collection of _Employee_ objects. The name of the employee currently focused in the TreeView is displayed in a text editor.

The _Employee_ class is [self-referential data source](../data-binding/binding-to-self-referential-data-source.md). It stores information on parent-child relationships in two service properties (_ID_ and _ParentID_).

In the example the following main properties are used to set up the `TreeViewControl`:

- `DataControlBase.ItemsSource` — Specifies the control's data source.
- `TreeListControlBase.KeyFieldName` — Specifies the name of the _Key field_ (property) that stores unique record identifiers.
- `TreeListControlBase.ParentFieldName` — Specifies the name of the parent record's _Key field_ (property).
- `TreeListControlBase.RootValue` — Identifies root records in the bound collection. The `RootValue` property specifies the value that root records have in the _Parent key field_ (property).
- `TreeViewControl.DataFieldName` — Specifies the name of the field (property) whose data is displayed in the `TreeViewControl`.

When a user focuses a node, you can use the TreeView's `DataControlBase.FocusedItem` inherited property to retrieve the focused node's underlying data object.
In the example, the `DataControlBase.FocusedItem` property returns an _Employee_ object. The _Name_ value of the focused _Employee_ object is displayed in a `TextEditor`.

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
        <mxtl:TreeViewControl 
            Grid.Column="0"
            Name="treeView1"
            ItemsSource="{Binding Employees}"
            DataFieldName="Name"
            KeyFieldName="ID"
            ParentFieldName="ParentID"
            FocusedItem="{Binding Current}"
            >
            <mxtl:TreeViewControl.RootValue>
                <sys:Int32>-1</sys:Int32>
            </mxtl:TreeViewControl.RootValue>
        </mxtl:TreeViewControl>
        <StackPanel Orientation="Vertical" Grid.Column="1" >
            <Label Content="Focused Item:"></Label>
            
        <mxe:TextEditor 
            ReadOnly="True"
            EditorValue="{Binding Current.Name}"
            >
        </mxe:TextEditor>
        </StackPanel>
    </Grid>
</Window>
```

``` cs
using Avalonia.Controls;
using CommunityToolkit.Mvvm.ComponentModel;
using System;
using System.Collections.ObjectModel;

namespace TreeControls
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            MyViewModel viewModel = new MyViewModel();
            this.DataContext = viewModel;

            InitializeComponent();

            treeView1.ExpandAllNodes();
        }
    }

    public partial class MyViewModel : ObservableObject
    {
        public MyViewModel() 
        {
            Employees = new ObservableCollection<Employee>
            {
                new Employee() 
                { 
                    ID = 0, ParentID = -1, Name = "Serge Smolin", Birthdate = new DateTime(1990, 01, 5) 
                },
                new Employee() 
                { 
                    ID = 1, ParentID = 0, Name = "Alex Douglas", Birthdate = new DateTime(1975, 8, 27) 
                },
                new Employee() 
                { 
                    ID = 2, ParentID = 0, Name = "Dennis Parker", Birthdate = new DateTime(1985, 12, 17) 
                },
                new Employee() 
                { 
                    ID = 3, ParentID = 1, Name = "Pavel Morris", Birthdate = new DateTime(1987, 10, 15) 
                },
                new Employee() 
                { 
                    ID = 4, ParentID = 2, Name = "Mary Thompson", Birthdate = new DateTime(1991, 03, 16) 
                },
                new Employee() 
                { 
                    ID = 5, ParentID = 3, Name = "Vera Liskina", Birthdate = new DateTime(1991, 04, 16) 
                }
            };

            Current = null;
        }

        public ObservableCollection<Employee> Employees { get; set; }

        [ObservableProperty]
        public Employee? current;
    }

    public partial class Employee : ObservableObject
    {
        [ObservableProperty]
        public string name = "";

        [ObservableProperty]
        public DateTime? birthdate = null;

        public int ID { get; set; }

        public int ParentID { get; set; }
    }
}
```