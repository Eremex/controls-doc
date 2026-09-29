---
title: Styles
order: 1000
seealso: []
---

# Styles

Система стилей Avalonia позволяет настраивать параметры контролов Eremex Avalonia Controls, а также параметры конкретных визуальных элементов, из которых состоят контролы. Этот раздел показывает, как использовать стили для настройки следующих визуальных элементов контрола Data Grid:

- Заголовок колонки
- Строка
- Строка группы
- Ячейка строки

Используйте свойство `DataGridControl.Styles`, чтобы изменить стили контрола.

Типичный стиль состоит из селектора стиля и набора установщиков свойств (setters). Селектор задаёт целевой объект Control, инкапсулирующий визуальный элемент. Установщики свойств задают свойства целевого контрола и их значения.

Следующий код создаёт простой стиль, который задаёт одинаковый цвет фона для всех строк данных.

``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
xmlns:mxdgvis="clr-namespace:Eremex.AvaloniaUI.Controls.DataGrid.Visuals;assembly=Eremex.Avalonia.Controls"

<mxdg:DataGridControl.Styles>
    <Style Selector="mxdgvis|DataGridRowControl">
        <Setter Property="Background" Value="Ivory" />
    </Style>
</mxdg:DataGridControl.Styles>
```

## Применение стилей к определённым состояниям контрола

Селекторы стилей в Avalonia поддерживают псевдоклассы. Псевдокласс — это ключевое слово, добавляемое к селектору. Оно задаёт состояние целевого контрола, к которому применяется стиль.

DataGrid предоставляет пользовательские псевдоклассы для обращения к конкретным состояниям визуальных элементов контролов. В разделах ниже перечислены пользовательские псевдоклассы, поддерживаемые для визуальных элементов контролов.

Код ниже создаёт селектор стиля, нацеленный на строки DataGrid. Псевдокласс `:focusedAndSelectedState` используется, чтобы применить стиль только к строкам, находящимся в состоянии фокуса.

``` xml
xmlns:mxdgvis="clr-namespace:Eremex.AvaloniaUI.Controls.DataGrid.Visuals;assembly=Eremex.Avalonia.Controls"

<Style Selector="mxdgvis|DataGridRowControl:focusedAndSelectedState">
    ...
</Style>
```

## Контролы визуальных элементов

Синтаксис селектора стиля должен указывать целевой контрол (объект Control, инкапсулирующий визуальный элемент), к которому применяется стиль. На следующем изображении показаны визуальные элементы Data Grid и соответствующие целевые контролы.

![datagrid-styling](../../images/datagrid-styling.png)

<!--TODO
Group row's DataContext?
-->

## Стилизация строки данных

Строка данных отображает ячейки с данными.

Используйте следующую информацию для настройки стиля строки данных:

### Класс целевого контрола
`DataGridRowControl`

### DataContext
Объект данных (бизнес-объект) строки

### Пользовательские псевдоклассы

<!--TODO
uncomment when multiple selection is implemented

- ":selectedState" — A row is selected, but not focused. This state is in effect in multiple row selection mode.
- ":focusedState" —  A row is focused, but not selected. This state is in effect in multiple row selection mode. 
-->

- ":focusedAndSelectedState" — строка сфокусирована.

 <!--TODO
 uncomment when multiple selection is implemented
  and selected. This state is in effect in multiple- and single row selection modes. -->

- ":editingState" — строка имеет активный встроенный редактор.

### Пример - как настроить стиль сфокусированной строки

Следующий код создаёт стиль, настраивающий фон сфокусированной строки.

Строки Data Grid отрисовываются согласно предопределённому шаблону. Этот шаблон содержит объект `Border` (с именем _RowBorder_), который оформляет ячейки рамкой и фоном.
Пример ниже изменяет параметр `Background` объекта _RowBorder_ для сфокусированной строки.

``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
xmlns:mxdgvis="clr-namespace:Eremex.AvaloniaUI.Controls.DataGrid.Visuals;assembly=Eremex.Avalonia.Controls"

<mxdg:DataGridControl.Styles>
    <Style Selector="mxdgvis|DataGridRowControl:focusedAndSelectedState /template/ Border#RowBorder">
        <Setter Property="Background" Value="SkyBlue" />
    </Style>
</mxdg:DataGridControl.Styles>
```

<!--TODO
The code for the DataGrid differs from TreeList
``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
xmlns:mxdgvis="clr-namespace:Eremex.AvaloniaUI.Controls.DataGrid.Visuals;assembly=Eremex.Avalonia.Controls"

<mxdg:DataGridControl.Styles>
    <Style Selector="mxdgvis|TreeListRowControl:focusedAndSelectedState">
        <Setter Property="Background" Value="SkyBlue" />
    </Style>
</mxdg:DataGridControl.Styles>
``` 

-->

### Пример - как настроить параметры внешнего вида строки в зависимости от значений ячеек

Следующий код настраивает цвет фона и параметры шрифта строк в зависимости от значений строки.

![datagrid-rowstyle-example](../../images/datagrid-rowstyle-example.png)

Строки со значением _Contract_ в колонке _EmploymentType_ отображаются курсивом.
Когда ячейки строки не находятся в режиме редактирования, они отрисовываются с помощью контролов _TextBlock_. Созданный стиль изменяет присоединённое свойство _TextBlock.FontStyle_, чтобы настроить стиль шрифта текста во всех ячейках строки. Фактический стиль шрифта определяется объектом _EmploymentTypeToFontStyleConverter_.

Строки со статусом _Married_ имеют цвет фона, установленный в значение _CornSilk_. Объект `Binding` получает значение логического свойства _Married_ из DataContext, который содержит бизнес-объект строки. Затем он преобразует логическое значение в кисть с помощью конвертера `Eremex.AvaloniaUI.Controls.BoolToObjectConverter`.




``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
xmlns:mxdgvis="clr-namespace:Eremex.AvaloniaUI.Controls.DataGrid.Visuals;assembly=Eremex.Avalonia.Controls"
xmlns:views="using:DemoCenter.Views"

<UserControl.Resources>
    <views:EmploymentTypeToFontStyleConverter x:Key="employmentTypeToFontStyleConverter" />
</UserControl.Resources>

<mxdg:DataGridControl.Styles>
    <Style Selector="mxdgvis|DataGridRowControl">
        <Setter Property="TextBlock.FontStyle" Value="{Binding EmploymentType, 
         Converter={StaticResource employmentTypeToFontStyleConverter}}"/>
        <Setter Property="Background">
            <Setter.Value>
                <Binding Path="Married">
                    <Binding.Converter>
                        <mx:BoolToObjectConverter>
                            <mx:BoolToObjectConverter.TrueValue>
                                <SolidColorBrush>Cornsilk</SolidColorBrush>
                            </mx:BoolToObjectConverter.TrueValue>
                        </mx:BoolToObjectConverter>
                    </Binding.Converter>
                </Binding>
            </Setter.Value>
        </Setter>
    </Style>
</mxdg:DataGridControl.Styles>
```
``` csharp
public class EmploymentTypeToFontStyleConverter : IValueConverter
{
    static Brush lightRedBrush = new SolidColorBrush(0xFFffe6e6);
    public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
    {
        if (value == null) return null;
        EmploymentType empType = (EmploymentType)value;

        if (empType == EmploymentType.Contract)
            return FontStyle.Italic;

        return null;
    }

    public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}
```

## Стилизация ячейки строки

Ячейки в строках данных отображают значения для колонок сетки.

Чтобы настроить стиль ячейки строки, используйте следующую информацию:

### Класс целевого контрола

`CellControl`

### DataContext

Объект `Eremex.AvaloniaUI.Controls.DataControl.Visuals.CellData`. Основные свойства, предоставляемые объектом `CellData`:

- `Column` — колонка (объект `GridColumn`), отображающая ячейку.
- `DataControl` — текущий объект `DataGridControl`.
- `Row` — объект данных (бизнес-объект) строки.
- `ValidationInfo` — объект, содержащий информацию о валидации ячейки.
- `Value` — значение ячейки.

### Пользовательские псевдоклассы

Пользовательские псевдоклассы совпадают с теми, что применяются к объектам строк. Они показаны ниже:

<!--TODO
uncomment when multiple selection is implemented

 - ":selectedState" — A row is selected, but not focused. This state is in effect in multiple row selection mode.
- ":focusedState" —  A row is focused, but not selected. This state is in effect in multiple row selection mode. -->

- ":focusedAndSelectedState" — строка сфокусирована.

 <!--TODO
uncomment when multiple selection is implemented

 and selected. This state is in effect in multiple- and single row selection modes. 
 -->

- ":editingState" — встроенный редактор ячейки активен.

### Пример - как настроить стиль ячейки в зависимости от значения ячейки

Объект Style в коде ниже задаёт фон ячеек, содержащих значение `true` в свойстве строки _OnVacation_.

Style устанавливает свойство `Background` контролов ячеек (объекты `CellControl`) в кисть, возвращаемую пользовательским конвертером _OnVacationCellValueToBrushConverter_. Конвертер возвращает кисть в зависимости от колонки и значения ячейки.

``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
xmlns:mxvis="clr-namespace:Eremex.AvaloniaUI.Controls.DataControl.Visuals;
 assembly=Eremex.Avalonia.Controls"
xmlns:local="clr-namespace:AvaloniaApplication1.Views"

<Grid.Resources>
    <local:OnVacationCellValueToBrushConverter x:Key="myOnVacationCellValueToBrushConverter" />
</Grid.Resources>

<mxdg:DataGridControl.Styles>
    <Style Selector="mxvis|CellControl">
        <Setter Property="Background">
            <Setter.Value>
                <MultiBinding Converter="{StaticResource myOnVacationCellValueToBrushConverter}">
                    <Binding Path="Row.OnVacation" />
                    <Binding Path="Column" />
                </MultiBinding>
            </Setter.Value>
        </Setter>
    </Style>
</mxdg:DataGridControl.Styles>
```

``` csharp
using Eremex.AvaloniaUI.Controls.DataGrid;

namespace AvaloniaApplication1.Views;

public class OnVacationCellValueToBrushConverter : IMultiValueConverter
{
    public object? Convert(IList<object?> values, Type targetType, 
     object? parameter, CultureInfo culture)
    {
        bool onVacation = (bool)values[0];
        GridColumn column = (GridColumn)values[1];
        if (column.FieldName == "OnVacation" && onVacation)
            return new SolidColorBrush(Colors.Aqua);
        return null;
    }
}
```

<!--TODO
bool onVacation = (bool)values[0]; - InvalidCastException
bug - MX-114
-->

##  Стилизация строки группы

Строки группы объединяют другие строки при группировке данных по колонке(ам).

Чтобы настроить стиль строк группы, используйте следующую информацию:

### Класс целевого контрола

`DataGridGroupRowControl`

<!--TODO
### DataContext
??
-->

<!--TODO
### Custom Pseudo Classes
check:

The custom pseudo classes match those applied to row objects. They are shown below:

- ":selectedState" — A row is selected, but not focused. This state is in effect in multiple row selection mode.
- ":focusedState" —  A row is focused, but not selected. This state is in effect in multiple row selection mode.
- ":focusedAndSelectedState" — A row is focused and selected. This state is in effect in multiple- and single row selection modes.
- ":editingState" — A node has an active in-place editor. -->

### Пример - как настроить параметры внешнего вида строки группы

Следующий код показывает, как отобразить текст строк группы жирным шрифтом.

``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
xmlns:mxdgvis="clr-namespace:Eremex.AvaloniaUI.Controls.DataGrid.Visuals;assembly=Eremex.Avalonia.Controls"

<mxdg:DataGridControl.Styles>
    <Style Selector="mxdgvis|DataGridGroupRowControl">
        <Setter Property="FontWeight" Value="SemiBold"/>
    </Style>
</mxdg:DataGridControl.Styles>
```

## Стилизация заголовка колонки

Заголовок колонки отображает подпись колонки и индикаторы сортировки.

Используйте следующую информацию для настройки стиля заголовка колонки:

### Класс целевого контрола

`ColumnHeaderControl`

### DataContext

`GridColumn`

### Пользовательские псевдоклассы

- ":sortascending" — колонка отсортирована по возрастанию.
- ":sortdescending" — колонка отсортирована по убыванию.
- ":dragging" — колонка перетаскивается.

### Пример - как настроить параметры внешнего вида заголовка конкретной колонки

Следующий код отображает заголовок колонки _OnVacation_ жирным шрифтом.

``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
xmlns:mxvis="clr-namespace:Eremex.AvaloniaUI.Controls.DataControl.Visuals;
 assembly=Eremex.Avalonia.Controls"
xmlns:local="clr-namespace:AvaloniaApplication1.Views"

<Grid.Resources>
    <local:ColumnToFontWeightConverter x:Key="myColumnToFontWeightConverter" />
</Grid.Resources>

<mxdg:DataGridControl.Styles>
    <Style Selector="mxvis|ColumnHeaderControl">
        <Setter Property="FontWeight" 
         Value="{Binding Converter={StaticResource myColumnToFontWeightConverter}}">
        </Setter>
    </Style>
</mxdg:DataGridControl.Styles>
```
``` csharp
using Eremex.AvaloniaUI.Controls.DataGrid;

public class ColumnToFontWeightConverter : IValueConverter
{
    public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
    {
        GridColumn col = value as GridColumn;
        if (col != null && col.FieldName == "OnVacation")
        {
            return FontWeight.Bold;
        }

        return null;
    }

    public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
    {
        throw new NotImplementedException();
    }
}
```

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
