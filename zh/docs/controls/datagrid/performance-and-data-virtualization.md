---
title: 性能和数据虚拟化
order: 900
seealso: []
---

# 性能和数据虚拟化

Data Grid 和 Tree List controls 支持数据虚拟化机制，可增强 control 对于大型数据集的性能（加载时间）。
When data virtualization is enabled (default), a control generates visual elements (cells, column headers, etc.) only for the current viewport.否则，即使对于视口之外的单元格和 column 标题，也会创建视觉元素并将其存储在内存中。

## 垂直和水平虚拟化

垂直虚拟化（当滚动行时）始终处于活动状态。

默认情况下启用水平虚拟化（滚动列时）。

#####相关API

- `DataGridControl.AllowHorizontalVirtualization` 属性 — 获取或设置是否启用水平虚拟化。


当行具有不同高度时（当根据单元格内容计算行高时），您可能需要禁用水平虚拟化。参见 [Row Auto-Height](rows.md#row-auto-height)。

启用水平虚拟化后，会根据当前可见单元格的内容自动计算行高。视口之外的单元格不影响行高计算。当您滚动到具有不同内容高度的单元格时，行高会动态调整。要防止水平滚动期间动态行高发生变化，请禁用水平虚拟化。

``` xml
<mxdg:DataGridControl x:Name="dataGrid" AllowHorizontalVirtualization="False">
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
