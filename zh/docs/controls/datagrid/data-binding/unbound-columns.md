---
title: 未绑定的列
order: 1000
seealso: []
---

# 未绑定的列

您可以创建未绑定列以在 DataGrid 控件中显示自定义信息。未绑定的 column 未绑定到 underlying 数据源中的字段。您 should 使用 `DataGridControl.CustomUnboundColumnData` 事件手动填充此 column 数据。

要创建未绑定的 column，请执行以下操作：

- 创建一个 `GridColumn` 对象。
- 将 column 的 `UnboundDataType` 属性设置为该 column 想要显示的数据类型。 
- 将 column 的 `FieldName` 属性设置为唯一的字段名称。
- 使用 `Add` 或 `Insert` 方法将 column 添加到 `DataGridControl.Columns` 集合。您还可以将 position 和 column 与 `GridColumn.VisibleIndex` 属性结合起来。

请注意，control 不存储或缓存未绑定列的数据。它调用 `CustomUnboundColumnData` 事件，您需要处理该事件来指定未绑定列的数据。

`CustomUnboundColumnData` 事件在以下情况下触发：

- 当即将显示未绑定 column 中的单元格值时（例如，在 control 初始加载期间或滚动时）。在这种情况下，`IsGettingData` 事件参数返回 `true`。您需要为 `Value` 事件参数分配一个值。

- 当用户更改未绑定的 column 单元格中的数据时。在这种情况下，`IsGettingData` 事件参数返回 `false`。读取 `Value` 事件参数并将其手动缓存在您的存储中以供进一步使用。

您可以通过以下方法强制触发`CustomUnboundColumnData`事件：

- `RefreshRow` - 更新指定行。
- `RefreshData` - 强制网格重新加载所有数据。

## 示例 1

以下示例创建未绑定的只读 _Total_ column，并处理 _CustomUnboundColumnData_ 事件以根据其他字段的值根据表达式 `Total=UnitPrice*Quantity` 计算 column 值。事件处理程序检查 `IsGettingData` 事件参数，并在该参数为 `true` 时检索值。

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

## 示例2

以下示例显示如何缓存用户在未绑定列中输入的数据。该示例创建_Data_ column 并处理`CustomUnboundColumnData` 事件，将supply 数据发送到DataGrid 并保存用户键入的数据。

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
