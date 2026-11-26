---
title: Привязка данных
order: 10000
seealso: []
---

# Привязка данных

После того как элемент управления TreeList/TreeView привязан к источнику данных, он создаёт узлы (объекты [`TreeListNode`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode.md)) для записей источника данных. Изначально узлы пусты. Вам необходимо указать свойства записей данных (поля источника данных), значения которых отображаются в узлах.

Чтобы отображать значения в узлах TreeList, создайте связанные или несвязанные колонки в коллекции [`TreeListControl.Columns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/Columns.md). Включите опцию [`TreeListControl.AutoGenerateColumns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AutoGenerateColumns.md), чтобы автоматически генерировать недостающие колонки для всех свойств/полей источника данных после привязки элемента управления. Дополнительную информацию смотрите в разделах [Колонки](../columns.md) и [Несвязанные колонки](unbound-columns.md).

Элемент управления TreeView — это однорядная (однопанельная) версия TreeList с одной колонкой. Используйте свойство [`TreeViewControl.DataFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/DataFieldName.md), чтобы указать, какие значения отображаются в его узлах в режиме привязки. Этот член определяет имя свойства/поля в источнике данных, данные которого отображаются элементом управления.

Свойство [`ItemsSource`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ItemsSource.md) позволяет привязать элемент управления TreeList/TreeView к источнику данных, который содержит информацию об отношениях "родитель-потомок" между записями. Элементы управления поддерживают два типа источников данных, которые отличаются способом кодирования информации об иерархии:

- Self-Referential (плоский) источник данных.
- Иерархический источник данных

## Self-Referential (плоский) источник данных

Self-Referential источник данных — это плоская таблица, коллекция или список, в котором записи имеют два служебных свойства/поля, используемых для создания отношений "родитель-потомок" между записями:

- Поле ключа (Key) — уникальный идентификатор записи.
- Поле ключа родителя (Parent Key) — хранит значение поля Key родительской записи.

Как правило, и поле Key, и поле Parent Key имеют целочисленный тип данных. Родительские и дочерние объекты данных всегда относятся к одному и тому же типу данных.

Дополнительную информацию смотрите в следующих разделах:

- [Привязка к Self-Referential источнику данных](binding-to-self-referential-data-source.md)
- [Как создать TreeView и привязать его к Self-Referential источнику данных](../examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)

### Общий API
- [`ItemsSource`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ItemsSource.md) — источник данных элемента управления.
- [`KeyFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/KeyFieldName.md) — имя поля, хранящего уникальные идентификаторы записей (значения поля Key).
- [`ParentFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ParentFieldName.md) — имя поля, хранящего идентификатор (значение поля Key) родителя записи.
- [`RootValue`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/RootValue.md) — значение поля Parent Key для корневого узла.

### API TreeList

- [`Columns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/Columns.md) — коллекция связанных и несвязанных колонок TreeList.
- [`AutoGenerateColumns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AutoGenerateColumns.md) — определяет, автоматически ли TreeList генерирует недостающие колонки для публичных свойств/полей, предоставляемых источником данных во время выполнения. Если коллекция [`Columns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/Columns.md) элемента управления уже содержит колонку, связанную с конкретным свойством/полем, дополнительная колонка, связанная с тем же свойством/полем, автоматически не создаётся.
- [`AutoGenerateServiceColumns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AutoGenerateServiceColumns.md) — определяет, автоматически ли TreeList создаёт колонки, связанные с полем Key и полем Parent Key. Это свойство действует, если включена опция [`AutoGenerateColumns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AutoGenerateColumns.md).

### API TreeView

- [`DataFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/DataFieldName.md) — имя поля, данные которого отображаются в элементе управления.

## Иерархический источник данных

В иерархическом источнике данных бизнес-объект (запись) имеет свойство, которое хранит коллекцию дочерних объектов данных. Родительские и дочерние объекты данных могут быть разных типов, но они должны иметь общий набор свойств, которые элементы управления TreeView/TreeList отображают в виде колонок.

### Динамическая загрузка данных

При привязке к иерархическому источнику данных контролы TreeList и TreeView загружают узлы по требованию: дочерние узлы загружаются динамически при разворачивании родительского узла. Это накладывает ограничения на отметку узлов флажками, фильтрацию, поиск и итоги.

Установите свойство [`AllowDynamicDataLoading`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/AllowDynamicDataLoading.md) в `false`, чтобы загружать все узлы одновременно сразу после привязки элемента управления к источнику данных.

Дополнительную информацию смотрите в следующих разделах:

- [Привязка к иерархическим данным](binding-to-hierarchical-data.md)
- [Как создать TreeList и привязать его к иерархическому источнику данных](../examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)

### Общий API

- [`ItemsSource`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ItemsSource.md) — установите это свойство в объект, содержащий данные (например, коллекцию корневых объектов), используемые для создания корневых узлов.
- [`ChildrenSelector`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenSelector.md) — селектор, возвращающий дочерние объекты для каждого бизнес-объекта (записи). Используйте либо [`ChildrenSelector`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenSelector.md), либо [`ChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenFieldName.md).
- [`ChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenFieldName.md) — имя свойства (поля), хранящего дочерние объекты для каждого бизнес-объекта. Используйте либо [`ChildrenSelector`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenSelector.md), либо [`ChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenFieldName.md).
- [`HasChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/HasChildrenFieldName.md) — имя логического свойства, возвращающего `true`, если объект имеет дочерние объекты. Свойство [`HasChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/HasChildrenFieldName.md) позволяет элементу управления динамически определять видимость кнопок разворачивания ('+'). Используйте [`HasChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/HasChildrenFieldName.md) вместе со свойством [`ChildrenFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ChildrenFieldName.md).

### API TreeView

- [`DataFieldName`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/DataFieldName.md) — имя поля, данные которого отображаются в элементе управления.

# Смотрите также
- [Привязка к иерархическим данным](binding-to-hierarchical-data.md)
- [Привязка к Self-Referential источнику данных](binding-to-self-referential-data-source.md)
- [Несвязанные колонки](unbound-columns.md)
- [Несвязанный режим](unbound-mode.md)
- [Как создать TreeView и привязать его к Self-Referential источнику данных](../examples/how-to-create-a-treeview-control-and-bind-it-to-a-self-referential-data-source.md)
- [Как создать TreeList и привязать его к иерархическому источнику данных](../examples/how-to-create-a-treelist-control-and-bind-it-to-a-hierarchical-data-source.md)

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
