---
title: Custom Editors in TreeList and TreeView Cells
seealso: []
---

# Custom Editors in TreeList and TreeView Cells

TreeList and TreeView controls use in-place Eremex editors for editing and formatting cell values, by default. See [Data Editing](./index.md) for information on how to assign and access default in-place editors.

The current topic shows how to use cell templates to embed custom editors in cells. The following two approaches are available:

- [Assign a Custom Editor to a  TreeList Column and TreeView Directly](#assign-a-custom-editor-to-a-treelist-column-and-treeview-directly)
- [Dynamically Assign Editors Based on TreeList Column Data Type](#dynamically-assign-editors-based-on-a-treelist-column-data-type)

!!! Note 

    Using templates has the following limitations:

    - Display text provided via cell templates is not used for sorting, grouping, and filtering data.
    - Cell templates are not [exported](../export.md).
 
## Assign a Custom Editor to a TreeList Column and TreeView Directly
 
You can assign an in-place editor to a TreeList column or TreeView by creating a `DataTemplate`. Use the `TreeListColumn.CellTemplate` and `TreeViewControl.CellTemplate` properties for this purpose, as follows.

- Create a `DataTemplate` object with an editor defined inside the template. 
- Assign the `DataTemplate` to the `CellTemplate` property.
- Bind the editor to a column value explicitly, when required. 
 
The following example shows XAML code that sets a TreeList column's `CellTemplate` property to a `TextBox` object:
 
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
 
### Implicit Data Binding for Eremex Editors
 
If you use an Eremex editor inside a `DataTemplate`, you may omit explicit data binding to a column value for the editor. Ensure that the Eremex editor has the `x:Name` property set to **"PART_Editor"**. In this case, the TreeList/TreeView control automatically binds the editor's `EditorValue` property to the column's cell value. Additionally, the control starts maintaining the in-place editor's appearance settings (the borders' visibility and foreground colors in the active and inactive states).
 
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
 
### Explicit Data Binding
 
Explicit data binding is required in the following cases:

- You use an editor that is not an Eremex editor. 

!!! tip

    Eremex editors are controls derived from the `Eremex.AvaloniaUI.Controls.Editors.BaseEditor` class.

- You need to specify a custom value converter in the data binding expression.
 
```xml
<DataTemplate DataType="pepa:Color">
    <mxe:PopupColorEditor x:Name="PART_Editor" 
     EditorValue="{Binding Path=Value, 
      Converter={ecadpg:EcadColorToAvaloniaColorConverter}}"/>
</DataTemplate>
```
 
## Dynamically Assign Editors Based on a TreeList Column Data Type
 
The TreeList control allows you to assign in-place editors wrapped within `DataTemplate`s to column cells based on the data type of the column's bound field. Use the `TreeListControl.CellTemplate` property for this purpose.

### Example - How to associate an editor with a single data type

The following example associates a `TextEditor` that paints values in green with columns bound to Integer fields:
 
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

### Example - How to associate editors with multiple data types

Assume that you have a list of `DataTemplate` objects associated with different data types, and want to create column in-place editors based on this list. 

Do the following to accomplish this task:
 
- Create a custom class (_CellTemplateLocator_) in code-behind that returns a `DataTemplate` for a specific data type, and creates a control associated with this data type.
 
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
 
- Initialize the `TreeListControl.CellTemplate` property with a *CellTemplateLocator* object.
- Populate the *CellTemplateLocator* object with `DataTemplate` objects associated with your data types.
 
The following example defines two `DataTemplate` objects with editors associated with the _String_ and _Integer_ data types, respectively.

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