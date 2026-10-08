---
title: Area Series View
order: 750
seealso: []
---

# Area Series View

The Area Series View ([`CartesianAreaSeriesView`](../../../API/Eremex.AvaloniaUI.Charts/CartesianAreaSeriesView.md)) connects points with lines and fills the areas between the charts and the _X_ axis with specified colors. You can fill these areas with semi-transparent colors to blend the colors of multiple series, and keep the chart's grid lines visible underneath.


![chart-views-area-series-view](../../../images/chart-views-area-series-view.png)



## Create an Area Series View

To create an Area Series View, add a [`CartesianSeries`](../../../API/Eremex.AvaloniaUI.Charts/CartesianSeries.md) object to the [`CartesianChart.Series`](../../../API/Eremex.AvaloniaUI.Charts/CartesianChart/Series.md) collection, and initialize the [`CartesianSeries.View`](../../../API/Eremex.AvaloniaUI.Charts/CartesianSeries/View.md) property with a [`CartesianAreaSeriesView`](../../../API/Eremex.AvaloniaUI.Charts/CartesianAreaSeriesView.md) object.

Use the [`CartesianSeries.DataAdapter`](../../../API/Eremex.AvaloniaUI.Charts/Series/DataAdapter.md) property to supply data for the series.

The following code shows how to create an Area Series View in XAML and code-behind.

``` xml
xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"

<mxc:CartesianChart x:Name="chartControl">
    <mxc:CartesianChart.Series>
        <mxc:CartesianSeries Name="areaSeries1" DataAdapter="{Binding DataAdapter}" >
            <mxc:CartesianAreaSeriesView Color="Green" Transparency="0.3" MarkerSize="5" ShowMarkers="True"/>
        </mxc:CartesianSeries>
    </mxc:CartesianChart.Series>
</mxc:CartesianChart>
```

``` cs
using Eremex.AvaloniaUI.Charts;

CartesianSeries series = new CartesianSeries();
chartControl.Series.Add(series);
double[] args = new double[] { 1,2,3,4,5,6,7 };
double[] values = new double[] { 5,4,3,2,3,4,5 };
series.DataAdapter = new SortedNumericDataAdapter(args, values);
series.View = new CartesianAreaSeriesView()
{
    Color = Avalonia.Media.Colors.Green,
    Transparency = 0.3,
    ShowMarkers = true,
    MarkerSize = 5
};
``` 

!!! tip

    If you use date-time arguments, you may also need to initialize the _X_ axis, and customize the axis scale options. Refer to the following topic for more details: [Axis Scale](../cartesian-chart.md#axis-scale).

### Example - Create Two Area Series Views


The following example creates a [`CartesianChart`](../../../API/Eremex.AvaloniaUI.Charts/CartesianChart.md) control with two Area Series Views. Data for the Series Views is provided by [`FormulaDataAdapter`](../../../API/Eremex.AvaloniaUI.Charts/FormulaDataAdapter.md) objects, which calculate values according to specified formulas. It is implied that a _MainWindowViewModel_ object is set as a data context for the window.

The created Series Views use semi-transparent red and blue colors. When the filled areas overlap, both series and grid lines remain visible.

![chart-views-areaeriesview-example](../../../images/chart-views-areaeriesview-example.png)

The example demonstrates how to customize the color, fill transparency, and point markers for the Series Views.

The _X_ and _Y_ axes are created in XAML to perform customization of their settings. Note the use of the [`NumericScaleOptions.LabelFormatter`](../../../API/Eremex.AvaloniaUI.Charts/ScaleOptions/LabelFormatter.md) property to format axis labels in a custom manner.



``` xml
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:ChartAreaSeriesView.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="ChartAreaSeriesView.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="ChartAreaSeriesView">

    <Design.DataContext>
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <mxc:CartesianChart x:Name="chartControl">
        <mxc:CartesianChart.Series>
            <mxc:CartesianSeries Name="areaSeries1" DataAdapter="{Binding AreaSeries1.DataAdapter}" >
                <mxc:CartesianAreaSeriesView Color="{Binding AreaSeries1.Color}" Transparency="0.6" MarkerSize="3" ShowMarkers="True"/>
            </mxc:CartesianSeries>
            <mxc:CartesianSeries Name="areaSeries2" DataAdapter="{Binding AreaSeries2.DataAdapter}" >
                <mxc:CartesianAreaSeriesView Color="{Binding AreaSeries2.Color}" Transparency="0.6" MarkerSize="3" ShowMarkers="True"/>
            </mxc:CartesianSeries>
        </mxc:CartesianChart.Series>

        <mxc:CartesianChart.AxesX>
            <mxc:AxisX Name="xAxis" Title="Arguments" >
                <mxc:AxisX.ScaleOptions>
                    <mxc:NumericScaleOptions LabelFormatter="{Binding ArgsLabelFormatter}"/>
                </mxc:AxisX.ScaleOptions>
            </mxc:AxisX>
        </mxc:CartesianChart.AxesX>
        <mxc:CartesianChart.AxesY>
            <mxc:AxisY Title="Values"/>
        </mxc:CartesianChart.AxesY>
    </mxc:CartesianChart>
</mx:MxWindow>
```

``` cs
using Avalonia.Media;
using CommunityToolkit.Mvvm.ComponentModel;
using Eremex.AvaloniaUI.Charts;
using System;

namespace ChartAreaSeriesView.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    static double Exp(double argument) => 2 * Math.Exp(-argument) - 2;
    static double Exp2(double argument) => Math.Exp(argument) + 2;

    [ObservableProperty] SeriesViewModel areaSeries1;
    [ObservableProperty] SeriesViewModel areaSeries2;
    [ObservableProperty] FuncLabelFormatter argsLabelFormatter = new(o => String.Format("{0:n1}", o));

    const int ItemCount = 41;
    const double Step = 0.1;

    public MainWindowViewModel()
    {
        AreaSeries1 = new() { Color = Color.FromUInt32(0xffDF3C5F), DataAdapter = new FormulaDataAdapter(-2, Step, ItemCount, Exp) };
        AreaSeries2 = new() { Color = Color.FromUInt32(0xff6F9BD1), DataAdapter = new FormulaDataAdapter(-2, Step, ItemCount, Exp2) };
    }
}

public partial class SeriesViewModel : ObservableObject
{
    [ObservableProperty] Color color;
    [ObservableProperty] ISeriesDataAdapter dataAdapter;
}
```


## Data for the Area Series View

You can use the following data adapters to provide data for Area Series Views:

Numeric _X_ Values:

- [`SortedNumericDataAdapter`](../../../API/Eremex.AvaloniaUI.Charts/SortedNumericDataAdapter.md)
- [`FormulaDataAdapter`](../../../API/Eremex.AvaloniaUI.Charts/FormulaDataAdapter.md)


Date and Time _X_ Values:

- [`SortedDateTimeDataAdapter`](../../../API/Eremex.AvaloniaUI.Charts/SortedDateTimeDataAdapter.md)
- [`SortedTimeSpanDataAdapter`](../../../API/Eremex.AvaloniaUI.Charts/SortedTimeSpanDataAdapter.md)

Qualitative _X_ Values:

- [`QualitativeDataAdapter`](../../../API/Eremex.AvaloniaUI.Charts/QualitativeDataAdapter.md)


## Area Series View Settings


- [`Color`](../../../API/Eremex.AvaloniaUI.Charts/CartesianPointSeriesView/Color.md) — Specifies the color used to paint the series.
- [`CrosshairMode`](../../../API/Eremex.AvaloniaUI.Charts/CartesianSortedLineSeriesView/CrosshairMode.md) — Specifies whether the crosshair's chart label snaps to the nearest data point, or displays an interpolated value. See [Show an Exact or Interpolated Value in Crosshair Chart Labels](../crosshair.md#show-an-exact-or-interpolated-value-in-crosshair-series-labels).
- [`MarkerImage`](../../../API/Eremex.AvaloniaUI.Charts/CartesianPointSeriesView/MarkerImage.md) — Gets or sets an image to use as custom point markers. If no image is specified, default square-shaped markers are displayed. You can use an `SvgImage` class instance to specify an SVG image.

    The [`MarkerImage`](../../../API/Eremex.AvaloniaUI.Charts/CartesianPointSeriesView/MarkerImage.md) property is declared with the `[Content]` attribute, which allows you to define an image directly between the &lt;CartesianAreaSeriesView&gt; tags.

    ``` xml
    <mxc:CartesianAreaSeriesView>
        <SvgImage Source="avares://Demo/Assets/circle.svg" />
    </mxc:CartesianAreaSeriesView>
    ```

    SVG files contain predefined colors for SVG elements. To make these colors match your data series color, you can either:
    
    - Manually edit the source SVG image file beforehand
    - Use the [`MarkerImageCss`](../../../API/Eremex.AvaloniaUI.Charts/CartesianPointSeriesView/MarkerImageCss.md) property to dynamically customize [styles](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/style) for SVG elements. The styles are applied when point markers are rendered.




- [`MarkerImageCss`](../../../API/Eremex.AvaloniaUI.Charts/CartesianPointSeriesView/MarkerImageCss.md) — Specifies [CSS styles](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/style) for runtime customization of an SVG image defined by the [`MarkerImage`](../../../API/Eremex.AvaloniaUI.Charts/CartesianPointSeriesView/MarkerImage.md) property. The primary use case is replacing SVG element colors with the series color ([`Color`](../../../API/Eremex.AvaloniaUI.Charts/CartesianPointSeriesView/Color.md)). Include the `{0}` placeholder to insert the value of the [`Color`](../../../API/Eremex.AvaloniaUI.Charts/CartesianPointSeriesView/Color.md) property in the CSS code. 

    For example, when the [`MarkerImage`](../../../API/Eremex.AvaloniaUI.Charts/CartesianPointSeriesView/MarkerImage.md) property contains an SVG image with a circle element, the following CSS code styles the `circle` with an Orange fill (using the series color) and Dark Red border:

    ``` xml
    <mxc:CartesianAreaSeriesView Color="orange" MarkerImageCss="circle {{fill:{0};stroke:darkred;}}">
        <SvgImage Source="avares://Demo/Assets/circle.svg" />
    </mxc:CartesianAreaSeriesView>
    ```
    
    See also: [Example - Create a Lollipop Series View and Use Custom SVG Markers](lollipop-series-view.md#example-create-a-lollipop-series-view-and-use-custom-svg-data-point-markers).


- [`MarkerSize`](../../../API/Eremex.AvaloniaUI.Charts/CartesianPointSeriesView/MarkerSize.md) — Specifies the size of point markers.
- [`ShowInCrosshair`](../../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesViewBase/ShowInCrosshair.md) — Specifies the visibility of the crosshair chart label for the current series. See [Customize Chart Labels of the Crosshair](../crosshair.md#hide-a-series-in-the-crosshair).
- [`ShowMarkers`](../../../API/Eremex.AvaloniaUI.Charts/CartesianLineSeriesViewBase/ShowMarkers.md) — Enables or disables point markers.
- `Thickness` — Specifies the line thickness.
- [`Transparency`](../../../API/Eremex.AvaloniaUI.Charts/CartesianAreaSeriesView/Transparency.md) — A value between `0` and `1` which specifies the transparency level of filled areas:
    - `0` means fully opaque
    - `1` means fully transparent