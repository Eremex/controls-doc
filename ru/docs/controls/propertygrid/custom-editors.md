---
title: Пользовательские редакторы
order: 600
seealso: []
---

# Пользовательские редакторы

`PropertyGrid` поддерживает [встроенные редакторы](data-editing.md) в ячейках. Они используются для отображения и редактирования значений ячеек. Вы можете встраивать пользовательские редакторы в ячейки, тем самым заменяя редакторы по умолчанию.

![propertygrid-inplaceeditor](../../images/propertygrid-inplaceeditor.png)

Используйте следующие подходы для задания пользовательских редакторов:

- [Назначить редактор непосредственно конкретной строке](#назначение-редактора-ячейке-строки-напрямую)
- [Динамически назначать редакторы строкам на основе типа данных базового объекта строки](#динамическое-назначение-редакторов-на-основе-типа-данных-строки)

 
## Назначение редактора ячейке строки напрямую
 
Используйте свойство `PropertyGridRow.CellTemplate`, чтобы назначить редактор конкретной строке. Для этого сделайте следующее:
 
- Создайте объект DataTemplate с редактором, определённым внутри шаблона.
- Назначьте DataTemplate свойству `PropertyGridRow.CellTemplate`.
- При необходимости привяжите редактор к привязанному полю строки явно. 
 
Следующий пример показывает XAML-код, инициализирующий свойство `CellTemplate`:
 
``` xml
xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"
...
<mxpg:PropertyGridControl x:Name="pGrid1" SelectedObject="{Binding}" Grid.Column="1">
    <mxpg:PropertyGridCategoryRow Caption="MyCategory1">
        <mxpg:PropertyGridRow FieldName="Number">
            <mxpg:PropertyGridRow.CellTemplate>
                <DataTemplate>
                    <TextBox Text="{Binding Value}"/>
                </DataTemplate>
            </mxpg:PropertyGridRow.CellTemplate>
        </mxpg:PropertyGridRow>
    </mxpg:PropertyGridCategoryRow>
</mxpg:PropertyGridControl>
```
 
### Неявная привязка данных для редакторов Eremex
 
Если вы используете редактор Eremex внутри шаблона, вы можете опустить явную привязку данных редактора к привязанному полю строки. Убедитесь, что у редактора Eremex свойство `x:Name` установлено в **"PART_Editor"**. В этом случае PropertyGrid автоматически привязывает свойство редактора `EditorValue` к полю строки. Кроме того, PropertyGrid начинает поддерживать настройки внешнего вида встроенного редактора (видимость рамок и цвета текста в активном и неактивном состояниях).
 
``` xml
xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
...
<mxpg:PropertyGridRow FieldName="Caption">
    <mxpg:PropertyGridRow.CellTemplate>
        <DataTemplate>
            <mxe:ButtonEditor x:Name="PART_Editor">
                <mxe:ButtonEditor.Buttons>
                    <mxe:ButtonSettings Content="..."/>
                </mxe:ButtonEditor.Buttons>
            </mxe:ButtonEditor>
        </DataTemplate>
    </mxpg:PropertyGridRow.CellTemplate>
</mxpg:PropertyGridRow>
```
 
### Явная привязка данных
 
Явная привязка данных требуется в следующих случаях:

- Вы используете редактор, не являющийся редактором Eremex. Все редакторы Eremex наследуются от класса `Eremex.AvaloniaUI.Controls.Editors.BaseEditor`.
- Вам нужно задать пользовательский конвертер значений в выражении привязки данных.
 
```xml
<DataTemplate DataType="pepa:Color">
    <mxe:PopupColorEditor x:Name="PART_Editor" 
     EditorValue="{Binding Value, Converter={ecadpg:EcadColorToAvaloniaColorConverter}}"/>
</DataTemplate>
```
 
## Динамическое назначение редакторов на основе типа данных строки
 
Контрол PropertyGrid может автоматически назначать шаблоны ячейкам строк на основе типа данных привязанного поля строки. Используйте для этого свойство `PropertyGridControl.CellTemplate`.
 
Следующий пример связывает TextEditor (окрашивает значения в зелёный) со строками, привязанными к полям Integer:
 
```xml
xmlns:sys="clr-namespace:System;assembly=mscorlib"
xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"
...
<mxpg:PropertyGridControl.CellTemplate>
    <DataTemplate DataType="sys:Int32">
        <mxe:TextEditor x:Name="PART_Editor1" EditorValue="{Binding Value}" Foreground="Green"/>
    </DataTemplate>
</mxpg:PropertyGridControl.CellTemplate>
```
 
Используйте следующий подход, если у вас есть список объектов DataTemplate, связанных с разными типами данных, и вы хотите назначить этот список контролу PropertyGrid:
 
- Создайте пользовательский класс в code-behind, который находит DataTemplate на основе типа данных и создаёт контрол, связанный с этим типом данных, следующим образом:
 
    ```csharp
    using Avalonia.Collections;
    using Avalonia.Controls.Templates;

    namespace AvaloniaApplication1.Views;

    public class CellTemplateLocator : AvaloniaList<IDataTemplate>, IDataTemplate
    {
        public Control Build(object? param)
        {
            return this.First(x => x.Match(param)).Build(param);
        }

        public bool Match(object? data)
        {
            return this.Any(x => x.Match(data));
        }
    }
    ```
    
    !!! tip
        Параметр _data_ метода `Match` задаёт значение целевого шаблона ячейки. Параметр _data_ по умолчанию содержит значение привязанного свойства. Вы можете обработать событие `CustomCellTemplateData`, чтобы предоставить пользовательский объект в качестве значения шаблона ячейки. Указанный пользовательский объект будет передан в метод `Match`.

- Инициализируйте свойство `PropertyGridControl.CellTemplate` объектом *CellTemplateLocator*.
- Заполните объект *CellTemplateLocator* объектами DataTemplate, связанными с вашими типами данных.
 
Следующий пример определяет два объекта DataTemplate, связанных с типами данных String и Integer соответственно.

```xml
xmlns:sys="clr-namespace:System;assembly=mscorlib"
xmlns:local="clr-namespace:AvaloniaApplication1.Views"

<mxpg:PropertyGridControl.CellTemplate>
    <local:CellTemplateLocator>
        <DataTemplate DataType="sys:String">
            <mxe:TextEditor x:Name="PART_Editor" EditorValue="{Binding Value}" Foreground="Red"/>
        </DataTemplate>
        <DataTemplate DataType="sys:Int32">
            <mxe:TextEditor x:Name="PART_Editor1" EditorValue="{Binding Value}" Foreground="Green"/>
        </DataTemplate>
    </local:CellTemplateLocator>
</mxpg:PropertyGridControl.CellTemplate>
```

## Смотрите также

- [Редактирование данных](data-editing.md)


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
