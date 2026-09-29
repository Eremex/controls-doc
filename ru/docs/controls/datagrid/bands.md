---
title: Группы
order: 75000
seealso: []
---

# Группы

Вы можете использовать группы, чтобы визуально объединять колонки. DataGrid отображает группы в виде дополнительных заголовков над заголовками колонок. Заголовки групп и колонок могут содержать текст, изображения или пользовательское содержимое. Вы также можете создавать иерархическую структуру групп с неограниченным количеством уровней вложенности.

На следующем изображении показан DataGrid с четырьмя группами: «Customer», «Details», «Address» и «Contact»:

![datagrid-bands](../../images/datagrid-bands.png)

Существуют следующие подходы для создания групп:

- [Создание групп вручную](#создание-групп-вручную)
- [Создание групп на основе источника групп](#создание-групп-на-основе-источника-групп)
- [Создание групп на основе атрибутов DataAnnotation (для автоматически создаваемых колонок)](#создание-групп-на-основе-атрибутов-dataannotation-для-автоматически-создаваемых-колонок)


## Создание групп вручную

Чтобы вручную создать группы, выполните следующие действия:

1. Создайте объекты групп (экземпляры класса `GridBand`) и добавьте их в коллекцию `DataGridControl.Bands`. 

    Присвойте созданным группам уникальные имена, используя свойство `GridBand.BandName`.

    ``` xml
    <mxdg:DataGridControl.Bands>
        <mxdg:GridBand BandName="Customer" HeaderHorizontalAlignment="Center"/>
        <mxdg:GridBand BandName="Details" HeaderHorizontalAlignment="Center"/>
    </mxdg:DataGridControl.Bands>
    ```

    Вы можете создать иерархическую структуру групп. Чтобы создать вложенные группы:
        
    - В code-behind: добавьте группы в коллекцию `GridBand.Bands`.
    - В XAML: определите вложенные группы непосредственно между открывающим и закрывающим тегами `GridBand`.

    ``` xml
    <mxdg:GridBand BandName="Details" HeaderHorizontalAlignment="Center">
        <mxdg:GridBand BandName="DetailsAddress" Header="Address" HeaderHorizontalAlignment="Center"/>
        <mxdg:GridBand BandName="DetailsContact" Header="Contact" HeaderHorizontalAlignment="Center"/>
    </mxdg:GridBand>
    ```

    Свойство `GridBand.Header` позволяет задать пользовательское содержимое (например, произвольный текст) для группы. Если это свойство не задано, заголовок группы отображает значение свойства `GridBand.BandName`.

2. Свяжите колонки с конкретными группами, установив свойство каждой колонки `GridColumn.BandName` в имя соответствующей группы (`GridBand.BandName`).

    ``` xml
    <mxdg:DataGridControl.Columns>
        <mxdg:GridColumn FieldName="FirstName" BandName="Customer" Width="*"/>
        <mxdg:GridColumn FieldName="City" BandName="DetailsAddress" Width="*"/>
        <mxdg:GridColumn FieldName="Phone" BandName="DetailsContact" Width="*"/>
        <!-- ... -->
    </mxdg:DataGridControl.Columns>
    ```

Колонки располагаются в DataGrid в соответствии со значениями свойства `GridColumn.VisibleIndex`.
Контрол не переупорядочивает колонки автоматически, чтобы сгруппировать их по группам.

![datagrid-bands-not-keep-columns-together](../../images/datagrid-bands-not-keep-columns-together.png)

Смотрите [Порядок колонок и групп](#порядок-колонок-и-групп)




### Связанный API

- `GridBand` — класс, инкапсулирующий группу колонок.
- `GridBand.BandName` — уникальное имя, используемое для идентификации группы и её связи с колонками.
- `GridColumn.BandName` — имя группы, связанной с колонкой. Это значение совпадает со значением свойства `GridBand.BandName`.
- `DataGridControl.Bands` — коллекция корневых групп.
- `GridBand.Bands` — коллекция дочерних групп для данной группы.


### Пример - Ручное создание групп колонок в DataGrid

Следующий пример создаёт группы и связывает их с колонками, как показано на изображении ниже:

![datagrid-bands-example](../../images/datagrid-bands-example.png)

- Группы «Customer», «Address» и «Contact» связаны с колонками таблицы. 
- Группа «Details» содержит две вложенные группы («Address» и «Contact»). Сама эта группа не связана с колонками напрямую.

Каждой группе присваивается уникальное имя с помощью свойства `GridBand.BandName`. Чтобы связать колонки с конкретной группой, установите свойство колонки `GridColumn.BandName` равным значению `BandName` целевой группы.

Свойство `DataGridControl.Bands` определяет структуру групп. Чтобы создать вложенные группы, определите их как дочерние элементы родительской группы.

``` xml
<!-- MainWindow.axaml file -->
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:DataGridColumnBands.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
        xmlns:svg="using:Avalonia.Svg.Skia"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="DataGridColumnBands.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="DataGridColumnBands">

    <Design.DataContext>
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <Grid RowDefinitions="Auto *" Margin="10">
        <mxdg:DataGridControl BorderBrush="LightGray" BorderThickness="1" Name="gridControl1"
                              ItemsSource="{Binding Employees}"
                              AllowColumnMoving="False"
                          >
            <mxdg:DataGridControl.Bands>
                <mxdg:GridBand BandName="Customer" HeaderHorizontalAlignment="Center">
                    <mxdg:GridBand.HeaderTemplate>
                        <DataTemplate>
                            <StackPanel Orientation="Horizontal">
                                <svg:Svg Path="/Assets/customer.svg" Width="16" Height="16" Margin="5" />
                                <TextBlock Text="{Binding}" VerticalAlignment="Center"/>
                            </StackPanel>
                        </DataTemplate>
                    </mxdg:GridBand.HeaderTemplate>

                </mxdg:GridBand>
                <mxdg:GridBand BandName="Details" HeaderHorizontalAlignment="Center">
                    <mxdg:GridBand BandName="DetailsAddress" Header="Address" HeaderHorizontalAlignment="Center"/>
                    <mxdg:GridBand BandName="DetailsContact" Header="Contact" HeaderHorizontalAlignment="Center"/>
                </mxdg:GridBand>
            </mxdg:DataGridControl.Bands>

            <mxdg:DataGridControl.Columns>
                <mxdg:GridColumn Width="*" FieldName="FirstName" BandName="Customer"/>
                <mxdg:GridColumn Width="*" FieldName="LastName" BandName="Customer"/>
                <mxdg:GridColumn Width="*" FieldName="Title" BandName="Customer"/>
                <mxdg:GridColumn Width="*" FieldName="BirthDate" BandName="Customer"/>
                <mxdg:GridColumn Width="*" FieldName="Address" BandName="DetailsAddress"/>
                <mxdg:GridColumn Width="*" FieldName="City" BandName="DetailsAddress"/>
                <mxdg:GridColumn Width="*" FieldName="Country" BandName="DetailsAddress"/>
                <mxdg:GridColumn Width="*" FieldName="EMail" BandName="DetailsContact" Header="E-mail"/>
                <mxdg:GridColumn Width="*" FieldName="Phone" BandName="DetailsContact"/>
            </mxdg:DataGridControl.Columns>
        </mxdg:DataGridControl>
    </Grid>
</mx:MxWindow>
```

``` cs
//MainWindow.axaml.cs file
using Avalonia.Controls;
using Eremex.AvaloniaUI.Controls.Common;
using DataGridColumnBands.ViewModels;

namespace DataGridColumnBands.Views
{
    public partial class MainWindow : MxWindow
    {
        public MainWindow()
        {
            InitializeComponent();
            this.DataContext = new MainWindowViewModel();
        }
    }
}
```

``` cs
//MainWindowViewModel.cs file
using System.ComponentModel;
using CommunityToolkit.Mvvm.ComponentModel;
using System.Collections.Generic;
using System;

namespace DataGridColumnBands.ViewModels
{
    public partial class MainWindowViewModel : ViewModelBase
    {
        [ObservableProperty]
        IList<CustomerInfo> employees;

        public MainWindowViewModel()
        {
            Employees = GetSampleCustomers();
        }

        public static List<CustomerInfo> GetSampleCustomers() => new()
        {
            new("Raj", "Patel", "Financial Analyst", new DateTime(1988, 7, 12),
                "15 Gandhi Road", "Mumbai", "India", "raj.patel@example.in", "+91 22 6789 1234"),
            new("Yuki", "Tanaka", "Owner", new DateTime(1985, 3, 25),
                "3-5-1 Roppongi", "Tokyo", "Japan", "y.tanaka@example.jp", "+81 3 9876 5432"),
            new("Wei", "Zhang", "Financial Analyst", new DateTime(1991, 11, 8),
                "88 Nanjing Road", "Shanghai", "China", "wei.zhang@example.cn", "+86 21 3456 7890"),
            new("Amina", "Diallo", "HR Manager", new DateTime(1987, 4, 17),
                "12 Rue des Almadies", "Dakar", "Senegal", "a.diallo@example.sn", "+221 33 987 6543"),
            new("Carlos", "Silva", "Sales Executive", new DateTime(1983, 9, 30),
                "Av. Paulista 1000", "Sao Paulo", "Brazil", "c.silva@example.br", "+55 11 98765 4321"),
            new("Priya", "Wijesinghe", " Accounting Manager", new DateTime(1992, 2, 14),
                "25 Galle Road", "Colombo", "Sri Lanka", "priya.w@example.lk", "+94 11 234 5678"),
            new("Kwame", "Osei", "Project Manager", new DateTime(1980, 12, 5),
                "24 Independence Ave", "Accra", "Ghana", "k.osei@example.gh", "+233 30 123 4567"),
            new("María", "Gonzalez", "Owner", new DateTime(1986, 6, 22),
                "Calle 7 #5-20", "Bogota", "Colombia", "m.gonzalez@example.co", "+57 1 654 3210")
        };
    }

    public partial class CustomerInfo : ObservableObject
    {
        [ObservableProperty]
        public string firstName;

        [ObservableProperty]
        public string lastName;

        [ObservableProperty]
        public string title;

        [ObservableProperty]
        public DateTime birthDate;

        [ObservableProperty]
        public string address;

        [ObservableProperty]
        public string city;

        [ObservableProperty]
        public string country;

        [ObservableProperty]
        public string eMail;

        [ObservableProperty]
        public string phone;

        public CustomerInfo(string firstName, string lastName, string title,
                      DateTime birthDate, string address, string city,
                      string country, string eMail, string phone)
        {
            FirstName = firstName;
            LastName = lastName;
            Title = title;
            BirthDate = birthDate;
            Address = address;
            City = city;
            Country = country;
            EMail = eMail;
            Phone = phone;
        }
    }
}
```

``` cs
// customer.svg file is placed in the project's `Assets` folder, and its `Build Action` property is set to `AvaloniaResource`.
```

## Создание групп на основе источника групп

Вы можете заполнять группы колонок данными из источника групп, определённого в View Model. Используйте свойства `DataGridControl.BandsSource` и `DataGridControl.BandTemplate`, чтобы создавать группы из коллекции бизнес-объектов. 

В качестве альтернативы указанию свойства `BandTemplate` вы можете использовать свойство `Styles`, чтобы инициализировать объекты `GridBand` из бизнес-объектов. Смотрите [Инициализация групп с помощью стиля](#инициализация-групп-с-помощью-стиля) для примера.

Чтобы связать колонки с группами, установите свойство каждой колонки `GridColumn.BandName` равным имени соответствующей группы (`GridBand.BandName`).

### Связанный API

- `DataGridControl.BandsSource` — коллекция бизнес-объектов, используемая для создания корневых групп.
- `DataGridControl.BandTemplate` — шаблон, создающий экземпляры `GridBand` из бизнес-объектов.
- `GridBand.BandsSource` — коллекция бизнес-объектов, используемая для создания дочерних групп.
- `GridBand.BandName` — уникальное имя, используемое для идентификации группы и её связи с колонками.
- `GridColumn.BandName` — имя группы, связанной с колонкой. Это значение совпадает со значением свойства `GridBand.BandName`.

### Пример - Создание групп на основе источника групп

Следующий пример создаёт группы из коллекции объектов _BandInfo_, определённой в View Model.

DataGrid отображает коллекцию бизнес-объектов _Order_. Колонки таблицы создаются автоматически на основе публичных свойств класса _Order_. Обработчик события `AutoGeneratingColumn` контрола связывает автоматически созданные колонки с соответствующими группами.

![grid-bands-source-example](../../images/grid-bands-source-example.png)

``` xml
<!-- MainWindow.axaml -->
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:DataGridBandSource.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
        xmlns:local="using:DataGridBandSource.Views"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="DataGridBandSource.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="DataGridBandSource">

    <Design.DataContext>
        <!-- This only sets the DataContext for the previewer in an IDE,
             to set the actual DataContext for runtime, set the DataContext property in code (look at App.axaml.cs) -->
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <Border BorderThickness="1" BorderBrush="LightGray" Margin="5">
    <mxdg:DataGridControl Name="dataGrid1" 
                          ItemsSource="{Binding Orders}" 
                          AutoGenerateColumns="True"
                          BandsSource="{Binding BandInfos}"
                          AutoGeneratingColumn="DataGrid1_AutoGeneratingColumn"
                          >
        <mxdg:DataGridControl.BandTemplate>
            <local:DataGridBandTemplate/>
        </mxdg:DataGridControl.BandTemplate>
    </mxdg:DataGridControl>
    </Border>
</mx:MxWindow>

```

``` cs
// MainWindow.axaml.cs
using Avalonia.Controls.Templates;
using DataGridBandSource.ViewModels;
using Eremex.AvaloniaUI.Controls.Common;
using Eremex.AvaloniaUI.Controls.DataGrid;

namespace DataGridBandSource.Views;

public partial class MainWindow : MxWindow
{
    public MainWindow()
    {
        this.DataContext = new MainWindowViewModel();
        InitializeComponent();
    }

    private void DataGrid1_AutoGeneratingColumn(object? sender, Eremex.AvaloniaUI.Controls.DataGrid.DataGridControlAutoGeneratingColumnEventArgs e)
    {
        string columnFieldName = e.Column.FieldName.ToLower();
        if (columnFieldName.StartsWith("ship"))
        {
            if (columnFieldName.Contains("country") || columnFieldName.Contains("city"))
                e.Column.BandName = MainWindowViewModel.ShippingAddressBandName;
            else 
                e.Column.BandName = MainWindowViewModel.ShippingStatusBandName;
        }
        else
            e.Column.BandName= MainWindowViewModel.OrderBandName;
    }
}

public class DataGridBandTemplate : ITemplate<object, GridBand>
{
    public GridBand Build(object param)
    {
        var bandInfo = (BandInfo)param;
        var gridBand = new GridBand()
        {
            BandName = bandInfo.Name,
            Header = bandInfo.DisplayName,
            BandsSource = bandInfo.ChildBands,
            HeaderHorizontalAlignment = Avalonia.Layout.HorizontalAlignment.Center
        };
        return gridBand;
    }
}
```

``` cs
// MainWindowViewModel.cs
using CommunityToolkit.Mvvm.ComponentModel;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel.DataAnnotations;

namespace DataGridBandSource.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    public static string OrderBandName => "Orders";
    public static string ShippingAddressBandName => "ShipAddress";
    public static string ShippingStatusBandName => "ShipStatus";

    [ObservableProperty]
    private ObservableCollection<Order> orders;

    [ObservableProperty]
    private ObservableCollection<BandInfo> bandInfos;

    public MainWindowViewModel()
    {
        Orders = new ObservableCollection<Order>
        {
            new Order(10248, "Queso Cabrales", "Egypt", "Cairo",
                    new DateTime(2023, 7, 4), new DateTime(2023, 7, 16),
                    "Paul Henriot", "Delivered"),
            new Order(10249, "Singaporean Hokkien Fried Mee", "Russia", "Vladivostok",
                    new DateTime(2023, 7, 5), new DateTime(2023, 7, 10),
                    "Robert Schumann", "Delivered"),
            new Order(10252, "Manjimup Dried Apples", "Peru", "Lima",
                    new DateTime(2023, 7, 9), new DateTime(2023, 7, 11),
                    "Yang Wang", "Delivered"),
            new Order(10254, "Wimmers gute Semmelknodel", "Indonesia", "Jakarta",
                    new DateTime(2023, 7, 11), new DateTime(2023, 7, 23),
                    "Shelley Burke", "In Transit")
        };

        BandInfo childBandInfoAddress = new BandInfo(ShippingAddressBandName, "Address", null);
        BandInfo childBandInfoStatus = new BandInfo(ShippingStatusBandName, "Status", null);

        BandInfos = new ObservableCollection<BandInfo>
        {
            new BandInfo(OrderBandName, "Order", null),
            new BandInfo("ShippingInfo", "Shipping Info", new List<BandInfo>{ childBandInfoAddress, childBandInfoStatus })
        };
    }
}

public class BandInfo
{
    public BandInfo(string name, string displayName, IList<BandInfo> childBands)
    {
        this.Name = name;
        this.DisplayName = displayName;
        this.ChildBands = childBands;
    }
    public string Name { get; set; }
    public string DisplayName { get; set; }
    public IList<BandInfo> ChildBands { get; set; }
}

public partial class Order : ObservableObject
{
    [ObservableProperty][property: Display(Order = 0)]
    private int orderId;

    [ObservableProperty][property: Display(Order = 1)]
    private string productName = string.Empty;

    [ObservableProperty][property: Display(Order = 4)]
    private DateTime orderDate;

    [ObservableProperty][property: Display(Order = 5)]
    private string customerName = string.Empty;

    [ObservableProperty][property: Display(Order = 23)]
    private DateTime shippedDate;

    [ObservableProperty][property: Display(Order = 20)]
    private string shipCountry = string.Empty;

    [ObservableProperty][property: Display(Order = 21)]
    private string shipCity = string.Empty;

    [ObservableProperty][property: Display(Order = 24)]
    private string shippingStatus = string.Empty;

    public Order(int orderId, string productName, 
                string shipCountry, string shipCity, DateTime orderDate, DateTime shippedDate,
                string customerName, string shipStatus)
    {
        OrderId = orderId; ProductName = productName;
        ShipCountry = shipCountry; ShipCity = shipCity;
        OrderDate = orderDate; ShippedDate = shippedDate;
        CustomerName = customerName; ShippingStatus = shipStatus;
    }
}
```

### Инициализация групп с помощью стиля

В качестве альтернативы указанию свойства `BandTemplate` вы можете использовать свойство `Styles`, чтобы инициализировать объекты `GridBand` из бизнес-объектов. 

``` xml
<mxdg:DataGridControl.Styles>
    <Style Selector="mxdg|GridBand">
        <Setter Property="BandName" Value="{Binding Name}"/>
        <Setter Property="Header" Value="{Binding DisplayName}"/>
        <Setter Property="HeaderHorizontalAlignment" Value="Left"/>
    </Style>
</mxdg:DataGridControl.Styles>
```

Пример использования свойств `BandsSource` и `Styles` смотрите в демонстрации «Column Bands».

## Создание групп на основе атрибутов DataAnnotation (для автоматически создаваемых колонок)

Этот подход позволяет использовать атрибуты для связывания [автоматически создаваемых колонок](columns.md#automatic-column-generation) с группами. 

Когда включена автоматическая генерация колонок (смотрите [DataGridControl.AutoGenerateColumns](columns.md#automatic-column-generation)), DataGrid может инициализировать настройки колонок на основе [специальных атрибутов](columns.md#use-attributes-to-customize-settings-of-auto-generated-columns), применённых к свойствам бизнес-объекта. 
Атрибут `System.ComponentModel.DataAnnotations.DisplayAttribute` позволяет связывать автоматически создаваемые колонки с группами. Укажите параметр `DisplayAttribute.GroupName`, чтобы задать имя группы для соответствующей колонки.

``` cs
public partial class Order : ObservableObject
{
    [ObservableProperty]
    [property: Display(Order = 0, GroupName = "Order")]
    private int orderId;
    //...
}
```

Когда DataGrid встречает `DisplayAttribute.GroupName`, он проверяет наличие существующей группы с совпадающим именем (`GridBand.BandName`). Если такая группа не найдена, она создаётся и инициализируется следующим образом:

- Контрол автоматически создаёт группу и присваивает её свойству `GridBand.BandName` значение `DisplayAttribute.GroupName`.
- Группа добавляется в коллекцию `DataGridControl.Bands` контрола. Вложенные группы добавляются в соответствующие коллекции `GridBand.Bands`.
- Созданная группа связывается с автоматически созданной колонкой с помощью свойства `GridColumn.BandName`.

Параметр `DisplayAttribute.GroupName` поддерживает вложенные группы. Используйте символ '/' для разделения родительской и дочерней группы (например, «ParentBandName/ChildBandName»). Чтобы использовать '/' как обычный символ, применяйте двойной слэш ("//").

!!! note

    Имена отдельных дочерних групп должны быть уникальными в пределах всего DataGrid.

``` cs
public partial class Order : ObservableObject
{
    [ObservableProperty]
    [property: Display(Order = 20, GroupName = "Shipping Info/Address")]
    private string shipCountry = string.Empty;
    //...
}
```

### Связанный API

- `DataGridControl.AutoGenerateBands` (значение по умолчанию — `true`) — определяет, создаются ли группы автоматически на основе атрибутов `DisplayAttribute.GroupName`, применённых к свойствам исходного бизнес-объекта. Такие группы автоматически связываются с соответствующими автоматически создаваемыми колонками.

    Автоматическое создание групп (и их связывание с автоматически создаваемыми колонками) принудительно отключается, если `DataGridControl.AutoGenerateColumns` имеет значение `false`.
    
- `DataGridControl.Bands` и `GridBand.Bands` — эти коллекции позволяют получить доступ к автоматически созданным группам.

### Пример - Создание групп на основе параметра DisplayAttribute.GroupName

В этом примере DataGrid отображает список объектов _Order_. Опция `AutoGenerateColumns` включает автоматическое создание колонок на основе публичных свойств класса _Order_. Группы создаются на основе атрибута `System.ComponentModel.DataAnnotations.DisplayAttribute`, применённого к свойствам класса _Order_.

![datagrid-bands-from-attributes-example](../../images/datagrid-bands-from-attributes-example.png)

Параметр `DisplayAttribute.GroupName` определяет имена групп для автоматически создаваемых колонок.

``` xml
<!-- MainWindow.axaml -->
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:DataGridBandsFromAttributes.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="DataGridBandsFromAttributes.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="DataGridBandsFromAttributes">

    <Design.DataContext>
        <!-- This only sets the DataContext for the previewer in an IDE,
             to set the actual DataContext for runtime, set the DataContext property in code (look at App.axaml.cs) -->
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <Grid RowDefinitions="Auto" ColumnDefinitions="Auto" >
        <Border BorderThickness="1" BorderBrush="LightGray" Margin="10">
            <mxdg:DataGridControl Name="dataGrid1"
                                  ItemsSource="{Binding Orders}"
                                  AutoGenerateColumns="True"
                          >
                <mxdg:DataGridControl.Styles>
                    <Style Selector="mxdg|GridBand">
                        <Setter Property="HeaderHorizontalAlignment" Value="Center"/>
                    </Style>
                </mxdg:DataGridControl.Styles>
            </mxdg:DataGridControl>
        </Border>
    </Grid>
</mx:MxWindow>
```

``` cs
// MainWindowViewModel.cs
using CommunityToolkit.Mvvm.ComponentModel;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel.DataAnnotations;

namespace DataGridBandsFromAttributes.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    [ObservableProperty]
    private ObservableCollection<Order> orders;

    public MainWindowViewModel()
    {
        Orders = new ObservableCollection<Order>
        {
            new(10424, "Brazilian Coffee Beans", "Brazil", "Sao Paulo",
                new DateTime(2023, 9, 16), new DateTime(2023, 9, 25),
                "Carlos Silva", "Delivered"),

            new(10425, "Thai Silk Cushions", "Thailand", "Bangkok",
                new DateTime(2023, 9, 17), new DateTime(2023, 9, 26),
                "Somsak Chai", "Shipped")
        };
    }
}


public partial class Order : ObservableObject
{
    [ObservableProperty][property: Display(Order = 0, GroupName = "Details")]
    private int orderId;

    [ObservableProperty][property: Display(Order = 1, GroupName = "Details")]
    private string productName = string.Empty;

    [ObservableProperty][property: Display(Order = 4, GroupName = "Details")]
    private DateTime orderDate;

    [ObservableProperty][property: Display(Order = 5, GroupName = "Customer")]
    private string customerName = string.Empty;

    [ObservableProperty][property: Display(Order = 23, GroupName ="Shipping Information/Status")]
    private DateTime shippedDate;

    [ObservableProperty][property: Display(Order = 20, GroupName = "Shipping Information/Address")]
    private string shipCountry = string.Empty;

    [ObservableProperty][property: Display(Order = 21, GroupName = "Shipping Information/Address")]
    private string shipCity = string.Empty;

    [ObservableProperty][property: Display(Order = 24, GroupName = "Shipping Information/Status")]
    private string shippingStatus = string.Empty;

    public Order(int orderId, string productName, 
                string shipCountry, string shipCity, DateTime orderDate, DateTime shippedDate,
                string customerName, string shipStatus)
    {
        OrderId = orderId; ProductName = productName;
        ShipCountry = shipCountry; ShipCity = shipCity;
        OrderDate = orderDate; ShippedDate = shippedDate;
        CustomerName = customerName; ShippingStatus = shipStatus;
    }
}
```

### Порядок колонок и групп

DataGrid располагает колонки в соответствии со значениями свойства `GridColumn.VisibleIndex`.

Порядок заголовков групп определяется визуальным порядком колонок. 
Если колонки, связанные с одной и той же группой, расположены рядом друг с другом, их заголовки групп объединяются.

``` xml
<mxdg:DataGridControl.Columns>
    <mxdg:GridColumn Width="*" FieldName="FirstName" BandName="Customer"/>
    <mxdg:GridColumn Width="*" FieldName="LastName" BandName="Customer"/>
    <mxdg:GridColumn Width="*" FieldName="Address" BandName="Details"/>
</mxdg:DataGridControl.Columns>
```
![datagrid-bands-merged-band-header](../../images/datagrid-bands-merged-band-header.png)


Контрол не переупорядочивает колонки автоматически, чтобы сгруппировать их по группам. 
Если колонки, связанные с одной группой, расположены не рядом друг с другом (разделены колонками, связанными с другими группами), DataGrid создаёт несколько заголовков группы с одинаковым именем над заголовками колонок.

В следующем фрагменте кода колонки, связанные с группой _Customer_, разделены колонкой _Address_, который связан с группой _Details_. Контрол не переупорядочивает колонки автоматически, чтобы объединить их в одну группу _Customer_:

``` xml
<mxdg:DataGridControl.Columns>
    <mxdg:GridColumn Width="*" FieldName="FirstName" BandName="Customer"/>
    <mxdg:GridColumn Width="*" FieldName="LastName" BandName="Customer"/>
    <mxdg:GridColumn Width="*" FieldName="Address" BandName="Details"/>
    <mxdg:GridColumn Width="*" FieldName="Title" BandName="Customer"/>
</mxdg:DataGridControl.Columns>
```

![datagrid-bands-not-keep-columns-together](../../images/datagrid-bands-not-keep-columns-together.png)


## Операции перетаскивания

### Перетаскивание колонок

Пользователи могут свободно перетаскивать колонки в пределах контрола, если свойство `DataGridControl.AllowColumnMoving` имеет значение `true` (по умолчанию). Если пользователь перетаскивает колонку в другую группу, контрол отображает соответствующий заголовок группы (`GridColumn.BandHeader`) над этой колонкой на новой позиции. Смотрите [Порядок колонок и групп](#порядок-колонок-и-групп).

#### Связанный API

- `DataGridControl.AllowColumnMoving` — определяет, разрешены ли операции перетаскивания колонок.

### Перетаскивание групп

DataGrid не поддерживает операции перетаскивания для групп.

## Отображение и скрытие панели групп

Панель групп отображает заголовки групп. Панель видима, если хотя бы одна колонка связана с существующей группой. Используйте следующее свойство, чтобы принудительно скрыть панель групп, если это необходимо:

- `DataGridControl.ShowBands` — определяет, видима ли панель групп.

## Указание содержимого заголовка группы

- `Header` — задаёт содержимое заголовка группы. Если это свойство не задано, группа отображает значение свойства `GridBand.BandName`.
- `HeaderTemplate` — задаёт шаблон, используемый для отрисовки объекта `Header`. Шаблон позволяет отображать изображения и пользовательские контролы, а также произвольно оформлять текст.

### Пример - Отображение изображения в заголовке группы

В следующем примере в заголовке группы отображается SVG-изображение, за которым следует текстовая подпись. SVG-изображение (файл `customer.svg`) находится в папке `Assets` проекта, а его свойство `Build Action` установлено в значение `AvaloniaResource`.

![grid-bandheader-ImageAndText](../../images/grid-bandheader-ImageAndText.png)

``` xml
xmlns:svg="using:Avalonia.Svg.Skia"

<mxdg:DataGridControl.Bands>
    <mxdg:GridBand BandName="Customer" HeaderHorizontalAlignment="Center">
        <mxdg:GridBand.HeaderTemplate>
            <DataTemplate>
                <StackPanel Orientation="Horizontal">
                    <svg:Svg Path="/Assets/customer.svg" Width="16" Height="16" Margin="5" />
                    <TextBlock Text="{Binding}" VerticalAlignment="Center"/>
                </StackPanel>
            </DataTemplate>
        </mxdg:GridBand.HeaderTemplate>
</mxdg:DataGridControl.Bands>
```

## Пустой заголовок группы

Колонки, не связанные с существующими группами, отображаются под пустым заголовком группы.

``` xml
<mxdg:DataGridControl.Columns>
    <mxdg:GridColumn Width="*" FieldName="Address" BandName="Details"/>
    <mxdg:GridColumn Width="*" FieldName="City" BandName="Details"/>
    <mxdg:GridColumn Width="*" FieldName="Title"/>
</mxdg:DataGridControl.Columns>    
```

![datagrid-bands-blank-band](../../images/datagrid-bands-blank-band.png)


## Разделители групп

- `DataGridControl.ShowBandSeparators` — включает толстые разделители между соседними группами. Используйте это свойство, чтобы визуально выделить границы между группами. Если `ShowBandSeparators` отключено, таблица отображает обычные разделители колонок (тонкие линии) между группами.

    Следующее изображение демонстрирует разделители групп.

    ![datagrid-band-separators](../../images/datagrid-band-separators.png)

## Скрытие групп

Объекты группы не имеют свойства 'Visible'. Чтобы скрыть группу, необходимо скрыть колонки, связанные с этой группой.

Группы, не имеющие связанных колонок, никогда не отображаются.



## Всплывающие подсказки заголовков групп

Используйте свойство `HeaderToolTip`, чтобы задать пользовательские подсказки для заголовков групп. Пользовательские подсказки отображаются при наведении на заголовок группы независимо от того, обрезан текст заголовка или нет.

``` xml
<mxdg:GridBand BandName="Details" HeaderHorizontalAlignment="Center" HeaderToolTip="Contact and location information">
```

![grid-band-headertooltip](../../images/grid-band-headertooltip.png)

Если пользовательская подсказка не назначена группе, для заголовка группы отображается стандартная подсказка в случае, если текст заголовка обрезан. Стандартная подсказка отображает полный, неусечённый текст заголовка.

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
