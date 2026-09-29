---
title: Экспорт
order: 15
seealso: []
---

# Экспорт

Вы можете использовать метод `Graphics3DControl.Export`, чтобы захватить отрисовку контрола и вернуть её в виде объекта `Bitmap`. Размер растрового изображения соответствует размеру отображения контрола (`Graphics3DControl.Bounds.Size`).

Следующий пример сохраняет отрисовку `Graphics3DControl` в файл изображения.

``` cs
Bitmap bitmap = g3DControl.Export();
bitmap.Save("3d-rendering.png");
```


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
