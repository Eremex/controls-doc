---
title: Custom Editors
order: 1000
seealso: []
---

# Custom Editors

DataGrid's default behavior is to use Eremex in-place editors to edit and format cell values. See [Data Editing](./index.md) for information on how to assign and access default in-place editors.

The current topic shows how to use cell templates to embed custom editors in cells. The following two approaches are available:

- [Assign a Custom Editor to a DataGrid Column Directly](#assign-a-custom-editor-to-a-grid-column-directly)
- [Dynamically Assign Editors Based on a Grid Column Data Type](#dynamically-assign-editors-based-on-a-grid-column-data-type)

!!! Note 

    Using templates has the following limitations:

    - Display text provided via cell templates is not used for sorting, grouping, and filtering data.
    - Cell templates are not [exported](../export.md).
 
## Assign a Custom Editor to a Grid Column Directly
 
You can specify an in-place editor for a grid column by assigning a `DataTemplate` to the [`GridColumn.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md) property.

- Create a `DataTemplate` object with an editor defined inside the template. 
- Assign the `DataTemplate` to the [`CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md) property.
- Bind the editor to a column value explicitly, when required. 
 
The following example shows XAML code that sets a grid column's [`CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md) property to a `TextBox` object:
 
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
 
### Implicit Data Binding for Eremex Editors
 
If you use an Eremex editor inside a `DataTemplate`, you may omit explicit data binding to a column value for the editor. 

Set the `x:Name` property to **"PART_Editor"** for the Eremex editor defined in a template. This ensures automatic binding of the editor's value ([`BaseEditor.EditorValue`](../../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md)) to the column's field. Additionally, the editor's appearance settings (border visibility and foreground colors in the active and inactive states) will be managed by the DataGrid control.

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
 
### Explicit Data Binding for Inplace Editors
 
Explicit data binding for inplace editors is required in the following cases:

- You use an editor that is not an Eremex editor. 

    !!! tip
    
        Eremex editors are controls derived from the [`Eremex.AvaloniaUI.Controls.Editors.BaseEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor.md) class.

- You need to specify a custom value converter in the data binding expression.
 
```xml
<DataTemplate DataType="pepa:Color">
    <mxe:PopupColorEditor x:Name="PART_Editor" EditorValue="{Binding Path=Value, 
     Converter={ecadpg:EcadColorToAvaloniaColorConverter}}"/>
</DataTemplate>
```
 
## Dynamically Assign Editors Based on a Grid Column Data Type
 
You can assign in-place editors to columns based on the data type of the column's bound field, as follows:

- Define an editor within a `DataTemplate`.
- Set the `DataTemplate.DataType` property to the target data type. 
- Assign the created template to the [`DataGridControl.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CellTemplate.md) property.

### Example - How to associate an in-place editor with a column's data type

The following example associates a [`TextEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) that paints values in green with columns bound to Integer fields:
 
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
 
- Initialize the [`DataGridControl.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CellTemplate.md) property with a *CellTemplateLocator* object.
- Populate the *CellTemplateLocator* object with `DataTemplate` objects associated with your data types.
 
The following example defines two `DataTemplate` objects with editors associated with the _String_ and _Integer_ data types, respectively.

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