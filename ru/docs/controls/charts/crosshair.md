---
title: Crosshair
order: 985
seealso: []
image: /images/chart-crosshair-one-series.png
---

# Crosshair

## Что такое Crosshair?


Контрол Cartesian Chart включает функцию Crosshair, которая позволяет видеть точные значения серий в текущей позиции курсора. Отображаемый в виде пары горизонтальной и вертикальной линий, Crosshair следует за указателем мыши при перемещении над областью диаграммы. Он показывает метку серии (или несколько меток для нескольких серий), отображающую значение серии, и выделяет текущие координаты _X_ и _Y_ на осях.


![chart-crosshair-one-series](../../images/chart-crosshair-one-series.png)

Чтобы настроить параметры отображения Crosshair или отключить эту функцию, инициализируйте свойство [`CartesianChart.CrosshairOptions`](../../API/Eremex.AvaloniaUI.Charts/ChartControl/CrosshairOptions.md) экземпляром класса [`Eremex.AvaloniaUI.Charts.CrosshairOptions`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions.md). Затем используйте свойства класса [`CrosshairOptions`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions.md), чтобы настроить параметры Crosshair по мере необходимости.


## Отключение Crosshair

Свойство [`CrosshairOptions.ShowCrosshair`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ShowCrosshair.md) позволяет отключить Crosshair.

``` xml
<mxc:CartesianChart x:Name="chartControl1" >
    <mxc:CartesianChart.CrosshairOptions>
        <mxc:CrosshairOptions ShowCrosshair="False"/>
    </mxc:CartesianChart.CrosshairOptions>
    <!-- ... -->
</mxc:CartesianChart>
```

## Отключение отдельных линий и меток осей Crosshair

Свойства [`CrosshairOptions.ShowArgumentLine`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ShowArgumentLine.md) и [`CrosshairOptions.ShowValueLine`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ShowValueLine.md) можно использовать, чтобы скрыть вертикальную и горизонтальную линии Crosshair соответственно. Чтобы предотвратить отображение меток Crosshair для осей _X_ и _Y_, используйте свойства [`CrosshairOptions.ShowArgumentLabel`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ShowArgumentLabel.md) и [`CrosshairOptions.ShowValueLabel`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ShowValueLabel.md).

Этот пример скрывает вертикальную линию Crosshair и метку для оси _X_:

![chart-crosshair-vertical-line-hidden](../../images/chart-crosshair-vertical-line-hidden.png)

``` xml
<mxc:CartesianChart x:Name="chartControl1" >
    <mxc:CartesianChart.CrosshairOptions>
        <mxc:CrosshairOptions ShowArgumentLabel="False" ShowValueLabel="False"/>
    </mxc:CartesianChart.CrosshairOptions>
    <!-- ... -->
</mxc:CartesianChart>
```

## Настройка меток серий Crosshair

Метки серий Crosshair отображают имена и текущие значения серий.

![chart-crosshair-chart-labels](../../images/chart-crosshair-chart-labels.png)

### Форматирование значений в метках серий Crosshair

Значения, отображаемые в метках Crosshair, изначально используют форматы по умолчанию:

![chart-crosshair-chart-labels-no-formatting](../../images/chart-crosshair-chart-labels-no-formatting.png)

Чтобы отформатировать эти значения пользовательским образом, создайте объект-форматтер и назначьте его свойству `Axis.ScaleOptions.CrosshairLabelFormatter`. Значения осей можно [форматировать](cartesian-chart.md#форматирование-меток-осей) аналогичным образом (см. свойство `Axis.ScaleOptions.LabelFormatter`). 

Вы можете реализовать пользовательский форматтер меток на основе функции/выражения с помощью объекта [`Eremex.AvaloniaUI.Charts.FuncLabelFormatter`](../../API/Eremex.AvaloniaUI.Charts/FuncLabelFormatter.md).

Этот пример создаёт объект-форматтер, который форматирует числовые значения как валюту. Этот форматтер используется для форматирования значений оси _Y_ и значений в метке серии Crosshair.

![chart-crosshair-chart-labels-formatting-example](../../images/chart-crosshair-chart-labels-formatting-example.png)

``` xml
<mxc:CartesianChart.AxesY>
    <mxc:AxisY Title="Payment">
        <mxc:AxisY.ScaleOptions>
            <mxc:NumericScaleOptions
                CrosshairLabelFormatter="{Binding CurrencyFormatter}"
                LabelFormatter="{Binding CurrencyFormatter}"/>
        </mxc:AxisY.ScaleOptions>
    </mxc:AxisY>
</mxc:CartesianChart.AxesY>
```

``` cs
public partial class MainViewModel : ViewModelBase 
{
[ObservableProperty] 
FuncLabelFormatter currencyFormatter = new(o => String.Format("{0:c}", o));
}
```


<!-- 
TODO
### Change the Template of Crosshair Series Labels 

-->


### Скрытие серии в Crosshair

Свойство [`CrosshairSeriesViewBase.ShowInCrosshair`](../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesViewBase/ShowInCrosshair.md) представления серии определяет видимость этой серии в метке Crosshair.

<!-- TODO
Add an image of the crosshair chart label, as many other topics refer to this section
 -->

Следующий код определяет две серии (_Interest_ и _Principal_). Для первой серии свойство [`ShowInCrosshair`](../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesViewBase/ShowInCrosshair.md) установлено в значение `false`, чтобы скрыть её в Crosshair:


``` xml
<mxc:CartesianChart.Series>
    <mxc:CartesianSeries DataAdapter="{Binding InterestSeriesDataAdapter}" SeriesName="Interest">
        <mxc:CartesianAreaSeriesView Color="#F9A825" Transparency="0.2" 
          MarkerSize="2" ShowMarkers="True"
          ShowInCrosshair="False" />
    </mxc:CartesianSeries>

    <mxc:CartesianSeries DataAdapter="{Binding PrincipalSeriesDataAdapter}" SeriesName="Principal">
        <mxc:CartesianAreaSeriesView Color="#2E7D32" Transparency="0.2" MarkerSize="2" ShowMarkers="True" />
    </mxc:CartesianSeries>
</mxc:CartesianChart.Series>
```

![chart-crosshair-showincrosshair-disabled](../../images/chart-crosshair-showincrosshair-disabled.png)

### Горизонтальный отступ метки серии Crosshair

Свойство [`CrosshairOptions.SeriesLabelIndent`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/SeriesLabelIndent.md) позволяет настроить горизонтальное расстояние между меткой серии Crosshair и вертикальной линией Crosshair. Значение по умолчанию — 2.

![chart-crosshair-serieslabelindent](../../images/chart-crosshair-serieslabelindent.png)

``` xml
<mxc:CartesianChart.CrosshairOptions>
    <mxc:CrosshairOptions SeriesLabelIndent="30"/>
</mxc:CartesianChart.CrosshairOptions>
```


### Отображение точного или интерполированного значения в метках серий Crosshair

Cartesian Chart поддерживает серии, состоящие из отсортированных дискретных точек данных. Для таких серий линии Crosshair не всегда пересекают точки данных, а чаще отображаются между ними. 
Вы можете использовать свойство [`CartesianSortedLineSeriesView.CrosshairMode`](../../API/Eremex.AvaloniaUI.Charts/CartesianSortedLineSeriesView/CrosshairMode.md), чтобы задать, привязывается ли метка Crosshair к ближайшей точке данных или отображает интерполированное значение. Доступны следующие варианты:

- [`CrosshairSeriesMode.Point`](../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesMode.md) — метка Crosshair привязывается к ближайшей точке данных и отображает её значение.
  
  ![chart-CrosshairSeriesMode-Point](../../images/chart-CrosshairSeriesMode-Point.png)

- [`CrosshairSeriesMode.Interpolate`](../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesMode.md) — метка серии Crosshair отображает интерполированное значение точки в месте пересечения вертикальной линии Crosshair с диаграммой.

  ![chart-CrosshairSeriesMode-Interpolate](../../images/chart-CrosshairSeriesMode-Interpolate.png)

Следующий код показывает, как настроить параметр [`CrosshairMode`](../../API/Eremex.AvaloniaUI.Charts/CartesianSortedLineSeriesView/CrosshairMode.md):

``` xml
<mxc:CartesianChart.Series>
    <mxc:CartesianSeries DataAdapter="{Binding Series.DataAdapter}">
        <mxc:CartesianLineSeriesView Color="{Binding Series.Color}" CrosshairMode="Interpolate">
            <mxc:CartesianLineSeriesView.LineStyle>
                <mxc:LineStyle Thickness="2" />
            </mxc:CartesianLineSeriesView.LineStyle>
        </mxc:CartesianLineSeriesView>
    </mxc:CartesianSeries>
</mxc:CartesianChart.Series>

```

### Настройка меток Crosshair для нескольких серий

#### Режим отображения меток

Когда Cartesian Chart содержит несколько серий, Crosshair отображает метку для каждой серии:

![chart-crosshair-two-series ](../../images/chart-crosshair-two-series.png)

Свойство [`CrosshairOptions.SeriesLabelMode`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/SeriesLabelMode.md) определяет, объединяются ли метки нескольких серий, и каким образом. Доступны следующие варианты:

- [`CrosshairSeriesLabelMode.Smart`](../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesLabelMode.md) (по умолчанию) — каждая серия отображает собственную метку Crosshair. Когда метки перекрываются, они объединяются в одну.
  
  ![chart-CrosshairSeriesLabelMode-smart](../../images/chart-CrosshairSeriesLabelMode-smart.png)


- [`CrosshairSeriesLabelMode.ForEachSeries`](../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesLabelMode.md) — каждая серия отображает собственную метку Crosshair. В этом режиме метки могут перекрываться.
  
  ![chart-CrosshairSeriesLabelMode-ForEachSeries](../../images/chart-CrosshairSeriesLabelMode-ForEachSeries.png)

- [`CrosshairSeriesLabelMode.ForNearestSeries`](../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesLabelMode.md) — метка Crosshair отображается только для серии, ближайшей к курсору.
  
  ![chart-CrosshairSeriesLabelMode-ForNearestSeries](../../images/chart-CrosshairSeriesLabelMode-ForNearestSeries.png)

- [`CrosshairSeriesLabelMode.OneForAllSeries`](../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesLabelMode.md) — Crosshair отображает единую метку, объединяющую информацию по всем сериям.

  ![chart-CrosshairSeriesLabelMode-OneForAllSeries](../../images/chart-CrosshairSeriesLabelMode-OneForAllSeries.png)

Этот пример включает единую метку Crosshair при наличии нескольких серий.

``` xml
<mxc:CartesianChart.CrosshairOptions>
    <mxc:CrosshairOptions SeriesLabelMode="OneForAllSeries"/>
</mxc:CartesianChart.CrosshairOptions>
```

#### Сортировка серий

Когда несколько серий объединены в одну метку Crosshair, вы можете использовать свойство [`CrosshairOptions.SeriesLabelItemSortMode`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/SeriesLabelItemSortMode.md), чтобы задать порядок отображения серий в метке. Это свойство может принимать следующие значения:

- [`CrosshairSeriesLabelItemSortMode.BySeries`](../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesLabelItemSortMode.md) (по умолчанию) — сортирует серии в порядке их добавления в коллекцию [`CartesianChart.Series`](../../API/Eremex.AvaloniaUI.Charts/CartesianChart/Series.md).

    ![chart-CrosshairSeriesLabelItemSortMode-BySeries](../../images/chart-CrosshairSeriesLabelItemSortMode-BySeries.png)

- [`CrosshairSeriesLabelItemSortMode.ByValue`](../../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesLabelItemSortMode.md) — сортирует серии по их значениям _Y_.

    ![chart-CrosshairSeriesLabelItemSortMode-ByValue](../../images/chart-CrosshairSeriesLabelItemSortMode-ByValue.png)

## Задержка отображения

Используйте свойство [`CrosshairOptions.SeriesLabelShowDelay`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/SeriesLabelShowDelay.md), чтобы задать задержку (в миллисекундах) перед отображением метки серии Crosshair.

## Включение только серий, близких к курсору

По умолчанию линейные диаграммы отображают метки Crosshair для всех серий, имеющих точки данных при текущем значении аргумента.

![chart-Crosshair-MaxPickDistance-Disabled](../../images/chart-Crosshair-MaxPickDistance-Disabled.png)

Контрол диаграммы позволяет ограничить метки Crosshair сериями, близкими к курсору. Используйте свойство [`CrosshairOptions.MaxPickDistance`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/MaxPickDistance.md), чтобы задать диапазон, в пределах которого выполняется поиск точек данных для включения в метки Crosshair. Для обычных линейных диаграмм свойство [`MaxPickDistance`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/MaxPickDistance.md) задаёт максимальное вертикальное расстояние (в пикселях) вверх или вниз.

![chart-Crosshair-MaxPickDistance](../../images/chart-Crosshair-MaxPickDistance.png)

На изображении выше только точки данных из _Series 1_ и _Series 3_ находятся в пределах диапазона, ограниченного пользовательским значением [`MaxPickDistance`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/MaxPickDistance.md). Точка данных из _Series 2_ (красная линия) выходит за пределы этого диапазона и не отображается.



Для [представлений Scatter Line](cartesian-series-views/scatter-line-series-view.md) свойство [`MaxPickDistance`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/MaxPickDistance.md) задаёт радиус круговой области вокруг курсора, в пределах которой выполняется поиск точек данных.

!!! Tip

    Чтобы отобразить метку Crosshair только для серии, ближайшей к курсору, установите свойство [`CrosshairOptions.SeriesLabelMode`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/SeriesLabelMode.md) в значение `ForNearestSeries`. См. [Режим отображения меток](#режим-отображения-меток).



## Настройка линий и меток Crosshair на осях _X_ и _Y_

Объект [`CrosshairOptions`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions.md) контрола диаграммы содержит набор свойств, позволяющих изменить визуальные параметры линий Crosshair, метки оси _X_ и метки оси _Y_.

- [`ArgumentColor`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ArgumentColor.md) — цвет фона меток оси _X_ Crosshair.
- [`ArgumentLineThickness`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ArgumentLineThickness.md) — толщина линии аргумента Crosshair.
- [`ArgumentTextColor`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ArgumentTextColor.md) — цвет текста (переднего плана) меток оси _X_ Crosshair.
- [`ValueColor`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ValueColor.md) — цвет фона меток оси _Y_ Crosshair.
- [`ValueLineThickness`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ValueLineThickness.md) — толщина линии значения Crosshair.
- [`ValueTextColor`](../../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/ValueTextColor.md) — цвет текста (переднего плана) меток оси _Y_ Crosshair.

Следующий код XAML демонстрирует, как настроить эти параметры для примера контрола диаграммы. Толщина линии Crosshair установлена равной 3. Метки Crosshair имеют серый фон, но разные цвета текста: жёлтый для меток оси _X_ и голубой для меток оси _Y_.

![crosshair-lines-and-labels-customization-example](../../images/crosshair-lines-and-labels-customization-example.png)


``` xml
<mxc:CartesianChart ...>
    <mxc:CartesianChart.CrosshairOptions>
        <mxc:CrosshairOptions 
            ArgumentColor="Gray" ArgumentTextColor="Yellow" ArgumentLineThickness="3"
            ValueColor="Gray" ValueTextColor="Cyan" ValueLineThickness="3" />
    </mxc:CartesianChart.CrosshairOptions>
</mxc:CartesianChart>
```

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
