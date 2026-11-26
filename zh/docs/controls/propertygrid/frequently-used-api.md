---
title: 常用 API
order: 100
seealso: []
---

# 常用 API {#frequently-used-api}

## 属性 {#properties}

属性 | 说明 
---|---
[`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) | 返回当前活动的 Eremex 单元格编辑器。如果当前没有活动的编辑器，或者焦点单元格中活动的是非 Eremex 编辑器，则该属性返回 `null`。
[`AllowEditing`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/AllowEditing.md) | 获取或设置是否启用单元格编辑操作。
[`AutoGenerateRows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/AutoGenerateRows.md) | 获取或设置控件在初始化时，是否为空控件自动生成行，以显示绑定对象中所有可用的公共属性。如果控件中已经包含行，则自动行生成会被禁用。若要手动为控件填充行，可以使用 [`RetrieveFields`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/RetrieveFields.md) 方法，或直接向 [`Rows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/Rows.md) 集合添加行。
[`CellTemplate`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CellTemplate.md)  | 获取或设置用于在所有单元格中渲染单元格编辑器的模板。您可以使用 [`PropertyGridRow.CellTemplate`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridRow/CellTemplate.md) 属性为特定行指定单元格编辑器。
[`FocusedRow`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/FocusedRow.md) | 获取或设置获得焦点的行。此属性允许您使特定行获得焦点。
[`Rows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/Rows.md) | 返回控件在根级别显示的行。对于该集合中存储的分类行（[`PropertyGridCategoryRow`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridCategoryRow.md) 对象），您可以使用 [`PropertyGridCategoryRow.Rows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridCategoryRow/Rows.md) 属性访问其子行。
[`RowsDataTemplates`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/RowsDataTemplates.md) | 指定用于从行数据源（[`RowsSource`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridExpandableRowBase/RowsSource.md) 属性）渲染行的数据模板。
[`RowsSource`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridExpandableRowBase/RowsSource.md) | 指定用于通过数据模板（[`RowsDataTemplates`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/RowsDataTemplates.md)）生成行的数据源。
[`SelectedObject`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObject.md) | 获取或设置要在控件中显示其属性的对象。
[`SelectedObjects`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObjects.md) | 获取或设置要在控件中显示其属性的对象列表。

## 方法 {#methods}

方法 | 说明
------|------
[`CloseEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CloseEditor.md) | 隐藏活动的编辑器并保存所做的更改。
[`HideEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/HideEditor.md) | 隐藏活动的编辑器并放弃所做的更改。
[`RetrieveFields`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/RetrieveFields.md) | 为绑定对象（[`SelectedObject`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObject.md) 和 [`SelectedObjects`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObjects.md) 属性）公开的公共属性生成行。在开始生成行之前，会先清除现有的行。
[`PostEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/PostEditor.md) | 将单元格中所做的更改保存到绑定对象。
[`ShowEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowEditor.md) |  激活获得焦点的行的编辑器。 

## 事件 {#events}

事件 | 说明
------|------
[`CellValueChanged`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CellValueChanged.md) | 当单元格的值发生更改时触发。
[`CustomCellTemplateData`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CustomCellTemplateData.md) | 允许您提供一个自定义对象作为单元格模板的值。有关详细信息，请参阅以下主题：[自定义编辑器](custom-editors.md#dynamically-assign-editors-based-on-row-data-type)。
[`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md) | 激活单元格编辑器时触发。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
