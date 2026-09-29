---
title: Начало работы с диаграммами — паттерн MVVM
order: 9000
seealso: []
---

# Начало работы с диаграммами — паттерн MVVM

Вы можете заполнять контролы диаграмм данными, используя паттерн проектирования MVVM. Это полезно, когда требуется отобразить несколько серий данных.

Этот учебник показывает, как отрисовать два линейных графика в контроле `CartesianChart`, используя паттерн MVVM. Данные для линейных графиков в этом примере вычисляются с помощью математических функций (синус и косинус). 
Полный код этого учебника можно найти в модуле _Cartesian Chart&rarr;Line_ демонстрационного приложения.

![charts-get-started-mvvm-two-lines](../../images/charts-get-started-mvvm-two-lines.png)

## Определение View Model

Начните с определения View Model, предоставляющих данные и настройки серий для контрола диаграммы.

- _CartesianLineSeriesViewViewModel_ — главная View Model, которая будет назначена в качестве Data Context контрола диаграммы. Главная View Model предоставляет свойство _CartesianLineSeriesViewViewModel.Series_, которое задаёт коллекцию View Model серий данных.

- _SeriesViewModel_ — View Model для серии данных.


``` cs
// The main View Model
public partial class CartesianLineSeriesViewViewModel : ChartsPageViewModel
{
    static double Sin(double argument) => Math.Sin(argument);
    static double Cos(double argument) => Math.Cos(argument);

    const int ItemCount = 100;
    const double Step = 4 * Math.PI / ItemCount;

    // A collection of View Models used to create data series.
    [ObservableProperty] ObservableCollection<SeriesViewModel> series = new()
    {
        new SeriesViewModel { Color = Color.FromArgb(255, 189, 20, 54), DataAdapter = new FormulaDataAdapter(0, Step, ItemCount, Sin)},
        new SeriesViewModel { Color = Color.FromArgb(255, 0, 120, 122), DataAdapter = new FormulaDataAdapter(0, Step, ItemCount, Cos)},
    };
}

// A View Model for a data series.
public partial class SeriesViewModel : ObservableObject
{
    [ObservableProperty] string axisXKey;
    [ObservableProperty] string axisYKey;
    [ObservableProperty] Color color;
    [ObservableProperty] ISeriesDataAdapter dataAdapter;
}
```

Коллекция _CartesianLineSeriesViewViewModel.Series_ инициализируется двумя View Model серий. Cartesian Chart отрисует их как две серии данных.

View Model серии данных (_SeriesViewModel_) предоставляет свойства, задающие данные и цвет для отрисовки серии в контроле диаграммы:

- _Color_ — цвет для отрисовки серии данных.
- _DataAdapter_ — объект `ISeriesDataAdapter`, предоставляющий данные для серии. 
  
  Eremex Charts поставляются с несколькими адаптерами данных для различных типов данных (числовых, дата-время и качественных). Все адаптеры данных реализуют интерфейс `ISeriesDataAdapter`.
  
  В этом учебнике используется объект `Eremex.AvaloniaUI.Charts.FormulaDataAdapter`. Он задаёт функцию, возвращающую числовые значения _Y_ с шагом _Step_. 
  
  Несколько примеров других адаптеров данных:
  - `SortedNumericDataAdapter` — предоставляет пары (числовое значение X, числовое значение Y), отсортированные по значениям X.
  - `QualitativeDataAdapter` — предоставляет пары (строковое значение X, числовое значение Y).

  Подробнее см. в разделе [Cartesian Chart](cartesian-chart.md).

## Создание контрола диаграммы

В XAML создайте контрол `CartesianChart` и инициализируйте его свойства `CartesianChart.SeriesSource` и `CartesianChart.SeriesTemplate`:

- `CartesianChart.SeriesSource` — коллекция View Model, представляющих серии данных (коллекция _CartesianLineSeriesViewViewModel.Series_, хранящая объекты _SeriesViewModel_).
  
  Предполагается, что Data Context контрола диаграммы установлен в объект _CartesianLineSeriesViewViewModel_.

- `CartesianChart.SeriesTemplate` — шаблон, создающий объект `CartesianSeries` из View Model серии. Класс `CartesianSeries` инкапсулирует одну серию данных в контроле `CartesianChart`.

``` xml
<mxc:CartesianChart Grid.Column="0" Classes="DemoChart" 
 SeriesSource="{Binding Series}" x:Name="chart1">
    <mxc:CartesianChart.SeriesTemplate>
        <DataTemplate x:DataType="vm:SeriesViewModel">
            <mxc:CartesianSeries DataAdapter="{Binding DataAdapter}">
                <mxc:CartesianLineSeriesView Color="{Binding Color}"
                                             ShowMarkers="True"
                                             MarkerSize="4"
                                             Thickness="2"/>
            </mxc:CartesianSeries>
        </DataTemplate>
    </mxc:CartesianChart.SeriesTemplate>
</mxc:CartesianChart>
```

При создании объекта `CartesianSeries` инициализируйте следующие свойства, чтобы задать данные и представление серии:

- `CartesianSeries.DataAdapter` — адаптер данных, предоставляющий данные. Установите это свойство равным свойству _DataAdapter_, определённому в View Model.
- `CartesianSeries.View` — представление серии, определяющее визуальное отображение серии данных. 

## Настройка представления серии

Свойство `CartesianSeries.View` задаёт визуальное отображение серии данных. В XAML вы можете указать представление в качестве содержимого объекта `CartesianSeries`.

``` xml
<mxc:CartesianSeries DataAdapter="{Binding DataAdapter}">
    <mxc:CartesianLineSeriesView Color="{Binding Color}"
                                    ShowMarkers="True"
                                    MarkerSize="4"
                                    Thickness="2"/>
</mxc:CartesianSeries>
```

В этом учебнике свойство `CartesianSeries.View` инициализируется объектом `CartesianLineSeriesView`, чтобы отобразить данные в виде линии, соединяющей исходные точки данных.

![get-started-view-example-CartesianLineSeriesView](../../images/get-started-view-example-CartesianLineSeriesView.png)

Чтобы представить данные другим образом в ваших проектах, используйте другие представления серий (классы-наследники `SeriesViewBase`). Несколько примеров доступных представлений серий показаны ниже:

![get-started-view-example-others](../../images/get-started-view-example-others.png)


Представление серии содержит настройки, позволяющие изменить стиль отображения серии. 

``` xml
<mxc:CartesianLineSeriesView Color="{Binding Color}"
                             ShowMarkers="True"
                             MarkerSize="4"
                             Thickness="2"/>
```

Например, класс `CartesianLineSeriesView` предоставляет следующие свойства:

- `Color` — цвет для отрисовки серии.
- `CrosshairMode` — определяет, отображать ли интерполированное значение _Y_ или значение _Y_ ближайшей точки, когда активна функция Crosshair и включена опция `ShowInCrosshair`.
- `MarkerSize` — задаёт размер маркера точки.
- `MarkerImage` — позволяет указать пользовательское изображение для использования в качестве маркеров точек данных. Для назначения SVG-изображений используйте объекты класса `SvgImage`.
- `MarkerImageCss` — код CSS, позволяющий настроить цвета элементов указанного SVG-изображения (`MarkerImage`).
- `ShowInCrosshair` — определяет, отображать ли значение _Y_ диаграммы в точке пересечения вертикальной линии Crosshair с графиком.
- `ShowMarkers` — включает или отключает маркеры точек.
- `Thickness` — задаёт толщину линии.

<!-- TODO
Desribe MarkerImage and MarkerImageCss in greater detail.
 -->


## Создание осей диаграммы

Контрол `CartesianChart` автоматически создаёт декартовы оси (ось X и ось Y), если вы не определяете их вручную. Если вы хотите настроить оси в XAML, добавьте объекты `AxisX` и/или `AxisY` в коллекции `CartesianChart.AxesX`/`CartesianChart.AxesY`, а затем измените параметры осей.

<!-- TODO
how to define an axis for the second series

check the text: automatically creates cartesian axes (the X-axis and Y-axis) if you do not define them manually. If you want to customize axes in XAML, add them to the `CartesianChart.AxesX` and `CartesianChart.AxesY` collections, and then modify settings of these axes.
 -->


``` xml
 <mxc:CartesianChart Grid.Column="0" Classes="DemoChart" SeriesSource="{Binding Series}" x:Name="chart1">
    <!-- ... -->
    <mxc:CartesianChart.AxesX>
        <mxc:AxisX ShowTitle="True"  />
    </mxc:CartesianChart.AxesX>
    <mxc:CartesianChart.AxesY>
        <mxc:AxisY ShowTitle="False" />
    </mxc:CartesianChart.AxesY>
</mxc:CartesianChart>
``` 

В следующем списке приведены основные настройки декартовых осей:

- `ConstantLines` и `ConstantLinesSource` — позволяют отрисовать постоянные линии для конкретных значений. См. также `Strips` и `StripsSource`.
- `EnableScrolling` — позволяет пользователю прокручивать ось операцией перетаскивания мышью.
- `EnableZooming` — позволяет пользователю масштабировать ось.
- `MinorCount` — задаёт количество второстепенных отметок (tickmarks) и линий сетки.
- `Position` — задаёт положение оси. Доступные варианты: `Near` (ось X отображается снизу, ось Y — у левого края диаграммы) и `Far` (ось X отображается сверху, ось Y — у правого края диаграммы).
- `Range` — настройки диапазона значений.
- `ScaleOptions` — задаёт параметры масштаба.
- `ShowAxisLine` — задаёт видимость линии оси.
- `ShowInterlacing` — определяет, закрашивать ли чередующиеся полосы между основными линиями сетки.
- `ShowLabels` — задаёт видимость меток, соответствующих основным отметкам.
- `ShowMajorGridlines` — задаёт видимость линий сетки, соответствующих основным отметкам.
- `ShowMajorTickmarks` — задаёт видимость основных отметок.
- `ShowMinorGridlines` — задаёт видимость линий сетки, соответствующих второстепенным отметкам.
- `ShowMinorTickmarks` — задаёт видимость второстепенных отметок.
- `ShowTitle` — задаёт видимость заголовка оси (свойство `Title`).
- `Strips` и `StripsSource` — позволяют закрасить диапазоны между конкретными значениями. См. также `ConstantLines` и `ConstantLinesSource`.
- `Thickness` — толщина линии оси.
- `Title` — задаёт заголовок оси.
- `TitlePosition` — задаёт положение заголовка оси.


## Результат

Запустите приложение, чтобы увидеть результат этого учебника. Контрол `CartesianChart` отображает две серии данных с использованием представления Line series view. 

![charts-get-started-mvvm-two-lines](../../images/charts-get-started-mvvm-two-lines.png)

## Полный код

Полный код этого учебника можно найти в модуле _Cartesian Chart&rarr;Line_ демонстрационного приложения.


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
