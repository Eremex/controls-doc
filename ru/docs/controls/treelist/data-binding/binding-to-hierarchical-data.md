---
title: Привязка к иерархическим данным
order: 100000
seealso: []
---

# Привязка к иерархическим данным

В типичном иерархическом источнике данных бизнес-объект имеет свойство, которое хранит коллекцию дочерних объектов данных. Существует два подхода, позволяющих предоставить дочерние данные элементам управления TreeList и TreeView в режиме иерархической привязки:

- [Указать путь к дочерним данным](#указание-пути-к-дочерним-данным)

- [Указать селектор дочерних элементов](#указание-селектора-дочерних-элементов)

    Селектор дочерних элементов полезен в следующих случаях:
    - Когда родительский и дочерний бизнес-объекты имеют разные типы
    - Когда невозможно указать путь к дочерним данным



## Динамическая загрузка данных

При привязке к иерархическому источнику данных элементы управления TreeList и TreeView по умолчанию загружают узлы по требованию: дочерние узлы динамически загружаются при разворачивании родительского узла.

Установите свойство `AllowDynamicDataLoading` в `false`, чтобы загружать все узлы одновременно после привязки элемента управления к источнику данных.

Если вы используете динамическую загрузку узлов, элементы управления TreeList и TreeView не имеют доступа к узлам (и связанным с ними данным), которые ещё не были загружены. Это накладывает следующие ограничения на функциональность проверки узлов и фильтрации/поиска:

- При установке отметки родительского узла в рекурсивном режиме (см. `AllowRecursiveNodeChecking`) элемент управления отмечает этот узел вместе с уже загруженными дочерними узлами. Дочерние узлы, которые ещё не были загружены, не отмечаются.

- При поиске данных во встроенном поле поиска или фильтрации данных с помощью строки автофильтра элемент управления выполняет поиск только среди уже загруженных узлов.

## Указание пути к дочерним данным

Один из подходов для предоставления дочерних данных элементу управления TreeList/TreeView заключается в указании имени свойства, которое хранит дочерние данные в бизнес-объекте. Для этого используйте свойство `ChildrenFieldName`. Например, если бизнес-объект хранит дочерние данные в коллекции `Items`, установите свойство `ChildrenFieldName` в значение "_Items_".

Вам также необходимо установить свойство `HasChildrenFieldName` в имя свойства, которое возвращает `true`, если бизнес-объект имеет дочерние данные, и `false` в противном случае. Эта информация требуется для отображения или скрытия кнопок разворачивания узлов.
Если вы не укажете свойство `HasChildrenFieldName`, элемент управления будет отображать кнопки разворачивания для узлов без потомков до тех пор, пока пользователь не попытается развернуть эти узлы.

Следующий пример демонстрирует, как привязать элемент управления TreeList к данным. Объект _Employee_ в примере имеет коллекцию _Subordinates_, содержащую дочерние элементы. Свойство `ChildrenFieldName` указывает имя свойства (строка "_Subordinates_"), которое хранит дочерние данные.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
...
<mxtl:TreeListControl Grid.Column="0" Width="400" Name="treeList1" >
    <mxtl:TreeListControl.Columns>
        <mxtl:TreeListColumn Name="colName" FieldName="Name" Header="Name" />
        <mxtl:TreeListColumn Name="colBirthdate" FieldName="Birthdate" Header="Birthdate"/>
    </mxtl:TreeListControl.Columns>
</mxtl:TreeListControl>
```
``` cs
using CommunityToolkit.Mvvm.ComponentModel;

Employee p1 = new Employee() { Name = "Mark Douglas", Birthdate=new DateTime(1990, 01, 5) };
Employee p2 = new Employee() { Name = "Mary Watson", Birthdate = new DateTime(1985, 12, 17) };
Employee p3 = new Employee() { Name = "Alex Wude", Birthdate = new DateTime(2000, 10, 7) };
Employee p4 = new Employee() { Name = "Sam Louis", Birthdate = new DateTime(1975, 8, 27) };
Employee p5 = new Employee() { Name = "Dan Miller", Birthdate = new DateTime(1981, 3, 6) };
p1.Subordinates.Add(p2);
p1.Subordinates.Add(p3);
p2.Subordinates.Add(p4);
p3.Subordinates.Add(p5);

ObservableCollection<Employee> employees = new ObservableCollection<Employee>() { p1 };

treeList1.ChildrenFieldName = "Subordinates";
treeList1.HasChildrenFieldName = "HasChildren";

treeList1.ItemsSource = employees;

public partial class Employee : ObservableObject
{
    [ObservableProperty]
    public string name="";

    [ObservableProperty]
    public DateTime? birthdate=null;

    public ObservableCollection<Employee> Subordinates { get; } = new();

    public bool HasChildren { get { return Subordinates.Count > 0; } }
}
```

## Указание селектора дочерних элементов

Другой подход к предоставлению дочерних данных в режиме иерархической привязки заключается в реализации _селектора дочерних элементов_ (children selector). Селектор определяет, доступны ли дочерние данные в бизнес-объекте, и возвращает эти дочерние данные по требованию. Элемент управления TreeList/TreeView использует информацию, предоставленную селектором, для создания дочерних узлов и отрисовки кнопок разворачивания узлов.

Селектор дочерних элементов полезен в следующих сценариях:

- Когда родительский и дочерний бизнес-объекты [имеют разные типы](#использование-селектора-дочерних-элементов-когда-родительский-и-дочерний-бизнес-объекты-различны)
- Во всех остальных случаях, когда невозможно указать путь к дочерним элементам с помощью свойства `ChildrenFieldName`.



Используйте свойство `TreeListControlBase.ChildrenSelector`, чтобы назначить селектор элементу управления TreeList/TreeView. Селектор — это объект, реализующий интерфейс `ITreeListChildrenSelector`:

``` cs
public interface ITreeListChildrenSelector
{
    // The method should return whether a business object has child data. 
    // The control uses this information to display or hide node expand buttons.
    bool HasChildren(object item) => true;
    // The method should return child objects for a business object.
    IEnumerable? SelectChildren(object item);
}
```



### Пример — реализация простого селектора дочерних элементов

Следующий пример создаёт селектор (_MyTreeListChildrenSelector_), который предоставляет информацию о дочерних элементах для элемента управления TreeList.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
...
<Grid RowDefinitions="Auto, Auto, Auto, Auto" ColumnDefinitions="400, *">
    <Grid.Resources>
        <local:MyTreeListChildrenSelector x:Key="mySelector" />
    </Grid.Resources>

    <mxtl:TreeListControl Grid.Column="0" Name="treeList2"
     ChildrenSelector="{StaticResource mySelector}">
        <mxtl:TreeListControl.Columns>
            <mxtl:TreeListColumn Name="colName1" FieldName="Name" />
            <mxtl:TreeListColumn Name="colBirthdate1" FieldName="Birthdate"/>
        </mxtl:TreeListControl.Columns>
    </mxtl:TreeListControl>
</Grid>
```
``` cs
using CommunityToolkit.Mvvm.ComponentModel;

Employee p1 = new Employee() { Name = "Mark Douglas", Birthdate = new DateTime(1990, 01, 5)};
Employee p2 = new Employee() { Name = "Mary Watson", Birthdate = new DateTime(1985, 12, 17)};
Employee p3 = new Employee() { Name = "Alex Wude", Birthdate = new DateTime(2000, 10, 7)};
Employee p4 = new Employee() { Name = "Sam Louis", Birthdate = new DateTime(1975, 8, 27)};
Employee p5 = new Employee() { Name = "Dan Miller", Birthdate = new DateTime(1981, 3, 6)};
p1.Subordinates.Add(p2);
p1.Subordinates.Add(p3);
p2.Subordinates.Add(p4);
p3.Subordinates.Add(p5);

ObservableCollection<Employee> employees = new ObservableCollection<Employee>() { p1 };

treeList2.ItemsSource = employees;

public class MyTreeListChildrenSelector : ITreeListChildrenSelector
{
    public bool HasChildren(object? item) => (item as Employee).HasChildren;
    public IEnumerable? SelectChildren(object? item) => (item as Employee).Subordinates;
}

public partial class Employee : ObservableObject
{
    [ObservableProperty]
    public string name="";

    [ObservableProperty]
    public DateTime? birthdate=null;

    public ObservableCollection<Employee> Subordinates = new();

    public bool HasChildren { get { return Subordinates.Count > 0; } }
}
```


### Использование селектора дочерних элементов, когда родительский и дочерний бизнес-объекты различны

Следующие соображения применимы, когда родительский и дочерний бизнес-объекты относятся к разным типам.

- TreeList отображает значения из полей, к которым привязаны колонки TreeList (см. `TreeListColumn.FieldName`). Родительский и дочерний бизнес-объекты должны предоставлять эти поля.

- Элемент управления TreeView отображает значения бизнес-объектов из поля, имя которого задано свойством `DataFieldName`. Убедитесь, что родительский и дочерний объекты данных имеют это поле.

### Пример — реализация селектора дочерних элементов в случае разных бизнес-объектов

Предположим, что элемент управления TreeView привязан к коллекции объектов _City_. Каждый объект _City_ владеет коллекцией объектов _Street_, которые, в свою очередь, владеют коллекциями объектов _Building_. TreeView должен отображать города на корневом уровне, улицы — на втором уровне, а номера домов — на третьем уровне.

![treeview-hierarchical-different-bus-objects-example](../../../images/treeview-hierarchical-different-bus-objects-example.png)

Приведённый ниже код показывает определения бизнес-объектов _City_, _Street_ и _Building_.
Обратите внимание, что все эти объекты имеют свойство _Name_. Имя этого свойства будет присвоено свойству `TreeViewControl.DataFieldName` в XAML.

``` cs
public class City
{
    public City(string name) { Name = name; }
    public string Name { get; set; }
    public ObservableCollection<Street> Streets = new();
}

public class Street 
{
    public Street(string name, string[] buidingNumbers) { 
        Name = name;
        foreach (string number in buidingNumbers)
        {
            Buildings.Add(new Building(number));
        }
    }
    public string Name { get; set; }
    public ObservableCollection<Building> Buildings = new();
}

public class Building  
{
    public Building(string name) { Name = name; }
    public string Name { get; set; }
}
```

Элемент управления TreeView привязан к коллекции _Cities_, определённой во View Model. Свойство `TreeViewControl.DataFieldName` установлено в значение "Name". Это свойство определяет поле бизнес-объектов, значения которого должны отображаться в элементе управления TreeView.

``` cs
public partial class MainWindowViewModel : ViewModelBase
{
    [ObservableProperty]
    ObservableCollection<City> cities = new();
    //...
}
```
``` xml
<mxtl:TreeViewControl 
    Name="treeView"
    ItemsSource="{Binding Cities}"
    DataFieldName="Name"
    ...
/>
```

Поскольку бизнес-объекты в иерархическом источнике данных относятся к разным типам, для получения дочерних элементов узлов TreeView необходимо реализовать селектор.

``` cs
public class MyTreeListChildrenSelector : ITreeListChildrenSelector
{
    public bool HasChildren(object item)
    {
        if (item is City city)
            return city.Streets.Count > 0;
        if (item is Street street)
            return street.Buildings.Count > 0;
        return false;
    }
    public IEnumerable? SelectChildren(object item)
    {
        if (item is City city)
            return city.Streets;
        if (item is Street street)
            return street.Buildings;
        return null;
    }
}
```

Чтобы назначить селектор _MyTreeListChildrenSelector_ элементу управления TreeView, используйте свойство `TreeListControlBase.ChildrenSelector`.

``` xml
xmlns:local="clr-namespace:EremexAvaloniaApplication10.Views"

<mx:MxWindow.Resources>
    <local:MyTreeListChildrenSelector x:Key="mySelector" />
</mx:MxWindow.Resources>

<mxtl:TreeViewControl ...
    ChildrenSelector="{StaticResource mySelector}"
/>
```

#### Полный код

Полный код этого примера приведён ниже.

``` xml
<!-- MainWindow.axaml -->

<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:EremexAvaloniaApplication10.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="EremexAvaloniaApplication10.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="EremexAvaloniaApplication10"
        xmlns:local="clr-namespace:EremexAvaloniaApplication10.Views"
        >

    <Design.DataContext>
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <mx:MxWindow.Resources>
        <local:MyTreeListChildrenSelector x:Key="mySelector" />
    </mx:MxWindow.Resources>

    <mxtl:TreeViewControl Name="treeView"
                          ItemsSource="{Binding Cities}"
                          DataFieldName="Name"
                          ChildrenSelector="{StaticResource mySelector}"
                          />
</mx:MxWindow>
```

``` cs
//MainWindow.axaml.cs

using Avalonia.Controls;
using Eremex.AvaloniaUI.Controls.Common;
using Eremex.AvaloniaUI.Controls.TreeList;
using EremexAvaloniaApplication10.ViewModels;
using System.Collections;

namespace EremexAvaloniaApplication10.Views
{
    public partial class MainWindow : MxWindow
    {
        public MainWindow()
        {
            InitializeComponent();
        }
    }

    public class MyTreeListChildrenSelector : ITreeListChildrenSelector
    {
        public bool HasChildren(object item)
        {
            if (item is City city)
                return city.Streets.Count > 0;
            if (item is Street street)
                return street.Buildings.Count > 0;
            return false;
        }
        public IEnumerable? SelectChildren(object item)
        {
            if (item is City city)
                return city.Streets;
            if (item is Street street)
                return street.Buildings;
            return null;
        }
    }
}
```

``` cs
//MainWindowViewModel.cs

using CommunityToolkit.Mvvm.ComponentModel;
using DynamicData;
using System.Collections.ObjectModel;
using System.Security.Cryptography;

namespace EremexAvaloniaApplication10.ViewModels
{
    public partial class MainWindowViewModel : ViewModelBase
    {
        [ObservableProperty]
        ObservableCollection<City> cities = new();

        public MainWindowViewModel()
        {
            Street s1 = new Street("Khaosan Rd", new string[] { "234", "278", "299" });
            Street s2 = new Street("Nonsi Rd", new string[] { "678", "639" });
            Street s3 = new Street("Airport Rd", new string[] { "324", "373" } );
            Street s4 = new Street("Pipeline Rd", new string[] { "111", "185" });

            City c1 = new City("Bangkok");
            City c2 = new City("Mumbai");

            c1.Streets.Add(s1);
            c1.Streets.Add(s2);
            c2.Streets.Add(s3);
            c2.Streets.Add(s4);

            cities.AddRange(new[] { c1, c2 });
        }
    }

    public class City
    {
        public City(string name) { Name = name; }
        public string Name { get; set; }
        public ObservableCollection<Street> Streets = new();
    }

    public class Street 
    {
        public Street(string name, string[] buildingNumbers) { 
            Name = name;
            foreach (string number in buildingNumbers)
            {
                Buildings.Add(new Building(number));
            }
        }
        public string Name { get; set; }
        public ObservableCollection<Building> Buildings = new();
    }

    public class Building  
    {
        public Building(string name) { Name = name; }
        public string Name { get; set; }
    }
}
```

# Смотрите также
- [Привязка данных](./index.md)
- [Привязка к Self-Referential источнику данных](binding-to-self-referential-data-source.md)
- [Колонки](../columns.md)
- [Как создать TreeList и привязать его к иерархическому источнику данных](../examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
