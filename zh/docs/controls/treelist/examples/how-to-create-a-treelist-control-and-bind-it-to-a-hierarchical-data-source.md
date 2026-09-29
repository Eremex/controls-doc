---
title: 如何创建 TreeList 并将其绑定到层次化数据源
seealso: []
---

# 如何创建 TreeList 并将其绑定到层次化数据源

本示例创建以下控件:

- 一个 `TreeListControl` 控件,用于显示 _Employee_ 对象的层次化列表。已启用多节点选择,允许您一次选中(高亮)多个节点。
- 一个文本编辑器,用于显示当前在 TreeList 中获得焦点的员工姓名。
- 一个列表框控件,用于显示在 TreeList 中被选中(高亮)的员工姓名。

TreeList 绑定到 _Employee_ 业务对象,该对象表示一个[层次化数据源](../data-binding/binding-to-hierarchical-data.md)。它包含 _Subordinates_ 集合,该集合的内容应作为子节点显示。

在本示例中,以下主要属性用于设置 `TreeListControl`:

- `DataControlBase.ItemsSource` — 指定控件的数据源。
- `TreeListControl.Columns` — 指定绑定到数据源属性的 TreeList 列集合。
- `TreeListControlBase.ChildrenFieldName` — 指定在底层业务对象中存储子数据的字段(属性)名称。
- `TreeListControlBase.HasChildrenFieldName` — 指定一个字段(属性)的名称,如果业务对象拥有子数据,该字段返回 `true`,否则返回 `false`。
- `TreeListControlBase.SelectionMode` — 启用多节点选择。

在多节点选择模式下,用户可以使用鼠标和键盘选中(高亮)多个节点。例如,用户可以按住 CTRL 键并单击各个节点来选中它们。TreeList 允许您通过 `DataControlBase.SelectedItems` 集合访问当前选中的节点。

以下两个控件用于显示当前获得焦点和被选中的 TreeList 节点的信息:

- 文本编辑器显示获得焦点节点的 _Employee_ 对象的姓名。该控件绑定到 TreeList 的 `FocusedItem` 属性。
- 列表框显示与 TreeList 选中节点对应的 _Employee_ 对象的姓名。

本示例在应用程序启动时按姓名查找两个 TreeList 节点,并选中它们。

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

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
