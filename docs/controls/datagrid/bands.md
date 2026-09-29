---
title: Bands
order: 75000
seealso: []
---

# Bands

You can use bands to visually combine columns together. The DataGrid control displays bands as additional headers above the column headers. Both band and column headers can contain text, images, or custom content. You can also create hierarchical bands with an unlimited number of nesting levels.

The following image shows a DataGrid control with four bands: 'Customer', 'Details', 'Address', and 'Contact':

![datagrid-bands](../../images/datagrid-bands.png)

The following approaches allow you to generate column bands:

- [Create bands manually](#create-bands-manually)
- [Create bands from a band source](#generate-bands-from-a-band-source)
- [Create bands based on DataAnnotation attributes (for auto-generated columns)](#generate-bands-based-on-dataannotation-attributes-for-auto-generated-columns)


## Create Bands Manually

Follow these steps to manually create bands:

1. Create band objects (`GridBand` class instances) and add them to the `DataGridControl.Bands` collection. 

    Assign unique band names to the created bands using the `GridBand.BandName` property.

    ``` xml
    <mxdg:DataGridControl.Bands>
        <mxdg:GridBand BandName="Customer" HeaderHorizontalAlignment="Center"/>
        <mxdg:GridBand BandName="Details" HeaderHorizontalAlignment="Center"/>
    </mxdg:DataGridControl.Bands>
    ```

    You can create a hierarchical band structure. To create nested bands:
        
    - In code-behind: Add bands to the `GridBand.Bands` collection.
    - In XAML: Define nested bands directly between the opening and closing `GridBand` tags.

    ``` xml
    <mxdg:GridBand BandName="Details" HeaderHorizontalAlignment="Center">
        <mxdg:GridBand BandName="DetailsAddress" Header="Address" HeaderHorizontalAlignment="Center"/>
        <mxdg:GridBand BandName="DetailsContact" Header="Contact" HeaderHorizontalAlignment="Center"/>
    </mxdg:GridBand>
    ```

    The `GridBand.Header` property allows you to specify custom content (for example, custom text) for a band. If this property is not set, the band header displays the `GridBand.BandName` property's value.

2. Associate columns with specific bands by setting each column's `GridColumn.BandName` property to the corresponding band name (`GridBand.BandName`).

    ``` xml
    <mxdg:DataGridControl.Columns>
        <mxdg:GridColumn FieldName="FirstName" BandName="Customer" Width="*"/>
        <mxdg:GridColumn FieldName="City" BandName="DetailsAddress" Width="*"/>
        <mxdg:GridColumn FieldName="Phone" BandName="DetailsContact" Width="*"/>
        <!-- ... -->
    </mxdg:DataGridControl.Columns>
    ```

Columns are arranged in the DataGrid control according to their `GridColumn.VisibleIndex` properties.
The control does not automatically rearrange columns to group them by bands.

![datagrid-bands-not-keep-columns-together](../../images/datagrid-bands-not-keep-columns-together.png)

See [Order of Columns and Bands](#order-of-columns-and-bands)




### Related API

- `GridBand` class — Encapsulates a column band.
- `GridBand.BandName` — A unique name used to identify a band and associate it with columns.
- `GridColumn.BandName` — The name of the band associated with the column. This value matches the `GridBand.BandName` property's value.
- `DataGridControl.Bands` — A collection of root bands.
- `GridBand.Bands` — A collection of child bands for this band.


### Example - Manually create column bands in a DataGrid control

The following example creates bands and assigns them to columns, as demonstrated in the image below:

![datagrid-bands-example](../../images/datagrid-bands-example.png)

- The "Customer", "Address", and "Contact" bands are associated with grid columns. 
- The "Details" band owns two nested bands ("Address" and "Contact"). This band is not directly associated with columns.

Each band is assigned a unique name using the `GridBand.BandName` property. To link columns to a specific band, set the column's `GridColumn.BandName` property to the target band's `BandName` value.

The `DataGridControl.Bands` property defines the structure of bands. To create nested bands, define them as children of a parent band.

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

## Generate Bands from a Band Source

You can populate column bands from a band source defined in a View Model. Use the `DataGridControl.BandsSource` and `DataGridControl.BandTemplate` properties to generate bands from a collection of business objects. 

As an alternative to specifying the `BandTemplate` property, you can use the `Styles` property to initialize `GridBand` objects from business objects. See [Initialize Bands Using a Style](#initialize-bands-using-a-style) for an example.

To associate columns with bands, set each column's `GridColumn.BandName` to the corresponding band name (`GridBand.BandName`).

### Related API

- `DataGridControl.BandsSource` — A collection of business objects used to generate root bands.
- `DataGridControl.BandTemplate` — A template that creates `GridBand` instances from business objects.
- `GridBand.BandsSource` — A collection of business objects used to generate child bands.
- `GridBand.BandName` — A unique name used to identify a band and associate it with columns.
- `GridColumn.BandName` — The name of the band associated with the column. This value matches the `GridBand.BandName` property's value.

### Example - Generate bands from a band source

The following example creates bands from a collection of _BandInfo_ objects defined in a View Model.

The DataGrid control displays a collection of _Order_ business objects. Grid columns are automatically generated from the public properties exposed by the _Order_ class. The data grid's `AutoGeneratingColumn` event handler associates the generated columns with the appropriate bands.

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

### Initialize Bands Using a Style

As an alternative to specifying the `BandTemplate` property, you can use the `Styles` property to initialize `GridBand` objects from business objects. 

``` xml
<mxdg:DataGridControl.Styles>
    <Style Selector="mxdg|GridBand">
        <Setter Property="BandName" Value="{Binding Name}"/>
        <Setter Property="Header" Value="{Binding DisplayName}"/>
        <Setter Property="HeaderHorizontalAlignment" Value="Left"/>
    </Style>
</mxdg:DataGridControl.Styles>
```

See the "Column Bands" demo for an example of using the `BandsSource` and `Styles` properties.

## Generate Bands Based on DataAnnotation Attributes (for Auto-Generated Columns)

This approach allows you to use attributes to associate [auto-generated columns](columns.md#automatic-column-generation) with bands. 

When column auto-generation is enabled (see [DataGridControl.AutoGenerateColumns](columns.md#automatic-column-generation)), Data Grid control can initialize column settings from [dedicated attributes](columns.md#use-attributes-to-customize-settings-of-auto-generated-columns) applied to a business object's properties. 
The `System.ComponentModel.DataAnnotations.DisplayAttribute` attribute allows you to associate auto-generated columns with bands. Specify the `DisplayAttribute.GroupName` parameter to define the band name for the corresponding column.

``` cs
public partial class Order : ObservableObject
{
    [ObservableProperty]
    [property: Display(Order = 0, GroupName = "Order")]
    private int orderId;
    //...
}
```

When Data Grid encounters `DisplayAttribute.GroupName`, it checks for an existing band with a matching name (`GridBand.BandName`). If no such band is found, the band is created and initialized as follows:

- The control automatically creates the band and set its `GridBand.BandName` property to the `DisplayAttribute.GroupName` value.
- The band is added to the control's `DataGridControl.Bands` collection. Nested bands are added to the appropriate `GridBand.Bands` collections.
- The created band is associated with the auto-generated column, using the `GridColumn.BandName` property.

The `DisplayAttribute.GroupName` parameter supports nested bands. Use the '/' character to separate parent and child bands (for instance, "ParentBandName/ChildBandName"). To include '/' as a literal character, use the double slash ("//") notation.

!!! note

    Individual child band names must be unique throughout the DataGrid control.

``` cs
public partial class Order : ObservableObject
{
    [ObservableProperty]
    [property: Display(Order = 20, GroupName = "Shipping Info/Address")]
    private string shipCountry = string.Empty;
    //...
}
```

### Related API

- `DataGridControl.AutoGenerateBands` (default is `true`) — Gets or sets whether bands are automatically generated from the `DisplayAttribute.GroupName` attributes applied to the underlying business object's properties. These bands are then automatically linked to their corresponding auto-generated columns.

    Automatic band generation (and linking bands to auto-generated columns) is forcibly disabled if `DataGridControl.AutoGenerateColumns` is `false`.
    
- `DataGridControl.Bands` and `GridBand.Bands` — You can use these collections to access automatically generated bands.

### Example - Generate bands based on the DisplayAttribute.GroupName parameter

In this example, the DataGrid control displays a list of _Order_ objects. The `AutoGenerateColumns` option enables automatic generation of columns from the public properties of the _Order_ class. Bands are generated based on the `System.ComponentModel.DataAnnotations.DisplayAttribute` attribute applied to the _Order_ class properties.

![datagrid-bands-from-attributes-example](../../images/datagrid-bands-from-attributes-example.png)

The `DisplayAttribute.GroupName` parameter defines band names for the auto-generated columns.

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

### Order of Columns and Bands

The DataGrid control arranges columns according to their `GridColumn.VisibleIndex` properties.

The order of band headers is determined by the visual order of the columns. 
If columns linked to the same band are placed next to each other, their band headers are merged.

``` xml
<mxdg:DataGridControl.Columns>
    <mxdg:GridColumn Width="*" FieldName="FirstName" BandName="Customer"/>
    <mxdg:GridColumn Width="*" FieldName="LastName" BandName="Customer"/>
    <mxdg:GridColumn Width="*" FieldName="Address" BandName="Details"/>
</mxdg:DataGridControl.Columns>
```
![datagrid-bands-merged-band-header](../../images/datagrid-bands-merged-band-header.png)


The control does not automatically rearrange columns to group them by bands. 
If columns linked to the same band are placed in non-adjacent positions (separated by columns linked to a different band(s)), the DataGrid control creates multiple band headers with the same name above the column headers.

In the following code snippet, columns linked to the _Customer_ band are separated by the _Address_ column, which is linked to the _Details_ band. The control does not automatically reorder the columns to combine them into a single _Customer_ band:

``` xml
<mxdg:DataGridControl.Columns>
    <mxdg:GridColumn Width="*" FieldName="FirstName" BandName="Customer"/>
    <mxdg:GridColumn Width="*" FieldName="LastName" BandName="Customer"/>
    <mxdg:GridColumn Width="*" FieldName="Address" BandName="Details"/>
    <mxdg:GridColumn Width="*" FieldName="Title" BandName="Customer"/>
</mxdg:DataGridControl.Columns>
```

![datagrid-bands-not-keep-columns-together](../../images/datagrid-bands-not-keep-columns-together.png)


## Drag-and-Drop Operations

### Column Drag-and-Drop

Users can freely drag and drop columns within the control if `DataGridControl.AllowColumnMoving` is `true` (default). If they drag a column into a different band, the control draws an appropriate band header (`GridColumn.BandHeader`) above this column in its new position. See [Order of Columns and Bands](#order-of-columns-and-bands).

#### Related API

- `DataGridControl.AllowColumnMoving` — Gets or sets whether column drag-and-drop operations are enabled.

### Band Drag-and-Drop

DataGrid does not support drag-and-drop operations on bands.

## Show and Hide the Band Panel

The band panel displays band headers. The panel is visible when any column is associated with an existing band. Use the following property to forcibly hide the band panel, when required:

- `DataGridControl.ShowBands` — Gets or sets whether the band panel is visible.

## Specify Band Header Content

- `Header` — Gets or sets a band header's content. If this property is not set, the band displays the value of the `GridBand.BandName` property.
- `HeaderTemplate` —  Gets or sets a template used to render the `Header` object. The template allows you to display images and custom controls, and to render text in a custom manner.

### Example - Display an image in a band header

The following example displays an SVG image followed by a text caption in a band header. The SVG image (`customer.svg` file) is located in the project's `Assets` folder, with its `Build Action` property set to `AvaloniaResource`.

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

## Blank Band Header

Columns not associated with existing bands are displayed under a blank band header.

``` xml
<mxdg:DataGridControl.Columns>
    <mxdg:GridColumn Width="*" FieldName="Address" BandName="Details"/>
    <mxdg:GridColumn Width="*" FieldName="City" BandName="Details"/>
    <mxdg:GridColumn Width="*" FieldName="Title"/>
</mxdg:DataGridControl.Columns>    
```

![datagrid-bands-blank-band](../../images/datagrid-bands-blank-band.png)


## Band Separators

- `DataGridControl.ShowBandSeparators` — Enables thick separators between adjacent bands. Use this property to emphasize divisions between bands. If `ShowBandSeparators` is disabled, the grid draws regular column separators (thin lines) between bands.

    The following image demonstrates band separators.

    ![datagrid-band-separators](../../images/datagrid-band-separators.png)

## Hide Bands

Band objects do not have a 'Visible' property. To hide a band, you should hide columns linked to this band.

Bands without associated columns are never displayed.



## Band Header Tooltips

Use the `HeaderToolTip` property to specify custom tooltips for band headers. Custom tooltips are displayed when hovering over band headers regardless of whether band header text is trimmed or not.

``` xml
<mxdg:GridBand BandName="Details" HeaderHorizontalAlignment="Center" HeaderToolTip="Contact and location information">
```

![grid-band-headertooltip](../../images/grid-band-headertooltip.png)

When no custom tooltip is assigned to a band, the default tooltip is shown for the band header in case the header text is trimmed. The default tooltip displays the full, untrimmed header text.

