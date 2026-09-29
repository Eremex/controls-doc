---
title: Scatter Line Series View
order: 950
seealso: []
---

# Scatter Line Series View

Scatter Line Series View (`CartesianScatterLineSeriesView`) соединяет точки линиями. В отличие от [Line Series View](line-series-vew.md), точки для Scatter Line Series View не обязательно должны быть отсортированы по значениям X. Вместо этого точки соединяются в том порядке, в котором они появляются в серии данных.

<!-- TODO
Check whether points for the Line Series View must be sorted by X-values.
 -->

![chart-views-scatter-line-series-view](../../../images/chart-views-scatter-line-series-view.png)

## Создание Scatter Line Series View

Чтобы создать Scatter Line Series View, добавьте объект `CartesianSeries` в коллекцию `CartesianChart.Series` и инициализируйте `CartesianSeries.View` экземпляром `CartesianScatterLineSeriesView`.

В следующем коде показано, как создать Scatter Line Series View в XAML и code-behind.

``` xml
<mxc:CartesianChart x:Name="chartControl">
    <mxc:CartesianChart.Series>
        <mxc:CartesianSeries Name="scatterLineSeries1" DataAdapter="{Binding DataAdapter}" >
            <mxc:CartesianScatterLineSeriesView Color="Red" 
                                                ShowMarkers="True"
                                                MarkerSize="4" Thickness="2"/>
        </mxc:CartesianSeries>
    </mxc:CartesianChart.Series>
</mxc:CartesianChart>
```

``` cs
CartesianSeries series = new CartesianSeries();
chartControl.Series.Add(series);
List<(double, double)> points = new List<(double, double)>() { (0, 2), (-1, 3), (-2, 0), (2,1), (-2,5) };
// The ScatterDataAdapter allows unsorted points
series.DataAdapter = new ScatterDataAdapter(points);
series.View = new CartesianScatterLineSeriesView()
{
    Color = Avalonia.Media.Colors.Green,
    MarkerSize = 4,
};
```

## Пример - Использование Scatter Line Series View для соединения точек в серии данных

В этом примере Scatter Line Series View соединяет точки, образующие квадратную спираль. Для предоставления данных для диаграммы используется адаптер `ScatterDataAdapter`. Точки соединяются в том порядке, в котором они появляются в серии данных. 

![chart-views-scatterLineSeriesView-example](../../../images/chart-views-scatterLineSeriesView-example.png)

``` xml
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:ChartScatterLineSeriesView.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="ChartScatterLineSeriesView.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="ChartScatterLineSeriesView"
        Width="500" Height="500">
    <Design.DataContext>
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <mxc:CartesianChart x:Name="chartControl">
        <mxc:CartesianChart.Series>
            <mxc:CartesianSeries Name="scatterLineSeries1" DataAdapter="{Binding ScatterLineSeriesVM1.DataAdapter}" >
                <mxc:CartesianScatterLineSeriesView Color="{Binding ScatterLineSeriesVM1.Color}" 
                                                    ShowMarkers="True"
                                                    MarkerSize="4" Thickness="2"/>
            </mxc:CartesianSeries>
        </mxc:CartesianChart.Series>
        <mxc:CartesianChart.AxesX>
            <mxc:AxisX Name="xAxis" Title="Parameter 1" />
        </mxc:CartesianChart.AxesX>
        <mxc:CartesianChart.AxesY>
            <mxc:AxisY Title="Parameter 2"/>
        </mxc:CartesianChart.AxesY>
    </mxc:CartesianChart>
</mx:MxWindow>
```

``` cs
using Avalonia;
using Avalonia.Media;
using CommunityToolkit.Mvvm.ComponentModel;
using Eremex.AvaloniaUI.Charts;
using System;
using System.Collections.Generic;

namespace ChartScatterLineSeriesView.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    [ObservableProperty] SeriesViewModel scatterLineSeriesVM1;

    public MainWindowViewModel()
    {
        ScatterLineSeriesVM1 = new()
        {
            Color = Color.FromUInt32(0xff0d628d),
            DataAdapter = new ScatterDataAdapter(GenerateSquareSpiralData())
        };
    }

    private List<(double, double)> GenerateSquareSpiralData()
    {
        List<(double, double)> points = new List<(double, double)> ();
        double x = 2, y = 2;
        int stepsPerSide = 1; // Steps before changing direction
        int direction = 3; // 0=right, 1=up, 2=left, 3=down
        int turns = 4;
        double stepSize = 1.0;

        points.Add((x, y));
        
        for (int i = 0; i < turns * 4; i++) // 4 sides per turn
        {
            for (int step = 0; step < stepsPerSide; step++)
            {
                switch (direction)
                {
                    case 0: x += stepSize; break; // Right
                    case 1: y += stepSize; break; // Up
                    case 2: x -= stepSize; break; // Left
                    case 3: y -= stepSize; break; // Down
                }
                points.Add((x, y));
            }
            direction = (direction + 1) % 4; // Change direction
            if (i % 2 == 1) stepsPerSide++; // Increase steps every 2 turns
        }
        return points;
    }
}

public partial class SeriesViewModel : ObservableObject
{
    [ObservableProperty] Color color;
    [ObservableProperty] ScatterDataAdapter dataAdapter;
}
```

## Данные для Scatter Line Series View

Вы можете использовать следующий адаптер данных для предоставления данных для Scatter Line Series View:

- `ScatterDataAdapter`


## Параметры Scatter Line Series View

- `Color` — Задаёт цвет, используемый для закраски серии.
- `MarkerImage` — Получает или задаёт изображение, используемое в качестве пользовательских маркеров точек. Если изображение не указано, отображаются стандартные маркеры в форме квадрата. Вы можете использовать экземпляр класса `SvgImage`, чтобы задать SVG-изображение.

    Свойство `MarkerImage` объявлено с атрибутом `[Content]`, что позволяет определить изображение непосредственно между тегами &lt;CartesianScatterLineSeriesView&gt;.

    ``` xml
    <mxc:CartesianScatterLineSeriesView>
        <SvgImage Source="avares://Demo/Assets/circle.svg" />
    </mxc:CartesianScatterLineSeriesView>
    ```

    SVG-файлы содержат предопределённые цвета для SVG-элементов. Чтобы эти цвета соответствовали цвету вашей серии данных, вы можете:
    
    - Вручную отредактировать исходный SVG-файл заранее
    - Использовать свойство `MarkerImageCss`, чтобы динамически настраивать [стили](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/style) для SVG-элементов. Стили применяются при отрисовке маркеров точек.
- `MarkerImageCss` — Задаёт [CSS-стили](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/style) для настройки SVG-изображения, заданного свойством `MarkerImage`, во время выполнения. Основной сценарий использования — замена цветов SVG-элементов на цвет серии (`Color`). Включите заполнитель `{0}`, чтобы вставить значение свойства `Color` в CSS-код. 

    Например, когда свойство `MarkerImage` содержит SVG-изображение с элементом circle, следующий CSS-код стилизует `circle` заливкой Orange (используя цвет серии) и границей Dark Red:

    ``` xml
    <mxc:CartesianScatterLineSeriesView Color="orange" MarkerImageCss="circle {{fill:{0};stroke:darkred;}}">
        <SvgImage Source="avares://Demo/Assets/circle.svg" />
    </mxc:CartesianScatterLineSeriesView>
    ```
    
    Смотрите также: [Пример - Создание Lollipop Series View и использование пользовательских SVG-маркеров](lollipop-series-view.md#пример---создание-lollipop-series-view-и-использование-пользовательских-svg-маркеров-точек-данных).

- `MarkerSize` — Задаёт размер маркеров точек.
- `ShowInCrosshair` — Задаёт видимость подписи перекрестия для текущей серии. См. [Настройка подписей перекрестия](../crosshair.md#скрытие-серии-в-crosshair).
- `ShowMarkers` — Включает или отключает маркеры точек.
- `Thickness` — Задаёт толщину линии.

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
