---
title: Line Series View
order: 1000
seealso: []
---

# Line Series View

Line Series View (`CartesianLineSeriesView`) соединяет точки линиями. Серия позволяет отображать или скрывать маркеры точек, а также настраивать толщину линий и маркеров точек. На следующем изображении показан контрол диаграммы с двумя линейными сериями, каждая из которых закрашена своим цветом.


![chart-views-line-series-view](../../../images/chart-views-line-series-view.png)

## Создание Line Series View

Чтобы создать Line Series View, добавьте объект `CartesianSeries` в коллекцию `CartesianChart.Series` и инициализируйте свойство `CartesianSeries.View` экземпляром `CartesianLineSeriesView`.

Используйте свойство `CartesianSeries.DataAdapter`, чтобы предоставить данные для серии.

В следующем коде показано, как создать Line Series View в XAML и code-behind.

``` xml
xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"

<mxc:CartesianChart x:Name="chartControl">
    <mxc:CartesianChart.Series>
        <mxc:CartesianSeries Name="lineSeries1" DataAdapter="{Binding DataAdapter}" >
            <mxc:CartesianLineSeriesView Color="Red" MarkerSize="4" ShowMarkers="True" Thickness="2"/>
        </mxc:CartesianSeries>
    </mxc:CartesianChart.Series>
</mxc:CartesianChart>
```

``` cs
using Eremex.AvaloniaUI.Charts;

CartesianSeries series = new CartesianSeries();
chartControl.Series.Add(series);
double[] args = new double[] { 1, 2, 3, 4, 5, 6, 7 };
double[] values = new double[] { 0, 0.4, 1.5, 1.3, 0.4, 0, 0.1 };
series.DataAdapter = new SortedNumericDataAdapter(args, values);
series.View = new CartesianLineSeriesView()
{
    Color = Avalonia.Media.Colors.Green,
    ShowMarkers = true,
    MarkerSize = 4,
    Thickness = 2
};
```

### Пример - Создание двух Line Series View


Следующий пример создаёт контрол `CartesianChart` с двумя Line Series View. Данные для представлений серий предоставляются объектами `FormulaDataAdapter`, которые вычисляют значения согласно указанным формулам. Предполагается, что объект _MainWindowViewModel_ установлен в качестве контекста данных окна.

![chart-views-lineeriesview-example](../../../images/chart-views-lineeriesview-example.png)

Пример демонстрирует, как настроить толщину линии и маркеры точек для представлений серий.

Оси _X_ и _Y_ создаются в XAML для настройки их параметров. Обратите внимание на использование свойства `NumericScaleOptions.LabelFormatter` для форматирования подписей оси пользовательским способом.

``` xml
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:ChartLinearSeriesView.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="ChartLinearSeriesView.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="ChartLinearSeriesView"
        Width="600" Height="350"
        >
    <Design.DataContext>
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <mxc:CartesianChart x:Name="chartControl">
        <mxc:CartesianChart.Series>
            <mxc:CartesianSeries Name="lineSeries1" DataAdapter="{Binding LineSeries1.DataAdapter}" >
                <mxc:CartesianLineSeriesView Color="{Binding LineSeries1.Color}" MarkerSize="4" ShowMarkers="True" Thickness="2"/>
            </mxc:CartesianSeries>
            <mxc:CartesianSeries Name="lineSeries2" DataAdapter="{Binding LineSeries2.DataAdapter}" >
                <mxc:CartesianLineSeriesView Color="{Binding LineSeries2.Color}" MarkerSize="4" ShowMarkers="True" Thickness="2"/>
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
            <mxc:AxisY Title="Values">
                <mxc:AxisY.ScaleOptions>
                    <mxc:NumericScaleOptions LabelFormatter="{Binding ArgsLabelFormatter}"/>
                </mxc:AxisY.ScaleOptions>
            </mxc:AxisY>
        </mxc:CartesianChart.AxesY>
    </mxc:CartesianChart>
</mx:MxWindow>
```

``` cs
using Avalonia.Media;
using CommunityToolkit.Mvvm.ComponentModel;
using Eremex.AvaloniaUI.Charts;
using System;

namespace ChartLinearSeriesView.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    static double Sin(double argument) => 0.5* Math.Sin(argument)+0.5;
    static double Cos(double argument) => 0.6*Math.Cos(argument);

    [ObservableProperty] SeriesViewModel lineSeries1;
    [ObservableProperty] SeriesViewModel lineSeries2;
    [ObservableProperty] FuncLabelFormatter argsLabelFormatter = new(o => String.Format("{0:n1}", o));

    const int ItemCount = 37;
    const double Step = 0.1;

    public MainWindowViewModel()
    {
        LineSeries1 = new() 
        { 
            Color = Color.FromUInt32(0xfffeb640), 
            DataAdapter = new FormulaDataAdapter(-3, Step, ItemCount, Sin) 
        };
        LineSeries2 = new() 
        { 
            Color = Color.FromUInt32(0xff9389bd), 
            DataAdapter = new FormulaDataAdapter(-2, Step, ItemCount, Cos) 
        };
    }
}

public partial class SeriesViewModel : ObservableObject
{
    [ObservableProperty] Color color;
    [ObservableProperty] ISeriesDataAdapter dataAdapter;
}
```

## Данные для Line Series View

Вы можете использовать следующие адаптеры данных для предоставления данных для Line Series View:

Числовые значения _X_:

- `SortedNumericDataAdapter`
- `FormulaDataAdapter`

Значения даты и времени _X_:

- `SortedDateTimeDataAdapter`
- `SortedTimeSpanDataAdapter`


Качественные значения _X_:

- `QualitativeDataAdapter`


## Параметры Line Series View


- `Color` — Задаёт цвет, используемый для закраски серии.
- `CrosshairMode` — Задаёт, привязывается ли подпись перекрестия к ближайшей точке данных, или отображает интерполированное значение. См. [Отображение точного или интерполированного значения в подписях перекрестия](../crosshair.md#отображение-точного-или-интерполированного-значения-в-метках-серий-crosshair).
- `MarkerImage` — Получает или задаёт изображение, используемое в качестве пользовательских маркеров точек. Если изображение не указано, отображаются стандартные маркеры в форме квадрата. Вы можете использовать экземпляр класса `SvgImage`, чтобы задать SVG-изображение.

    Свойство `MarkerImage` объявлено с атрибутом `[Content]`, что позволяет определить изображение непосредственно между тегами &lt;CartesianLineSeriesView&gt;.

    ``` xml
    <mxc:CartesianLineSeriesView>
        <SvgImage Source="avares://Demo/Assets/circle.svg" />
    </mxc:CartesianLineSeriesView>
    ```

    SVG-файлы содержат предопределённые цвета для SVG-элементов. Чтобы эти цвета соответствовали цвету вашей серии данных, вы можете:
    
    - Вручную отредактировать исходный SVG-файл заранее
    - Использовать свойство `MarkerImageCss`, чтобы динамически настраивать [стили](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/style) для SVG-элементов. Стили применяются при отрисовке маркеров точек.

- `MarkerImageCss` — Задаёт [CSS-стили](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/style) для настройки SVG-изображения, заданного свойством `MarkerImage`, во время выполнения. Основной сценарий использования — замена цветов SVG-элементов на цвет серии (`Color`). Включите заполнитель `{0}`, чтобы вставить значение свойства `Color` в CSS-код. 

    Например, когда свойство `MarkerImage` содержит SVG-изображение с элементом circle, следующий CSS-код стилизует `circle` заливкой Orange (используя цвет серии) и границей Dark Red:

    ``` xml
    <mxc:CartesianLineSeriesView Color="orange" MarkerImageCss="circle {{fill:{0};stroke:darkred;}}">
        <SvgImage Source="avares://Demo/Assets/circle.svg" />
    </mxc:CartesianLineSeriesView>
    ```
    
    Смотрите также: [Пример - Создание Lollipop Series View и использование пользовательских SVG-маркеров](lollipop-series-view.md#пример---создание-lollipop-series-view-и-использование-пользовательских-svg-маркеров-точек-данных).

- `MarkerSize` — Задаёт размер маркеров точек.
- `ShowInCrosshair` — Задаёт видимость подписи перекрестия для текущей серии. См. [Настройка подписей перекрестия](../crosshair.md#скрытие-серии-в-crosshair).
- `ShowMarkers` — Включает или отключает маркеры точек.
- `Thickness` — Задаёт толщину линии.

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
