---
title: Сохранение и восстановление размещения панелей
order: 50000
seealso: []
---

# Сохранение и восстановление размещения панелей

Dock Manager позволяет сохранять размещение dock-панелей и документов, а затем восстанавливать его позже. Используйте методы `DockManager.SaveLayout` и `DockManager.RestoreLayout` для сериализации и десериализации размещения.

Все панели и документы должны иметь уникальные имена, которые можно задать с помощью свойства `Name`. Уникальные имена обеспечивают корректную идентификацию и сериализацию элементов докинга.

``` xml
<mxd:DockGroup Orientation="Horizontal" DockHeight="*">
    <mxd:DockPane Name="dockPaneErrors" Header="Error List"/>
    <mxd:DockPane Name="dockPaneOutput" Header="Output"/>
</mxd:DockGroup>
```

Метод `DockManager.SaveLayout` использует заданный поток как есть — он не очищает поток и не меняет текущую позицию потока перед сохранением размещения.


## Пример

Следующий пример показывает, как можно сохранить размещение элементов докинга в файл и восстановить сохранённое размещение. 

``` cs
string fileName = "docking_layout.xml";

private void BtnSave_Click(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    using (var stream = new FileStream(fileName, FileMode.Create, FileAccess.Write))
    {
        dockManager1.SaveLayout(stream);
    }
}

private void BtnRestore_Click(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    if (!File.Exists(fileName)) return;
    using (FileStream fileStream = File.OpenRead(fileName))
    {
        dockManager1.RestoreLayout(fileStream);
    }
}
```


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
