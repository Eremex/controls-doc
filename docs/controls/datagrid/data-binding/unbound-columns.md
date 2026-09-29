---
title: Unbound Columns
order: 1000
seealso: []
---

# Unbound Columns

You can create unbound columns to display custom information in the DataGrid control. An unbound column is not bound to a field in the underlying data source. You should populate this column with data manually, using the `DataGridControl.CustomUnboundColumnData` event.

To create an unbound column, do the following:

- Create a `GridColumn` object.
- Set the column's `UnboundDataType` property to the type of data this column is intended to display. 
- Set the column's `FieldName` property to a unique field name.
- Add the column to the `DataGridControl.Columns` collection, using the `Add` or `Insert` method. You can also position the column with the `GridColumn.VisibleIndex` property.

Note that the control does not store or cache data for unbound columns. It invokes the `CustomUnboundColumnData` event, which you need to handle to specify data for unbound columns. 

The `CustomUnboundColumnData` event fires in the following cases:

- When a cell value in an unbound column is about to be displayed (for instance, during the initial load of the control or while scrolling). In this case, the `IsGettingData` event parameter returns `true`. You need to assign a value to the `Value` event parameter.

- When a user changes data in an unbound column's cells. In this case, the `IsGettingData` event parameter returns `false`. Read the `Value` event parameter and cache it manually in your storage for further use.

You can forcibly fire the `CustomUnboundColumnData` event with the following methods:

- `RefreshRow` - Updates a specified row.
- `RefreshData` - Forces the grid to reload all data.

## Example 1

The following example creates an unbound read-only _Total_ column, and handles the _CustomUnboundColumnData_ event to calculate column values based on values of other fields, according to the expression: `Total=UnitPrice*Quantity`. The event handler checks the `IsGettingData` event parameter, and retrieves values when this parameter is `true`. 

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

The following example shows how you can cache data entered by users in unbound columns. The example creates a _Data_ column and handles the `CustomUnboundColumnData` event to supply data to the DataGrid and save data typed by users.

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