---
title: 性能和数据虚拟化
order: 900
seealso: []
---

# 性能和数据虚拟化 {#performance-and-data-virtualization}

Tree List 和 Data Grid 控件支持数据虚拟化，可提升处理大型数据集时的性能（缩短加载时间）。
启用数据虚拟化后（默认设置），控件仅为可见区域生成可视元素（单元格、列标题等）。否则，控件会为所有项创建可视元素并将其保存在内存中，包括可见区域之外的隐藏项。

## 垂直和水平虚拟化 {#vertical-and-horizontal-virtualization}

垂直虚拟化（当滚动行时）始终处于活动状态。

默认情况下启用水平虚拟化（滚动列时）。

##### 相关 API {#related-api}

- [`DataGridControl.AllowHorizontalVirtualization`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/AllowHorizontalVirtualization.md) 属性 — 获取或设置是否启用水平虚拟化。


当行具有不同高度时（当根据单元格内容计算行高时），您可能需要禁用水平虚拟化。参见 [行自动高度](rows.md#row-auto-height)。

启用水平虚拟化后，会根据当前可见单元格的内容自动计算行高。视口之外的单元格不影响行高计算。当您滚动到具有不同内容高度的单元格时，行高会动态调整。要防止水平滚动期间动态行高发生变化，请禁用水平虚拟化。

``` xml
<mxdg:DataGridControl x:Name="dataGrid" AllowHorizontalVirtualization="False">
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
