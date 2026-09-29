---
title: Сериализация и десериализация панелей инструментов
order: 10000
seealso: []
---

# Сериализация и десериализация панелей инструментов

Пользователи могут настраивать размещение панелей инструментов во время работы. См. [Настройка панели инструментов во время выполнения](toolbars.md#настройка-панели-инструментов-во-время-выполнения).

Размещение панелей (включая размещение команд панелей) можно сохранить в поток и загрузить из него позже (например, при следующем запуске приложения). Для этого используйте следующие методы сериализации и десериализации размещения:

- `ToolbarManager.SaveLayout` — сохраняет размещение панелей в поток.
- `ToolbarManager.RestoreLayout` — загружает ранее сохранённое размещение из потока.

!!! note

    Все панели и элементы панелей должны иметь уникальные имена, которые можно задать с помощью свойства `Name`. Уникальные имена обеспечивают корректную идентификацию и сериализацию панелей и их элементов.

``` xml
<mxb:Toolbar x:Name="FileToolbar" ...>

<mxb:ToolbarButtonItem Name="btnNew" .../>
```

Следующий пример показывает, как можно сохранить и восстановить размещение панелей в файл и из файла.

``` cs
string fileName = "bars_layout.xml";
private void BtnSave_Click(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    using (var stream = new FileStream(fileName, FileMode.Create, FileAccess.Write))
    {
        toolbarManager1.SaveLayout(stream);
    }
}

private void BtnLoad_Click(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    if (!File.Exists(fileName)) return;
    using (FileStream fileStream = File.OpenRead(fileName))
    {
        toolbarManager1.RestoreLayout(fileStream);
    }
}
```


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
