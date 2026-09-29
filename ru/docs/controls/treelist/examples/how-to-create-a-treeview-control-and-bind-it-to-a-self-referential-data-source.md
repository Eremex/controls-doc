---
title: Как создать TreeView и привязать его к Self-Referential источнику данных
seealso: []
---

# Как создать TreeView и привязать его к Self-Referential источнику данных

В этом примере создаётся элемент управления `TreeViewControl`, отображающий иерархическую коллекцию объектов _Employee_. Имя сотрудника, на котором в данный момент установлен фокус в TreeView, отображается в текстовом редакторе.

Класс _Employee_ представляет собой [Self-Referential источник данных](../data-binding/binding-to-self-referential-data-source.md). Он хранит информацию об отношениях "родитель-потомок" в двух служебных свойствах (_ID_ и _ParentID_).

В примере для настройки `TreeViewControl` используются следующие основные свойства:

- `DataControlBase.ItemsSource` — задаёт источник данных элемента управления.
- `TreeListControlBase.KeyFieldName` — задаёт имя поля _Key field_ (свойства), хранящего уникальные идентификаторы записей.
- `TreeListControlBase.ParentFieldName` — задаёт имя поля _Key field_ (свойства) родительской записи.
- `TreeListControlBase.RootValue` — определяет корневые записи в привязанной коллекции. Свойство `RootValue` задаёт значение, которое корневые записи имеют в поле _Parent key field_ (свойстве).
- `TreeViewControl.DataFieldName` — задаёт имя поля (свойства), данные которого отображаются в `TreeViewControl`.

Когда пользователь устанавливает фокус на узле, вы можете использовать унаследованное свойство `DataControlBase.FocusedItem` элемента TreeView, чтобы получить базовый объект данных сфокусированного узла.
В примере свойство `DataControlBase.FocusedItem` возвращает объект _Employee_. Значение _Name_ сфокусированного объекта _Employee_ отображается в `TextEditor`.

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

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
