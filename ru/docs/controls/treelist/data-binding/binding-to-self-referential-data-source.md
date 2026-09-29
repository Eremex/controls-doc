---
title: Привязка к Self-Referential источнику данных
order: 90000
seealso: []
---

# Привязка к Self-Referential источнику данных

Вы можете использовать Self-Referential источник данных для кодирования иерархических отношений между записями. Self-Referential источник данных — это плоский список или коллекция записей. Его записи имеют два служебных свойства, определяющих отношения "родитель-потомок":

- _Поле ключа (Key field)_ — уникальный идентификатор записи (простого типа данных, например Integer).
- _Поле ключа родителя (Parent key field)_ — значение поля _Key field_ родительской записи.

На следующем изображении показан пример таблицы данных с самоссылками и элемент управления TreeList, отображающий эти данные после настройки соответствующих параметров элемента управления.

![TreeList - Key and Parent Key fields](../../../images/treelist-key-parent-relations.png)

Все записи, которые должны отображаться как корневые узлы (на корневом уровне), должны иметь одинаковое значение поля _Parent key field_. Корневое значение должно быть уникальным — оно не должно совпадать ни с одним значением поля Key в источнике данных.

Чтобы привязать элемент управления TreeList/TreeView к Self-Referential источнику данных, выполните следующие действия:

- Убедитесь, что записи источника данных имеют два публичных свойства, определяющих поле Key и поле _Parent key field_.
- Установите свойство `TreeListControlBase.KeyFieldName` элемента управления в имя поля Key.
- Установите свойство `TreeListControlBase.ParentFieldName` элемента управления в имя поля _Parent key field_.
- Установите свойство `TreeListControlBase.RootValue` элемента управления в корневое значение, определённое для корневых записей в источнике данных.

## Видимость служебных колонок

По умолчанию TreeList не создаёт колонки, связанные со служебными полями ключей. Чтобы разрешить элементу управления автоматически создавать колонки, связанные с указанными полями _Key field_ и _Parent key field_, установите свойства `AutoGenerateColumns` и `AutoGenerateServiceColumns` в значение `true`.

## Пример

Следующий пример привязывает элемент управления TreeList к Self-Referential источнику данных (коллекции записей _Employee_). Класс Employee определяет два свойства (_ID_ и _ParentID_), которые задают поле _Key field_ и поле _Parent key field_ записи соответственно. Корневые записи имеют значение поля _Parent key field_, равное **-1**, поэтому свойство `RootValue` элемента управления устанавливается в это значение.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
...
<mxtl:TreeListControl Grid.Column="0" Name="treeList2">                
    <mxtl:TreeListControl.Columns>
        <mxtl:TreeListColumn Name="colName1" FieldName="Name" />
        <mxtl:TreeListColumn Name="colBirthdate1" FieldName="Birthdate" >
            <mxtl:TreeListColumn.EditorProperties>
                <mxe:TextEditorProperties DisplayFormatString="yyyy-MM-dd"/>
            </mxtl:TreeListColumn.EditorProperties>
                        
        </mxtl:TreeListColumn>
    </mxtl:TreeListControl.Columns>
</mxtl:TreeListControl>
```
``` cs
using CommunityToolkit.Mvvm.ComponentModel;

ObservableCollection<Employee> employees = new ObservableCollection<Employee>();
employees.Add(new Employee() { 
    ID = 0, ParentID = -1, Name = "Serge Smolin", Birthdate = new DateTime(1990, 01, 5)});
employees.Add(new Employee() { 
    ID = 1, ParentID = 0, Name = "Alex Douglas", Birthdate = new DateTime(1975, 8, 27)});
employees.Add(new Employee() { 
    ID = 2, ParentID = 0, Name = "Dennis Parker", Birthdate = new DateTime(1985, 12, 17)});
employees.Add(new Employee() { 
    ID = 3, ParentID = 1, Name = "Pavel Morris", Birthdate = new DateTime(1987, 10, 15)});
employees.Add(new Employee() { 
    ID = 4, ParentID = 2, Name = "Mary Thompson", Birthdate = new DateTime(1991, 03, 16)});
employees.Add(new Employee() { 
    ID = 5, ParentID = 3, Name = "Vera Liskina", Birthdate = new DateTime(1991, 04, 16)});

treeList2.KeyFieldName = "ID";
treeList2.ParentFieldName = "ParentID";
treeList2.RootValue = -1;

treeList2.ItemsSource = employees;

public partial class Employee : ObservableObject
{
    [ObservableProperty]
    public string name = "";

    [ObservableProperty]
    public DateTime? birthdate = null;

    public int ID { get; set; }

    public int ParentID { get; set; }

}
```

# Смотрите также
- [Привязка данных](./index.md)
- [Привязка к иерархическим данным](binding-to-hierarchical-data.md)
- [Колонки](../columns.md)
- [Как создать TreeView и привязать его к Self-Referential источнику данных](../examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
