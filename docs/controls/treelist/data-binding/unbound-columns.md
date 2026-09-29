---
title: Unbound Columns
order: 70000
seealso: []
---

# Unbound Columns (TreeList)

If you need to display custom information in a TreeList column, you can create an unbound column. This column is not bound to a field in the underlying data source. You should populate this column with data manually, using the `TreeListControl.CustomUnboundColumnData` event.

To create an unbound column, do the following:

- Create a `TreeListColumn` object.
- Set the column's `UnboundDataType` property to the type of data this column is intended to display. 
- Set the column's `FieldName` property to a unique field name.
- Add the column to the `TreeListControl.Columns` collection, using the `Add` or `Insert` method. You can also position the column with the `TreeListColumn.VisibleIndex` property.

Note that the control does not store or cache data for unbound columns. It invokes the `CustomUnboundColumnData` event, which you need to handle to specify data for unbound columns. 

The `CustomUnboundColumnData` event fires in the following cases:

- When a cell value in an unbound column is about to be displayed (for instance, during the initial load of the control or while scrolling). In this case, the `IsGettingData` event parameter returns `true`. You need to assign a value to the `Value` event parameter.

- When a user changes data in unbound columns' cells. In this case, the `IsGettingData` event parameter returns `false`. Read the `Value` event parameter and cache it manually in your storage for further use.

You can forcibly fire the `CustomUnboundColumnData` event with the following methods:

- `RefreshRow` - Updates a specified row.
- `RefreshData` - Forces the grid to reload all data.

## Example 1
The following example creates an unbound read-only _Total_ column, and handles the _CustomUnboundColumnData_ event to calculate column values based on values of other fields, according to the expression: `Total=UnitPrice*Quantity`. The event handler checks the `IsGettingData` event parameter, and retrieves values when this parameter is `true`. 

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

## Example 2

The following example shows how you can cache data entered by users in unbound columns. The example creates a _Data_ column and handles the `CustomUnboundColumnData` event to supply data to the TreeList and save data typed by users.

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