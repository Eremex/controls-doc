---
title: TreeList 和 TreeView 单元中的自定义编辑器
seealso: []
---

# TreeList 和 TreeView 单元中的自定义编辑器

默认情况下，TreeList 和 TreeView 控件使用就地 Eremex 编辑器来编辑和格式化单元格值。有关如何分配和访问默认就地编辑器的信息，请参阅 [数据编辑](./index.md)。

当前主题展示如何使用单元格模板在单元格中嵌入自定义编辑器。可以采用以下两种方法：

- [直接将自定义编辑器分配给 TreeList 列和 TreeView](#assign-a-custom-editor-to-a-treelist-column-and-treeview-directly)
- [基于 TreeList 列数据类型动态分配编辑器](#dynamically-assign-editors-based-on-a-treelist-column-data-type)

!!!笔记

使用模板有以下限制：

- 通过单元格模板提供的显示文本不用于排序、分组和过滤数据。
    - 单元格模板不会被[导出](../export.md)。
 
## 直接将自定义编辑器分配给 TreeList 列和 TreeView
 
您可以通过创建 `DataTemplate` 将就地编辑器分配给 TreeList、列或 TreeView。为此目的，请使用 `TreeListColumn.CellTemplate` 和 `TreeViewControl.CellTemplate` 属性，如下所示。

- 使用模板内定义的编辑器创建 `DataTemplate` 对象。 
- 将 `DataTemplate` 分配给 `CellTemplate` 属性。
- 需要时，将编辑器显式绑定到列值。
 
以下示例显示将 TreeList 列的 `CellTemplate` 属性设置为 `TextBox` 对象的 XAML 代码：
 
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
 
### Eremex 编辑器的隐式数据绑定
 
如果您在 `DataTemplate` 内使用 Eremex 编辑器，则可以省略编辑器与列值的显式数据绑定。确保 Eremex 编辑器的 `x:Name` 属性设置为 **“PART_Editor”**。在这种情况下，TreeList/TreeView 控件会自动将编辑器的 `EditorValue` 属性绑定到列的单元格值。此外，控件会开始维护就地编辑器的外观设置（活动和非活动状态下的边框可见性和前景色）。
 
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
 
### 显式数据绑定
 
在以下情况下需要显式数据绑定：

- 您使用的编辑器不是 Eremex 编辑器。

!!!提示

Eremex 编辑器是从 `Eremex.AvaloniaUI.Controls.Editors.BaseEditor` 类派生的控件。

- 您需要在数据绑定表达式中指定自定义值转换器。
 
```xml
<DataTemplate DataType="pepa:Color">
    <mxe:PopupColorEditor x:Name="PART_Editor" 
     EditorValue="{Binding Path=Value, 
      Converter={ecadpg:EcadColorToAvaloniaColorConverter}}"/>
</DataTemplate>
```
 
## 基于 TreeList 列数据类型动态分配编辑器
 
TreeList 控件允许您根据列绑定字段的数据类型将 `DataTemplate` 中包含的就地编辑器分配给列单元格。为此目的，请使用 `TreeListControl.CellTemplate` 属性。

### 示例 - 如何将编辑器与单一数据类型关联

以下示例将用绿色绘制值的 `TextEditor` 与绑定到整数字段的列相关联：
 
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

### 示例 - 如何将编辑器与多种数据类型关联

假设您有一个列表，其中包含与不同数据类型相关联的 `DataTemplate` 对象，并且想要基于此列表创建列的就地编辑器。

执行以下操作来完成此任务：
 
- 在后台代码 (code-behind) 中创建自定义类 (_CellTemplateLocator_)，该类返回特定数据类型对应的 `DataTemplate`，并将其与使用该数据类型的控件相关联。
 
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
 
- 使用 *CellTemplateLocator* 对象初始化 `TreeListControl.CellTemplate` 属性。
- 使用与您的数据类型相关联的 `DataTemplate` 对象填充 *CellTemplateLocator* 对象。
 
以下示例定义了两个与编辑器相关联的 `DataTemplate` 对象，分别具有 _String_ 和 _Integer_ 数据类型。

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

<sup>*</sup> 本页面使用机器翻译技术翻译。
