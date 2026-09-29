---
title: Сериализация и десериализация Ribbon
order: 300
seealso: []
---

# Сериализация и десериализация Ribbon

Конечные пользователи могут с помощью контекстных меню добавлять команды на [панель быстрого доступа](quick-access-toolbar.md) и удалять команды с неё во время работы.

![ribbon-qat-add-items-menu](../../images/ribbon-qat-add-items-menu.png) 

![ribbon-qat-remove-items-menu](../../images/ribbon-qat-remove-items-menu.png)

Размещение команд на панели быстрого доступа можно сохранить в поток и загрузить из него позже (например, при следующем запуске приложения). Для этого используйте следующие методы сериализации и десериализации размещения:

- `RibbonControl.SaveLayout` — сохраняет размещение элементов Ribbon на панели быстрого доступа в поток.
- `RibbonControl.RestoreLayout` — читает ранее сохранённое размещение из потока и применяет его к панели быстрого доступа.

!!! note

    Все элементы Ribbon должны иметь уникальные имена, которые можно задать с помощью свойства `Name` (или, как вариант, с помощью свойства `SerializationName`). Уникальные имена обеспечивают корректную идентификацию и сериализацию элементов Ribbon.

``` xml
<mxb:ToolbarButtonItem Name="btnNew" .../>
```

Следующий пример показывает, как можно сохранить и восстановить размещение элементов Ribbon в файл и из файла.

``` cs
string fileName = "ribbon_layout.xml";
private void BtnSave_Click(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    using (var stream = new FileStream(fileName, FileMode.Create, FileAccess.Write))
    {
        ribbon.SaveLayout(stream);
    }
}

private void BtnLoad_Click(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    if (!File.Exists(fileName)) return;
    using (FileStream fileStream = File.OpenRead(fileName))
    {
        ribbon.RestoreLayout(fileStream);
    }
}
```


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
