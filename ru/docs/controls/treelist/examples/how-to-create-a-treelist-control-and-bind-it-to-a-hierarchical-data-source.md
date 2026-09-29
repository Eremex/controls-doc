---
title: Как создать TreeList и привязать его к иерархическому источнику данных
seealso: []
---

# Как создать TreeList и привязать его к иерархическому источнику данных

В этом примере создаются следующие элементы управления:

- Элемент управления `TreeListControl`, отображающий иерархический список объектов _Employee_. Включён множественный выбор узлов, который позволяет выделять (подсвечивать) сразу несколько узлов.
- Текстовый редактор, отображающий имя сотрудника, на котором в данный момент установлен фокус в TreeList.
- Элемент управления "список" (list box), отображающий имена сотрудников, выделенных (подсвеченных) в TreeList.

TreeList привязан к бизнес-объекту _Employee_, который представляет собой [иерархический источник данных](../data-binding/binding-to-hierarchical-data.md). Он содержит коллекцию _Subordinates_, содержимое которой должно отображаться в виде дочерних узлов.

В примере для настройки `TreeListControl` используются следующие основные свойства:

- `DataControlBase.ItemsSource` — задаёт источник данных элемента управления.
- `TreeListControl.Columns` — задаёт коллекцию колонок TreeList, привязанных к свойствам источника данных.
- `TreeListControlBase.ChildrenFieldName` — задаёт имя поля (свойства), которое хранит дочерние данные в базовом бизнес-объекте.
- `TreeListControlBase.HasChildrenFieldName` — задаёт имя поля (свойства), которое возвращает `true`, если бизнес-объект имеет дочерние данные, и `false` в противном случае.
- `TreeListControlBase.SelectionMode` — включает множественный выбор узлов.

В режиме множественного выбора узлов пользователь может выделять (подсвечивать) несколько узлов с помощью мыши и клавиатуры. Например, пользователь может удерживать клавишу CTRL и щёлкать по отдельным узлам, чтобы выделить их. TreeList позволяет обращаться к текущим выделенным узлам через коллекцию `DataControlBase.SelectedItems`.

Следующие два элемента управления используются для отображения информации о текущем сфокусированном и выделенных узлах TreeList:

- Текстовый редактор отображает имя объекта _Employee_ сфокусированного узла. Элемент управления привязан к свойству `FocusedItem` TreeList.
- Список отображает имена объектов _Employee_, соответствующих выделенным узлам TreeList.

В примере при запуске приложения по имени находятся два узла TreeList, которые затем выделяются.

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

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
