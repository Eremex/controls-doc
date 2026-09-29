---
title: 自定义编辑器
order: 600
seealso: []
---

# 自定义编辑器

`PropertyGrid` 支持在单元格中使用[内嵌编辑器](data-editing.md)。它们用于显示和编辑单元格的值。您可以在单元格中嵌入自定义编辑器，从而替换默认编辑器。

![propertygrid-inplaceeditor](../../images/propertygrid-inplaceeditor.png)

使用以下方法来指定自定义编辑器：

- [将编辑器直接分配给特定行](#assign-an-editor-to-a-row-cell-directly)
- [根据行的基础对象的数据类型动态分配编辑器](#dynamically-assign-editors-based-on-row-data-type)

 
## 将编辑器直接分配给行单元格
 
使用 `PropertyGridRow.CellTemplate` 属性将编辑器分配给特定行。为此请执行以下操作：
 
- 创建一个 DataTemplate 对象，并在模板内部定义编辑器。
- 将该 DataTemplate 分配给 `PropertyGridRow.CellTemplate` 属性。
- 在需要时，将编辑器显式绑定到该行的绑定字段。
 
以下示例展示了初始化 `CellTemplate` 属性的 XAML 代码：
 
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
 
### Eremex 编辑器的隐式数据绑定
 
如果在模板中使用 Eremex 编辑器，您可以省略将编辑器显式绑定到行的绑定字段。请确保 Eremex 编辑器的 `x:Name` 属性设置为 **"PART_Editor"**。在这种情况下，PropertyGrid 会自动将编辑器的 `EditorValue` 属性绑定到该行的字段。此外，PropertyGrid 还会开始维护内嵌编辑器的外观设置（激活和非激活状态下边框的可见性和前景色）。
 
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
 
### 显式数据绑定
 
在以下情况下需要使用显式数据绑定：

- 您使用的编辑器不是 Eremex 编辑器。所有 Eremex 编辑器都派生自 `Eremex.AvaloniaUI.Controls.Editors.BaseEditor` 类。
- 您需要在数据绑定表达式中指定自定义值转换器。
 
```xml
<DataTemplate DataType="pepa:Color">
    <mxe:PopupColorEditor x:Name="PART_Editor" 
     EditorValue="{Binding Value, Converter={ecadpg:EcadColorToAvaloniaColorConverter}}"/>
</DataTemplate>
```
 
## 根据行的数据类型动态分配编辑器
 
PropertyGrid 控件可以根据行的绑定字段的数据类型，自动为行单元格分配模板。为此请使用 `PropertyGridControl.CellTemplate` 属性。
 
以下示例将 TextEditor（将值绘制为绿色）与绑定到 Integer 字段的行相关联：
 
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
 
如果您有一个与不同数据类型相关联的 DataTemplate 对象列表，并希望将此列表分配给 PropertyGrid 控件，请使用以下方法：
 
- 在 code-behind 中创建一个自定义类，该类根据数据类型定位 DataTemplate，并创建与该数据类型关联的控件，如下所示：
 
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
        `Match` 方法的 _data_ 参数指定目标单元格模板的值。默认情况下，_data_ 参数包含绑定属性的值。您可以处理 `CustomCellTemplateData` 事件，以提供自定义对象作为单元格模板的值。指定的自定义对象将传递给 `Match` 方法。

- 使用 *CellTemplateLocator* 对象初始化 `PropertyGridControl.CellTemplate` 属性。
- 使用与您的数据类型相关联的 DataTemplate 对象填充 *CellTemplateLocator* 对象。
 
以下示例分别定义了两个与 String 和 Integer 数据类型相关联的 DataTemplate 对象。

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

## 另请参阅

- [数据编辑](data-editing.md)

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
