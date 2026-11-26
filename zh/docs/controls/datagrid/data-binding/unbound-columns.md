---
title: 未绑定列
order: 1000
seealso: []
---

# 未绑定列 {#unbound-columns}

您可以创建未绑定列，在 DataGrid 控件中显示自定义信息。未绑定列不绑定到基础数据源中的字段。您需要使用 [`DataGridControl.CustomUnboundColumnData`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomUnboundColumnData.md) 事件手动为此列填充数据。

要创建未绑定列，请执行以下操作：

- 创建一个 [`GridColumn`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/GridColumn.md) 对象。
- 将列的 [`UnboundDataType`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/UnboundDataType.md) 属性设置为此列要显示的数据类型。
- 将列的 [`FieldName`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/FieldName.md) 属性设置为唯一的字段名。
- 使用 `Add` 或 `Insert` 方法将列添加到 [`DataGridControl.Columns`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/Columns.md) 集合中。还可以使用 [`GridColumn.VisibleIndex`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/VisibleIndex.md) 属性指定列的位置。

请注意，控件不会存储或缓存未绑定列的数据。控件会调用 [`CustomUnboundColumnData`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomUnboundColumnData.md) 事件，您需要处理该事件来为未绑定列指定数据。

[`CustomUnboundColumnData`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomUnboundColumnData.md) 事件在以下情况下触发：

- 未绑定列中的单元格值即将显示时（例如，在控件初次加载期间或滚动时）。在这种情况下，[`IsGettingData`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridUnboundColumnDataEventArgs/IsGettingData.md) 事件参数返回 `true`。您需要为 [`Value`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridUnboundColumnDataEventArgs/Value.md) 事件参数赋值。

- 用户更改未绑定列单元格中的数据时。在这种情况下，[`IsGettingData`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridUnboundColumnDataEventArgs/IsGettingData.md) 事件参数返回 `false`。读取 [`Value`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridUnboundColumnDataEventArgs/Value.md) 事件参数，并将其手动缓存到您的存储中以供后续使用。

可以使用以下方法强制触发 [`CustomUnboundColumnData`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomUnboundColumnData.md) 事件：

- [`RefreshRow`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/RefreshRow.md) - 更新指定的行。
- [`RefreshData`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/RefreshData.md) - 强制网格重新加载所有数据。

## 示例 1 {#example-1}

以下示例创建一个只读的未绑定列 _Total_，并处理 _CustomUnboundColumnData_ 事件，按照表达式 `Total=UnitPrice*Quantity` 根据其他字段的值计算列值。事件处理程序会检查 [`IsGettingData`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridUnboundColumnDataEventArgs/IsGettingData.md) 事件参数，并在该参数为 `true` 时提供值。

``` xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
xmlns:sys="clr-namespace:System;assembly=System.Runtime"
...
<mxdg:DataGridControl Name="dataGrid1" 
 CustomUnboundColumnData="dataGrid1_CustomUnboundColumnData" >
    <mxdg:DataGridControl.Columns>
        <mxdg:GridColumn Name="colUnitPrice" FieldName="UnitPrice" 
         Header="Unit Price" Width="*"  />
        <mxdg:GridColumn Name="colQuantity" FieldName="Quantity" 
         Header="Quantity" Width="*"/>
        <mxdg:GridColumn Name="colTotal" FieldName="Total" Header="Total" 
         Width="*" ReadOnly="True" UnboundDataType="{x:Type sys:Decimal}" />
    </mxdg:DataGridControl.Columns>
</mxdg:DataGridControl>
```
``` cs
List<PurchaseRecord> list = new List<PurchaseRecord>();
list.Add(new PurchaseRecord() { UnitPrice = 1.3m, Quantity = 2 });
list.Add(new PurchaseRecord() { UnitPrice = 4m, Quantity = 1 });
list.Add(new PurchaseRecord() { UnitPrice = 10m, Quantity = 20 });
list.Add(new PurchaseRecord() { UnitPrice = 7m, Quantity = 12 });

dataGrid1.ItemsSource = list;

private void dataGrid1_CustomUnboundColumnData(object? sender, DataGridUnboundColumnDataEventArgs e)
{
    if (e.IsGettingData && e.Column.FieldName == "Total")
    {
        PurchaseRecord rec = e.Item as PurchaseRecord;
        if (rec != null)
        {
            e.Value = rec.Quantity * rec.UnitPrice;
        }
    }
}

public partial class PurchaseRecord : ObservableObject
{
    [ObservableProperty]
    decimal unitPrice;
    [ObservableProperty]
    int quantity;
}
```

<!--TODO - There is no ListSourceRowIndex in the CustomUnboundColumnData

## Example 2

The following example shows how you can cache data entered by users in unbound columns. The example creates a _Data_ column and handles the [`CustomUnboundColumnData`](../../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomUnboundColumnData.md) event to supply data to the DataGrid and save data typed by users.

``` cs
dataGrid1.Columns.Add(new GridColumn() { FieldName = "UserData", UnboundDataType = typeof(string), Header = "Data" });
dataGrid1.CustomUnboundColumnData += dataGrid1_CustomUnboundColumnData;

Dictionary<object, string> cache = new Dictionary<object, string>();

private void dataGrid1_CustomUnboundColumnData(object? sender, DataGridUnboundColumnDataEventArgs e)
{
    if (e.Column.FieldName != "UserData") return;
    if (e.IsGettingData)
    {
        if (cache.ContainsKey(e.Item))
            e.Value = cache[e.Item];
        else
            e.Value = cache[e.Item] = "-empty-";
    }
    else
    {
        cache[e.Item] = e.Value.ToString();
    }
}

```

-->


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
