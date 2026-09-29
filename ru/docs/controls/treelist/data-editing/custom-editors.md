---
title: Пользовательские редакторы в ячейках TreeList и TreeView
seealso: []
---

# Пользовательские редакторы в ячейках TreeList и TreeView

Элементы управления TreeList и TreeView по умолчанию используют встроенные редакторы Eremex для редактирования и форматирования значений ячеек. Информацию о том, как назначать встроенные редакторы по умолчанию и получать к ним доступ, смотрите в разделе [Data Editing](./index.md).

Текущий раздел показывает, как использовать шаблоны ячеек для встраивания пользовательских редакторов в ячейки. Доступны следующие два подхода:

- [Назначение пользовательского редактора напрямую колонке TreeList и TreeView](#назначение-пользовательского-редактора-напрямую-колонке-treelist-и-treeview)
- [Динамическое назначение редакторов на основе типа данных колонки TreeList](#динамическое-назначение-редакторов-на-основе-типа-данных-колонки-treelist)

!!! Note 

    Использование шаблонов имеет следующие ограничения:

    - Отображаемый текст, предоставляемый через шаблоны ячеек, не используется для сортировки, группировки и фильтрации данных.
    - Шаблоны ячеек не [экспортируются](../export.md).
 
## Назначение пользовательского редактора напрямую колонке TreeList и TreeView
 
Вы можете назначить встроенный редактор колонке TreeList или TreeView, создав `DataTemplate`. Для этого используйте свойства `TreeListColumn.CellTemplate` и `TreeViewControl.CellTemplate`, как показано ниже.

- Создайте объект `DataTemplate` с редактором, определённым внутри шаблона.
- Назначьте `DataTemplate` свойству `CellTemplate`.
- При необходимости явно привяжите редактор к значению колонки.
 
В следующем примере показан код XAML, устанавливающий свойство `CellTemplate` колонки TreeList в объект `TextBox`:
 
``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"

<mxtl:TreeListColumn Header="Phone" FieldName="Phone">
    <mxtl:TreeListColumn.CellTemplate>
        <DataTemplate>
            <TextBox Text="{Binding Value}"/>
        </DataTemplate>
    </mxtl:TreeListColumn.CellTemplate>
</mxtl:TreeListColumn>
```
 
### Неявная привязка данных для редакторов Eremex
 
Если вы используете редактор Eremex внутри `DataTemplate`, вы можете не указывать явную привязку данных к значению колонки для редактора. Убедитесь, что у редактора Eremex свойство `x:Name` установлено в значение **"PART_Editor"**. В этом случае элемент управления TreeList/TreeView автоматически привязывает свойство `EditorValue` редактора к значению ячейки колонки. Кроме того, контрол начинает управлять параметрами внешнего вида встроенного редактора (видимостью рамок и цветами переднего плана в активном и неактивном состояниях).
 
``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
...
<mxtl:TreeListColumn Header="Phone" FieldName="Phone">
    <mxtl:TreeListColumn.CellTemplate>
        <DataTemplate>
            <mxe:ButtonEditor x:Name="PART_Editor">
                <mxe:ButtonEditor.Buttons>
                    <mxe:ButtonSettings Content="..."/>
                </mxe:ButtonEditor.Buttons>
            </mxe:ButtonEditor>
        </DataTemplate>
    </mxtl:TreeListColumn.CellTemplate>
</mxtl:TreeListColumn>
```
 
### Явная привязка данных
 
Явная привязка данных требуется в следующих случаях:

- Вы используете редактор, который не является редактором Eremex.

!!! tip

    Редакторы Eremex — это элементы управления, производные от класса `Eremex.AvaloniaUI.Controls.Editors.BaseEditor`.

- Вам необходимо указать пользовательский конвертер значений в выражении привязки данных.
 
```xml
<DataTemplate DataType="pepa:Color">
    <mxe:PopupColorEditor x:Name="PART_Editor" 
     EditorValue="{Binding Path=Value, 
      Converter={ecadpg:EcadColorToAvaloniaColorConverter}}"/>
</DataTemplate>
```
 
## Динамическое назначение редакторов на основе типа данных колонки TreeList
 
Элемент управления TreeList позволяет назначать ячейкам колонок встроенные редакторы, обёрнутые в `DataTemplate`, на основе типа данных привязанного поля колонки. Для этого используйте свойство `TreeListControl.CellTemplate`.

### Пример — как связать редактор с одним типом данных

В следующем примере `TextEditor`, отображающий значения зелёным цветом, связывается с колонками, привязанными к полям типа Integer:
 
```xml
xmlns:sys="clr-namespace:System;assembly=mscorlib"
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxtl:TreeListControl.CellTemplate>
    <DataTemplate DataType="sys:Int32">
        <mxe:TextEditor x:Name="PART_Editor1" EditorValue="{Binding Value}" Foreground="Green"/>
    </DataTemplate>
</mxtl:TreeListControl.CellTemplate>
```

### Пример — как связать редакторы с несколькими типами данных

Предположим, у вас есть список объектов `DataTemplate`, связанных с разными типами данных, и вы хотите создать встроенные редакторы колонок на основе этого списка.

Чтобы выполнить эту задачу, сделайте следующее:
 
- Создайте пользовательский класс (_CellTemplateLocator_) в code-behind, который возвращает `DataTemplate` для конкретного типа данных и создаёт элемент управления, связанный с этим типом данных.
 
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
 
- Инициализируйте свойство `TreeListControl.CellTemplate` объектом *CellTemplateLocator*.
- Заполните объект *CellTemplateLocator* объектами `DataTemplate`, связанными с вашими типами данных.
 
В следующем примере определяются два объекта `DataTemplate` с редакторами, связанными соответственно с типами данных _String_ и _Integer_.

```xml
xmlns:sys="clr-namespace:System;assembly=mscorlib"
xmlns:local="clr-namespace:AvaloniaApplication1.Views"

<mxtl:TreeListControl.CellTemplate>
    <local:CellTemplateLocator>
        <DataTemplate DataType="sys:String">
            <mxe:TextEditor x:Name="PART_Editor" EditorValue="{Binding Value}" Foreground="Red"/>
        </DataTemplate>
        <DataTemplate DataType="sys:Int32">
            <mxe:TextEditor x:Name="PART_Editor1" EditorValue="{Binding Value}" Foreground="Green"/>
        </DataTemplate>
    </local:CellTemplateLocator>
</mxtl:TreeListControl.CellTemplate>
```

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
