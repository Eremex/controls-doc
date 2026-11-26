## Пространство имён Eremex.AvaloniaUI.Charts

| открытый тип | описание |
| --- | --- |
| abstract class [Axis](./Axis.md) | Служит базовым классом для осей диаграммы, которые сопоставляют значения данных с позициями на экране и предоставляют метки, деления и линии сетки. |
| enum [AxisPosition](./AxisPosition.md) | Перечисляет значения, задающие, с какой стороны области построения отображается ось. |
| abstract class [AxisRange](./AxisRange.md) | Служит базовым классом для диапазонов осей, границы которых можно задавать и пересчитывать по данным серий. |
| abstract class [AxisRangeBase](./AxisRangeBase.md) | Служит базовым классом для диапазонов осей, которые определяют окно значений, отображаемых осью в данный момент. |
| enum [AxisTitlePosition](./AxisTitlePosition.md) | Перечисляет значения, задающие расположение заголовка оси относительно меток оси. |
| enum [AxisType](./AxisType.md) | Перечисляет значения, задающие вид данных серии, для которого предназначена ось. |
| class [AxisX](./AxisX.md) | Представляет ось аргументов декартовой диаграммы. Отображает аргументы точек данных серий. Ось располагается вдоль горизонтального края области построения или вдоль вертикального края, если диаграмма меняет оси местами. |
| struct [AxisXCoordinate](./AxisXCoordinate.md) | Представляет значение на определённой оси X. |
| class [AxisXRange](./AxisXRange.md) | Представляет диапазон горизонтальной оси, например AxisX или HeatmapAxisX. |
| class [AxisY](./AxisY.md) | Представляет ось значений декартовой диаграммы. Отображает значения точек данных серий. Ось располагается вдоль вертикального края области построения или вдоль горизонтального края, если диаграмма меняет оси местами. |
| struct [AxisYCoordinate](./AxisYCoordinate.md) | Представляет значение на определённой оси Y. |
| class [AxisYRange](./AxisYRange.md) | Представляет диапазон вертикальной оси, например AxisY или PolarAxisY. |
| class [CandlestickDataAdapter](./CandlestickDataAdapter.md) | Преобразует аргументы даты и времени и значения открытия, максимума, минимума и закрытия в точки данных серии. Аргументы должны быть отсортированы по возрастанию, чтобы свечи отображались в правильном порядке. |
| class [CartesianAreaSeriesView](./CartesianAreaSeriesView.md) | Отображает данные декартовой серии в виде области, залитой между ломаной линией и нулевой линией оси значений. |
| abstract class [CartesianAxis](./CartesianAxis.md) | Служит базовым классом для осей декартовой диаграммы. Добавляет позицию, заголовок и расположение заголовка. |
| class [CartesianCandlestickSeriesView](./CartesianCandlestickSeriesView.md) | Отображает данные декартовой серии в виде свечей, построенных по значениям открытия, максимума, минимума и закрытия каждой точки данных. |
| class [CartesianChart](./CartesianChart.md) | Отображает серии в прямоугольной области графика, заданной осью X и осью Y. |
| class [CartesianDiagramCoordinates](./CartesianDiagramCoordinates.md) | Представляет точку [`CartesianChart`](./CartesianChart.md), выраженную в значениях её осей X и Y. |
| class [CartesianFullStackedAreaSeriesView](./CartesianFullStackedAreaSeriesView.md) | Отображает несколько декартовых серий в виде областей с накоплением, значения которых нормализуются до ста процентов в каждом значении оси X. |
| class [CartesianLineSeriesView](./CartesianLineSeriesView.md) | Отображает данные декартовой серии в виде ломаной линии, соединяющей точки, отсортированные по значению оси X. |
| abstract class [CartesianLineSeriesViewBase](./CartesianLineSeriesViewBase.md) | Служит базовым классом для представлений декартовых серий, соединяющих точки данных линией. |
| enum [CartesianLollipopOrientation](./CartesianLollipopOrientation.md) | Перечисляет значения, задающие, растут ли стебли леденцов вертикально или горизонтально. |
| class [CartesianLollipopSeriesView](./CartesianLollipopSeriesView.md) | Отображает данные декартовой серии в виде леденцов. Каждая точка данных отображается как тонкий стебель, который начинается на нулевой линии и заканчивается маркером. |
| class [CartesianPointSeriesView](./CartesianPointSeriesView.md) | Отображает данные декартовой серии в виде набора не соединённых друг с другом маркеров. |
| class [CartesianRangeAreaSeriesView](./CartesianRangeAreaSeriesView.md) | Отображает данные декартовой серии в виде области, залитой между первым и вторым значением каждой точки данных, с линией вдоль каждой границы. |
| class [CartesianScatterLineSeriesView](./CartesianScatterLineSeriesView.md) | Отображает данные декартовой серии в виде ломаной линии, соединяющей точки в том порядке, в котором они переданы. |
| class [CartesianSeries](./CartesianSeries.md) | Представляет серию декартовой диаграммы. Серия отображает данные, предоставляемые её адаптером данных, в области построения с горизонтальной и вертикальной осями. |
| class [CartesianSeriesCollection](./CartesianSeriesCollection.md) | Хранит серии декартовой диаграммы и уведомляет диаграмму об изменении серий. |
| abstract class [CartesianSeriesView](./CartesianSeriesView.md) | Служит базовым классом для представлений серий декартовой диаграммы. |
| class [CartesianSideBySideBarSeriesView](./CartesianSideBySideBarSeriesView.md) | Отображает несколько декартовых серий в виде столбцов, расположенных рядом в одном значении оси X. |
| class [CartesianSideBySideRangeBarSeriesView](./CartesianSideBySideRangeBarSeriesView.md) | Отображает несколько декартовых серий в виде расположенных рядом столбцов, охватывающих диапазон между первым и вторым значением каждой точки данных. |
| class [CartesianSortedLineSeriesView](./CartesianSortedLineSeriesView.md) | Соединяет точки данных декартовой серии линией, сортируя точки по значению оси X. |
| class [CartesianStackedAreaSeriesView](./CartesianStackedAreaSeriesView.md) | Отображает несколько декартовых серий в виде областей с накоплением. Каждая область начинается там, где заканчивается предыдущая. |
| class [CartesianStepAreaSeriesView](./CartesianStepAreaSeriesView.md) | Отображает данные декартовой серии в виде области, залитой между ступенчатой линией и нулевой линией оси значений. |
| class [CartesianStepLineSeriesView](./CartesianStepLineSeriesView.md) | Отображает данные декартовой серии в виде ступенчатой линии, идущей горизонтально, а затем вертикально между точками, отсортированными по значению оси X. |
| abstract class [ChartControl](./ChartControl.md) | Служит базовым классом для контролов диаграмм, отображающих данные в системе координат. |
| abstract class [ChartElement](./ChartElement.md) | Служит базовым классом для стилизуемых элементов диаграммы, определяющих её внешний вид, таких как оси, серии и стили линий. |
| abstract class [ChartElementBase](./ChartElementBase.md) | Служит базовым классом для облегчённых элементов диаграммы, которые не отрисовываются как контролы. |
| abstract class [ChartElementChangedEventArgs](./ChartElementChangedEventArgs.md) | Предоставляет данные для события [`ChartElementChanged`](./ChartElement/ChartElementChanged.md). |
| delegate [ChartElementChangedEventHandler](./ChartElementChangedEventHandler.md) | Представляет метод, обрабатывающий событие [`ChartElementChanged`](./ChartElement/ChartElementChanged.md). |
| class [ChartElementCollection&lt;T&gt;](./ChartElementCollection-T.md) | Представляет коллекцию элементов диаграммы, которую можно заполнить, либо добавляя элементы напрямую, либо привязывая коллекцию к источнику данных через соответствующие свойства источника элементов и шаблона контрола-владельца. |
| class [ChartElementCollectionChangedEventArgs](./ChartElementCollectionChangedEventArgs.md) | Предоставляет данные для уведомления об изменении элементов коллекции элементов диаграммы. |
| class [ConstantLine](./ConstantLine.md) | Представляет прямую линию, проведённую через область построения на фиксированном значении оси, к которой она относится. |
| enum [ConstantLineTitlePosition](./ConstantLineTitlePosition.md) | Перечисляет значения, задающие расположение заголовка постоянной линии относительно линии. |
| class [CrosshairAllSeriesLabelControl](./CrosshairAllSeriesLabelControl.md) | Отображает значения всех серий в позиции перекрестия. |
| class [CrosshairAllSeriesLabelControlData](./CrosshairAllSeriesLabelControlData.md) | Предоставляет содержимое метки перекрестия, отображающей значения всех серий. |
| class [CrosshairOptions](./CrosshairOptions.md) | Определяет внешний вид и поведение перекрестия, отслеживающего указатель над диаграммой. |
| class [CrosshairSeriesLabelItem](./CrosshairSeriesLabelItem.md) | Представляет одну строку серии, отображаемую меткой перекрестия. |
| enum [CrosshairSeriesLabelItemSortMode](./CrosshairSeriesLabelItemSortMode.md) | Перечисляет значения, задающие порядок отображения серий в метках перекрестия. |
| enum [CrosshairSeriesLabelMode](./CrosshairSeriesLabelMode.md) | Перечисляет значения, задающие, значения скольких серий показывает перекрестие. |
| class [CrosshairSeriesLabelSeriesValueItem](./CrosshairSeriesLabelSeriesValueItem.md) | Представляет одно значение серии, отображаемое меткой перекрестия. |
| class [CrosshairSeriesLabelValue](./CrosshairSeriesLabelValue.md) | Представляет одно значение, отображаемое меткой серии перекрестия. |
| enum [CrosshairSeriesMode](./CrosshairSeriesMode.md) | Перечисляет значения, задающие, как перекрестие находит значение серии в позиции указателя. |
| abstract class [CrosshairSeriesViewBase](./CrosshairSeriesViewBase.md) | Служит базовым классом для представлений серий, которые может находить перекрестие. |
| class [CrosshairSingleSeriesLabelControl](./CrosshairSingleSeriesLabelControl.md) | Отображает значения одной серии в позиции перекрестия. |
| class [CrosshairSingleSeriesLabelControlData](./CrosshairSingleSeriesLabelControlData.md) | Предоставляет содержимое метки перекрестия, отображающей значения одной серии. |
| class [DateTimeRangeDataAdapter](./DateTimeRangeDataAdapter.md) | Преобразует аргументы даты и времени и пары числовых значений в точки данных серии. Аргументы должны быть отсортированы по возрастанию, чтобы серия диапазонов могла отображать их в правильном порядке. |
| class [DateTimeScaleOptions](./DateTimeScaleOptions.md) | Определяет шкалу, измеряющую значения даты и времени в настраиваемых единицах. |
| enum [DateTimeUnit](./DateTimeUnit.md) | Перечисляет значения, задающие детализацию, используемую при автоматическом масштабировании или настройке оси даты и времени. |
| class [FormulaDataAdapter](./FormulaDataAdapter.md) | Создаёт точки данных серии по формуле. Аргументы расположены равномерно: они начинаются с начального аргумента и увеличиваются на шаг аргумента, а значения вычисляются по формуле. |
| class [FuncLabelFormatter](./FuncLabelFormatter.md) | Форматирует метки оси, вызывая функцию, предоставленную пользователем. |
| class [Heatmap](./Heatmap.md) | Отображает двумерную матрицу значений в виде сетки цветных ячеек, цвет каждой из которых выбирается с помощью [`IHeatmapColorProvider`](./IHeatmapColorProvider.md). |
| abstract class [HeatmapAxis](./HeatmapAxis.md) | Служит базовым классом для осей тепловой карты. Использует качественную шкалу и отображается вдоль внешнего края области построения. |
| class [HeatmapAxisX](./HeatmapAxisX.md) | Представляет угловую ось тепловой карты. Отображает угловой размах выборок тепловой карты. |
| class [HeatmapAxisY](./HeatmapAxisY.md) | Представляет радиальную ось тепловой карты. Отображает расстояние от центра области построения. |
| class [HeatmapDataAdapter](./HeatmapDataAdapter.md) | Предоставляет двумерную таблицу значений, которую отображает серия тепловой карты. |
| class [HeatmapDiagramCoordinates](./HeatmapDiagramCoordinates.md) | Представляет ячейку [`Heatmap`](./Heatmap.md), определяемую именами её колонки и строки. |
| class [HeatmapGrayscaleColorProvider](./HeatmapGrayscaleColorProvider.md) | Предоставляет цвет ячейки тепловой карты, сопоставляя значение ячейки с оттенком серого. |
| class [HeatmapRangeColorProvider](./HeatmapRangeColorProvider.md) | Предоставляет цвет ячейки тепловой карты путём интерполяции между заданными пользователем опорными цветами. |
| class [HeatmapRangeStop](./HeatmapRangeStop.md) | Представляет одну опорную точку цветовой шкалы тепловой карты. Опорная точка связывает значение с цветом, который отображает ячейка тепловой карты, содержащая это значение. |
| interface [IAxisLabelFormatter](./IAxisLabelFormatter.md) | Преобразует значение оси в текст, отображаемый в виде метки оси. |
| interface [IHeatmapColorProvider](./IHeatmapColorProvider.md) | Предоставляет цвет ячейки тепловой карты для заданного значения данных. |
| interface [INumericAxisGridCalculator](./INumericAxisGridCalculator.md) | Предоставляет позиции линий сетки и делений, отображаемых на числовой оси. |
| interface [ISeriesDataAdapter](./ISeriesDataAdapter.md) | Определяет источник данных серии. Адаптер данных преобразует значения привязанной исходной коллекции в аргументы и значения, используемые серией и её осями. |
| abstract class [LinearAxis](./LinearAxis.md) | Служит базовым классом для осей, размещающих параметры своей шкалы вдоль прямой линии. |
| abstract class [LinearNumericScaleOptions](./LinearNumericScaleOptions.md) | Служит базовым классом для параметров числовой шкалы, поддерживающих линейную и логарифмическую шкалы. |
| class [LineStyle](./LineStyle.md) | Описывает обводку, используемую для отрисовки линий серий, линий осей и других контуров диаграммы. |
| struct [NumericGridEntry](./NumericGridEntry.md) | Представляет одно значение сетки числовой оси. |
| class [NumericRangeDataAdapter](./NumericRangeDataAdapter.md) | Преобразует числовые аргументы и пары числовых значений в точки данных серии. Аргументы должны быть отсортированы по возрастанию, чтобы серия диапазонов могла отображать их в правильном порядке. |
| class [NumericScaleOptions](./NumericScaleOptions.md) | Определяет числовую шкалу, которая по умолчанию линейная и может быть переключена на логарифмическую. |
| class [PercentLabelFormatter](./PercentLabelFormatter.md) | Форматирует метки оси в процентах. Значение 0.5 отображается как 50.00 процентов. |
| class [PolarAreaSeriesView](./PolarAreaSeriesView.md) | Отображает данные полярной серии в виде области, залитой между ломаной линией и центром области построения. |
| class [PolarAxisX](./PolarAxisX.md) | Представляет угловую ось полярной диаграммы. Отображает значения от нуля до 360 градусов. |
| class [PolarAxisXRange](./PolarAxisXRange.md) | Представляет диапазон PolarAxisX, который всегда охватывает полный оборот от 0 до 360 градусов. |
| class [PolarAxisY](./PolarAxisY.md) | Представляет радиальную ось полярной диаграммы. Отображает расстояние от центра области построения. |
| class [PolarChart](./PolarChart.md) | Отображает серии в круглой области графика, где ось X — это угол в радианах вокруг центра, а ось Y — расстояние от этого центра. |
| class [PolarDiagramCoordinates](./PolarDiagramCoordinates.md) | Представляет точку [`PolarChart`](./PolarChart.md), выраженную углом и значением. |
| class [PolarLineSeriesView](./PolarLineSeriesView.md) | Отображает данные полярной серии в виде ломаной линии, соединяющей точки, отсортированные по значению угловой оси. |
| abstract class [PolarLineSeriesViewBase](./PolarLineSeriesViewBase.md) | Служит базовым классом для представлений полярных серий, соединяющих точки данных линией. |
| class [PolarNumericScaleOptions](./PolarNumericScaleOptions.md) | Определяет числовую шкалу для угловой оси полярной диаграммы. Выбирает автоматически вычисляемый шаг сетки из набора множителей, подходящих для углов. |
| class [PolarPointSeriesView](./PolarPointSeriesView.md) | Отображает данные полярной серии в виде набора не соединённых друг с другом маркеров. |
| class [PolarRangeAreaSeriesView](./PolarRangeAreaSeriesView.md) | Отображает данные полярной серии в виде области, залитой между первым и вторым значением каждой точки данных, с линией вдоль каждой границы. |
| class [PolarScatterLineSeriesView](./PolarScatterLineSeriesView.md) | Отображает данные полярной серии в виде ломаной линии, соединяющей точки в том порядке, в котором они переданы. |
| class [PolarSeries](./PolarSeries.md) | Представляет серию полярной диаграммы. Серия отображает данные, предоставляемые её адаптером данных, в области построения с угловой и радиальной осями. |
| class [PolarSeriesCollection](./PolarSeriesCollection.md) | Хранит серии полярной диаграммы и уведомляет диаграмму об изменении серий. |
| abstract class [PolarSeriesView](./PolarSeriesView.md) | Служит базовым классом для представлений серий полярной диаграммы. |
| abstract class [PredefinedRange](./PredefinedRange.md) | Служит базовым классом для диапазонов осей с фиксированными границами, которые пользователь не может изменить. |
| class [QualitativeDataAdapter](./QualitativeDataAdapter.md) | Преобразует имена категорий и числовые значения в точки данных серии. Аргументы рассматриваются как имена категорий, а не как числа, поэтому их можно указывать в любом порядке. |
| class [QualitativeRangeDataAdapter](./QualitativeRangeDataAdapter.md) | Преобразует имена категорий и пары числовых значений в точки данных серии. Аргументы рассматриваются как имена категорий, а не как числа, поэтому их можно указывать в любом порядке. |
| class [QualitativeScaleOptions](./QualitativeScaleOptions.md) | Определяет шкалу, на которой деления размещаются через фиксированное количество категорий, а не на числовых значениях. |
| abstract class [ScaleOptions](./ScaleOptions.md) | Служит базовым классом для параметров шкалы, определяющих сопоставление исходных значений оси с позициями на экране, метками, делениями и линиями сетки. |
| enum [ScaleType](./ScaleType.md) | Перечисляет значения, задающие вид значений, предоставляемых адаптером данных серии. |
| class [ScatterDataAdapter](./ScatterDataAdapter.md) | Преобразует числовые аргументы и значения в точки данных серии. Аргументы можно указывать в любом порядке, чтобы точечная серия отображала точки именно так, как они переданы. |
| abstract class [Series](./Series.md) | Служит базовым классом для серий диаграмм. Серия владеет отображаемыми данными и представлением серии, определяющим её внешний вид. |
| class [SeriesDataAdapterDataChangedEventArgs](./SeriesDataAdapterDataChangedEventArgs.md) | Предоставляет данные для события изменения данных адаптера данных серии. |
| delegate [SeriesDataAdapterDataChangedEventHandler](./SeriesDataAdapterDataChangedEventHandler.md) | Представляет метод, обрабатывающий событие изменения данных адаптера данных серии. |
| enum [SeriesDataMemberType](./SeriesDataMemberType.md) | Перечисляет значения, задающие член точки данных серии, к которому относится значение. |
| enum [SeriesDataUpdateType](./SeriesDataUpdateType.md) | Перечисляет значения, задающие вид изменения данных адаптера данных серии. |
| abstract class [SeriesViewBase](./SeriesViewBase.md) | Служит базовым классом для представлений серий. Представление серии определяет внешний вид данных, отображаемых серией. |
| class [SmithAxisX](./SmithAxisX.md) | Представляет угловую ось диаграммы Смита. Отображает значения импеданса или адмиттанса. |
| class [SmithAxisXRange](./SmithAxisXRange.md) | Представляет диапазон SmithAxisX, который охватывает угловой размах полного оборота. |
| class [SmithAxisY](./SmithAxisY.md) | Представляет радиальную ось диаграммы Смита. Отображает значения импеданса или адмиттанса. |
| class [SmithAxisYRange](./SmithAxisYRange.md) | Представляет диапазон SmithAxisY, который охватывает полное расстояние от центра до внешнего края области построения в обоих направлениях. |
| class [SmithChart](./SmithChart.md) | Отображает серии на диаграмме Смита — круговой диаграмме импеданса, широко используемой в радиочастотной технике для построения коэффициентов отражения. |
| class [SmithDiagramCoordinates](./SmithDiagramCoordinates.md) | Представляет точку [`SmithChart`](./SmithChart.md), выраженную аргументом и значением. |
| abstract class [SmithLineSeriesViewBase](./SmithLineSeriesViewBase.md) | Служит базовым классом для представлений серий Смита, соединяющих точки данных линией. |
| class [SmithPointSeriesView](./SmithPointSeriesView.md) | Отображает данные серии Смита в виде набора не соединённых друг с другом маркеров. |
| class [SmithScaleOptions](./SmithScaleOptions.md) | Определяет фиксированную шкалу оси диаграммы Смита. Позиции линий сетки задаются диаграммой и не могут быть изменены. |
| class [SmithScatterLineSeriesView](./SmithScatterLineSeriesView.md) | Отображает данные серии Смита в виде ломаной линии, соединяющей точки в том порядке, в котором они переданы. |
| class [SmithSeries](./SmithSeries.md) | Представляет серию диаграммы Смита. Серия отображает данные, предоставляемые её адаптером данных, на круге импеданса области построения. |
| class [SmithSeriesCollection](./SmithSeriesCollection.md) | Хранит серии диаграммы Смита и уведомляет диаграмму об изменении серий. |
| abstract class [SmithSeriesView](./SmithSeriesView.md) | Служит базовым классом для представлений серий диаграммы Смита. |
| class [SortedDateTimeDataAdapter](./SortedDateTimeDataAdapter.md) | Преобразует аргументы даты и времени и числовые значения в точки данных серии. Аргументы должны быть отсортированы по возрастанию, чтобы линейная серия могла соединить их в правильном порядке. |
| class [SortedNumericDataAdapter](./SortedNumericDataAdapter.md) | Преобразует числовые аргументы и значения в точки данных серии. Аргументы должны быть отсортированы по возрастанию, чтобы линейная серия могла соединить их в правильном порядке. |
| class [SortedTimeSpanDataAdapter](./SortedTimeSpanDataAdapter.md) | Преобразует аргументы-интервалы времени и числовые значения в точки данных серии. Аргументы должны быть отсортированы по возрастанию, чтобы линейная серия могла соединить их в правильном порядке. |
| class [Strip](./Strip.md) | Представляет затенённую полосу, отображаемую через область построения между двумя значениями оси, к которой она относится. |
| class [SummaryCandlestickDataAdapter](./SummaryCandlestickDataAdapter.md) | Сводит аргументы даты и времени в точки данных свечей. Все исходные значения, попадающие в одну единицу измерения, образуют одну свечу, в которой значения открытия и закрытия — это первое и последнее значения группы, а минимальное и максимальное значения — минимум и максимум группы. |
| class [TimeSpanRangeDataAdapter](./TimeSpanRangeDataAdapter.md) | Преобразует аргументы-интервалы времени и пары числовых значений в точки данных серии. Аргументы должны быть отсортированы по возрастанию, чтобы серия диапазонов могла отображать их в правильном порядке. |
| class [TimeSpanScaleOptions](./TimeSpanScaleOptions.md) | Определяет шкалу, измеряющую интервалы времени в настраиваемых единицах. |
| enum [TimeSpanUnit](./TimeSpanUnit.md) | Перечисляет значения, задающие детализацию, используемую при автоматическом масштабировании или настройке оси интервалов времени. |

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Charts.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
