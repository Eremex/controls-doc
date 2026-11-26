## Eremex.AvaloniaUI.Charts 命名空间

| 公共类型 | 说明 |
| --- | --- |
| abstract class [Axis](./Axis.md) | 用作图表轴的基类，图表轴将数据值映射到屏幕位置，并提供标签、刻度线和网格线。 |
| enum [AxisPosition](./AxisPosition.md) | 列出指定轴绘制在绘图区域哪一侧的值。 |
| abstract class [AxisRange](./AxisRange.md) | 用作轴范围的基类，此类轴范围的边界可以设置，也可以根据系列数据重新计算。 |
| abstract class [AxisRangeBase](./AxisRangeBase.md) | 用作轴范围的基类，轴范围定义了轴当前显示的值窗口。 |
| enum [AxisTitlePosition](./AxisTitlePosition.md) | 列出指定轴标题相对于轴标签放置位置的值。 |
| enum [AxisType](./AxisType.md) | 列出指定轴所针对的系列数据类型的值。 |
| class [AxisX](./AxisX.md) | 表示笛卡尔图表的参数轴，用于显示系列数据点的参数。该轴沿绘图区域的水平边缘绘制；当图表交换坐标轴时，则沿垂直边缘绘制。 |
| struct [AxisXCoordinate](./AxisXCoordinate.md) | 表示特定 X 轴上的值。 |
| class [AxisXRange](./AxisXRange.md) | 表示水平轴（例如 AxisX 或 HeatmapAxisX）的范围。 |
| class [AxisY](./AxisY.md) | 表示笛卡尔图表的值轴，用于显示系列数据点的值。该轴沿绘图区域的垂直边缘绘制；当图表交换坐标轴时，则沿水平边缘绘制。 |
| struct [AxisYCoordinate](./AxisYCoordinate.md) | 表示特定 Y 轴上的值。 |
| class [AxisYRange](./AxisYRange.md) | 表示垂直轴（例如 AxisY 或 PolarAxisY）的范围。 |
| class [CandlestickDataAdapter](./CandlestickDataAdapter.md) | 将日期和时间参数以及开盘、最高、最低和收盘值转换为系列数据点。参数必须按升序排序，以便按正确的顺序绘制 K 线。 |
| class [CartesianAreaSeriesView](./CartesianAreaSeriesView.md) | 将笛卡尔系列的数据显示为在折线与值轴零线之间填充的区域。 |
| abstract class [CartesianAxis](./CartesianAxis.md) | 用作笛卡尔图表轴的基类。它添加了位置、标题和标题位置。 |
| class [CartesianCandlestickSeriesView](./CartesianCandlestickSeriesView.md) | 将笛卡尔系列的数据显示为根据每个数据点的开盘、最高、最低和收盘值构建的 K 线。 |
| class [CartesianChart](./CartesianChart.md) | 在由 X 轴和 Y 轴定义的矩形绘图区中显示系列。 |
| class [CartesianDiagramCoordinates](./CartesianDiagramCoordinates.md) | 表示 [`CartesianChart`](./CartesianChart.md) 中以其 X 轴和 Y 轴的值表示的点。 |
| class [CartesianFullStackedAreaSeriesView](./CartesianFullStackedAreaSeriesView.md) | 将多个笛卡尔系列显示为堆叠面积，其值在每个 X 轴值处归一化为百分之百。 |
| class [CartesianLineSeriesView](./CartesianLineSeriesView.md) | 将笛卡尔系列的数据显示为连接按 X 轴值排序的点的折线。 |
| abstract class [CartesianLineSeriesViewBase](./CartesianLineSeriesViewBase.md) | 用作使用线条连接数据点的笛卡尔系列视图的基类。 |
| enum [CartesianLollipopOrientation](./CartesianLollipopOrientation.md) | 列出指定棒棒糖图的茎是垂直还是水平延伸的值。 |
| class [CartesianLollipopSeriesView](./CartesianLollipopSeriesView.md) | 将笛卡尔系列的数据显示为棒棒糖图。每个数据点都绘制为一根细茎，从零线开始，以标记结束。 |
| class [CartesianPointSeriesView](./CartesianPointSeriesView.md) | 将笛卡尔系列的数据显示为一组彼此不相连的标记。 |
| class [CartesianRangeAreaSeriesView](./CartesianRangeAreaSeriesView.md) | 将笛卡尔系列的数据显示为在每个数据点的第一个值和第二个值之间填充的区域，并沿每条边界绘制一条线。 |
| class [CartesianScatterLineSeriesView](./CartesianScatterLineSeriesView.md) | 将笛卡尔系列的数据显示为按提供顺序连接各点的折线。 |
| class [CartesianSeries](./CartesianSeries.md) | 表示笛卡尔图表的系列。该系列在具有水平轴和垂直轴的绘图区域中绘制由其数据适配器提供的数据。 |
| class [CartesianSeriesCollection](./CartesianSeriesCollection.md) | 存储笛卡尔图表的系列，并在系列更改时通知图表。 |
| abstract class [CartesianSeriesView](./CartesianSeriesView.md) | 用作笛卡尔图表系列视图的基类。 |
| class [CartesianSideBySideBarSeriesView](./CartesianSideBySideBarSeriesView.md) | 将多个笛卡尔系列显示为在同一 X 轴值处并排放置的条形。 |
| class [CartesianSideBySideRangeBarSeriesView](./CartesianSideBySideRangeBarSeriesView.md) | 将多个笛卡尔系列显示为并排的条形，每个条形跨越每个数据点的第一个值和第二个值之间的范围。 |
| class [CartesianSortedLineSeriesView](./CartesianSortedLineSeriesView.md) | 使用线条连接笛卡尔系列的数据点，并按 X 轴值对点进行排序。 |
| class [CartesianStackedAreaSeriesView](./CartesianStackedAreaSeriesView.md) | 将多个笛卡尔系列显示为堆叠面积。每个面积从上一个面积结束的位置开始。 |
| class [CartesianStepAreaSeriesView](./CartesianStepAreaSeriesView.md) | 将笛卡尔系列的数据显示为在阶梯线与值轴零线之间填充的区域。 |
| class [CartesianStepLineSeriesView](./CartesianStepLineSeriesView.md) | 将笛卡尔系列的数据显示为在按 X 轴值排序的点之间先水平再垂直延伸的阶梯线。 |
| abstract class [ChartControl](./ChartControl.md) | 用作在坐标系中绘制数据的图表控件的基类。 |
| abstract class [ChartElement](./ChartElement.md) | 用作有助于图表视觉外观的样式化图表元素（例如轴、系列和线条样式）的基类。 |
| abstract class [ChartElementBase](./ChartElementBase.md) | 用作不以控件形式呈现的轻量级图表元素的基类。 |
| abstract class [ChartElementChangedEventArgs](./ChartElementChangedEventArgs.md) | 为 [`ChartElementChanged`](./ChartElement/ChartElementChanged.md) 事件提供数据。 |
| delegate [ChartElementChangedEventHandler](./ChartElementChangedEventHandler.md) | 表示处理 [`ChartElementChanged`](./ChartElement/ChartElementChanged.md) 事件的方法。 |
| class [ChartElementCollection&lt;T&gt;](./ChartElementCollection-T.md) | 表示图表元素的集合，既可以通过直接添加元素来填充，也可以通过所有者控件的相应项源属性和模板属性将集合绑定到数据源来填充。 |
| class [ChartElementCollectionChangedEventArgs](./ChartElementCollectionChangedEventArgs.md) | 为图表元素集合中的项已更改的通知提供数据。 |
| class [ConstantLine](./ConstantLine.md) | 表示在其所属轴的固定值处横穿绘图区域绘制的直线。 |
| enum [ConstantLineTitlePosition](./ConstantLineTitlePosition.md) | 列出指定常量线标题相对于线条放置位置的值。 |
| class [CrosshairAllSeriesLabelControl](./CrosshairAllSeriesLabelControl.md) | 在十字准线位置显示所有系列的值。 |
| class [CrosshairAllSeriesLabelControlData](./CrosshairAllSeriesLabelControlData.md) | 提供显示所有系列值的十字准线标签的内容。 |
| class [CrosshairOptions](./CrosshairOptions.md) | 定义在图表上跟踪指针的十字准线的外观和行为。 |
| class [CrosshairSeriesLabelItem](./CrosshairSeriesLabelItem.md) | 表示十字准线标签显示的单个系列行。 |
| enum [CrosshairSeriesLabelItemSortMode](./CrosshairSeriesLabelItemSortMode.md) | 列出指定系列在十字准线标签中显示顺序的值。 |
| enum [CrosshairSeriesLabelMode](./CrosshairSeriesLabelMode.md) | 列出指定十字准线显示多少个系列的值的值。 |
| class [CrosshairSeriesLabelSeriesValueItem](./CrosshairSeriesLabelSeriesValueItem.md) | 表示十字准线标签显示的单个系列值。 |
| class [CrosshairSeriesLabelValue](./CrosshairSeriesLabelValue.md) | 表示十字准线系列标签显示的单个值。 |
| enum [CrosshairSeriesMode](./CrosshairSeriesMode.md) | 列出指定十字准线如何在指针位置查找系列值的值。 |
| abstract class [CrosshairSeriesViewBase](./CrosshairSeriesViewBase.md) | 用作十字准线可定位的系列视图的基类。 |
| class [CrosshairSingleSeriesLabelControl](./CrosshairSingleSeriesLabelControl.md) | 在十字准线位置显示单个系列的值。 |
| class [CrosshairSingleSeriesLabelControlData](./CrosshairSingleSeriesLabelControlData.md) | 提供显示单个系列值的十字准线标签的内容。 |
| class [DateTimeRangeDataAdapter](./DateTimeRangeDataAdapter.md) | 将日期和时间参数以及数值对转换为系列数据点。参数必须按升序排序，以便范围系列能够按正确的顺序绘制它们。 |
| class [DateTimeScaleOptions](./DateTimeScaleOptions.md) | 定义以可配置单位度量日期和时间值的刻度。 |
| enum [DateTimeUnit](./DateTimeUnit.md) | 列出指定自动缩放或调整日期和时间轴时所用粒度的值。 |
| class [FormulaDataAdapter](./FormulaDataAdapter.md) | 根据公式生成系列数据点。参数均匀分布，从起始参数开始，按参数步长递增，值由公式计算。 |
| class [FuncLabelFormatter](./FuncLabelFormatter.md) | 通过调用用户提供的函数来格式化轴标签。 |
| class [Heatmap](./Heatmap.md) | 将二维值矩阵显示为彩色单元格网格，每个单元格的颜色由 [`IHeatmapColorProvider`](./IHeatmapColorProvider.md) 选择。 |
| abstract class [HeatmapAxis](./HeatmapAxis.md) | 用作热图轴的基类。它使用定性刻度，并沿绘图区域的外边缘绘制。 |
| class [HeatmapAxisX](./HeatmapAxisX.md) | 表示热图的角度轴，用于显示热图样本的角度范围。 |
| class [HeatmapAxisY](./HeatmapAxisY.md) | 表示热图的径向轴，用于显示距绘图区域中心的距离。 |
| class [HeatmapDataAdapter](./HeatmapDataAdapter.md) | 提供热图系列所绘制的二维值表。 |
| class [HeatmapDiagramCoordinates](./HeatmapDiagramCoordinates.md) | 表示由列名和行名标识的 [`Heatmap`](./Heatmap.md) 单元格。 |
| class [HeatmapGrayscaleColorProvider](./HeatmapGrayscaleColorProvider.md) | 通过将单元格值映射为灰色色调来提供热图单元格的颜色。 |
| class [HeatmapRangeColorProvider](./HeatmapRangeColorProvider.md) | 通过在用户定义的一组色标之间插值来提供热图单元格的颜色。 |
| class [HeatmapRangeStop](./HeatmapRangeStop.md) | 表示热图颜色刻度的单个色标。色标将一个值与热图单元格包含该值时显示的颜色配对。 |
| interface [IAxisLabelFormatter](./IAxisLabelFormatter.md) | 将轴值转换为作为轴标签显示的文本。 |
| interface [IHeatmapColorProvider](./IHeatmapColorProvider.md) | 为给定数据值提供热图单元格的颜色。 |
| interface [INumericAxisGridCalculator](./INumericAxisGridCalculator.md) | 提供在数值轴上绘制的网格线和刻度线的位置。 |
| interface [ISeriesDataAdapter](./ISeriesDataAdapter.md) | 定义系列的数据源。数据适配器将绑定的源集合中的值转换为系列及其轴所使用的参数和值。 |
| abstract class [LinearAxis](./LinearAxis.md) | 用作沿直线布置其刻度选项的轴的基类。 |
| abstract class [LinearNumericScaleOptions](./LinearNumericScaleOptions.md) | 用作支持线性和对数刻度的数值刻度选项的基类。 |
| class [LineStyle](./LineStyle.md) | 描述用于绘制系列线、轴线和其他图表轮廓的描边。 |
| struct [NumericGridEntry](./NumericGridEntry.md) | 表示数值轴网格的单个值。 |
| class [NumericRangeDataAdapter](./NumericRangeDataAdapter.md) | 将数值参数和数值对转换为系列数据点。参数必须按升序排序，以便范围系列能够按正确的顺序绘制它们。 |
| class [NumericScaleOptions](./NumericScaleOptions.md) | 定义默认为线性、并可切换为对数刻度的数值刻度。 |
| class [PercentLabelFormatter](./PercentLabelFormatter.md) | 将轴标签格式化为百分比。值 0.5 显示为 50.00%。 |
| class [PolarAreaSeriesView](./PolarAreaSeriesView.md) | 将极坐标系列的数据显示为在折线与绘图区域中心之间填充的区域。 |
| class [PolarAxisX](./PolarAxisX.md) | 表示极坐标图表的角度轴，显示从零到 360 度的值。 |
| class [PolarAxisXRange](./PolarAxisXRange.md) | 表示 PolarAxisX 的范围，该范围始终覆盖从 0 到 360 度的完整一圈。 |
| class [PolarAxisY](./PolarAxisY.md) | 表示极坐标图表的径向轴，用于显示距绘图区域中心的距离。 |
| class [PolarChart](./PolarChart.md) | 在圆形绘图区中显示系列，其中 X 轴是以弧度为单位、围绕中心测量的角度，Y 轴是距该中心的距离。 |
| class [PolarDiagramCoordinates](./PolarDiagramCoordinates.md) | 表示以角度和值表示的 [`PolarChart`](./PolarChart.md) 中的点。 |
| class [PolarLineSeriesView](./PolarLineSeriesView.md) | 将极坐标系列的数据显示为连接按角度轴值排序的点的折线。 |
| abstract class [PolarLineSeriesViewBase](./PolarLineSeriesViewBase.md) | 用作使用线条连接数据点的极坐标系列视图的基类。 |
| class [PolarNumericScaleOptions](./PolarNumericScaleOptions.md) | 为极坐标图表的角度轴定义数值刻度。它会从一组适合角度的乘数中选取自动计算的网格间距。 |
| class [PolarPointSeriesView](./PolarPointSeriesView.md) | 将极坐标系列的数据显示为一组彼此不相连的标记。 |
| class [PolarRangeAreaSeriesView](./PolarRangeAreaSeriesView.md) | 将极坐标系列的数据显示为在每个数据点的第一个值和第二个值之间填充的区域，并沿每条边界绘制一条线。 |
| class [PolarScatterLineSeriesView](./PolarScatterLineSeriesView.md) | 将极坐标系列的数据显示为按提供顺序连接各点的折线。 |
| class [PolarSeries](./PolarSeries.md) | 表示极坐标图表的系列。该系列在具有角度轴和径向轴的绘图区域中绘制由其数据适配器提供的数据。 |
| class [PolarSeriesCollection](./PolarSeriesCollection.md) | 存储极坐标图表的系列，并在系列更改时通知图表。 |
| abstract class [PolarSeriesView](./PolarSeriesView.md) | 用作极坐标图表系列视图的基类。 |
| abstract class [PredefinedRange](./PredefinedRange.md) | 用作边界固定且用户无法更改的轴范围的基类。 |
| class [QualitativeDataAdapter](./QualitativeDataAdapter.md) | 将类别名称和数值转换为系列数据点。参数被视为类别名称而不是数字，因此可以按任意顺序指定。 |
| class [QualitativeRangeDataAdapter](./QualitativeRangeDataAdapter.md) | 将类别名称和数值对转换为系列数据点。参数被视为类别名称而不是数字，因此可以按任意顺序指定。 |
| class [QualitativeScaleOptions](./QualitativeScaleOptions.md) | 定义一种刻度，按固定的类别数而不是数值来放置刻度线。 |
| abstract class [ScaleOptions](./ScaleOptions.md) | 用作刻度选项的基类，这些选项定义原始轴值如何映射到屏幕位置、标签、刻度线和网格线。 |
| enum [ScaleType](./ScaleType.md) | 列出指定系列数据适配器所提供值的类型的值。 |
| class [ScatterDataAdapter](./ScatterDataAdapter.md) | 将数值参数和值转换为系列数据点。参数可以按任意顺序指定，以便散点系列完全按照提供的方式绘制各点。 |
| abstract class [Series](./Series.md) | 用作图表系列的基类。系列拥有所显示的数据以及定义其外观的系列视图。 |
| class [SeriesDataAdapterDataChangedEventArgs](./SeriesDataAdapterDataChangedEventArgs.md) | 为系列数据适配器的数据更改事件提供数据。 |
| delegate [SeriesDataAdapterDataChangedEventHandler](./SeriesDataAdapterDataChangedEventHandler.md) | 表示处理系列数据适配器数据更改事件的方法。 |
| enum [SeriesDataMemberType](./SeriesDataMemberType.md) | 列出指定值所属的系列数据点成员的值。 |
| enum [SeriesDataUpdateType](./SeriesDataUpdateType.md) | 列出指定对系列数据适配器的数据所做更改类型的值。 |
| abstract class [SeriesViewBase](./SeriesViewBase.md) | 用作系列视图的基类。系列视图定义系列所绘制数据的外观。 |
| class [SmithAxisX](./SmithAxisX.md) | 表示史密斯圆图的角度轴，用于显示阻抗或导纳值。 |
| class [SmithAxisXRange](./SmithAxisXRange.md) | 表示 SmithAxisX 的范围，该范围覆盖完整一圈的角度范围。 |
| class [SmithAxisY](./SmithAxisY.md) | 表示史密斯圆图的径向轴，用于显示阻抗或导纳值。 |
| class [SmithAxisYRange](./SmithAxisYRange.md) | 表示 SmithAxisY 的范围，该范围在两个方向上覆盖从中心到绘图区域外边缘的全部距离。 |
| class [SmithChart](./SmithChart.md) | 在史密斯圆图上显示系列。史密斯圆图是射频工程中广泛用于绘制反射系数的圆形阻抗图。 |
| class [SmithDiagramCoordinates](./SmithDiagramCoordinates.md) | 表示以参数和值表示的 [`SmithChart`](./SmithChart.md) 中的点。 |
| abstract class [SmithLineSeriesViewBase](./SmithLineSeriesViewBase.md) | 用作使用线条连接数据点的史密斯系列视图的基类。 |
| class [SmithPointSeriesView](./SmithPointSeriesView.md) | 将史密斯系列的数据显示为一组彼此不相连的标记。 |
| class [SmithScaleOptions](./SmithScaleOptions.md) | 定义史密斯圆图轴的固定刻度。网格线位置由图表设置，无法更改。 |
| class [SmithScatterLineSeriesView](./SmithScatterLineSeriesView.md) | 将史密斯系列的数据显示为按提供顺序连接各点的折线。 |
| class [SmithSeries](./SmithSeries.md) | 表示史密斯圆图的系列。该系列在绘图区域的阻抗圆上绘制由其数据适配器提供的数据。 |
| class [SmithSeriesCollection](./SmithSeriesCollection.md) | 存储史密斯圆图的系列，并在系列更改时通知图表。 |
| abstract class [SmithSeriesView](./SmithSeriesView.md) | 用作史密斯圆图系列视图的基类。 |
| class [SortedDateTimeDataAdapter](./SortedDateTimeDataAdapter.md) | 将日期和时间参数以及数值转换为系列数据点。参数必须按升序排序，以便折线系列能够按正确的顺序连接它们。 |
| class [SortedNumericDataAdapter](./SortedNumericDataAdapter.md) | 将数值参数和值转换为系列数据点。参数必须按升序排序，以便折线系列能够按正确的顺序连接它们。 |
| class [SortedTimeSpanDataAdapter](./SortedTimeSpanDataAdapter.md) | 将时间跨度参数和数值转换为系列数据点。参数必须按升序排序，以便折线系列能够按正确的顺序连接它们。 |
| class [Strip](./Strip.md) | 表示在其所属轴的两个值之间横穿绘图区域绘制的阴影条带。 |
| class [SummaryCandlestickDataAdapter](./SummaryCandlestickDataAdapter.md) | 将日期和时间参数汇总为 K 线数据点。属于同一度量单位的所有源值生成一根 K 线，其中开盘值和收盘值是该组的第一个值和最后一个值，最低值和最高值是该组的最小值和最大值。 |
| class [TimeSpanRangeDataAdapter](./TimeSpanRangeDataAdapter.md) | 将时间跨度参数和数值对转换为系列数据点。参数必须按升序排序，以便范围系列能够按正确的顺序绘制它们。 |
| class [TimeSpanScaleOptions](./TimeSpanScaleOptions.md) | 定义以可配置单位度量时间跨度的刻度。 |
| enum [TimeSpanUnit](./TimeSpanUnit.md) | 列出指定自动缩放或调整时间跨度轴时所用粒度的值。 |

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Charts.dll -->

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
