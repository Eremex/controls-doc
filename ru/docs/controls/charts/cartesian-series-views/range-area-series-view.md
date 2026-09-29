---
title: Range Area Series View
order: 700
seealso: []
---

# Range Area Series View

Range Area Series View (`CartesianRangeAreaSeriesView`) строит две линии и закрашивает область между этими линиями.

![chart-views-range-area-series-view](../../../images/chart-views-range-area-series-view.png)

Вам необходимо предоставить два значения Y для каждой точки данных. Эти значения определяют нижнюю и верхнюю границы диапазона. Диаграмма соединяет значения Y каждой границы линиями и закрашивает область между ними указанным цветом. 

## Создание Range Series View

Чтобы создать Range Series View, добавьте объект `CartesianSeries` в коллекцию `CartesianChart.Series` и инициализируйте `CartesianSeries.View` экземпляром `CartesianRangeAreaSeriesView`.

Используйте свойство `CartesianSeries.DataAdapter`, чтобы предоставить данные для серии. Range Area Series View требует два значения Y на каждую точку данных. Вам следует использовать специальные адаптеры данных, чтобы предоставить значения Y для Range Area Series View. Информацию о поддерживаемых адаптерах данных см. по следующей ссылке: [Данные для Range Area Series View](#данные-для-range-area-series-view).

Объект `CartesianRangeAreaSeriesView` включает свойства `Color1`, `Color2` и `Color`, которые позволяют задать разные цвета для закраски линий и заливки.

В следующем коде показано, как создать Range Area Series View в XAML и code-behind.

``` xml
<mxc:CartesianChart x:Name="chartControl">
    <mxc:CartesianChart.Series>
        <mxc:CartesianSeries Name="rangeAreaSeries1" DataAdapter="{Binding DataAdapter}" >
            <mxc:CartesianRangeAreaSeriesView Color="Red" 
                                                Color1="Green" 
                                                Color2="Blue" 
                                                Transparency="0.4"/>
        </mxc:CartesianSeries>
    </mxc:CartesianChart.Series>
</mxc:CartesianChart>
```

``` cs
CartesianSeries series = new CartesianSeries();
chartControl.Series.Add(series);
List<double> args = new() { 1, 2, 3, 4, 5 };
List<double> values1 = new() { -1, 5, 3, 7, 4 };
List<double> values2 = new() { 5, 1, 6, 2, 3 };
series.DataAdapter = new NumericRangeDataAdapter(args, values1, values2);
series.View = new CartesianRangeAreaSeriesView()
{
    Color = Avalonia.Media.Colors.Red,
    Transparency = 0.4,
    Color1 = Avalonia.Media.Colors.Green,
    Color2 = Avalonia.Media.Colors.Blue
};
```

## Пример - Использование Range Area Series View для отображения минимальной и максимальной месячной температуры

Следующий пример использует Range Area Series View для отображения минимальной и максимальной месячной температуры в городе. Адаптер данных (`DateTimeRangeDataAdapter`) предоставляет два значения Y для каждой точки данных (месяца).

Обратите внимание на использование свойства `DateTimeScaleOptions.LabelFormatter` для форматирования подписей оси _X_ пользовательским способом.

![chart-views-rangeAreaSeriesView-example](../../../images/chart-views-rangeAreaSeriesView-example.png)

``` xml
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:ChartRangeAreaSeriesView.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="ChartRangeAreaSeriesView.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="ChartRangeAreaSeriesView">

    <Design.DataContext>
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <mxc:CartesianChart x:Name="chartControl">
        <mxc:CartesianChart.Series>
            <mxc:CartesianSeries Name="rangeAreaSeries1" DataAdapter="{Binding RangeAreaSeries1.DataAdapter}" >
                <mxc:CartesianRangeAreaSeriesView Color="{Binding RangeAreaSeries1.Color}" 
                                                  Color1="{Binding RangeAreaSeries1.Color1}" 
                                                  Color2="{Binding RangeAreaSeries1.Color2}" 
                                                  Transparency="0.6"/>
            </mxc:CartesianSeries>
        </mxc:CartesianChart.Series>
        <mxc:CartesianChart.AxesX>
            <mxc:AxisX Name="xAxis" Title="Month" >
                <mxc:AxisX.ScaleOptions>
                    <mxc:DateTimeScaleOptions LabelFormatter="{Binding MonthFormatter}"
                                              MeasureUnit="Month"/>
                </mxc:AxisX.ScaleOptions>
            </mxc:AxisX>
        </mxc:CartesianChart.AxesX>
        <mxc:CartesianChart.AxesY>
            <mxc:AxisY Title="Min/Max Daily Temperature"/>
        </mxc:CartesianChart.AxesY>
    </mxc:CartesianChart>
</mx:MxWindow>
```

``` cs
using CommunityToolkit.Mvvm.ComponentModel;
using Avalonia.Media;
using Eremex.AvaloniaUI.Charts;
using System;
using System.Collections.Generic;

namespace ChartRangeAreaSeriesView.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    
    [ObservableProperty] FuncLabelFormatter monthFormatter = new(o => String.Format("{0:MMM}", o));
    [ObservableProperty] SeriesViewModel rangeAreaSeries1;

    public MainWindowViewModel()
    {
        RangeAreaSeries1 = new() 
        { 
            Color = Color.FromUInt32(0xffE7E8D1), 
            Color1 = Color.FromUInt32(0xffe95057),
            Color2 = Color.FromUInt32(0xff589cc1),
        };
        List<double> values1 = new() { -4.2, -3.4, 2.5, 11.9, 19.6, 22.8, 25.1, 23.6, 17.3, 9.6, 1.6, -2.7 };
        List<double> values2 = new() { -9.7, -10.1, -5.3, 1.8, 7.9, 11.6, 14.0, 12.2, 7.4, 2.5, -3.1, -7.5 };
        List<DateTime> args = new();
        for (int i = 1; i <=12; i++) 
            args.Add(new DateTime(DateTime.Now.Year, i, 1));
        rangeAreaSeries1.DataAdapter = new DateTimeRangeDataAdapter(args, values1, values2);
    }
}

public partial class SeriesViewModel : ObservableObject
{
    [ObservableProperty] Color color;
    [ObservableProperty] Color color1;
    [ObservableProperty] Color color2;
    [ObservableProperty] DateTimeRangeDataAdapter dataAdapter;
}
```

## Данные для Range Area Series View

Вы можете использовать следующие адаптеры данных для предоставления данных для Range Area Series View. Эти адаптеры данных позволяют задать два значения Y на каждый аргумент.

Числовые значения _X_:

- `NumericRangeDataAdapter`

Значения даты и времени _X_:

- `DateTimeRangeDataAdapter`
- `TimeSpanRangeDataAdapter`

Качественные значения _X_:

- `QualitativeRangeDataAdapter` 

## Параметры Range Area Series View

- `Color` — Задаёт цвет для закраски области между двумя линиями. Используйте параметр `Transparency`, чтобы управлять уровнем прозрачности закрашенной области.
- `Color1` — Задаёт цвет для закраски первой линии.
- `Color2` — Задаёт цвет для закраски второй линии.
- `CrosshairMode` — Задаёт, привязывается ли подпись перекрестия к ближайшей точке данных, или отображает интерполированное значение. См. [Отображение точного или интерполированного значения в подписях перекрестия](../crosshair.md#отображение-точного-или-интерполированного-значения-в-метках-серий-crosshair).
- `Marker1Image` — Позволяет задать изображение в формате SVG в качестве маркеров точек для первой линии.
- `Marker1ImageCss` — Задаёт CSS-код, позволяющий настраивать цвета элементов в указанном SVG-изображении (`Marker1Image`).
- `Marker1Size` — Задаёт размер маркеров точек для первой линии.
- `Marker2Image` — Позволяет задать изображение в формате SVG в качестве маркеров точек для второй линии.
- `Marker2ImageCss` — Задаёт CSS-код, позволяющий настраивать цвета элементов в указанном SVG-изображении (`Marker2Image`).
- `Marker2Size` — Задаёт размер маркеров точек для второй линии.
- `ShowInCrosshair` — Задаёт видимость подписи перекрестия для текущей серии. См. [Настройка подписей перекрестия](../crosshair.md#скрытие-серии-в-crosshair).
- `ShowMarkers1` — Включает или отключает маркеры точек для первой линии.
- `ShowMarkers2` — Включает или отключает маркеры точек для второй линии.
- `Thickness1` — Задаёт толщину первой линии.
- `Thickness2` — Задаёт толщину второй линии.
- `Transparency` — Получает или задаёт уровень прозрачности закрашенной области, выраженный значением от `0` (полностью прозрачная) до `1` (полностью непрозрачная).

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
