---
title: CalendarControl
order: 2000
seealso: []
---

# CalendarControl

`CalendarControl` 显示允许用户选择日期的日历。 control 的导航标题显示用于浏览月份和年份的按钮。

![calendarcontrol](../../images/calendarcontrol.png)

control的主要特点包括：

- 使用鼠标和键盘在日历中选择日期。
- 导航 bar 允许浏览月份和年份。
- 三种日历视图：月视图、年视图和年份范围视图。
- option 用于限制可用日期范围。

## 选择日期

用户可以使用鼠标和键盘箭头键在日历中选择日期。

日历的导航标题允许用户浏览月份和年份。单击标题文本会缩小当前视图：
- 在月视图中，单击标题会切换到年视图。 
- 在年份视图中，单击标题会切换到年份范围视图。

![CalendarControl - select date](../../images/calendarcontrol-selectdate-animation.gif)

使用 `CalendarControl.SelectedDate` 属性选择日期或读取当前选择的日期。

## 自定义日历

使用以下属性来设置日历：

- `FirstDayOfWeek` — 获取或设置日历月视图中第一个出现的星期几。
- `IsTodayHighlighted` — 获取或设置是否在日历中突出显示今天的日期。 
- `DisplayDateStart` — 指定允许的最短日期。 `DisplayDateStart` 和 `DisplayDateEnd` 属性允许您指定日历中显示的值的范围。
- `DisplayDateEnd` — 指定允许的最大日期。
- `DisplayMode` — 获取或设置日历的查看模式（`Month`、`Year` 或 `Decade`）：

![dateeditor-calendar-displaymodes](../../images/dateeditor-calendar-displaymodes.png)

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
