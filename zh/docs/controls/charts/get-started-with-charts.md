---
title: 开始使用图表
order: 10000
seealso: []
---

# 开始使用图表

本教程介绍如何使用条形图和折线图系列视图在 `CartesianChart` 控件中显示三个数据系列。

![charts-get-started](../../images/charts-get-started.png)

首先，我们将为图表控件定义数据（在视图模型对象中），然后将图表控件绑定到该数据。

接下来，我们将定义和自定义默认轴，并展示如何添加额外的 _X_ 轴，并将其与特定系列关联。

## 为系列定义视图模型

首先为单个系列创建视图模型。

``` cs
using Eremex.AvaloniaUI.Charts;

public partial class SeriesViewModel : ObservableObject
{
    [ObservableProperty] Color color;
    [ObservableProperty] ISeriesDataAdapter dataAdapter;
}
```

_SeriesViewModel_ 类公开两个属性，用于指定系列的颜色和数据。

系列图表的数据是使用_Data Adapter_ 对象提供的。 
Eremex 图表支持用于各种数据类型（数字、日期时间和定性）的多个数据适配器。在本教程中，我们将使用两个数据适配器：

- `SortedNumericDataAdapter` — 供应按 _X_ 值排序的（数字 _X_、数字 _Y_）对。
- `SortedDateTimeDataAdapter` — 提供按 _X_ 值排序的（日期时间 _X_、数字 _Y_）对。

这些数据适配器在主视图模型中初始化。

有关其他数据适配器的信息，请参阅 [Cartesian Chart](cartesian-chart.md)。

## 定义主视图模型

创建 _MainWindowViewModel_ 类，封装窗口的主视图模型。 _MainWindowViewModel_ 实例将设置为窗口（和图表控件）的 `DataContext`。

将三个 _SeriesViewModel_ 属性添加到 _MainWindowViewModel_ 类。它们描述了目标图表控件中的三个数据系列。

``` cs
public partial class MainWindowViewModel : ViewModelBase
{
    [ObservableProperty] SeriesViewModel barSeries1; 
    [ObservableProperty] SeriesViewModel barSeries2; 
    [ObservableProperty] SeriesViewModel lineSeries;
}
```

在视图模型的构造函数中初始化这些对象，并指定该系列的颜色和数据适配器。

``` cs
public partial class MainWindowViewModel : ViewModelBase
{
    public MainWindowViewModel()
    {
        //Init data
        var random = new Random(4);
        var random2 = new Random(0);

        var startDate = new DateTime(DateTime.Now.Year, 1, 1);
        SortedDateTimeDataAdapter barSeries1DataAdapter = new();
        SortedDateTimeDataAdapter barSeries2DataAdapter = new();
        SortedNumericDataAdapter lineSeriesDataAdapter = new();
        for (int i = 0; i < 12; i++)
        {
            var argument = startDate.AddMonths(i);
            barSeries1DataAdapter.Add(argument, random.NextDouble() * 100 - 30);
            barSeries2DataAdapter.Add(argument, random.NextDouble() * 100 - 30);
        }
        double startValue = 20;
        for (int i = 0; i < 365; i++)
        {
            var argument = i;
            var value = startValue + (random2.NextDouble() - 0.5) * 10;
            lineSeriesDataAdapter.Add(argument, value);
            startValue = value;
        }
        // Create data series
        BarSeries1 = new() { Color = Color.FromArgb(255, 0, 120, 122), DataAdapter = barSeries1DataAdapter };
        BarSeries2 = new() { Color = Color.FromArgb(255, 0, 170, 110), DataAdapter = barSeries2DataAdapter };
        LineSeries = new() { Color = Color.FromArgb(255, 120, 10, 12), DataAdapter = lineSeriesDataAdapter };
    }

    [ObservableProperty] SeriesViewModel barSeries1; 
    [ObservableProperty] SeriesViewModel barSeries2; 
    [ObservableProperty] SeriesViewModel lineSeries;
}
```

数据适配器填充随机数据：

- `SortedDateTimeDataAdapter` 对象填充了 12 个点，对应于一年中的 12 个月。 `SortedDateTimeDataAdapter` 对象的 _X_ 值是 `DateTime` 值。

- `SortedNumericDataAdapter` 对象填充了与一年中的日期相对应的 365 个点。 `SortedNumericDataAdapter` 对象的 _X_ 值是数值。


## 创建Cartesian Chart控件

确保窗口和图表控件的 DataContext 设置为 _MainWindowViewModel_ 对象。


打开 MainWindow 的 XAML 文件，定义一个包含两个系列的 `CartersianChart` 控件，如下所示：

``` xml
xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"             

<mxc:CartesianChart>
    <mxc:CartesianChart.Series>
        <mxc:CartesianSeries Name="barSeries1" DataAdapter="{Binding BarSeries1.DataAdapter}" >
        </mxc:CartesianSeries>

        <mxc:CartesianSeries Name="barSeries2" DataAdapter="{Binding BarSeries2.DataAdapter}" >
        </mxc:CartesianSeries>
    </mxc:CartesianChart.Series>
</mxc:CartesianChart>
```

此代码将两个系列（`CartesianSeries` 对象）添加到 `CartesianChart.Series` 集合中，并将它们绑定到主视图模型中相应的数据适配器。

### 指定系列视图

**系列视图**决定系列的视觉外观和设置。 Cartesian Chart 支持多种系列视图：线、散点线、范围区域、条形图、范围条形图等。有关详细信息，请参阅以下主题：[Cartesian Chart](cartesian-chart.md)。

让我们将 Bar 系列视图应用于该系列。为此，将 `CartesianSideBySideBarSeriesView` 对象定义为 `CartesianSeries` 对象的内容。

``` xml
<mxc:CartesianChart>
    <mxc:CartesianChart.Series>
        <mxc:CartesianSeries Name="barSeries1" DataAdapter="{Binding BarSeries1.DataAdapter}" >
            <mxc:CartesianSideBySideBarSeriesView Color="{Binding BarSeries1.Color}" />
        </mxc:CartesianSeries>
        <mxc:CartesianSeries Name="barSeries2" DataAdapter="{Binding BarSeries2.DataAdapter}" >
            <mxc:CartesianSideBySideBarSeriesView Color="{Binding BarSeries2.Color}" />
        </mxc:CartesianSeries>
    </mxc:CartesianChart.Series>
</mxc:CartesianChart>
```

`CartesianSideBySideBarSeriesView` 将点渲染为矩形条：

![chart-CartesianSideBySideBarSeriesView-oneseries](../../images/chart-CartesianSideBySideBarSeriesView-oneseries.png)

系列视图的 `Color` 设置允许您指定渲染相关系列所使用的颜色。


## 创建和自定义默认轴

Cartesian Chart 可以自动为底层数据创建轴。如果您想要自定义轴设置（例如，指定标题和比例选项），您可能需要手动定义 _X_ 和 _Y_ 轴。

要定义轴，请将 `AxisX` 和/或 `AxisY` 对象添加到 `CartesianChart.AxesX`/`CartesianChart.AxesY` 集合：

``` xml
<mxc:CartesianChart>
    <!-- ... -->
    <mxc:CartesianChart.AxesX>
        <mxc:AxisX Name="salesAxis" Title="Sales">
            <mxc:AxisX.ScaleOptions>
                <mxc:DateTimeScaleOptions MeasureUnit="Month" />
            </mxc:AxisX.ScaleOptions>
        </mxc:AxisX>
    </mxc:CartesianChart.AxesX>

    <mxc:CartesianChart.AxesY>
        <mxc:AxisY Title="Currency"/>
    </mxc:CartesianChart.AxesY>
</mxc:CartesianChart>
```

上面的代码创建 _X_ 和 _Y_ 轴，并为其指定标题。

由于底层数据点表示各个月份的值，因此 `Month` 时间单位应用于水平日期时间轴（使用 `AxisX.ScaleOptions` 属性）。

如果您现在运行该应用程序，您将看到以下结果：

![charts-get-started-two-series](../../images/charts-get-started-two-series.png)


## 添加附加系列和 _X_ 轴

您可以根据需要向图表控件添加任意数量的系列。这些系列可以使用默认轴或它们自己的轴。

让我们向图表中添加一个线系列及其轴。

首先，在 `CartesianChart.Series` 集合中创建一个新的 `CartesianSeries` 对象，并将其绑定到视图模型中定义的 _LineSeries.DataAdapter_ 对象。

``` xml
<mxc:CartesianChart>
    <mxc:CartesianChart.Series>
        <!-- ... -->
        <mxc:CartesianSeries Name="lineSeries" DataAdapter="{Binding LineSeries.DataAdapter}" >
        </mxc:CartesianSeries> 
    </mxc:CartesianChart.Series>
</mxc:CartesianChart>
```

### 指定线系列视图

要将线系列视图应用于该系列，请将 `CartesianLineSeriesView` 对象定义为该系列的内容：

``` xml
<mxc:CartesianSeries Name="lineSeries" DataAdapter="{Binding LineSeries.DataAdapter}" >
    <mxc:CartesianLineSeriesView Color="{Binding LineSeries.Color}" />
</mxc:CartesianSeries> 
```

`CartesianLineSeriesView` 是点与线连接的系列视图：

![chart-CartesianLineSeriesView-one-series](../../images/chart-CartesianLineSeriesView-one-series.png)

与任何系列视图一样，您可以使用 `CartesianLineSeriesView.Color` 属性来指定用于绘制系列的颜色。

### 为线系列指定自己的轴

Line系列的_X_值是数字类型，而现有横轴显示的是`DateTime`值。因此，Line 系列需要一个额外的数字轴。

在 `CartesianChart.AxesX` 集合中定义一个新的数字 _X_ 轴。

``` xml
<mxc:CartesianChart.AxesX>
    <!-- ... -->
    <mxc:AxisX Position="Far" Title="Expenses">
        <mxc:AxisX.ScaleOptions>
            <mxc:NumericScaleOptions />
        </mxc:AxisX.ScaleOptions>
    </mxc:AxisX>
</mxc:CartesianChart.AxesX>
```


轴的 `Position` 属性设置为 `Far` 以在与默认位置相对的边缘处显示轴。对于水平轴，`Far` 选项对应于图表的顶部边缘。对于垂直轴，`Far` 选项将轴放置在图表的右边缘。

现在我们需要将 Line 系列与其轴关联。这是通过指定轴 ID（唯一的字符串值）来完成的。将轴的 `Key` 属性和系列的 `CartesianSeries.AxisXKey`/`CartesianSeries.AxisYKey` 属性设置为相同的 ID。

在本教程中，指定系列和轴的 _“lineSeriesAxis”_ ID，如下所示：

``` xml
<mxc:CartesianSeries Name="lineSeries" DataAdapter="{Binding LineSeries.DataAdapter}"  
  AxisXKey="lineSeriesAxis">
    <mxc:CartesianLineSeriesView Color="{Binding LineSeries.Color}" />
</mxc:CartesianSeries>

<mxc:CartesianChart.AxesX>
    <!-- ... -->
    <mxc:AxisX Position="Far" Title="Expenses"
       Key="lineSeriesAxis">
        <mxc:AxisX.ScaleOptions>
            <mxc:NumericScaleOptions />
        </mxc:AxisX.ScaleOptions>
    </mxc:AxisX>
</mxc:CartesianChart.AxesX>
```

您可以运行该应用程序来查看显示三个系列的图表控件：

![charts-get-started-three-series](../../images/charts-get-started-three-series.png)



## 创建自定义标签格式化程序

`CartesianChart` 根据轴缩放选项设置主要刻度线标签的格式。以下图像显示 `Month` 时间单位应用于 _X_ 轴时的标签格式：

![chart-get-started-label-formatting-month-default](../../images/chart-get-started-label-formatting-month-default.png)

轴的 `ScaleOptions.LabelFormatter` 属性允许您更改标签的显示格式。您可以使用 `Eremex.AvaloniaUI.Charts.FuncLabelFormatter` 类作为标签格式化程序，或者通过实现 `IAxisLabelFormatter` 接口来创建自定义标签格式化程序。

我们将使用 `FuncLabelFormatter` 类为 _X_ 轴的日期时间值创建短标签。在主视图模型中，实现 `FuncLabelFormatter` 类型的属性，以特定方式格式化标签。在 XAML 中，将轴的 `ScaleOptions.LabelFormatter` 选项绑定到此格式化程序。

![chart-get-started-label-formatting-month-custom](../../images/chart-get-started-label-formatting-month-custom.png)

``` xml
<mxc:AxisX Name="salesAxis" Title="Sales">
    <mxc:AxisX.ScaleOptions>
        <mxc:DateTimeScaleOptions MeasureUnit="Month" LabelFormatter="{Binding MonthFormatter}" />
    </mxc:AxisX.ScaleOptions>
</mxc:AxisX>
```

``` cs
public partial class MainWindowViewModel : ViewModelBase
{
    // ...
    [ObservableProperty] FuncLabelFormatter monthFormatter = new(o => String.Format("{0:MMM} {0:yy}", o));
}
```

## 结果

现在您可以运行该应用程序来查看本教程的结果。 `CartesianChart` 控件使用条形图和折线图系列视图显示三个数据系列。线系列与其自己的 _X_ 轴相关联，该轴显示在图表顶部。

![charts-get-started](../../images/charts-get-started.png)



## 完整代码

``` xml
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:EremexChartsSample.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"             
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="EremexChartsSample.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        
        Title="EremexChartsSample">

    <Design.DataContext>
        <!-- This only sets the DataContext for the previewer in an IDE,
             to set the actual DataContext for runtime, set the DataContext property in code (look at App.axaml.cs) -->
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <mxc:CartesianChart Name="chart1">
        <mxc:CartesianChart.Series>
            <mxc:CartesianSeries Name="barSeries1" DataAdapter="{Binding BarSeries1.DataAdapter}" >
                <mxc:CartesianSideBySideBarSeriesView Color="{Binding BarSeries1.Color}" BarWidth="1" />
            </mxc:CartesianSeries>
            <mxc:CartesianSeries Name="barSeries2" DataAdapter="{Binding BarSeries2.DataAdapter}" >
                <mxc:CartesianSideBySideBarSeriesView Color="{Binding BarSeries2.Color}" />
            </mxc:CartesianSeries>
            <mxc:CartesianSeries Name="lineSeries" DataAdapter="{Binding LineSeries.DataAdapter}"  AxisXKey="lineSeriesAxis" >
                <mxc:CartesianLineSeriesView Color="{Binding LineSeries.Color}" />
            </mxc:CartesianSeries>
        </mxc:CartesianChart.Series>

        <mxc:CartesianChart.AxesX>
            <mxc:AxisX Name="salesAxis" Title="Sales">
                <mxc:AxisX.ScaleOptions>
                    <mxc:DateTimeScaleOptions MeasureUnit="Month" LabelFormatter="{Binding MonthFormatter}" />
                </mxc:AxisX.ScaleOptions>
            </mxc:AxisX>
            <mxc:AxisX Key="lineSeriesAxis" Position="Far" Title="Expenses">
                <mxc:AxisX.ScaleOptions>
                    <mxc:NumericScaleOptions />
                </mxc:AxisX.ScaleOptions>
            </mxc:AxisX>
        </mxc:CartesianChart.AxesX>

        <mxc:CartesianChart.AxesY>
            <mxc:AxisY Title="Currency"/>
        </mxc:CartesianChart.AxesY>
            
    </mxc:CartesianChart>
</mx:MxWindow>
```

``` cs
using Avalonia.Media;
using CommunityToolkit.Mvvm.ComponentModel;
using Eremex.AvaloniaUI.Charts;
using System;

namespace EremexChartsSample.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    public MainWindowViewModel()
    {
        //Init data
        var random = new Random(4);
        var random2 = new Random(0);

        var startDate = new DateTime(DateTime.Now.Year, 1, 1);
        SortedDateTimeDataAdapter barSeries1DataAdapter = new();
        SortedDateTimeDataAdapter barSeries2DataAdapter = new();
        SortedNumericDataAdapter lineSeriesDataAdapter = new();
        for (int i = 0; i < 12; i++)
        {
            var argument = startDate.AddMonths(i);
            barSeries1DataAdapter.Add(argument, random.NextDouble() * 100 - 30);
            barSeries2DataAdapter.Add(argument, random.NextDouble() * 100 - 30);

        }

        double startValue = 20;
        for (int i = 0; i < 365; i++)
        {
            var argument = i;
            var value = startValue + (random2.NextDouble() - 0.5) * 10;
            lineSeriesDataAdapter.Add(argument, value);
            startValue = value;
        }

        // Create data series
        BarSeries1 = new() { Color = Color.FromArgb(255, 0, 120, 122), DataAdapter = barSeries1DataAdapter };
        BarSeries2 = new() { Color = Color.FromArgb(255, 0, 170, 110), DataAdapter = barSeries2DataAdapter };
        LineSeries = new() { Color = Color.FromArgb(255, 120, 10, 12), DataAdapter = lineSeriesDataAdapter };
    }

    [ObservableProperty] SeriesViewModel barSeries1; 
    [ObservableProperty] SeriesViewModel barSeries2; 
    [ObservableProperty] SeriesViewModel lineSeries;

    [ObservableProperty] CustomLabelFormatter monthFormatter = new(o => String.Format("{0:MMM} {0:yy}", o));
}

public partial class SeriesViewModel : ObservableObject
{
    [ObservableProperty] Color color;
    [ObservableProperty] ISeriesDataAdapter dataAdapter;
}

public class CustomLabelFormatter : IAxisLabelFormatter
{
    readonly Func<object, string> formatFunc;

    public CustomLabelFormatter(Func<object, string> formatFunc)
    {
        this.formatFunc = formatFunc;
    }
    public string Format(object value) => 
        formatFunc(value);
}
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
