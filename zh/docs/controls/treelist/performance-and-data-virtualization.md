---
title: 性能和数据虚拟化
order: 600
seealso: []
---

# 性能和数据虚拟化 {#performance-and-data-virtualization}

Tree List 和 Data Grid 控件支持数据虚拟化，可提升处理大型数据集时的性能（缩短加载时间）。
启用数据虚拟化后（默认设置），控件仅为可见区域生成可视元素（单元格、列标题等）。否则，控件会为所有项创建可视元素并将其保存在内存中，包括可见区域之外的隐藏项。

## 垂直虚拟化和水平虚拟化 {#vertical-and-horizontal-virtualization}

垂直虚拟化(滚动浏览行时)始终处于激活状态。

水平虚拟化(滚动浏览列时)默认处于启用状态。

##### 相关 API {#related-api}

- [`TreeListControl.AllowHorizontalVirtualization`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AllowHorizontalVirtualization.md) 属性 — 获取或设置是否启用水平虚拟化。


当行/节点具有不同的高度时(即行高根据单元格内容计算得出),您可能需要禁用水平虚拟化。请参阅[节点自动高度](nodes.md#node-auto-height)。

启用水平虚拟化后,自动行高会根据当前可见单元格的内容进行计算。可视区域之外的单元格不会影响行高的计算。当滚动到内容高度不同的单元格时,行高会动态调整。若要防止在水平滚动期间行高发生动态变化,请禁用水平虚拟化。

``` xml
<mxtl:TreeListControl x:Name="treeList" AllowHorizontalVirtualization="False">
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
