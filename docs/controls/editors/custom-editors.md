---
title: Custom Editors
order: 600
seealso: []
---

# Custom Editors

## Register Custom Editors for Use in Container Controls

A standard approach to specifying in-place editors in container controls is to use the `EditorProperties` property provided by these container controls:

- `GridColumn.EditorProperties`
- `TreeListColumn.EditorProperties`
- `TreeViewControl.EditorProperties`
- `PropertyGridRow.EditorProperties`
- `ToolbarEditorItem.EditorProperties`

For example, the following code assigns a `ButtonEditor` control to a grid column. The code sets the `GridColumn.EditorProperties` property to a `ButtonEditorProperties` object. As a result, the grid control will automatically create an in-place `ButtonEditor` control based on the specified `ButtonEditorProperties` object when a cell edit operation starts in this column.

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

To allow custom Eremex editor descendants to be assigned this way to cells in container controls, do the following:

1. Create a descendant of the Eremex editor control 

    !!! tip
    
        All Eremex editors are `BaseEditor` descendants.

2. Create a descendant of the corresponding `...Properties` class. For instance, if your custom editor is derived from the `ButtonEditor` control, derive your `...Properties` class from `ButtonEditorProperties`.

    !!! tip
    
        All `...Properties` classes of Eremex editors are descendants of the `BaseEditorProperties` class.

3. Add custom editor registration code to the static constructor of your `...Properties` class. Use the `EditorPropertiesProvider.Default.RegisterEditor` method to register the editor.

The `EditorPropertiesProvider.Default.RegisterEditor` method has the following signature:

``` cs
void RegisterEditor(Type editor, Type editorProperties, Func<IBaseEditor> createEditorFunc, Func<BaseEditorProperties> createEditorPropertiesFunc)
```
The method's parameters:

- `editor` — The type of a custom editor control.
- `editorProperties` — The type of a corresponding `...Properties` class.
- `createEditorFunc` — A custom function invoked when a custom editor control is created.
- `createEditorPropertiesFunc` — A custom function invoked when a custom `...Properties` object is created.

The following code creates a custom `TextEditor` control. It overrides the display format used to format the editor's values. The _TextEditorWithCustomFormatProperties_ class contains a static constructor which registers the editor.

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

