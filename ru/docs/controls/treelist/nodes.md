---
title: Узлы
order: 6800
seealso: []
---

# Узлы

Класс [`TreeListNode`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode.md) инкапсулирует узел в контролах TreeList и TreeView.
Узел TreeView отображает одно значение, тогда как узел TreeList может отображать несколько значений (по значению для каждой колонки).

![treelist-treeview-nodes](../../images/treelist-treeview-nodes.png)

## Создание и доступ к узлам

В связанном режиме контролы TreeList и TreeView автоматически создают узлы для всех элементов источника данных.
Вы можете обращаться к созданным узлам с помощью следующих свойств:

- [`TreeListControlBase.Nodes`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/Nodes.md) — Корневые узлы.
- [`TreeListNode.Nodes`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode/Nodes.md) — Дочерние узлы узла.

Вам нужно создавать узлы вручную, когда контрол работает в [несвязанном режиме](data-binding/unbound-mode.md).

Смотрите также: [Поиск узлов](#поиск-узлов).

## Получение и установка значений узла

Свойство [`TreeListNode.Content`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode/Content.md) определяет объект данных узла. Вы можете привести значение этого свойства к типу вашего бизнес-объекта и затем считывать отдельные значения.
В [несвязанном режиме](data-binding/unbound-mode.md) вы можете вручную назначить объект свойству [`TreeListNode.Content`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode/Content.md). Не назначайте объекты свойству [`TreeListNode.Content`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode/Content.md) в связанном режиме.

Чтобы получить и задать значения отдельных ячеек, вы можете использовать следующие методы:

- [`GetCellValue`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/GetCellValue.md) и [`GetCellDisplayText`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/GetCellDisplayText.md)
- [`SetCellValue`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/SetCellValue.md)

## Сфокусированный узел

Используйте свойство [`TreeListControlBase.FocusedNode`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/FocusedNode.md), чтобы получить доступ к текущему сфокусированному узлу (узлу, который получает события клавиатуры). Чтобы получить данные (бизнес-объект) сфокусированного узла, используйте унаследованное свойство [`DataControlBase.FocusedItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/FocusedItem.md).

Событие [`TreeListControlBase.FocusedNodeChanged`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/FocusedNodeChanged.md) позволяет реагировать на перемещение фокуса между узлами.

Смотрите также: [Множественное выделение узлов (подсветка)](#множественное-выделение-узлов-подсветка).

## Иконки узлов

Контролы TreeList и TreeView поддерживают иконки узлов. Эти иконки отображаются перед значениями ячеек в [колонке иерархии](columns.md#колонка-иерархии).

![treelist-nodeimages](../../images/treelist-nodeimages.png)


Установите свойство [`TreeListControlBase.ShowNodeImages`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ShowNodeImages.md) в значение `true`, чтобы включить иконки узлов.

Следующие подходы позволяют предоставлять иконки узлов:

- Используйте свойство [`TreeListControlBase.NodeImageFieldName`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/NodeImageFieldName.md), чтобы указать свойство (поле) бизнес-объекта, которое возвращает иконку узла (объект `IImage`).

- Используйте свойство [`TreeListControlBase.NodeImageSelector`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/NodeImageSelector.md), чтобы указать селектор (объект [`ITreeListNodeImageSelector`](../../API/Eremex.AvaloniaUI.Controls.TreeList/ITreeListNodeImageSelector.md)), который возвращает иконки узлов для конкретных узлов.

- В несвязанном режиме вы можете задать иконку узла с помощью свойства [`TreeListNode.Image`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode/Image.md).

### Пример

Следующий код отображает изображения для узлов, имеющих определённое значение ячейки.

В примере создаётся объект [`NodeImageSelector`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/NodeImageSelector.md), который возвращает изображения в зависимости от свойства бизнес-объекта _OnVacation_.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"

<Grid.Resources>
    <local:MyNodeImageSelector x:Key="myNodeImageSelector" />
    ...
</Grid.Resources>

<mxtl:TreeListControl 
    Grid.Column="0" Grid.Row="1" Name="treeList2"
    ChildrenSelector="{StaticResource mySelector}"
    ItemsSource="{Binding Employees}"
    NodeImageSelector="{StaticResource myNodeImageSelector}"
    ShowNodeImages="True"
    >
...
</mxtl:TreeListControl>
```

``` csharp
using Avalonia.Media.Imaging;
using Avalonia.Platform;

public class MyNodeImageSelector : ITreeListNodeImageSelector
{
    IImage onVacationImage;
    IImage defaultImage;

    public MyNodeImageSelector()
    {
        onVacationImage = new Bitmap(AssetLoader.Open(
            new Uri("avares://AvaloniaApp1/Assets/plane.png")));
        defaultImage = null;
    }
    public IImage SelectImage(TreeListNode node)
    {
        Employee row = node.Content as Employee;
        return row.OnVacation? onVacationImage: defaultImage;
    }
}
```


## Разворачивание и сворачивание узлов

Пользователь может разворачивать и сворачивать узлы, имеющие дочерние элементы, следующими способами:

- Щёлкнуть кнопки разворачивания узла
 
  ![treelist-node-expand-button](../../images/treelist-node-expand-button.png)
  
- Нажать клавиши "+" и "-" на клавиатуре



Вы можете скрыть кнопки разворачивания узлов с помощью свойства [`TreeListControlBase.ShowExpandButtons`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ShowExpandButtons.md). В этом случае узлы можно разворачивать и сворачивать только в коде и с клавиатуры.


В коде вы можете управлять разворачиванием узлов с помощью следующих членов API:

- [`TreeListControlBase.AutoExpandAllNodes`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/AutoExpandAllNodes.md) — Определяет, следует ли автоматически разворачивать узлы при загрузке.
- [`TreeListControlBase.CollapseAllNodes`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/CollapseAllNodes.md) — Сворачивает все узлы.
- [`TreeListControlBase.ExpandAllNodes`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ExpandAllNodes.md) — Разворачивает все узлы.
- [`TreeListControlBase.ExpandNodesOnFiltering`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ExpandNodesOnFiltering.md) — Определяет, следует ли выполнять [поиск](filter-and-search.md) в свёрнутых узлах во время поиска/фильтрации данных, и автоматически разворачивать их, если их дочерние узлы соответствуют текущим критериям фильтра/поиска. Контролы TreeList и TreeView выполняют поиск только среди уже загруженных узлов. Для [иерархических источников данных](data-binding/index.md#иерархический-источник-данных) вы можете установить свойство [`AllowDynamicDataLoading`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/AllowDynamicDataLoading.md) в значение `false`, чтобы отключить динамическую загрузку узлов и загрузить все узлы сразу.

- [`TreeListNode.IsExpanded`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode/IsExpanded.md) — Позволяет разворачивать/сворачивать отдельный узел или получать его состояние развёрнутости.

Логическое свойство/поле в источнике элементов контрола ([`DataControlBase.ItemsSource`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ItemsSource.md)) может хранить состояния развёрнутости узлов. Используйте свойство [`TreeListControlBase.ExpandStateFieldName`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ExpandStateFieldName.md), чтобы указать это свойство. После установки этого свойства состояния развёрнутости узлов синхронизируются со значениями, хранящимися в этом свойстве в источнике элементов.

Следующие события возникают при разворачивании и сворачивании узлов:

- [`TreeListControlBase.NodeExpanding`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/NodeExpanding.md) — Возникает, когда узел вот-вот будет развёрнут. Вы можете использовать параметр события `Allow`, чтобы предотвратить разворачивание узла.
- [`TreeListControlBase.NodeExpanded`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/NodeExpanded.md) — Возникает после того, как узел был развёрнут.
- [`TreeListControlBase.NodeCollapsing`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/NodeCollapsing.md) — Возникает, когда узел вот-вот будет свёрнут. Вы можете использовать параметр события `Allow`, чтобы предотвратить сворачивание узла.
- [`TreeListControlBase.NodeCollapsed`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/NodeCollapsed.md) — Возникает после того, как узел был свёрнут.


## Встроенные флажки

Свойство [`TreeListControlBase.ShowNodeCheckBoxes`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ShowNodeCheckBoxes.md) включает встроенные флажки узлов для контролов TreeList и TreeView. Флажки позволяют пользователю отмечать (выбирать) отдельные узлы.

![treelist-node-checkboxes](../../images/treelist-node-checkboxes.png)

По умолчанию флажки имеют два состояния — отмечено и не отмечено. Если установить свойство [`AllowIndeterminateCheckState`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/AllowIndeterminateCheckState.md) в значение `true`, флажки будут поддерживать три состояния — отмечено, не отмечено и неопределённое.

Для контрола TreeList вы можете включить параметр [`TreeListControl.ShowCheckAllNodesCheckBox`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowCheckAllNodesCheckBox.md), чтобы отобразить флажок `Check All` в заголовке [колонки иерархии](columns.md#колонка-иерархии). Этот флажок выбирает и снимает выбор со всех узлов одновременно.

![treelist-node-checkboxes-checkallnodes](../../images/treelist-node-checkboxes-checkallnodes.png)

### Получение и установка состояния отметки узла

Используйте свойство узла [`TreeListNode.IsChecked`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode/IsChecked.md), чтобы считывать и задавать состояние отметки узла. Свойство [`TreeListNode.IsChecked`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode/IsChecked.md) имеет тип Nullable Boolean, поэтому вы можете присвоить свойству значение `null`, чтобы перевести узел в неопределённое состояние.



### Получение отмеченных узлов

Используйте метод [`GetAllCheckedNodes`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/GetAllCheckedNodes.md), чтобы получить узлы с состоянием "отмечено".

Вы также можете создать итератор для получения узлов, соответствующих пользовательским критериям.


### Синхронизация состояний отметки с источником данных

Используйте свойство [`CheckBoxFieldName`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/CheckBoxFieldName.md), чтобы синхронизировать состояния отметки узлов с определённым полем источника данных. Это свойство указывает имя логического или Nullable-логического поля источника данных, которое хранит состояния отметки узлов.

### Рекурсивная отметка

Свойство [`AllowRecursiveNodeChecking`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/AllowRecursiveNodeChecking.md) включает рекурсивную отметку узлов. В этом режиме дочерние узлы изменяют своё состояние отметки при изменении состояния отметки родительского узла, и наоборот.

## Множественное выделение узлов (подсветка)

Контролы TreeList и TreeView поддерживают режим множественного выделения узлов, который позволяет вам и вашему пользователю выделять (подсвечивать) несколько узлов одновременно.

![treeList-multipleSelection](../../images/treeList-multipleSelection.png)

Установите свойство [`SelectionMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/SelectionMode.md) в значение `Multiple`, чтобы включить режим множественного выделения узлов.

### Выделение узлов с помощью мыши и клавиатуры

Пользователи могут выделять несколько узлов с помощью мыши и клавиатуры. Для этого нужно щёлкать узлы, удерживая клавишу CTRL и/или SHIFT.

### Работа с выделением узлов в коде

Следующее API позволяет выделять/снимать выделение с узлов и определять, выделен ли узел:

- [`SelectAll`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/SelectAll.md)
- [`SelectNode`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/SelectNode.md)
- [`SelectRange`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/SelectRange.md)
- [`UnselectNode`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/UnselectNode.md)
- [`ClearSelection`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ClearSelection.md)
- [`IsNodeSelected`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/IsNodeSelected.md)

Чтобы получить выделение узлов, используйте следующие члены:

- [`GetSelectedNodes`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/GetSelectedNodes.md) — Возвращает коллекцию текущих выделенных объектов [`TreeListNode`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNode.md).
- [`SelectedItems`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/SelectedItems.md) — Определяет коллекцию объектов данных (бизнес-объектов), соответствующих выделенным узлам.

Обработайте событие [`SelectionChanged`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/SelectionChanged.md), чтобы реагировать на изменения выделения узлов.

Вызов любого метода, изменяющего состояние выделения узла, вызывает обновление контрола TreeList/TreeView и возникновение события [`SelectionChanged`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/SelectionChanged.md).

Чтобы выполнить пакетные изменения выделения узлов и предотвратить лишние обновления, вы можете обернуть код, изменяющий состояние выделения узлов, парой методов [`BeginSelection`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/BeginSelection.md) и [`EndSelection`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/EndSelection.md). В этом случае контрол перерисовывает выделение, а событие [`SelectionChanged`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/SelectionChanged.md) возникает после вызова метода [`EndSelection`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/EndSelection.md).

``` csharp
treeList1.SelectionMode = Eremex.AvaloniaUI.Controls.DataControl.RowSelectionMode.Multiple;
// Start a batch update of the node selection.
treeList1.BeginSelection();
treeList1.ClearSelection();
treeList1.SelectNode(node1);
treeList1.SelectNode(node2);
//...
// Finish the batch update.
treeList1.EndSelection();
```
### Сфокусированный узел и выделенные узлы

Сфокусированный узел — это узел, который получает пользовательский ввод. Сфокусированный узел может не совпадать с выделенным (подсвеченным) узлом в режиме множественного выделения. Подробности смотрите в следующих разделах.

#### Сфокусированный узел в режиме одиночного выделения

В режиме одиночного выделения сфокусированный узел автоматически получает состояние выделения. Вы можете использовать свойство [`FocusedNode`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/FocusedNode.md) и метод [`GetSelectedNodes`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/GetSelectedNodes.md), чтобы получить сфокусированный узел.

#### Сфокусированный узел в режиме множественного выделения

Состояния фокуса и выделения различаются в режиме множественного выделения узлов.
Выделен ли узел, можно определить по подсветке узла. Подсвечиваются только выделенные узлы.


В режиме множественного выделения щелчок по узлу одновременно фокусирует и выделяет этот узел. Однако пользователь может переключить состояние выделения сфокусированного узла с помощью следующих действий:

- Нажать CTRL+SPACE.
- Щёлкнуть по сфокусированному узлу, удерживая клавишу CTRL.

Когда вы выделяете узел в коде, этот узел не получает состояния фокуса в режиме множественного выделения, и наоборот.

## Поиск узлов

Метод [`TreeListControlBase.FindNode`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/FindNode.md) позволяет находить узлы, соответствующие пользовательским критериям.

Следующий код включает множественное выделение узлов, а также находит и выделяет два узла, содержащих определённые значения в поле _Name_.

``` csharp
treeList1.SelectionMode = Eremex.AvaloniaUI.Controls.DataControl.RowSelectionMode.Multiple;
treeList1.ExpandAllNodes();
TreeListNode node1 = treeList1.FindNode(node => 
    (node.Content as Employee).Name.Contains("Sam"));
TreeListNode node2 = treeList1.FindNode(node => 
    (node.Content as Employee).Name.Contains("Dan"));
treeList1.ClearSelection();
treeList1.SelectNode(node1);
treeList1.SelectNode(node2);
```

Смотрите также: [Фильтрация и поиск](filter-and-search.md).

## Перебор узлов

Вы можете создать итератор (объект [`TreeListNodeIterator`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNodeIterator.md)), чтобы рекурсивно перебирать узлы и выполнять над ними операцию.

Используйте один из следующих конструкторов, чтобы создать объект [`TreeListNodeIterator`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListNodeIterator.md):

``` csharp
// Recursively iterates through child nodes of the specified node, and their children.
public TreeListNodeIterator(TreeListNode? node, bool onlyExpanded = false)

// Recursively iterates through the specified nodes, and their children.
public TreeListNodeIterator(TreeListNodeCollection? nodes, bool onlyExpanded = false)
```

Параметр _onlyExpanded_ определяет, следует ли перебирать только развёрнутые узлы, или развёрнутые и свёрнутые узлы.

``` csharp
foreach (var node in new TreeListNodeIterator(treeList1.Nodes))
{
    if (node != null)
    {
        //do smth
    }
}
```



## Высота узла

Изначально все узлы имеют одинаковую высоту, достаточную для отображения одной строки текста. Вы можете задать пользовательскую высоту узла, а также включить автоматический расчёт высоты узла для полного отображения больших текстовых данных в ячейках.

### Пользовательская высота узла

- Свойство [`DataControlBase.RowMinHeight`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/RowMinHeight.md) — Получает или задаёт минимальную высоту узла.

    Если функция автоматической высоты узла отключена, все узлы имеют одинаковую высоту, заданную свойством [`DataControlBase.RowMinHeight`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/RowMinHeight.md).

### Автовысота узла

Для колонок с длинным текстом вы можете включить перенос текста, чтобы динамически регулировать высоту узлов и полностью отображать содержимое ячеек.

![treelist-rowautoheight](../../images/treelist-rowautoheight.png)

Чтобы включить перенос текста для ячеек колонки, назначьте объект [`TextEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditorProperties.md) (или его потомок, например, [`ButtonEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditorProperties.md)) свойству [`GridColumn.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md), и установите параметр [`TextEditorProperties.TextWrapping`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditorProperties/TextWrapping.md) в значение `Wrap`.

!!! tip

    Объект [`TextEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditorProperties.md) используется для настройки встраиваемого редактора [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) для колонки. Во время работы редактор создаётся с использованием этих параметров. Дополнительную информацию смотрите в разделе [Редактирование данных](data-editing/index.md).

Следующий код включает перенос текста для колонки treelist.

``` xml
<mxtl:TreeListColumn FieldName="LongDescription" Width="2*">
    <mxtl:TreeListColumn.EditorProperties>
        <mxe:TextEditorProperties TextWrapping="Wrap"/>
    </mxtl:TreeListColumn.EditorProperties>
</mxtl:TreeListColumn>
```

#### Автоматическая настройка высоты узла при горизонтальной прокрутке

Горизонтальная [виртуализация](performance-and-data-virtualization.md), поддерживаемая TreeList, повышает производительность контрола за счёт сокращения времени загрузки.

При включённой этой функции (по умолчанию) высота узлов автоматически рассчитывается в соответствии с содержимым текущих видимых ячеек. Ячейки за пределами области просмотра не влияют на расчёт высоты узла. При прокрутке к ячейкам с другой высотой содержимого высота узла динамически корректируется. Чтобы предотвратить динамическое изменение высоты узла при горизонтальной прокрутке, используйте свойство [`DataGridControl.AllowHorizontalVirtualization`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/AllowHorizontalVirtualization.md), чтобы отключить горизонтальную виртуализацию.

``` xml
<mxtl:TreeListControl x:Name="treeList" AllowHorizontalVirtualization="False">
```

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
