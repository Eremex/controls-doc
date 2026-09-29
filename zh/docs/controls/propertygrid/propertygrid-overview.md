---
title: PropertyGrid 概述
order: 1900
seealso: []
---

# PropertyGrid 概述

`PropertyGridControl` 以垂直列表的形式显示绑定对象的公共属性及其值。每个列表项都渲染为一行，包含两个单元格：“属性名称”和“属性值”。

![propertygrid1](../../images/propertygrid1.png)

PropertyGrid 可以自动从绑定对象填充行，您也可以在代码中手动创建行。应用于绑定对象属性的专用特性允许您指定自定义的可见性、只读状态、显示名称、类别和类型转换器。

该控件支持分类行，可将若干行组合到可展开的分组中。

## 数据绑定与行自定义

当您将控件绑定到对象时，控件会自动为所有公共属性生成行。专用特性允许您自定义行生成选项。

该控件还支持手动生成常规行和分类行。有关详细信息，请参阅以下主题：

- [绑定到单个对象](data-binding.md#bind-to-one-object)
- [绑定到多个对象](data-binding.md#bind-to-multiple-objects)
- [行创建](data-binding.md#row-creation)
- [行](rows.md)

## 数据编辑

如果启用了数据编辑，用户可以编辑行的“值”部分。控件使用默认编辑器来显示和编辑常见数据类型（布尔型、双精度浮点型、整型、枚举等）的行值。您也可以根据需要为特定行指定自定义编辑器。

有关如何指定和访问编辑器、获取和设置单元格值的方法，请参阅以下主题：

- [数据编辑](data-editing.md)
- [自定义编辑器](custom-editors.md)

## 内置搜索

PropertyGrid 的搜索面板允许用户按名称快速定位行。

有关详细信息，请参阅以下主题：

- [数据搜索](data-search.md)

## 常用 API

请参阅以下主题，了解可帮助您完成最常见自定义任务的 API 成员：

- [常用 API](frequently-used-api.md)

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
