---
title: 导出
order: 15
seealso: []
---

# 导出 {#export}

您可以使用 [`Graphics3DControl.Export`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl/Export.md) 方法捕获控件的渲染结果，并将其作为 `Bitmap` 对象返回。位图的大小与控件的显示大小（`Graphics3DControl.Bounds.Size`）相匹配。

以下示例将 [`Graphics3DControl`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl.md) 的渲染结果保存到图像文件中。

``` cs
Bitmap bitmap = g3DControl.Export();
bitmap.Save("3d-rendering.png");
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
