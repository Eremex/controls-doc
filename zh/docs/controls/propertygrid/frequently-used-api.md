---
title: 常用 API
order: 100
seealso: []
---

# 常用 API

## 属性

属性 | 说明 
---|---
`ActiveEditor` | 返回当前活动的 Eremex 单元格编辑器。如果当前没有活动的编辑器，或者焦点单元格中活动的是非 Eremex 编辑器，则该属性返回 `null`。
`AllowEditing` | 获取或设置是否启用单元格编辑操作。
`AutoGenerateRows` | 获取或设置控件在初始化时，是否为空控件自动生成行，以显示绑定对象中所有可用的公共属性。如果控件中已经包含行，则自动行生成会被禁用。若要手动为控件填充行，可以使用 `PopulateRows` 方法，或直接向 `Rows` 集合添加行。
`CellTemplate`  | 获取或设置用于在所有单元格中渲染单元格编辑器的模板。您可以使用 `PropertyGridRow.CellTemplate` 属性为特定行指定单元格编辑器。
`FocusedRow` | 获取或设置获得焦点的行。此属性允许您使特定行获得焦点。
`Rows` | 返回控件在根级别显示的行。对于该集合中存储的分类行（`PropertyGridCategoryRow` 对象），您可以使用 `PropertyGridCategoryRow.Rows` 属性访问其子行。
`RowsDataTemplates` | 指定用于从行数据源（`RowsSource` 属性）渲染行的数据模板。
`RowsSource` | 指定用于通过数据模板（`RowsDataTemplates`）生成行的数据源。
`SelectedObject` | 获取或设置要在控件中显示其属性的对象。
`SelectedObjects` | 获取或设置要在控件中显示其属性的对象列表。
`UseModernAppearance` | 获取或设置控件是以 `Modern` 样式还是 `Classic` 样式绘制。

## 方法

方法 | 说明
------|------
`CloseEditor` | 隐藏活动的编辑器并保存所做的更改。
`HideEditor` | 隐藏活动的编辑器并放弃所做的更改。
`PopulateRows` | 为绑定对象（`SelectedObject` 和 `SelectedObjects` 属性）公开的公共属性生成行。在开始生成行之前，会先清除现有的行。
`PostEditor` | 将单元格中所做的更改保存到绑定对象。
`ShowEditor` |  激活获得焦点的行的编辑器。 

## 事件

事件 | 说明
------|------
`CellValueChanged` | 当单元格的值发生更改时触发。
`CustomCellTemplateData` | 允许您提供一个自定义对象作为单元格模板的值。有关详细信息，请参阅以下主题：[自定义编辑器](custom-editors.md#dynamically-assign-editors-based-on-row-data-type)。
`ShowingEditor` | 激活单元格编辑器时触发。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
