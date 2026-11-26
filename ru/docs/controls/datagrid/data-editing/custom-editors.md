---
title: Пользовательские редакторы
order: 1000
seealso: []
---

# Пользовательские редакторы

По умолчанию DataGrid использует встроенные редакторы Eremex для редактирования и форматирования значений ячеек. Смотрите раздел [Редактирование данных](./index.md), чтобы узнать, как назначать встроенные редакторы по умолчанию и получать к ним доступ.

Текущий раздел показывает, как использовать шаблоны ячеек для встраивания пользовательских редакторов в ячейки. Доступны следующие два подхода:

- [Назначение пользовательского редактора колонке DataGrid напрямую](#назначение-пользовательского-редактора-колонке-грида-напрямую)
- [Динамическое назначение редакторов на основе типа данных колонки грида](#динамическое-назначение-редакторов-на-основе-типа-данных-колонки-грида)

!!! Note 

    Использование шаблонов имеет следующие ограничения:

    - Отображаемый текст, предоставляемый через шаблоны ячеек, не используется для сортировки, группировки и фильтрации данных.
    - Шаблоны ячеек не [экспортируются](../export.md).
 
## Назначение пользовательского редактора колонке грида напрямую
 
Вы можете указать встроенный редактор для колонки грида, назначив `DataTemplate` свойству [`GridColumn.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md).

- Создайте объект `DataTemplate` с редактором, определённым внутри шаблона.
- Назначьте `DataTemplate` свойству [`CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md).
- При необходимости явно привяжите редактор к значению колонки.
 
Этот пример показывает XAML-код, который устанавливает свойство [`CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md) колонки грида в объект `TextBox`:
 
``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"

<mxdg:GridColumn Header="Phone" FieldName="Phone">
    <mxdg:GridColumn.CellTemplate>
        <DataTemplate>
            <TextBox Text="{Binding Value}"/>
        </DataTemplate>
    </mxdg:GridColumn.CellTemplate>
</mxdg:GridColumn>
```
 
### Неявная привязка данных для редакторов Eremex
 
Если вы используете редактор Eremex внутри `DataTemplate`, вы можете не указывать явную привязку данных к значению колонки для редактора.

Установите свойство `x:Name` в значение **"PART_Editor"** для редактора Eremex, определённого в шаблоне. Это обеспечивает автоматическую привязку значения редактора ([`BaseEditor.EditorValue`](../../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md)) к полю колонки. Кроме того, настройки внешнего вида редактора (видимость границы и цвета текста в активном и неактивном состояниях) будут управляться контролом DataGrid.

``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
...
<mxdg:GridColumn Header="Phone" FieldName="Phone">
    <mxdg:GridColumn.CellTemplate>
        <DataTemplate>
            <mxe:ButtonEditor x:Name="PART_Editor">
                <mxe:ButtonEditor.Buttons>
                    <mxe:ButtonSettings Content="..."/>
                </mxe:ButtonEditor.Buttons>
            </mxe:ButtonEditor>
        </DataTemplate>
    </mxdg:GridColumn.CellTemplate>
</mxdg:GridColumn>
```
 
### Явная привязка данных для встроенных редакторов
 
Явная привязка данных для встроенных редакторов требуется в следующих случаях:

- Вы используете редактор, который не является редактором Eremex.

    !!! tip
    
        Редакторы Eremex — это контролы, производные от класса [`Eremex.AvaloniaUI.Controls.Editors.BaseEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor.md).

- Вам нужно указать пользовательский конвертер значений в выражении привязки данных.
 
```xml
<DataTemplate DataType="pepa:Color">
    <mxe:PopupColorEditor x:Name="PART_Editor" EditorValue="{Binding Path=Value, 
     Converter={ecadpg:EcadColorToAvaloniaColorConverter}}"/>
</DataTemplate>
```
 
## Динамическое назначение редакторов на основе типа данных колонки грида
 
Вы можете назначать встроенные редакторы колонкам на основе типа данных связанного поля колонки следующим образом:

- Определите редактор внутри `DataTemplate`.
- Установите свойство `DataTemplate.DataType` равным целевому типу данных.
- Назначьте созданный шаблон свойству [`DataGridControl.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CellTemplate.md).

### Пример - Как связать встроенный редактор с типом данных колонки

Этот пример связывает [`TextEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md), отображающий значения зелёным цветом, с колонками, привязанными к полям типа Integer:
 
```xml
xmlns:sys="clr-namespace:System;assembly=mscorlib"
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxdg:DataGridControl.CellTemplate>
    <DataTemplate DataType="sys:Int32">
        <mxe:TextEditor x:Name="PART_Editor1" EditorValue="{Binding Value}" Foreground="Green"/>
    </DataTemplate>
</mxdg:DataGridControl.CellTemplate>
```

### Пример - Как связать редакторы с несколькими типами данных

Предположим, у вас есть список объектов `DataTemplate`, связанных с разными типами данных, и вы хотите создавать встроенные редакторы колонок на основе этого списка.

Чтобы решить эту задачу, выполните следующие действия:
 
- Создайте в code-behind пользовательский класс (_CellTemplateLocator_), который возвращает `DataTemplate` для конкретного типа данных и создаёт контрол, связанный с этим типом данных.
 
```csharp
using Avalonia.Collections;
using Avalonia.Controls.Templates;

namespace AvaloniaApplication1.Views;

public class CellTemplateLocator : AvaloniaList<IDataTemplate>, IDataTemplate
{
    public Control Build(object? param)
    {
        var cellData = param as Eremex.AvaloniaUI.Controls.DataControl.Visuals.CellData;
        if (cellData == null) return null;
        return this.First(x => x.Match(cellData.Value)).Build(cellData.Value);
    }

    public bool Match(object? data)
    {
        var cellData = data as Eremex.AvaloniaUI.Controls.DataControl.Visuals.CellData;
        if (cellData == null) return false;
        return this.Any(x => x.Match(cellData.Value));
    }
}
```
 
- Инициализируйте свойство [`DataGridControl.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CellTemplate.md) объектом *CellTemplateLocator*.
- Заполните объект *CellTemplateLocator* объектами `DataTemplate`, связанными с вашими типами данных.
 
Этот пример определяет два объекта `DataTemplate` с редакторами, связанными с типами данных _String_ и _Integer_ соответственно.

```xml
xmlns:sys="clr-namespace:System;assembly=mscorlib"
xmlns:local="clr-namespace:AvaloniaApplication1.Views"

<mxdg:DataGridControl.CellTemplate>
    <local:CellTemplateLocator>
        <DataTemplate DataType="sys:String">
            <mxe:TextEditor x:Name="PART_Editor" EditorValue="{Binding Value}" Foreground="Red"/>
        </DataTemplate>
        <DataTemplate DataType="sys:Int32">
            <mxe:TextEditor x:Name="PART_Editor1" EditorValue="{Binding Value}" Foreground="Green"/>
        </DataTemplate>
    </local:CellTemplateLocator>
</mxdg:DataGridControl.CellTemplate>
```

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
