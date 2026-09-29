---
title: Export
order: 15
seealso: []
---

# Export

You can use the `Graphics3DControl.Export` method to capture the control's rendering and return it as a `Bitmap` object. The size of the bitmap matches the control's display size (`Graphics3DControl.Bounds.Size`).

The following example saves a `Graphics3DControl`'s rendering to an image file.

``` cs
Bitmap bitmap = g3DControl.Export();
bitmap.Save("3d-rendering.png");
```