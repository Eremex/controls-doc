---
title: Side-by-side Bar Series View
order: 650
seealso: []
---

# Side-by-side Bar Series View

Side-by-side Bar Series View (`CartesianSideBySideBarSeriesView`) позволяет визуализировать данные в виде набора прямоугольных столбцов. Если вы предоставляете несколько серий, данные визуализируются в виде столбцов, расположенных бок о бок вдоль горизонтальной оси.

![chart-views-barseriesview](../../../images/chart-views-barseriesview.png)

## Создание Side-by-side Bar Series View

Чтобы создать Side-by-side Bar Series View, добавьте объект `CartesianSeries` в коллекцию `CartesianChart.Series` и инициализируйте свойство `CartesianSeries.View` объектом `CartesianSideBySideBarSeriesView`.

Используйте свойство `CartesianSeries.DataAdapter`, чтобы предоставить данные для серии.

В следующем коде показано, как создать Bar Series View в XAML и code-behind.

``` xml
xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"

<mxc:CartesianChart x:Name="chartControl">
    <mxc:CartesianChart.Series>
        <mxc:CartesianSeries Name="barSeries1" DataAdapter="{Binding DataAdapter}" >
            <mxc:CartesianSideBySideBarSeriesView Color="Red" />
        </mxc:CartesianSeries>
</mxc:CartesianChart>
```

``` cs
using Eremex.AvaloniaUI.Charts;

CartesianSeries series = new CartesianSeries();
chartControl.Series.Add(series);
DateTime[] args = new DateTime[] {DateTime.Today, DateTime.Today.AddMonths(1)};
double[] values = new double[] {10, 20};
series.DataAdapter = new SortedDateTimeDataAdapter(args, values );
series.View = new CartesianSideBySideBarSeriesView()
{
    Color = Avalonia.Media.Colors.Red
};
```

!!! tip

    Если вы используете аргументы типа "дата-время", вам также может потребоваться инициализировать ось _X_ и настроить параметры шкалы оси. Подробнее см. в разделе: [Шкала оси](../cartesian-chart.md#масштаб-оси).

<!-- TODO
No bars are displayed without axis X
 -->

### Пример - Создание двух Side-by-side Bar Series View

Следующий пример создаёт контрол `CartesianChart` с двумя Side-by-side Bar Series View. Данные для представлений столбцов предоставляются объектами `SortedDateTimeDataAdapter`, инициализированными в главной модели представления. Предполагается, что объект _MainWindowViewModel_ установлен в качестве контекста данных окна.

Пример показывает, как инициализировать цвет, ширину столбцов и расстояние между столбцами для объектов `CartesianSideBySideBarSeriesView`.

Оси _X_ и _Y_ создаются в XAML для настройки их параметров (включая заголовок и параметры шкалы). 

Когда вы используете объект `SortedDateTimeDataAdapter`, вам необходимо указать свойство `MeasureUnit`, чтобы определить масштабирование оси. В примере данные используют месячные интервалы, поэтому свойство `MeasureUnit` установлено в `Month`.

![chart-views-barseriesview-example](../../../images/chart-views-barseriesview-example.png)




``` xml
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:ChartBarSeriesView.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="ChartBarSeriesView.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="ChartBarSeriesView">

    <Design.DataContext>
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <mxc:CartesianChart x:Name="chartControl">
        <mxc:CartesianChart.Series>
            <mxc:CartesianSeries Name="barSeries1" DataAdapter="{Binding BarSeries1.DataAdapter}" >
                <mxc:CartesianSideBySideBarSeriesView Color="{Binding BarSeries1.Color}" BarWidth="0.9" BarDistanceFixed="1" />
            </mxc:CartesianSeries>
            <mxc:CartesianSeries Name="barSeries2" DataAdapter="{Binding BarSeries2.DataAdapter}" >
                <mxc:CartesianSideBySideBarSeriesView Color="{Binding BarSeries2.Color}" BarWidth="0.9" />
            </mxc:CartesianSeries>
        </mxc:CartesianChart.Series>

        <mxc:CartesianChart.AxesX>
            <mxc:AxisX Name="salesAxis" Title="Months">
                <mxc:AxisX.ScaleOptions>
                    <mxc:DateTimeScaleOptions MeasureUnit="Month"  LabelFormatter="{Binding MonthFormatter}"/>
                </mxc:AxisX.ScaleOptions>
            </mxc:AxisX>
        </mxc:CartesianChart.AxesX>
        <mxc:CartesianChart.AxesY>
            <mxc:AxisY Title="Sales"/>
        </mxc:CartesianChart.AxesY>
    </mxc:CartesianChart>
</mx:MxWindow>
```

``` cs
using Avalonia.Media;
using CommunityToolkit.Mvvm.ComponentModel;
using Eremex.AvaloniaUI.Charts;
using System;

namespace ChartBarSeriesView.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    [ObservableProperty] SeriesViewModel barSeries1;
    [ObservableProperty] SeriesViewModel barSeries2;
    [ObservableProperty] FuncLabelFormatter monthFormatter = new(o => String.Format("{0:MMM} {0:yy}", o));

    public MainWindowViewModel()
    {
        var random = new Random(11);
        var startDate = new DateTime(DateTime.Now.Year, 1, 1);
        SortedDateTimeDataAdapter barSeries1DataAdapter = new();
        SortedDateTimeDataAdapter barSeries2DataAdapter = new();
        for (int i = 0; i < 12; i++)
        {
            var argument = startDate.AddMonths(i);
            barSeries1DataAdapter.Add(argument, random.NextDouble() * 100 - 30);
            barSeries2DataAdapter.Add(argument, random.NextDouble() * 100 - 30);
        }
        // Create data series
        BarSeries1 = new() { Color = Color.FromUInt32(0xffe07a5f), DataAdapter = barSeries1DataAdapter };
        BarSeries2 = new() { Color = Color.FromUInt32(0xff3D405B), DataAdapter = barSeries2DataAdapter };
    }
}

public partial class SeriesViewModel : ObservableObject
{
    [ObservableProperty] Color color;
    [ObservableProperty] ISeriesDataAdapter dataAdapter;
}
```


## Данные для Bar Series View

Вы можете использовать следующие адаптеры данных для предоставления данных для Side-by-side Bar Series View:


Числовые значения _X_:

- `SortedNumericDataAdapter`
- `FormulaDataAdapter`

Значения даты и времени _X_:

- `SortedDateTimeDataAdapter`
- `SortedTimeSpanDataAdapter`

Качественные значения _X_:

- `QualitativeDataAdapter`



## Параметры Bar Series View

- `CartesianSideBySideBarSeriesView.BarDistanceFixed` — Ширина пустого пространства справа от столбцов, принадлежащих текущему Bar Series View. Свойство `BarDistanceFixed` позволяет настроить расстояние между столбцами разных серий.
- `CartesianSideBySideBarSeriesView.BarWidth` — Ширина столбцов текущего Bar Series View.
- `CartesianSideBySideBarSeriesView.BorderColor` — Цвет границы столбцов.
- `CartesianSideBySideBarSeriesView.BorderThickness` — Толщина границы столбцов.
- `CartesianSideBySideBarSeriesView.Color` — Цвет заливки столбцов.

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
