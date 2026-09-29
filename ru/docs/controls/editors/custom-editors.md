---
title: Пользовательские редакторы
order: 600
seealso: []
---

# Пользовательские редакторы

## Регистрация пользовательских редакторов для использования в контейнерных контролах

Стандартный подход к заданию встроенных редакторов в контейнерных контролах — использовать свойство `EditorProperties`, предоставляемое этими контейнерными контролами:

- `GridColumn.EditorProperties`
- `TreeListColumn.EditorProperties`
- `TreeViewControl.EditorProperties`
- `PropertyGridRow.EditorProperties`
- `ToolbarEditorItem.EditorProperties`

Например, следующий код назначает контрол `ButtonEditor` столбцу грида. Код устанавливает свойство `GridColumn.EditorProperties` в объект `ButtonEditorProperties`. В результате контрол грида автоматически создаст встроенный контрол `ButtonEditor` на основе заданного объекта `ButtonEditorProperties`, когда в этом столбце начнётся операция редактирования ячейки.

``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid" 
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxdg:DataGridControl.Columns>
    <mxdg:GridColumn Header="Name" FieldName="Name">
        <mxdg:GridColumn.EditorProperties>
            <mxe:ButtonEditorProperties>
                <mxe:ButtonEditorProperties.Buttons>
                    <mxe:ButtonSettings Content="Clear" 
                     Command="{Binding 
                      $parent[mxdg:CellControl].DataControl.DataContext.ClearValueCommand}"/>
                </mxe:ButtonEditorProperties.Buttons>
            </mxe:ButtonEditorProperties>
        </mxdg:GridColumn.EditorProperties>
    </mxdg:GridColumn>
</mxdg:DataGridControl.Columns>
```

Чтобы позволить назначать таким образом потомки редакторов Eremex ячейкам в контейнерных контролах, сделайте следующее:

1. Создайте потомок контрола-редактора Eremex 

    !!! tip
    
        Все редакторы Eremex являются потомками `BaseEditor`.

2. Создайте потомок соответствующего класса `...Properties`. Например, если ваш пользовательский редактор производен от контрола `ButtonEditor`, производите ваш класс `...Properties` от `ButtonEditorProperties`.

    !!! tip
    
        Все классы `...Properties` редакторов Eremex являются потомками класса `BaseEditorProperties`.

3. Добавьте код регистрации пользовательского редактора в статический конструктор вашего класса `...Properties`. Используйте метод `EditorPropertiesProvider.Default.RegisterEditor`, чтобы зарегистрировать редактор.

Метод `EditorPropertiesProvider.Default.RegisterEditor` имеет следующую сигнатуру:

``` cs
void RegisterEditor(Type editor, Type editorProperties, Func<IBaseEditor> createEditorFunc, Func<BaseEditorProperties> createEditorPropertiesFunc)
```
Параметры метода:

- `editor` — тип пользовательского контрола-редактора.
- `editorProperties` — тип соответствующего класса `...Properties`.
- `createEditorFunc` — пользовательская функция, вызываемая при создании пользовательского контрола-редактора.
- `createEditorPropertiesFunc` — пользовательская функция, вызываемая при создании пользовательского объекта `...Properties`.

Следующий код создаёт пользовательский контрол `TextEditor`. Он переопределяет формат отображения, используемый для форматирования значений редактора. Класс _TextEditorWithCustomFormatProperties_ содержит статический конструктор, который регистрирует редактор.

``` cs
using Eremex.AvaloniaUI.Controls.Editors;

public class TextEditorWithCustomFormat : TextEditor
{
    protected override Type StyleKeyOverride => typeof(TextEditor);
}

public class TextEditorWithCustomFormatProperties : TextEditorProperties
{
    public static string Formatter = $"Header_{{0}}";
    public TextEditorWithCustomFormatProperties()
    {
        DisplayFormatString = Formatter;
    }
    static TextEditorWithCustomFormatProperties()
    {
        RegisterEditor();
    }

    static void RegisterEditor()
    {
        EditorPropertiesProvider.Default.RegisterEditor(typeof(TextEditorWithCustomFormat), typeof(TextEditorWithCustomFormatProperties),
            () => new TextEditorWithCustomFormat(), () => new TextEditorWithCustomFormatProperties());
    }
}
```


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
