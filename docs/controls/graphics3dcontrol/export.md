---
title: Export
order: 15
seealso: []
---

# Export

You can use the [`Graphics3DControl.Export`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl/Export.md) method to capture the control's rendering and return it as a `Bitmap` object. The size of the bitmap matches the control's display size (`Graphics3DControl.Bounds.Size`).

The following example saves a [`Graphics3DControl`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl.md)'s rendering to an image file.

``` cs
Bitmap bitmap = g3DControl.Export();
bitmap.Save("3d-rendering.png");
```