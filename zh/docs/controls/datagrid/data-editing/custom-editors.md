---
title: 自定义编辑器
order: 1000
seealso: []
---

# 自定义编辑器

默认情况下，DataGrid 使用 Eremex 内置编辑器来编辑和格式化单元格值。有关如何分配和访问默认内置编辑器的信息，请参阅 [数据编辑](./index.md)。

本主题介绍如何使用单元格模板将自定义编辑器嵌入到单元格中。以下两种方式均可使用：

- [直接为 DataGrid 列分配自定义编辑器](#直接为-datagrid-列分配自定义编辑器)
- [根据表格列的数据类型动态分配编辑器](#根据表格列的数据类型动态分配编辑器)

!!! Note 

    使用模板存在以下限制：

    - 通过单元格模板提供的显示文本不会用于数据的排序、分组和筛选。
    - 单元格模板不会被[导出](../export.md)。
 
## 直接为表格列分配自定义编辑器
 
您可以通过将 `DataTemplate` 分配给 `GridColumn.CellTemplate` 属性，为表格列指定内置编辑器。

- 创建一个 `DataTemplate` 对象，并在模板内部定义编辑器。
- 将该 `DataTemplate` 分配给 `CellTemplate` 属性。
- 如有需要，显式将编辑器绑定到列的值。
 
以下示例展示了将表格列的 `CellTemplate` 属性设置为 `TextBox` 对象的 XAML 代码：
 
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
 
### Eremex 编辑器的隐式数据绑定
 
如果您在 `DataTemplate` 内部使用 Eremex 编辑器，则可以省略对编辑器到列值的显式数据绑定。

请将模板中定义的 Eremex 编辑器的 `x:Name` 属性设置为 **"PART_Editor"**。这将确保编辑器的值（`BaseEditor.EditorValue`）自动绑定到该列的字段。此外，编辑器的外观设置（边框可见性以及激活和非激活状态下的前景色）将由 DataGrid 控件进行管理。

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
 
### 内置编辑器的显式数据绑定
 
在以下情况下需要为内置编辑器指定显式数据绑定：

- 您使用的编辑器不是 Eremex 编辑器。

    !!! tip
    
        Eremex 编辑器是派生自 `Eremex.AvaloniaUI.Controls.Editors.BaseEditor` 类的控件。

- 您需要在数据绑定表达式中指定自定义值转换器。
 
```xml
<DataTemplate DataType="pepa:Color">
    <mxe:PopupColorEditor x:Name="PART_Editor" EditorValue="{Binding Path=Value, 
     Converter={ecadpg:EcadColorToAvaloniaColorConverter}}"/>
</DataTemplate>
```
 
## 根据表格列的数据类型动态分配编辑器
 
您可以根据列所绑定字段的数据类型，按如下方式为列分配内置编辑器：

- 在 `DataTemplate` 内部定义编辑器。
- 将 `DataTemplate.DataType` 属性设置为目标数据类型。
- 将创建好的模板分配给 `DataGridControl.CellTemplate` 属性。

### 示例 - 如何将内置编辑器与列的数据类型关联

以下示例将一个以绿色显示值的 `TextEditor` 与绑定到 Integer 字段的列关联起来：
 
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

### 示例 - 如何将编辑器与多种数据类型关联

假设您有一个与不同数据类型关联的 `DataTemplate` 对象列表，并希望基于该列表创建列的内置编辑器。

要完成此任务，请执行以下操作：
 
- 在 code-behind 中创建一个自定义类（_CellTemplateLocator_），该类为特定数据类型返回一个 `DataTemplate`，并创建与该数据类型关联的控件。
 
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
 
- 使用 *CellTemplateLocator* 对象初始化 `DataGridControl.CellTemplate` 属性。
- 使用与您的数据类型关联的 `DataTemplate` 对象填充 *CellTemplateLocator* 对象。
 
以下示例定义了两个 `DataTemplate` 对象，其中的编辑器分别与 _String_ 和 _Integer_ 数据类型关联。

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

<sup>*</sup> 本页面使用机器翻译技术翻译。
