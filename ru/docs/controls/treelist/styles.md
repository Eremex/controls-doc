---
title: Styles
order: 1000
seealso: []
---

# Styles

Элементы управления TreeList и TreeView поддерживают систему стилей Avalonia, которая позволяет настраивать параметры визуальных элементов контролов.
Используйте свойство `TreeListControl.Styles`, чтобы применять стили к следующим визуальным элементам:

- Заголовок колонки
- Строка
- Ячейка строки
- Область отступа строки

Типичный стиль состоит из селектора стиля и набора установщиков свойств (setters). Селектор задаёт целевой объект Control, который инкапсулирует визуальный элемент. Установщики свойств задают свойства целевого контрола и их значения.

Следующий код создаёт простой стиль, который устанавливает одинаковый цвет фона для всех строк TreeList.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxtlvis="clr-namespace:Eremex.AvaloniaUI.Controls.TreeList.Visuals;assembly=Eremex.Avalonia.Controls"

<mxtl:TreeListControl.Styles>
    <Style Selector="mxtlvis|TreeListRowControl">
        <Setter Property="Background" Value="Ivory" />
    </Style>
</mxtl:TreeListControl.Styles>
```

## Применение стилей к определённым состояниям контрола

Селекторы стилей в Avalonia поддерживают псевдоклассы. Псевдокласс — это ключевое слово, добавляемое к селектору. Оно задаёт состояние целевого контрола, к которому применяется стиль.

Элементы управления TreeList и TreeView предоставляют пользовательские псевдоклассы для определения конкретных состояний визуальных элементов контролов. В разделах ниже перечислены пользовательские псевдоклассы, поддерживаемые для визуальных элементов контролов.

Приведённый ниже код создаёт селектор стиля, нацеленный на строки TreeList. Псевдокласс `:focusedAndSelectedState` используется, чтобы применять стиль только к строкам, находящимся в фокусированном состоянии.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxtlvis="clr-namespace:Eremex.AvaloniaUI.Controls.TreeList.Visuals;assembly=Eremex.Avalonia.Controls"

<Style Selector="mxtlvis|TreeListRowControl:focusedAndSelectedState">
    ...
</Style>
```

## Контролы визуальных элементов

Синтаксис селектора стиля должен указывать целевой контрол (объект Control, инкапсулирующий визуальный элемент), к которому применяется стиль. На следующем изображении показаны визуальные элементы TreeList/TreeView и соответствующие целевые контролы.

![TreeList - Styling](../../images/treelist-styling.png)

## Стилизация строки (узла)

Строка — это визуальный элемент, отображающий ячейки.

Используйте следующую информацию для настройки стиля строки:

### Класс целевого контрола 
`TreeListRowControl` (в элементе управления TreeList), `TreeViewRowControl` (в элементе управления TreeView)

### DataContext
Данные (бизнес-объект) строки

### Пользовательские псевдоклассы

- ":selectedState" — строка выбрана, но не фокусирована. Это состояние действует в режиме множественного выбора строк.
- ":focusedState" — строка фокусирована, но не выбрана. Это состояние действует в режиме множественного выбора строк.
- ":focusedAndSelectedState" — строка фокусирована и выбрана. Это состояние действует как в режиме множественного, так и в режиме одиночного выбора строк.
- ":editingState" — у узла активен встроенный редактор.

### Пример — как настроить стиль фокусированного узла

Следующий код создаёт стиль, настраивающий цвет фона фокусированного узла TreeList.

Строки TreeList отрисовываются согласно предопределённому шаблону. Этот шаблон содержит объект `Border` (с именем _RowBorder_), который оформляет ячейки рамкой и фоном.
В примере ниже изменяется параметр `Background` объекта _RowBorder_ для фокусированного узла.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxtlvis="clr-namespace:Eremex.AvaloniaUI.Controls.TreeList.Visuals;assembly=Eremex.Avalonia.Controls"

<mxtl:TreeListControl.Styles>
    <Style Selector="mxtlvis|TreeListRowControl:focusedAndSelectedState /template/ Border#RowBorder">
        <Setter Property="Background" Value="SkyBlue" />
    </Style>
</mxtl:TreeListControl.Styles>
```

### Пример — как настроить параметры внешнего вида узла в зависимости от значений ячеек

Следующий код настраивает цвет фона и параметры шрифта строк (узлов) в зависимости от значений строки.

![treelist-rowstyle-example](../../images/treelist-rowstyle-example.png)

Фон строки зависит от свойства строки _Status_.
Объект _RowStatusToBrushConverter_ задаёт кисть, используемую для строк, у которых свойство _Status_ равно _InProgress_.

Если строки имеют дочерние элементы, логическое свойство _HasTasks_ этих строк возвращает значение _true_. Такие строки отображаются полужирным шрифтом.

Когда ячейки строки не находятся в режиме редактирования, они отрисовываются с помощью элементов управления _TextBlock_. Созданный стиль изменяет присоединённое свойство _TextBlock.FontWeight_, чтобы настроить насыщенность шрифта текста во всех ячейках строки. Объект _Eremex.AvaloniaUI.Controls.BoolToObjectConverter_ определяет фактическую насыщенность шрифта. Конвертер возвращает значение в зависимости от свойства _HasTasks_ строки.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxtlvis="clr-namespace:Eremex.AvaloniaUI.Controls.TreeList.Visuals;assembly=Eremex.Avalonia.Controls"
xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
xmlns:views="using:DemoCenter.Views"

<UserControl.Resources>
    <views:RowStatusToBrushConverter x:Key="myRowStatusToBrushConverter"/>
</UserControl.Resources>

<mxtl:TreeListControl.Styles>
    <Style Selector="mxtlvis|TreeListRowControl">
        <Setter Property="Background" Value="{Binding Status, 
         Converter={StaticResource myRowStatusToBrushConverter}}"/>
        <Setter Property="TextBlock.FontWeight">
            <Setter.Value>
                <Binding Path="HasTasks">
                    <Binding.Converter>
                        <mx:BoolToObjectConverter>
                            <mx:BoolToObjectConverter.TrueValue>
                                <FontWeight>Bold</FontWeight>
                            </mx:BoolToObjectConverter.TrueValue>
                            <mx:BoolToObjectConverter.FalseValue>
                                <FontWeight>Normal</FontWeight>
                            </mx:BoolToObjectConverter.FalseValue>
                        </mx:BoolToObjectConverter>
                    </Binding.Converter>
                </Binding>
            </Setter.Value>
        </Setter>
    </Style>
</mxtl:TreeListControl.Styles>
```
``` csharp
public class RowStatusToBrushConverter : IValueConverter
{
    static Brush lightGreenBrush = new SolidColorBrush(0xFFA8F0ED);
    public object Convert(object value, Type targetType, object parameter, 
     CultureInfo culture)
    {
        if (value == null) return null;
        DemoData.TaskStatus rowStatus = (DemoData.TaskStatus)value;

        if (rowStatus == DemoData.TaskStatus.InProgress)
            return lightGreenBrush;

        return null;
    }

    public object ConvertBack(object value, Type targetType, object parameter, 
     CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}
```

## Стилизация ячейки строки

Ячейки строки (узла) отображают значения колонок. В элементе управления TreeView каждая строка отображает только одно значение.

Чтобы настроить стиль ячейки строки, используйте следующую информацию:

### Класс целевого контрола

`TreeListCellControl`

### DataContext

Объект `Eremex.AvaloniaUI.Controls.DataControl.Visuals.CellData`. Основные свойства, предоставляемые объектом `CellData`:

- `Column` — колонка (объект `ColumnBase`), отображающая ячейку. Когда стиль применяется к объекту TreeView, свойство `CellData.Column` содержит объект `ColumnBase`, инкапсулирующий колонку значений TreeView.
- `DataControl` — элемент управления TreeList/TreeView (объект `DataControlBase`).
- `Row` — базовый объект данных (бизнес-объект) строки.
- `ValidationInfo` — объект, содержащий информацию о валидации ячейки.
- `Value` — значение ячейки.

### Пользовательские псевдоклассы

Пользовательские псевдоклассы совпадают с теми, что применяются к объектам строк. Они перечислены ниже:

- ":selectedState" — строка выбрана, но не фокусирована. Это состояние действует в режиме множественного выбора строк.
- ":focusedState" — строка фокусирована, но не выбрана. Это состояние действует в режиме множественного выбора строк.
- ":focusedAndSelectedState" — строка фокусирована и выбрана. Это состояние действует как в режиме множественного, так и в режиме одиночного выбора строк.
- ":editingState" — активен встроенный редактор ячейки.

### Пример — как настроить стиль ячейки в зависимости от значения ячейки

Объект Style в коде ниже устанавливает цвет фона ячеек, содержащих значение `true` в свойстве строки _OnVacation_.

Style устанавливает свойство `Background` объектов ячеек (`TreeListCellControl`) равным кисти, возвращаемой пользовательским конвертером _OnVacationCellValueToBrushConverter_. Конвертер возвращает кисть в зависимости от колонки и значения ячейки.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxtlvis="clr-namespace:Eremex.AvaloniaUI.Controls.TreeList.Visuals;assembly=Eremex.Avalonia.Controls"
xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
xmlns:local="clr-namespace:AvaloniaApp1"

<Grid.Resources>
    <local:OnVacationCellValueToBrushConverter x:Key="myOnVacationCellValueToBrushConverter" />
</Grid.Resources>

<mxtl:TreeListControl.Styles>
    <Style Selector="mxtlvis|TreeListCellControl">
        <Setter Property="Background">
            <Setter.Value>
                <MultiBinding Converter="{StaticResource myOnVacationCellValueToBrushConverter}">
                    <Binding Path="Row.OnVacation" />
                    <Binding Path="Column" />
                </MultiBinding>
            </Setter.Value>
        </Setter>
    </Style>
</mxtl:TreeListControl.Styles>
```

``` csharp
public class OnVacationCellValueToBrushConverter : IMultiValueConverter
{
    public object? Convert(IList<object?> values, Type targetType, 
     object? parameter, CultureInfo culture)
    {
        bool onVacation = (bool)values[0];
        TreeListColumn column = (TreeListColumn)values[1];
        if (column.FieldName == "OnVacation" && onVacation)
            return new SolidColorBrush(Colors.Aqua);
        return null;
    }
}
```




##  Стилизация области отступа строки

Область отступа отображает кнопки развёртывания и иконки узлов. Область отступа — это часть ячейки, отображающая иерархию узлов.

Чтобы настроить стиль области отступа строки, используйте следующую информацию:

### Класс целевого контрола

`TreeListIndentControl`

### DataContext

Объект `Eremex.AvaloniaUI.Controls.DataControl.Visuals.CellData`. Дополнительную информацию смотрите в разделе [Стилизация ячейки строки](#стилизация-ячейки-строки).

### Пользовательские псевдоклассы

Пользовательские псевдоклассы совпадают с теми, что применяются к объектам строк. Они перечислены ниже:

- ":selectedState" — строка выбрана, но не фокусирована. Это состояние действует в режиме множественного выбора строк.
- ":focusedState" — строка фокусирована, но не выбрана. Это состояние действует в режиме множественного выбора строк.
- ":focusedAndSelectedState" — строка фокусирована и выбрана. Это состояние действует как в режиме множественного, так и в режиме одиночного выбора строк.
- ":editingState" — у узла активен встроенный редактор.

### Пример — как настроить область отступа конкретной строки

Следующий код создаёт стиль, настраивающий цвет фона отступов в строках, у которых значение _HasChildren_ равно `true`.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxtlvis="clr-namespace:Eremex.AvaloniaUI.Controls.TreeList.Visuals;assembly=Eremex.Avalonia.Controls"
xmlns:mx="https://schemas.eremexcontrols.net/avalonia"

<mxtl:TreeListControl.Styles>
    <Style Selector="mxtlvis|TreeListIndentControl">
        <Setter Property="Background">
            <Setter.Value>
                <Binding Path="Row.HasChildren">
                    <Binding.Converter>
                        <mx:BoolToObjectConverter>
                            <mx:BoolToObjectConverter.TrueValue>
                                <SolidColorBrush Color="Coral"/>
                            </mx:BoolToObjectConverter.TrueValue>
                        </mx:BoolToObjectConverter>
                    </Binding.Converter>
                </Binding>
            </Setter.Value>
        </Setter>
    </Style>
</mxtl:TreeListControl.Styles>
```

## Стилизация заголовка колонки (элемент управления TreeList)

Заголовок колонки отображает заголовок колонки и индикаторы сортировки.

Используйте следующую информацию для настройки стиля заголовка колонки:

### Класс целевого контрола

`ColumnHeaderControl`

### DataContext

`TreeListColumn`

### Пользовательские псевдоклассы

- ":sortascending" — колонка отсортирована по возрастанию.
- ":sortdescending" — колонка отсортирована по убыванию.
- ":dragging" — колонка перетаскивается.

### Пример — как настроить параметры внешнего вида конкретного заголовка колонки

Следующий код показывает, как отобразить заголовок колонки _OnVacation_ TreeList полужирным шрифтом.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxvis="Eremex.AvaloniaUI.Controls.DataControl.Visuals;assembly=Eremex.Avalonia.Controls"
xmlns:local="clr-namespace:AvaloniaApp1"

<Grid.Resources>
    <local:ColumnToFontWeightConverter x:Key="myColumnToFontWeightConverter" />
</Grid.Resources>

<mxtl:TreeListControl.Styles>
    <Style Selector="mxvis|ColumnHeaderControl">
        <Setter Property="FontWeight" 
         Value="{Binding Converter={StaticResource myColumnToFontWeightConverter}}">
        </Setter>
    </Style>
</mxtl:TreeListControl.Styles>
```
``` csharp
public class ColumnToFontWeightConverter : IValueConverter
{
    public object? Convert(object? value, Type targetType, object? parameter, 
     CultureInfo culture)
    {
        TreeListColumn col = value as TreeListColumn;
        if(col!=null && col.FieldName=="OnVacation")
        {
            return FontWeight.Bold;
        }

        return null;
    }

    public object? ConvertBack(object? value, Type targetType, object? parameter, 
     CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}
```

<!--
<Style Selector="mxtl|ColumnHeaderControl">
    <Setter Property="Background">
        <Setter.Value>
            <Binding Path="HasChildren">
                <Binding.Converter>
                    <mx:BoolToObjectConverter>
                        <mx:BoolToObjectConverter.TrueValue>
                            <SolidColorBrush Color="LightYellow"/>
                        </mx:BoolToObjectConverter.TrueValue>
                        <mx:BoolToObjectConverter.FalseValue>
                            <SolidColorBrush Color="LightCyan"/>
                        </mx:BoolToObjectConverter.FalseValue>
                    </mx:BoolToObjectConverter>
                </Binding.Converter>
            </Binding>
        </Setter.Value>
    </Setter>
</Style>
-->


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
