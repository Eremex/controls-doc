---
title: 滚动和缩放图表控件
order: 980
seealso: []
---

# 在图表控件中滚动和缩放

`CartesianChart` control 支持整个视图和各个轴的滚动和缩放操作。用户可以使用鼠标和键盘缩放和滚动图表。在代码中，这些操作可通过 dedicated API 进行。

## 允许滚动和缩放操作

默认情况下启用滚动和缩放操作。以下选项允许您对各个轴禁用这些操作：

- `Axis.EnableZooming`
- `Axis.EnableScrolling`

``` xml
<mxc:CartesianChart.AxesX>
    <mxc:AxisX ShowTitle="False" EnableScrolling="False" EnableZooming="False" />
</mxc:CartesianChart.AxesX>
```
``` cs
chartControl1.AxesX[0].EnableZooming = false;
```

图表 control 的最小缩放范围可防止缩小得太远而导致视图太小。总轴范围定义了最小缩放范围。要指定总轴范围，请使用 `AxisX.Range`/`AxisY.Range` 对象的 `WholeMin` 和 `WholeMax` 属性。

``` xml
<mxc:CartesianChart.AxesY>
    <mxc:AxisY ShowTitle="False">
        <mxc:AxisYRange WholeMin="100" WholeMax="200" AutoCorrectWholeRange="False" AlwaysShowZeroLevel="True" />
    </mxc:AxisY>
</mxc:CartesianChart.AxesY>
```

有关详细信息，请参阅以下主题：[Axis Value Range](cartesian-chart.md#axis-value-range)

## 用户滚动和缩放

### 同时滚动所有轴

- 用鼠标拖动图表区域

或者

- 按 Ctrl+箭头键使用键盘滚动。


### 同时缩放所有轴

- 在图表区域上滚动鼠标滚轮

或者

- 按 Ctrl+'+' 放大，按 Ctrl+'-' 缩小。

![chart-zoom-and-scroll-all-series.gif](../../images/chart-zoom-and-scroll-all-series.gif)

### 滚动单个轴
- 用鼠标在相应的轴区域内拖动。

### 缩放单个轴

- 在相应的轴区域内滚动鼠标滚轮。

![chart-zoom-and-scroll-individual-series.gif](../../images/chart-zoom-and-scroll-individual-series.gif)

### 放大特定区域

- 在图表区域中按住 SHIFT，然后拖动以选择所需的矩形。

### 放大轴上的值范围

- 在轴区域按住 SHIFT，然后拖动以选择所需的范围。

![chart-zoom-into-rectangle](../../images/chart-zoom-into-rectangle.gif)

## 滚动并放大代码

### 使特定数据部分可见

要在 control 视口中查看特定数据部分，请自定义图表 control 轴的可见范围。使用 `AxisX.Range`/`AxisY.Range` 对象的 `VisualMin` 和 `VisualMax` 属性指定视口的值范围。

``` cs
chartControl1.AxesX[0].Range.VisualMin = 10;
chartControl1.AxesX[0].Range.VisualMax = 20;
chartControl1.AxesY[0].Range.VisualMin = -50;
chartControl1.AxesY[0].Range.VisualMax = 50;
```

### 在代码中模拟用户滚动操作

使用 `CartesianChart.Scroll` method 可沿特定轴或同时滚动所有轴的系列数据。该method模仿用户执行的滚动操作。

method的签名如下所示：

``` cs
public void Scroll(double deltaX, double deltaY, IEnumerable<Axis>? axes = null)
```

- `deltaX` — 指定沿水平轴滚动的像素数。正值对应于向右滚动；负值对应于向左滚动。
- `deltaY` — 指定沿垂直轴滚动的像素数。正值对应于滚动到顶部；负值对应于滚动到底部。
- `axes` — 滚动视口所沿的轴。如果省略此参数，视口将同时沿所有轴滚动。

``` cs
//Scroll along all X axes horizontally by 10 units
chartControl1.Scroll(10, 0);

//Scroll along all Y axes vertically by 10 units
chartControl1.Scroll(0, 10);

//Scroll along the first X axis
AxisX axisX = chartControl1.AxesX[0];
chartControl1.Scroll(10, 0, new[] { axisX });
```

### 在代码中模仿用户缩放操作

使用 `CartesianChart.Zoom` method 可沿特定轴或同时缩放所有轴的系列数据。该method模仿用户执行的缩放操作。

method的签名如下所示：

``` cs
public void Zoom(double delta, IEnumerable<Axis>? axes = null)
```

- `delta` — 指定鼠标滚轮向上/向下滚动操作的次数。该值决定缩放系数。 
    - 正值对应于鼠标滚轮向上滚动（放大）操作。 `1` 值对应于单个向上滚动操作。 
    - 负值对应于鼠标滚轮向下滚动（缩小）操作。 `-1` 的值对应于单个向下滚动操作。
    
- `axes` — 缩放视口所沿的轴。如果省略此参数，视口将同时沿所有轴缩放。

``` cs
//Zoom in (imitate a single scroll up action)
chartControl1.Zoom(1);

//Zoom out (imitate a single scroll down action)
chartControl1.Zoom(-1);
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
