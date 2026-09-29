---
title: 控件
order: 1000
seealso: []
---

# 控件

<style>

th {
    visibility: collapse;
}
td, th, tr {
   border: none!important;
   vertical-align: top;
}
</style>



## 数据管理控件


| <div style="width:400px"></div> | col 2 |
| --- | --- |
| **Data Grid** |  |
| ![thumb-datagrid](../images/thumb-datagrid.png) | 以二维表格的形式显示来自数据源的数据，并提供丰富的数据整形与编辑功能。<br><br>- 支持大型数据源<br>- 非绑定数据<br>- 数据排序和分组<br>- 内置编辑器<br>- 数据搜索与过滤<br>- 多行选择<br>- 行拖放<br>- 数据验证<br>- 内置和自定义上下文菜单<br>- 列组（Column Bands）<br>[了解更多...](datagrid/index.md) |  
| **Tree List 和 Tree View** |
| ![thumb-treelist](../images/thumb-treelist.png) | 以树形结构呈现层次化数据。Tree List 支持多个数据列，而 Tree View 是单列控件。<br><br>- 支持绑定到自引用（平面）和层次化数据源<br>- 非绑定模式（允许您手动提供数据）<br>- 多行选择<br>- 通过内置复选框进行行选择<br>- 数据排序<br>- 内置编辑器<br>- 数据搜索与过滤<br>- 行拖放<br>- 数据验证<br>- 内置和自定义上下文菜单<br>- 列组（Column Bands）<br>[了解更多...](treelist/index.md) | 
| **Property Grid** |
| ![thumb-propertygrid](../images/thumb-propertygrid.png) | 用于浏览和编辑一个或多个对象属性的高效解决方案。<br><br>- 根据绑定对象的公共属性自动生成行<br>- 手动创建行的模式<br>- 将行合并为分类行<br>- 将行合并为内嵌选项卡<br>- 搜索面板（用于快速定位行）<br>- 内置编辑器<br>[了解更多...](propertygrid/index.md) | 
| **List View** |
| ![thumb-propertygrid](../images/thumb-listview.png) | 一个根据您的模板渲染项的高级列表。支持项的排序、分组、过滤和多选。<br><br>- 两种项排列模式：`Stack`（单列排列）和 `Wrap`（多列排列并支持项换行）<br>- 按照您的模板以自定义方式渲染 ListView 的项<br>- 针对无限数量的项属性进行排序和分组<br>- 通过事件进行项过滤<br>- 单选和多选模式<br>[了解更多...](listview/index.md) | 


## 导航和布局控件

| <div style="width:400px"></div> | col 2 |
| --- | --- |
| **Ribbon** |
| ![thumb-ribbon](../images/thumb-ribbon.png) | 灵感来自 Microsoft Office 产品中功能区（ribbon）界面的菜单。<br><br>- 经典视图和简化视图<br>- 支持[传统菜单](toolbars-and-menus/index.md)中提供的所有类型的项（命令）：普通按钮、复选按钮、编辑器、标签、子菜单和按钮组。<br>- 内嵌式和下拉式图库<br>- 快速访问工具栏——用户可以在运行时通过上下文菜单将常用命令添加到该工具栏。<br>- 自定义快速访问工具栏的位置（Ribbon 命令面板上方或下方）及其可见性<br>- 在选项卡标题区域显示项<br>- 选项卡标题着色（可用于突出显示上下文相关的选项卡）——通过键盘导航 Ribbon 项<br>- 组和项的自适应布局（当 Ribbon 控件宽度变化时调整命令布局）<br>[了解更多...](ribbon/index.md) |
| **工具栏和菜单** |  |
| ![thumb-bars](../images/thumb-bars.png) | 适用于您的应用程序的传统工具栏和菜单。<br><br>- 支持的工具栏项类型：按钮、复选按钮、子菜单、项组等<br>- 在容器边缘停靠工具栏<br>- 将工具栏放置在窗口内的任意位置（例如客户端控件的顶部）<br>- 水平和垂直工具栏方向<br>- 命令的自适应布局<br>- 运行时通过拖放操作自定义工具栏布局<br>- 用于高级工具栏个性化设置的运行时自定义模式<br>- 快速自定义（无需激活自定义模式）<br>- 在工具栏中显示值，并允许用户使用内置编辑器进行编辑<br>- 支持热键，包括 Ctrl+R、Ctrl+K 等复杂快捷键组合<br>- 外部控件的上下文菜单<br>[了解更多...](toolbars-and-menus/index.md) | 
| **Docking 界面** |
| ![thumb-docking](../images/thumb-docking.png) | 灵感来自 Microsoft Visual Studio IDE 的经典停靠界面。<br><br>- Dock 面板可帮助您创建工具窗格<br>- 文档（内嵌的停靠窗口）可用于显示界面的主要内容<br>- 浮动面板<br>- 面板自动隐藏功能<br>- 选项卡容器<br>- 面板调整大小和拖放<br>- 停靠提示<br>- 用于对面板和文档执行操作的内置上下文菜单<br>- MVVM 支持<br>- 多显示器停靠<br>- 在应用程序运行之间保存和恢复 dock 面板的布局<br>[了解更多...](docking/index.md) |



## 数据可视化控件

| <div style="width:400px"></div> | col 2 |
| --- | --- |
| **图表控件** |  |
| ![thumb-chartcontrol](../images/thumb-chartcontrol.png) | `CartesianChart`、`PolarChart` 和 `SmithChart` 控件使您能够将最流行的交互式图表集成到应用程序界面中。<br><br>- 无限数量的数据系列<br>- 支持的视图：Line、Bar、Range Bar、Step Line、Candlestick 等<br>- 多种坐标轴类型：数值、日期时间、时间跨度、定性和对数<br>- 整个视图和单个坐标轴的滚动与缩放<br>- 显示大量数据时的高性能表现。<br>- 实时数据可视化。<br>[了解更多...](charts/index.md) | 
| **Heatmap 控件** |  |
| ![thumb-heatmap](../images/thumb-heatmap.png) | 一个二维热力图——通过彩色点来可视化数据的图表。<br><br>- 将数值以颜色的形式进行二维呈现<br>- 自定义 X 轴和 Y 轴<br>- 十字准线（Crosshair）<br>- 条带和常量线<br>- 使用鼠标进行滚动和缩放<br>- 将渲染结果导出为位图<br>[了解更多...](charts/heatmap.md) | 

## 3D 图形

| <div style="width:400px"></div> | col 2 |
| --- | --- |
| **Graphics3D 控件** |  |
| ![thumb-graphics3dcontrol2](../images/thumb-graphics3dcontrol2.png) | 使您能够在 Avalonia 应用程序中可视化 3D 模型。<br><br>- 用于指定 3D 模型的 API<br>- 简单材质<br>- PBR 格式的纹理材质<br>- 同时显示多个 3D 模型<br>- 透视和等距相机模式<br>- 运行时使用鼠标和键盘进行模型旋转、平移和缩放<br>- 使用 Vulkan SDK 在显卡上进行渲染<br>- 支持使用 MVVM 模式指定 3D 模型<br>[了解更多...](graphics3dcontrol/index.md) | 

## 编辑器和实用工具控件
| <div style="width:400px"></div> | col 2 |
| --- | --- |
| **数据编辑器** |  |
| ![thumb-editors](../images/thumb-editors.png) | 简单和高级的编辑器，使用户几乎可以编辑任何内容——从文本、数字到日期/时间值和颜色。您可以将它们用作独立控件，也可以用作内置编辑器 <br><br>- ButtonEditor<br>- CheckEditor<br>- ComboBoxEditor<br>- DateEditor<br>- HyperlinkEditor<br>- MemoEditor<br>- PopupColorEditor<br>- SegmentedEditor<br>- SpinEditor<br>- TextEditor<br><br>[了解更多...](editors/index.md) |
| **实用工具控件** |  |
| ![thumb-utilitycontrols](../images/thumb-utilitycontrols.png) | Eremex Controls 库附带的一组实用控件，使您能够创建功能丰富的应用程序。<br><br>- TabControl<br>-  SplitContainerControl<br>-  GroupBox<br>-  CalendarControl<br>-  MxMessageBox<br>-  CircleProgressIndicator<br>[了解更多...](utility-controls/index.md) |

## Eremex 绘制主题

Eremex Controls 库附带 “DeltaDesign” 绘制主题，帮助您使用浅色和深色两种配色方案打造界面。


| <div style="width:400px"></div> | <div style="width:400px"></div> |
| --- | --- |
| **DeltaDesign 浅色主题** | **DeltaDesign 深色主题** |
| ![thumb-lighttheme](../images/thumb-lighttheme.png) | ![thumb-darktheme](../images/thumb-darktheme.png) |
| ![thumb-lighttheme2](../images/thumb-lighttheme2.png) | ![thumb-darktheme2](../images/thumb-darktheme2.png) |

有关更多信息，请参阅以下主题：

- [主题](themes/index.md)

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
</content>
</invoke>
