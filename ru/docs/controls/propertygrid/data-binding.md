---
title: Привязка данных и создание строк
order: 900
seealso: []
---

# Привязка данных и создание строк

В этом разделе показано, как привязать PropertyGrid к одному и нескольким объектам. По умолчанию контрол автоматически генерирует строки для публичных свойств привязанного объекта (объектов). Вы можете отключить автоматическую генерацию строк, создавать строки вручную, настраивать параметры строк и задавать шаблоны строк.

## Привязка к одному объекту

Используйте свойство `PropertyGridControl.SelectedObject`, чтобы привязать контрол к одному объекту. После привязки контрол автоматически отображает свойства объекта.

### Пример

Следующий пример привязывает PropertyGrid к объекту _MyBusinessObject_, определённому во ViewModel.

![propertygrid-sample](../../images/propertygrid-sample.png)

``` xml
xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"
xmlns:local="using:PropertyGridTest"

<Window.DataContext>
    <local:SampleViewModel/>
</Window.DataContext>

<mxpg:PropertyGridControl 
    Name="propertyGridControl1"
    SelectedObject="{Binding MyBusinessObject}"
    BorderThickness="1"
    UseModernAppearance="True" 
    Margin="5"/>
```

``` csharp
using CommunityToolkit.Mvvm.ComponentModel;

public partial class SampleViewModel : ViewModelBase
{
    [ObservableProperty]
    MyBusinessObject myBusinessObject;
}

public partial class MyBusinessObject : ViewModelBase
{
    [ObservableProperty]
    string text = "Sample text";

    [ObservableProperty]
    double borderSize = 5;

    [property: Category("Font")]
    [ObservableProperty]
    string fontFamily = FontManager.Current.DefaultFontFamily.Name;

    [property: Category("Font")]
    [ObservableProperty]
    double fontSize = 14;

    [property: Category("Font")]
    [ObservableProperty]
    bool isBold = true;

    [property: Category("Font")]
    [ObservableProperty]
    bool isItalic;

    [property: Category("Alignment")]
    [ObservableProperty]
    HorizontalAlignment horizontalAlignment = HorizontalAlignment.Center;

    [property: Category("Alignment")]
    [ObservableProperty]
    VerticalAlignment verticalAlignment;

    [ObservableProperty]
    Point location = new Point(11, 22);
}

public class ViewModelBase : ObservableObject
{
}
```

## Привязка к нескольким объектам

`PropertyGridControl` может отображать и редактировать свойства, общие для двух или более объектов. Назначьте список этих объектов свойству `PropertyGridControl.SelectedObjects`. Это заставляет контрол отображать только совпадающие свойства (те, что имеют одинаковое имя и тип данных).

``` xml
xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"

<mxpg:PropertyGridControl>
    <mxpg:PropertyGridControl.SelectedObjects>
        <local:MyList>
            <local:MyBusinessObject1/>
            <local:MyBusinessObject2/>
        </local:MyList>
    </mxpg:PropertyGridControl.SelectedObjects>
</mxpg:PropertyGridControl>
```
``` csharp
public class MyList : List<object>
{        
}
```

## Создание строк

После привязки PropertyGrid к объекту (объектам) поведение контрола по умолчанию — автоматически генерировать строки для отображения и редактирования свойств привязанного объекта (объектов). Контрол автоматически генерирует следующие типы строк во время инициализации:

- Строки данных (объекты `PropertyGridRow`) генерируются для всех публичных свойств. Эти строки отображают имена и значения привязанных свойств.
  
  ![data-rows](../../images/data-rows.png)

- Категориальные строки (объекты `PropertyGridCategoryRow`) генерируются из атрибутов `System.ComponentModel.CategoryAttribute`, применённых к базовым публичным свойствам. Соответствующие строки данных группируются внутри этих категориальных строк.

  ![category-rows](../../images/category-rows.png)

PropertyGrid предоставляет следующие возможности настройки строк:

- Отключение автоматической генерации строк с помощью свойства `PropertyGridControl.AutoGenerateRows`.
- Ручное создание строк.
- Использование атрибутов Annotation для настройки параметров строк.
- Задание шаблонов данных для отрисовки отдельных строк.
- Генерация строк из коллекции View Model строк (`RowsSource`).

Дополнительную информацию смотрите в следующем разделе: [Строки](rows.md).


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
