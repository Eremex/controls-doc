---
title: Несвязанные колонки
order: 1000
seealso: []
---

# Несвязанные колонки

Вы можете создавать несвязанные колонки, чтобы отображать пользовательскую информацию в контроле DataGrid. Несвязанная колонка не привязана к полю в базовом источнике данных. Вам следует заполнять такую колонку данными вручную, используя событие `DataGridControl.CustomUnboundColumnData`.

Чтобы создать несвязанную колонку, выполните следующие действия:

- Создайте объект `GridColumn`.
- Установите свойство колонки `UnboundDataType` равным типу данных, который эта колонка должна отображать.
- Установите свойство колонки `FieldName` равным уникальному имени поля.
- Добавьте колонку в коллекцию `DataGridControl.Columns` с помощью метода `Add` или `Insert`. Вы также можете задать положение колонки с помощью свойства `GridColumn.VisibleIndex`.

Обратите внимание, что контрол не хранит и не кэширует данные для несвязанных колонок. Он вызывает событие `CustomUnboundColumnData`, которое вам нужно обработать, чтобы предоставить данные для несвязанных колонок.

Событие `CustomUnboundColumnData` вызывается в следующих случаях:

- Когда значение ячейки в несвязанной колонке должно быть отображено (например, при первоначальной загрузке контрола или во время прокрутки). В этом случае параметр события `IsGettingData` возвращает `true`. Вам нужно присвоить значение параметру события `Value`.

- Когда пользователь изменяет данные в ячейках несвязанной колонки. В этом случае параметр события `IsGettingData` возвращает `false`. Прочитайте параметр события `Value` и вручную кэшируйте его в своём хранилище для дальнейшего использования.

Вы можете принудительно вызвать событие `CustomUnboundColumnData` с помощью следующих методов:

- `RefreshRow` - Обновляет указанную строку.
- `RefreshData` - Заставляет грид перезагрузить все данные.

## Пример 1

Следующий пример создаёт несвязанную колонку только для чтения _Total_ и обрабатывает событие _CustomUnboundColumnData_ для вычисления значений колонки на основе значений других полей согласно выражению: `Total=UnitPrice*Quantity`. Обработчик события проверяет параметр события `IsGettingData` и получает значения, когда этот параметр равен `true`.

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

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
