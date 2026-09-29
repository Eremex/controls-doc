---
title: 如何创建 TreeView 并将其绑定到 Self-Referential 数据源
seealso: []
---

# 如何创建 TreeView 并将其绑定到 Self-Referential 数据源

本示例创建一个 `TreeViewControl` 控件,用于显示 _Employee_ 对象的层次化集合。当前在 TreeView 中获得焦点的员工姓名会显示在一个文本编辑器中。

_Employee_ 类是一个 [Self-Referential 数据源](../data-binding/binding-to-self-referential-data-source.md)。它在两个服务属性(_ID_ 和 _ParentID_)中存储父子关系信息。

在本示例中,以下主要属性用于设置 `TreeViewControl`:

- `DataControlBase.ItemsSource` — 指定控件的数据源。
- `TreeListControlBase.KeyFieldName` — 指定存储唯一记录标识符的 _Key field_(属性)名称。
- `TreeListControlBase.ParentFieldName` — 指定父记录的 _Key field_(属性)名称。
- `TreeListControlBase.RootValue` — 标识绑定集合中的根记录。`RootValue` 属性指定根记录在 _Parent key field_(属性)中所具有的值。
- `TreeViewControl.DataFieldName` — 指定其数据显示在 `TreeViewControl` 中的字段(属性)名称。

当用户将焦点设置到某个节点时,您可以使用 TreeView 继承的 `DataControlBase.FocusedItem` 属性来获取获得焦点节点的底层数据对象。
在本示例中,`DataControlBase.FocusedItem` 属性返回一个 _Employee_ 对象。获得焦点的 _Employee_ 对象的 _Name_ 值显示在 `TextEditor` 中。

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

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
