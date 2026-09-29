---
title: ListView
order: 59000
seealso: []
---

# ListView

`ListViewControl` 是一个项容器,支持多种项排列布局、项排序、分组、筛选和选择功能。您可以使用 `ListViewControl` 创建类似于 Microsoft Windows 资源管理器右侧窗格的界面。

通过指定项模板,您可以以任意自定义方式呈现 ListView 项。例如,模板可以让 ListView 将项绘制为图标、带文本的图标或纯文本。

![ListView-svgbrowser](../../images/ListView-svgbrowser.png)

该控件的主要功能包括:

- 以单列(垂直列表)或多列(启用换行)方式排列项。
- 支持 MVVM 设计模式 — 您可以使用项源中的项来填充控件。
- 项模板允许您以任意自定义方式呈现项。
- 项排序 — 您可以根据任意数量的项字段(属性)对项进行排序。
- 项分组 — 具有相同特定项字段(属性)值的项将被合并到同一组中。与项排序一样,您可以按一个或多个字段(属性)对项进行分组。
- 组的展开和折叠。
- 项筛选 — 通过处理专用事件来筛选项。
- 两种项选择模式:单选和多选。
- 使用键盘导航和选择项。

有关更多信息,请参阅以下主题: [ListView 控件概述](listview-overview.md)。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
