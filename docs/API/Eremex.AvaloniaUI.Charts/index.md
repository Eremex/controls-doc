## Eremex.AvaloniaUI.Charts namespace

| public type | description |
| --- | --- |
| abstract class [Axis](./Axis.md) | Serves as the base class for chart axes, which map data values to screen positions and supply labels, tickmarks, and gridlines. |
| enum [AxisPosition](./AxisPosition.md) | Lists values that specify which side of the drawing area an axis is drawn on. |
| abstract class [AxisRange](./AxisRange.md) | Serves as the base class for the axis ranges whose bounds can be set and recalculated from series data. |
| abstract class [AxisRangeBase](./AxisRangeBase.md) | Serves as the base class for axis ranges, which define the window of values currently displayed by an axis. |
| enum [AxisTitlePosition](./AxisTitlePosition.md) | Lists values that specify where an axis title is placed relative to the axis labels. |
| enum [AxisType](./AxisType.md) | Lists values that specify the kind of series data an axis is built for. |
| class [AxisX](./AxisX.md) | Represents the argument axis of a Cartesian chart. It displays the arguments of series data points. The axis is drawn along a horizontal edge of the drawing area, or along a vertical edge when the chart swaps its axes. |
| struct [AxisXCoordinate](./AxisXCoordinate.md) | Represents a value on a specific X axis. |
| class [AxisXRange](./AxisXRange.md) | Represents the range of a horizontal axis, such as AxisX or HeatmapAxisX. |
| class [AxisY](./AxisY.md) | Represents the value axis of a Cartesian chart. It displays the values of series data points. The axis is drawn along a vertical edge of the drawing area, or along a horizontal edge when the chart swaps its axes. |
| struct [AxisYCoordinate](./AxisYCoordinate.md) | Represents a value on a specific Y axis. |
| class [AxisYRange](./AxisYRange.md) | Represents the range of a vertical axis, such as AxisY or PolarAxisY. |
| class [CandlestickDataAdapter](./CandlestickDataAdapter.md) | Converts date and time arguments and open, high, low, and close values into series data points. The arguments must be sorted in ascending order, so that the candlesticks are drawn in the correct order. |
| class [CartesianAreaSeriesView](./CartesianAreaSeriesView.md) | Displays the data of a Cartesian series as an area filled between the polyline and the zero line of the value axis. |
| abstract class [CartesianAxis](./CartesianAxis.md) | Serves as the base class for the axes of a Cartesian chart. It adds a position, a title, and a title position. |
| class [CartesianCandlestickSeriesView](./CartesianCandlestickSeriesView.md) | Displays the data of a Cartesian series as candlesticks built from the open, high, low, and close values of each data point. |
| class [CartesianChart](./CartesianChart.md) | Displays series in a rectangular plot area defined by an X axis and a Y axis. |
| class [CartesianDiagramCoordinates](./CartesianDiagramCoordinates.md) | Represents a point of a [`CartesianChart`](./CartesianChart.md) expressed in the values of its X and Y axes. |
| class [CartesianFullStackedAreaSeriesView](./CartesianFullStackedAreaSeriesView.md) | Displays several Cartesian series as stacked areas whose values are normalized to one hundred percent at each X axis value. |
| class [CartesianLineSeriesView](./CartesianLineSeriesView.md) | Displays the data of a Cartesian series as a polyline that connects the points sorted by the X axis value. |
| abstract class [CartesianLineSeriesViewBase](./CartesianLineSeriesViewBase.md) | Serves as the base class for Cartesian series views that connect the data points with a line. |
| enum [CartesianLollipopOrientation](./CartesianLollipopOrientation.md) | Lists values that specify whether lollipop stems grow vertically or horizontally. |
| class [CartesianLollipopSeriesView](./CartesianLollipopSeriesView.md) | Displays the data of a Cartesian series as lollipops. Each data point is drawn as a thin stem that starts at the zero line and ends at a marker. |
| class [CartesianPointSeriesView](./CartesianPointSeriesView.md) | Displays the data of a Cartesian series as a set of markers that are not connected to each other. |
| class [CartesianRangeAreaSeriesView](./CartesianRangeAreaSeriesView.md) | Displays the data of a Cartesian series as an area filled between the first and the second value of each data point, with a line along each boundary. |
| class [CartesianScatterLineSeriesView](./CartesianScatterLineSeriesView.md) | Displays the data of a Cartesian series as a polyline that connects the points in the order in which they are supplied. |
| class [CartesianSeries](./CartesianSeries.md) | Represents a series of a Cartesian chart. The series plots the data supplied by its data adapter in a drawing area that has a horizontal and a vertical axis. |
| class [CartesianSeriesCollection](./CartesianSeriesCollection.md) | Stores the series of a Cartesian chart and notifies the chart when the series are changed. |
| abstract class [CartesianSeriesView](./CartesianSeriesView.md) | Serves as the base class for series views of a Cartesian chart. |
| class [CartesianSideBySideBarSeriesView](./CartesianSideBySideBarSeriesView.md) | Displays several Cartesian series as bars that are placed side by side at the same X axis value. |
| class [CartesianSideBySideRangeBarSeriesView](./CartesianSideBySideRangeBarSeriesView.md) | Displays several Cartesian series as side-by-side bars that span the range between the first and the second value of each data point. |
| class [CartesianSortedLineSeriesView](./CartesianSortedLineSeriesView.md) | Connects the data points of a Cartesian series with a line, sorting the points by the X axis value. |
| class [CartesianStackedAreaSeriesView](./CartesianStackedAreaSeriesView.md) | Displays several Cartesian series as stacked areas. Each area starts where the previous one ends. |
| class [CartesianStepAreaSeriesView](./CartesianStepAreaSeriesView.md) | Displays the data of a Cartesian series as an area filled between the stepped line and the zero line of the value axis. |
| class [CartesianStepLineSeriesView](./CartesianStepLineSeriesView.md) | Displays the data of a Cartesian series as a stepped line that runs horizontally and then vertically between the points sorted by the X axis value. |
| abstract class [ChartControl](./ChartControl.md) | Serves as the base class for the chart controls that plot data in a coordinate system. |
| abstract class [ChartElement](./ChartElement.md) | Serves as the base class for the styled chart elements that contribute to the visual appearance of a chart, such as axes, series, and line styles. |
| abstract class [ChartElementBase](./ChartElementBase.md) | Serves as the base class for the lightweight chart elements that are not rendered as controls. |
| abstract class [ChartElementChangedEventArgs](./ChartElementChangedEventArgs.md) | Provides data for the [`ChartElementChanged`](./ChartElement/ChartElementChanged.md) event. |
| delegate [ChartElementChangedEventHandler](./ChartElementChangedEventHandler.md) | Represents the method that handles the [`ChartElementChanged`](./ChartElement/ChartElementChanged.md) event. |
| class [ChartElementCollection&lt;T&gt;](./ChartElementCollection-T.md) | Represents a collection of chart elements that can be filled either by adding elements directly or by binding the collection to a data source through the matching items source and template properties of the owner control. |
| class [ChartElementCollectionChangedEventArgs](./ChartElementCollectionChangedEventArgs.md) | Provides data for a notification that the items of a chart element collection have changed. |
| class [ConstantLine](./ConstantLine.md) | Represents a straight line drawn across the drawing area at a fixed value of the axis it belongs to. |
| enum [ConstantLineTitlePosition](./ConstantLineTitlePosition.md) | Lists values that specify where a constant line title is placed relative to the line. |
| class [CrosshairAllSeriesLabelControl](./CrosshairAllSeriesLabelControl.md) | Displays the values of all series at the position of the crosshair. |
| class [CrosshairAllSeriesLabelControlData](./CrosshairAllSeriesLabelControlData.md) | Provides the content of a crosshair label that displays the values of all series. |
| class [CrosshairOptions](./CrosshairOptions.md) | Defines the appearance and the behavior of the crosshair that tracks the pointer over a chart. |
| class [CrosshairSeriesLabelItem](./CrosshairSeriesLabelItem.md) | Represents a single series row displayed by a crosshair label. |
| enum [CrosshairSeriesLabelItemSortMode](./CrosshairSeriesLabelItemSortMode.md) | Lists values that specify the order in which series appear in the crosshair labels. |
| enum [CrosshairSeriesLabelMode](./CrosshairSeriesLabelMode.md) | Lists values that specify how many series the crosshair shows the values of. |
| class [CrosshairSeriesLabelSeriesValueItem](./CrosshairSeriesLabelSeriesValueItem.md) | Represents a single series value displayed by a crosshair label. |
| class [CrosshairSeriesLabelValue](./CrosshairSeriesLabelValue.md) | Represents a single value displayed by a crosshair series label. |
| enum [CrosshairSeriesMode](./CrosshairSeriesMode.md) | Lists values that specify how the crosshair finds the value of a series at the pointer position. |
| abstract class [CrosshairSeriesViewBase](./CrosshairSeriesViewBase.md) | Serves as the base class for series views that can be located by the crosshair. |
| class [CrosshairSingleSeriesLabelControl](./CrosshairSingleSeriesLabelControl.md) | Displays the values of a single series at the position of the crosshair. |
| class [CrosshairSingleSeriesLabelControlData](./CrosshairSingleSeriesLabelControlData.md) | Provides the content of a crosshair label that displays the values of a single series. |
| class [DateTimeRangeDataAdapter](./DateTimeRangeDataAdapter.md) | Converts date and time arguments and pairs of numeric values into series data points. The arguments must be sorted in ascending order, so that a range series can draw them in the correct order. |
| class [DateTimeScaleOptions](./DateTimeScaleOptions.md) | Defines a scale that measures date and time values in a configurable unit. |
| enum [DateTimeUnit](./DateTimeUnit.md) | Lists values that specify the granularity used when a date and time axis is scaled or adjusted automatically. |
| class [FormulaDataAdapter](./FormulaDataAdapter.md) | Generates series data points from a formula. The arguments are evenly spaced, starting from the start argument and increasing by the argument step, and the values are calculated by the formula. |
| class [FuncLabelFormatter](./FuncLabelFormatter.md) | Formats axis labels by calling a user-supplied function. |
| class [Heatmap](./Heatmap.md) | Displays a two-dimensional matrix of values as a grid of colored cells, where the color of each cell is chosen by an [`IHeatmapColorProvider`](./IHeatmapColorProvider.md). |
| abstract class [HeatmapAxis](./HeatmapAxis.md) | Serves as the base class for the axes of a heatmap. It uses a qualitative scale and is drawn around the outer edge of the drawing area. |
| class [HeatmapAxisX](./HeatmapAxisX.md) | Represents the angular axis of a heatmap. It displays the angular sweep of heatmap samples. |
| class [HeatmapAxisY](./HeatmapAxisY.md) | Represents the radial axis of a heatmap. It displays the distance from the center of the drawing area. |
| class [HeatmapDataAdapter](./HeatmapDataAdapter.md) | Provides the two-dimensional table of values that the heatmap series draws. |
| class [HeatmapDiagramCoordinates](./HeatmapDiagramCoordinates.md) | Represents a cell of a [`Heatmap`](./Heatmap.md) identified by its column and row names. |
| class [HeatmapGrayscaleColorProvider](./HeatmapGrayscaleColorProvider.md) | Provides the color of a heatmap cell by mapping the cell value to a shade of gray. |
| class [HeatmapRangeColorProvider](./HeatmapRangeColorProvider.md) | Provides the color of a heatmap cell by interpolating between a user-defined set of color stops. |
| class [HeatmapRangeStop](./HeatmapRangeStop.md) | Represents a single stop of the color scale of a heatmap. A stop pairs a value with the color that a heatmap cell displays when it holds that value. |
| interface [IAxisLabelFormatter](./IAxisLabelFormatter.md) | Converts an axis value into the text shown as an axis label. |
| interface [IHeatmapColorProvider](./IHeatmapColorProvider.md) | Provides the color of a heatmap cell for a given data value. |
| interface [INumericAxisGridCalculator](./INumericAxisGridCalculator.md) | Supplies the positions of the gridlines and tickmarks drawn on a numeric axis. |
| interface [ISeriesDataAdapter](./ISeriesDataAdapter.md) | Defines a data source of a series. A data adapter converts the values of the bound source collection into the arguments and values that the series and its axes use. |
| abstract class [LinearAxis](./LinearAxis.md) | Serves as the base class for the axes that lay out their scale options along a straight line. |
| abstract class [LinearNumericScaleOptions](./LinearNumericScaleOptions.md) | Serves as the base class for the numeric scale options that support linear and logarithmic scales. |
| class [LineStyle](./LineStyle.md) | Describes the stroke used to draw series lines, axis lines, and other chart outlines. |
| struct [NumericGridEntry](./NumericGridEntry.md) | Represents a single value of a numeric axis grid. |
| class [NumericRangeDataAdapter](./NumericRangeDataAdapter.md) | Converts numeric arguments and pairs of numeric values into series data points. The arguments must be sorted in ascending order, so that a range series can draw them in the correct order. |
| class [NumericScaleOptions](./NumericScaleOptions.md) | Defines a numeric scale that is linear by default and can be switched to a logarithmic scale. |
| class [PercentLabelFormatter](./PercentLabelFormatter.md) | Formats axis labels as percentages. A value of 0.5 is displayed as 50.00 percent. |
| class [PolarAreaSeriesView](./PolarAreaSeriesView.md) | Displays the data of a polar series as an area filled between the polyline and the center of the drawing area. |
| class [PolarAxisX](./PolarAxisX.md) | Represents the angular axis of a polar chart. It displays values from zero to 360 degrees. |
| class [PolarAxisXRange](./PolarAxisXRange.md) | Represents the range of PolarAxisX, which always covers a full turn from 0 to 360 degrees. |
| class [PolarAxisY](./PolarAxisY.md) | Represents the radial axis of a polar chart. It displays the distance from the center of the drawing area. |
| class [PolarChart](./PolarChart.md) | Displays series on a circular plot area, where the X axis is an angle measured in radians around the center and the Y axis is a distance from that center. |
| class [PolarDiagramCoordinates](./PolarDiagramCoordinates.md) | Represents a point of a [`PolarChart`](./PolarChart.md) expressed as an angle and a value. |
| class [PolarLineSeriesView](./PolarLineSeriesView.md) | Displays the data of a polar series as a polyline that connects the points sorted by the angular axis value. |
| abstract class [PolarLineSeriesViewBase](./PolarLineSeriesViewBase.md) | Serves as the base class for polar series views that connect the data points with a line. |
| class [PolarNumericScaleOptions](./PolarNumericScaleOptions.md) | Defines a numeric scale for the angular axis of a polar chart. It picks automatically calculated grid spacing from a set of multipliers suited to angles. |
| class [PolarPointSeriesView](./PolarPointSeriesView.md) | Displays the data of a polar series as a set of markers that are not connected to each other. |
| class [PolarRangeAreaSeriesView](./PolarRangeAreaSeriesView.md) | Displays the data of a polar series as an area filled between the first and the second value of each data point, with a line along each boundary. |
| class [PolarScatterLineSeriesView](./PolarScatterLineSeriesView.md) | Displays the data of a polar series as a polyline that connects the points in the order in which they are supplied. |
| class [PolarSeries](./PolarSeries.md) | Represents a series of a polar chart. The series plots the data supplied by its data adapter in a drawing area that has an angular axis and a radial axis. |
| class [PolarSeriesCollection](./PolarSeriesCollection.md) | Stores the series of a polar chart and notifies the chart when the series are changed. |
| abstract class [PolarSeriesView](./PolarSeriesView.md) | Serves as the base class for series views of a polar chart. |
| abstract class [PredefinedRange](./PredefinedRange.md) | Serves as the base class for the axis ranges whose bounds are fixed and cannot be changed by the user. |
| class [QualitativeDataAdapter](./QualitativeDataAdapter.md) | Converts category names and numeric values into series data points. The arguments are treated as category names rather than numbers, so they may be specified in any order. |
| class [QualitativeRangeDataAdapter](./QualitativeRangeDataAdapter.md) | Converts category names and pairs of numeric values into series data points. The arguments are treated as category names rather than numbers, so they may be specified in any order. |
| class [QualitativeScaleOptions](./QualitativeScaleOptions.md) | Defines a scale that places tickmarks at a fixed number of categories rather than at numeric values. |
| abstract class [ScaleOptions](./ScaleOptions.md) | Serves as the base class for the scale options that define how raw axis values map to screen positions, labels, ticks, and gridlines. |
| enum [ScaleType](./ScaleType.md) | Lists values that specify the kind of values a series data adapter provides. |
| class [ScatterDataAdapter](./ScatterDataAdapter.md) | Converts numeric arguments and values into series data points. The arguments may be specified in any order, so that a scatter series draws the points exactly as they are supplied. |
| abstract class [Series](./Series.md) | Serves as the base class for chart series. A series owns the data that is displayed and a series view that defines its appearance. |
| class [SeriesDataAdapterDataChangedEventArgs](./SeriesDataAdapterDataChangedEventArgs.md) | Provides data for the data changed event of a series data adapter. |
| delegate [SeriesDataAdapterDataChangedEventHandler](./SeriesDataAdapterDataChangedEventHandler.md) | Represents the method that handles the data changed event of a series data adapter. |
| enum [SeriesDataMemberType](./SeriesDataMemberType.md) | Lists values that specify the member of a series data point that a value belongs to. |
| enum [SeriesDataUpdateType](./SeriesDataUpdateType.md) | Lists values that specify the kind of change made to the data of a series data adapter. |
| abstract class [SeriesViewBase](./SeriesViewBase.md) | Serves as the base class for series views. A series view defines the appearance of the data that is plotted by a series. |
| class [SmithAxisX](./SmithAxisX.md) | Represents the angular axis of a Smith chart. It displays impedance or admittance values. |
| class [SmithAxisXRange](./SmithAxisXRange.md) | Represents the range of SmithAxisX, which covers the angular sweep of a full turn. |
| class [SmithAxisY](./SmithAxisY.md) | Represents the radial axis of a Smith chart. It displays impedance or admittance values. |
| class [SmithAxisYRange](./SmithAxisYRange.md) | Represents the range of SmithAxisY, which covers the full distance from the center to the outer edge of the drawing area in both directions. |
| class [SmithChart](./SmithChart.md) | Displays series on a Smith chart, the circular impedance diagram widely used in radio frequency engineering to plot reflection coefficients. |
| class [SmithDiagramCoordinates](./SmithDiagramCoordinates.md) | Represents a point of a [`SmithChart`](./SmithChart.md) expressed as an argument and a value. |
| abstract class [SmithLineSeriesViewBase](./SmithLineSeriesViewBase.md) | Serves as the base class for Smith series views that connect the data points with a line. |
| class [SmithPointSeriesView](./SmithPointSeriesView.md) | Displays the data of a Smith series as a set of markers that are not connected to each other. |
| class [SmithScaleOptions](./SmithScaleOptions.md) | Defines the fixed scale of a Smith chart axis. The gridline positions are set by the chart and cannot be changed. |
| class [SmithScatterLineSeriesView](./SmithScatterLineSeriesView.md) | Displays the data of a Smith series as a polyline that connects the points in the order in which they are supplied. |
| class [SmithSeries](./SmithSeries.md) | Represents a series of a Smith chart. The series plots the data supplied by its data adapter on the impedance circle of the drawing area. |
| class [SmithSeriesCollection](./SmithSeriesCollection.md) | Stores the series of a Smith chart and notifies the chart when the series are changed. |
| abstract class [SmithSeriesView](./SmithSeriesView.md) | Serves as the base class for series views of a Smith chart. |
| class [SortedDateTimeDataAdapter](./SortedDateTimeDataAdapter.md) | Converts date and time arguments and numeric values into series data points. The arguments must be sorted in ascending order, so that a line series can connect them in the correct order. |
| class [SortedNumericDataAdapter](./SortedNumericDataAdapter.md) | Converts numeric arguments and values into series data points. The arguments must be sorted in ascending order, so that a line series can connect them in the correct order. |
| class [SortedTimeSpanDataAdapter](./SortedTimeSpanDataAdapter.md) | Converts time span arguments and numeric values into series data points. The arguments must be sorted in ascending order, so that a line series can connect them in the correct order. |
| class [Strip](./Strip.md) | Represents a shaded band drawn across the drawing area between two values of the axis it belongs to. |
| class [SummaryCandlestickDataAdapter](./SummaryCandlestickDataAdapter.md) | Summarizes date and time arguments into candlestick data points. All source values that fall into the same measure unit produce a single candlestick, where the opening and closing values are the first and the last value of the group, and the low and high values are the minimum and the maximum of the group. |
| class [TimeSpanRangeDataAdapter](./TimeSpanRangeDataAdapter.md) | Converts time span arguments and pairs of numeric values into series data points. The arguments must be sorted in ascending order, so that a range series can draw them in the correct order. |
| class [TimeSpanScaleOptions](./TimeSpanScaleOptions.md) | Defines a scale that measures time spans in a configurable unit. |
| enum [TimeSpanUnit](./TimeSpanUnit.md) | Lists values that specify the granularity used when a time span axis is scaled or adjusted automatically. |

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Charts.dll -->
