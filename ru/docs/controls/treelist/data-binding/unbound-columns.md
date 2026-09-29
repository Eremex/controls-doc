---
title: Несвязанные колонки (TreeList)
order: 70000
seealso: []
---

# Несвязанные колонки (TreeList)

Если вам нужно отобразить пользовательскую информацию в колонке TreeList, вы можете создать несвязанную колонку. Такая колонка не привязана к полю в базовом источнике данных. Данные для этой колонки необходимо предоставлять вручную, используя событие `TreeListControl.CustomUnboundColumnData`.

Чтобы создать несвязанную колонку, выполните следующие действия:

- Создайте объект `TreeListColumn`.
- Установите свойство `UnboundDataType` колонки в тип данных, который предполагается отображать в этой колонке.
- Установите свойство `FieldName` колонки в уникальное имя поля.
- Добавьте колонку в коллекцию `TreeListControl.Columns` с помощью метода `Add` или `Insert`. Вы также можете задать положение колонки с помощью свойства `TreeListColumn.VisibleIndex`.

Обратите внимание, что элемент управления не хранит и не кэширует данные для несвязанных колонок. Он вызывает событие `CustomUnboundColumnData`, которое необходимо обрабатывать для указания данных несвязанных колонок.

Событие `CustomUnboundColumnData` возникает в следующих случаях:

- Когда значение ячейки в несвязанной колонке должно быть отображено (например, при первоначальной загрузке элемента управления или при прокрутке). В этом случае параметр события `IsGettingData` возвращает `true`. Вам необходимо присвоить значение параметру события `Value`.

- Когда пользователь изменяет данные в ячейках несвязанных колонок. В этом случае параметр события `IsGettingData` возвращает `false`. Считайте параметр события `Value` и вручную сохраните его в своём хранилище для дальнейшего использования.

Вы можете принудительно вызвать событие `CustomUnboundColumnData` с помощью следующих методов:

- `RefreshRow` — обновляет указанную строку.
- `RefreshData` — заставляет сетку перезагрузить все данные.

## Пример 1
Следующий пример создаёт несвязанную колонку _Total_, доступную только для чтения, и обрабатывает событие _CustomUnboundColumnData_ для вычисления значений колонки на основе значений других полей по формуле: `Total=UnitPrice*Quantity`. Обработчик события проверяет параметр события `IsGettingData` и получает значения, когда этот параметр равен `true`.

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

## Пример 2

Следующий пример показывает, как можно кэшировать данные, введённые пользователями в несвязанных колонках. В примере создаётся колонка _Data_, а событие `CustomUnboundColumnData` обрабатывается для предоставления данных TreeList и сохранения данных, введённых пользователями.

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

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
