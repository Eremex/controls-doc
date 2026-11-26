---
title: 自定义编辑器
order: 600
seealso: []
---

# 自定义编辑器 {#custom-editors}

## 注册要在容器控件中使用的自定义编辑器 {#register-custom-editors-for-use-in-container-controls}

在容器控件中指定就地编辑器的标准方法是使用这些容器控件提供的 `EditorProperties` 属性：

- [`GridColumn.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md)
- [`TreeListColumn.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md)
- [`TreeViewControl.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/EditorProperties.md)
- [`PropertyGridRow.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridRow/EditorProperties.md)
- [`ToolbarEditorItem.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarEditorItem/EditorProperties.md)

例如，以下代码将 [`ButtonEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md) 控件分配给一个网格列。该代码将 [`GridColumn.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md) 属性设置为一个 [`ButtonEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditorProperties.md) 对象。因此，当该列开始单元格编辑操作时，网格控件将根据指定的 [`ButtonEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditorProperties.md) 对象自动创建一个内嵌的 [`ButtonEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md) 控件。

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

要允许以这种方式将自定义 Eremex 编辑器的派生类分配给容器控件中的单元格，请执行以下操作：

1. 创建 Eremex 编辑器控件的派生类

    !!! tip
    
        所有 Eremex 编辑器都是 [`BaseEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor.md) 的派生类。

2. 创建相应 `...Properties` 类的派生类。例如，如果你的自定义编辑器派生自 [`ButtonEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md) 控件，则应将你的 `...Properties` 类派生自 [`ButtonEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditorProperties.md)。

    !!! tip
    
        Eremex 编辑器的所有 `...Properties` 类都是 [`BaseEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditorProperties.md) 类的派生类。

3. 在你的 `...Properties` 类的静态构造函数中添加自定义编辑器注册代码。使用 `EditorPropertiesProvider.Default.RegisterEditor` 方法来注册编辑器。

`EditorPropertiesProvider.Default.RegisterEditor` 方法具有以下签名：

``` cs
void RegisterEditor(Type editor, Type editorProperties, Func<IBaseEditor> createEditorFunc, Func<BaseEditorProperties> createEditorPropertiesFunc)
```
该方法的参数：

- `editor` — 自定义编辑器控件的类型。
- `editorProperties` — 相应 `...Properties` 类的类型。
- `createEditorFunc` — 创建自定义编辑器控件时调用的自定义函数。
- `createEditorPropertiesFunc` — 创建自定义 `...Properties` 对象时调用的自定义函数。

以下代码创建了一个自定义 [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) 控件。它重写了用于格式化编辑器值的显示格式。_TextEditorWithCustomFormatProperties_ 类包含一个静态构造函数，用于注册该编辑器。

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

<sup>*</sup> 本页面使用机器翻译技术翻译。
