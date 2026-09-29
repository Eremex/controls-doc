---
title: 未绑定的列
order: 70000
seealso: []
---

# 未绑定列 (TreeList)

如果您需要在 TreeList 列中显示自定义信息，您可以创建一个未绑定列。此列未绑定到底层数据源中的字段。您应使用 `TreeListControl.CustomUnboundColumnData` 事件手动填充此列的数据。

要创建未绑定列，请执行以下操作：

- 创建一个 `TreeListColumn` 对象。
- 将该列的 `UnboundDataType` 属性设置为该列想要显示的数据类型。 
- 将该列的 `FieldName` 属性设置为唯一的字段名称。
- 使用 `Add` 或 `Insert` 方法将该列添加到 `TreeListControl.Columns` 集合。您还可以结合使用 `TreeListColumn.VisibleIndex` 属性来指定列的位置。

请注意，该控件不存储或缓存未绑定列的数据。它会调用 `CustomUnboundColumnData` 事件，您需要处理该事件来指定未绑定列的数据。

`CustomUnboundColumnData` 事件在以下情况下触发：

- 当即将显示未绑定列中的单元格值时（例如，在该控件初始加载期间或滚动时）。在这种情况下，`IsGettingData` 事件参数返回 `true`。您需要为 `Value` 事件参数分配一个值。

- 当用户更改未绑定列的单元格中的数据时。在这种情况下，`IsGettingData` 事件参数返回 `false`。读取 `Value` 事件参数并将其手动缓存在您的存储中以供进一步使用。

您可以通过以下方法强制触发`CustomUnboundColumnData`事件：

- `RefreshRow` - 更新指定行。
- `RefreshData` - 强制网格重新加载所有数据。

## 示例 1
以下示例创建未绑定的只读 _Total_ 列，并处理 _CustomUnboundColumnData_ 事件，根据表达式 `Total=UnitPrice*Quantity` 依据其他字段的值计算列的值。事件处理程序检查 `IsGettingData` 事件参数，并在该参数为 `true` 时检索值。

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:sys="clr-namespace:System;assembly=System.Runtime"
...
<mxtl:TreeListControl Grid.Column="5" Width="400" Name="treeList1" 
                      CustomUnboundColumnData="treeList1_CustomUnboundColumnData" >
    <mxtl:TreeListControl.Columns>
        <mxtl:TreeListColumn Name="colUnitPrice" FieldName="UnitPrice" 
         Header="Unit Price" Width="*"  />
        <mxtl:TreeListColumn Name="colQuantity" FieldName="Quantity" 
         Header="Quantity" Width="*"/>
        <mxtl:TreeListColumn Name="colTotal" FieldName="Total" 
         Header="Total" Width="*" ReadOnly="True" 
         UnboundDataType="{x:Type sys:Decimal}" />
    </mxtl:TreeListControl.Columns>
</mxtl:TreeListControl>
```
``` cs
List<PurchaseRecord> list = new List<PurchaseRecord>();
list.Add(new PurchaseRecord() { UnitPrice = 1.3m, Quantity = 2 });
list.Add(new PurchaseRecord() { UnitPrice = 4m, Quantity = 1 });
list.Add(new PurchaseRecord() { UnitPrice = 10m, Quantity = 20 });
list.Add(new PurchaseRecord() { UnitPrice = 7m, Quantity = 12 });

treeList1.ItemsSource = list;

private void treeList1_CustomUnboundColumnData(object? sender, 
 TreeListUnboundColumnDataEventArgs e)
{
    if (e.IsGettingData && e.Column.FieldName == "Total")
    {
        PurchaseRecord rec = e.Node.Content as PurchaseRecord;
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

## 示例2

以下示例显示如何缓存用户在未绑定列中输入的数据。该示例创建 _Data_ 列并处理 `CustomUnboundColumnData` 事件，将提供的数据发送到 TreeList 并保存用户键入的数据。

``` cs
treeList1.Columns.Add(new TreeListColumn() 
{ 
    FieldName = "UserData", UnboundDataType = typeof(string), Header = "Data" 
});
treeList1.CustomUnboundColumnData += treeList1_CustomUnboundColumnData;

Dictionary<int, string> cache = new Dictionary<int, string>();

private void treeList1_CustomUnboundColumnData(object? sender, 
 TreeListUnboundColumnDataEventArgs e)
{
    if (e.Column.FieldName != "UserData") return;
    if (e.IsGettingData)
    {
        if (cache.ContainsKey(e.Node.Id))
            e.Value = cache[e.Node.Id];
        else
            e.Value = cache[e.Node.Id] = "-empty-";
    }
    else
    {
        cache[e.Node.Id] = e.Value.ToString();
    }
}

```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
