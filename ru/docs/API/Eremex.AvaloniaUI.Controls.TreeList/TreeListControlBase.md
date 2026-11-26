# Класс TreeListControlBase

Предоставляет базовый класс для контролов данных, отображающих коллекцию элементов, упорядоченных в иерархию узлов.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.TreeList`](./index.md)  
**Сборка:** `Eremex.Avalonia.Controls.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Объявление

```csharp
public abstract class TreeListControlBase : DataControlBase
```

## Свойства

| имя | описание |
| --- | --- |
| [AllowDragDrop](TreeListControlBase/AllowDragDrop.md) { get; set; } | Возвращает или задаёт, включено ли перетаскивание узлов. |
| [AllowDragDropSortedNodes](TreeListControlBase/AllowDragDropSortedNodes.md) { get; set; } | Возвращает или задаёт, можно ли перетаскивать узлы, когда данные отсортированы. |
| [AllowDropInsideNode](TreeListControlBase/AllowDropInsideNode.md) { get; set; } | Возвращает или задаёт, может ли узел принимать перетаскиваемые узлы внутрь себя. |
| [AllowDynamicDataLoading](TreeListControlBase/AllowDynamicDataLoading.md) { get; set; } | Возвращает или задаёт, загружаются ли дочерние узлы по требованию при разворачивании их родителя. |
| [AllowIndeterminateCheckState](TreeListControlBase/AllowIndeterminateCheckState.md) { get; set; } | Возвращает или задаёт, могут ли флажки родительских узлов находиться в неопределённом состоянии. |
| [AllowRecursiveNodeChecking](TreeListControlBase/AllowRecursiveNodeChecking.md) { get; set; } | Возвращает или задаёт, отмечает ли отметка узла всех его потомков. |
| [AllowScrollingOnDrag](TreeListControlBase/AllowScrollingOnDrag.md) { get; set; } | Возвращает или задаёт, прокручивается ли представление автоматически, когда перетаскиваемый элемент приближается к его краю. |
| [AutoExpandAllNodes](TreeListControlBase/AutoExpandAllNodes.md) { get; set; } | Возвращает или задаёт, разворачиваются ли все узлы автоматически. |
| [AutoExpandDelayOnDrag](TreeListControlBase/AutoExpandDelayOnDrag.md) { get; set; } | Возвращает или задаёт задержку перед автоматическим разворачиванием узла при перетаскивании над ним. |
| [AutoExpandOnDrag](TreeListControlBase/AutoExpandOnDrag.md) { get; set; } | Возвращает или задаёт, разворачивается ли свёрнутый узел автоматически, когда над ним находится перетаскиваемый элемент. |
| [AutoScrollOnSorting](TreeListControlBase/AutoScrollOnSorting.md) { get; set; } | Возвращает или задаёт, прокручивается ли представление к узлу с фокусом после сортировки. |
| [CheckBoxFieldName](TreeListControlBase/CheckBoxFieldName.md) { get; set; } | Возвращает или задаёт поле, хранящее состояния флажков узлов. |
| [ChildrenFieldName](TreeListControlBase/ChildrenFieldName.md) { get; set; } | Возвращает или задаёт поле, содержащее дочерние элементы узла. |
| [ChildrenSelector](TreeListControlBase/ChildrenSelector.md) { get; set; } | Возвращает или задаёт объект, предоставляющий дочерние элементы для узлов. |
| [Commands](TreeListControlBase/Commands.md) { get; } | Возвращает команды дерева. |
| [ExpandNodesOnFiltering](TreeListControlBase/ExpandNodesOnFiltering.md) { get; set; } | Возвращает или задаёт, разворачиваются ли узлы автоматически при применении фильтра. |
| [ExpandStateFieldName](TreeListControlBase/ExpandStateFieldName.md) { get; set; } | Возвращает или задаёт поле, хранящее развёрнутое состояние узлов. |
| [FilterMode](TreeListControlBase/FilterMode.md) { get; set; } | Возвращает или задаёт, какие узлы отображаются при применении фильтра. |
| [FocusedNode](TreeListControlBase/FocusedNode.md) { get; set; } | Возвращает или задаёт узел с фокусом. |
| [HasChildrenFieldName](TreeListControlBase/HasChildrenFieldName.md) { get; set; } | Возвращает или задаёт поле, указывающее, есть ли у узла дочерние узлы. |
| [KeyFieldName](TreeListControlBase/KeyFieldName.md) { get; set; } | Возвращает или задаёт поле, однозначно идентифицирующее узлы в Self-Referential данных. |
| [NodeImageFieldName](TreeListControlBase/NodeImageFieldName.md) { get; set; } | Возвращает или задаёт поле, содержащее изображения узлов. |
| [NodeImageSelector](TreeListControlBase/NodeImageSelector.md) { get; set; } | Возвращает или задаёт объект, предоставляющий изображения для узлов. |
| [Nodes](TreeListControlBase/Nodes.md) { get; } | Возвращает корневую коллекцию узлов. |
| [ParentFieldName](TreeListControlBase/ParentFieldName.md) { get; set; } | Возвращает или задаёт поле, ссылающееся на ключ родительского узла в Self-Referential данных. |
| [RestoreStateKeyFieldName](TreeListControlBase/RestoreStateKeyFieldName.md) { get; set; } | Возвращает или задаёт поле, значения которого идентифицируют узлы при восстановлении сохранённого состояния контрола. |
| [RootValue](TreeListControlBase/RootValue.md) { get; set; } | Возвращает или задаёт значение родительского ключа, идентифицирующее корневые узлы в Self-Referential данных. |
| [RowCellMenu](TreeListControlBase/RowCellMenu.md) { get; set; } | Возвращает или задаёт контекстное меню, вызываемое для ячеек данных. |
| [ShowExpandButtons](TreeListControlBase/ShowExpandButtons.md) { get; set; } | Возвращает или задаёт, отображаются ли кнопки разворачивания. |
| [ShowNodeCheckBoxes](TreeListControlBase/ShowNodeCheckBoxes.md) { get; set; } | Возвращает или задаёт, отображаются ли флажки узлов. |
| [ShowNodeImages](TreeListControlBase/ShowNodeImages.md) { get; set; } | Возвращает или задаёт, отображаются ли изображения узлов. |
| [ShowRootIndent](TreeListControlBase/ShowRootIndent.md) { get; set; } | Возвращает или задаёт, отображается ли отступ корневого уровня. |
| [UsePlatformRowDragDrop](TreeListControlBase/UsePlatformRowDragDrop.md) { get; set; } | Возвращает или задаёт, используется ли перетаскивание платформы при перетаскивании узлов. |
| [VisibleNodeCount](TreeListControlBase/VisibleNodeCount.md) { get; } | Возвращает количество видимых в данный момент узлов. |

## Методы

| имя | описание |
| --- | --- |
| [CheckAllNodes](TreeListControlBase/CheckAllNodes.md)() | Отмечает все видимые узлы. |
| [CollapseAllNodes](TreeListControlBase/CollapseAllNodes.md)() | Сворачивает все узлы. |
| override [CommitEditing](TreeListControlBase/CommitEditing.md)() |  |
| [ExpandAllNodes](TreeListControlBase/ExpandAllNodes.md)() | Разворачивает все узлы. |
| [FindNode](TreeListControlBase/FindNode.md)(…) | Возвращает первый узел, удовлетворяющий указанному условию. |
| [GetAllCheckedNodes](TreeListControlBase/GetAllCheckedNodes.md)() | Возвращает список всех отмеченных узлов. |
| [GetNodeByVisibleIndex](TreeListControlBase/GetNodeByVisibleIndex.md)(…) | Возвращает узел, отображаемый по указанному видимому индексу. |
| [GetSelectedNodes](TreeListControlBase/GetSelectedNodes.md)() | Возвращает список выделенных узлов. |
| [GetVisibleIndexByNode](TreeListControlBase/GetVisibleIndexByNode.md)(…) | Возвращает видимый индекс указанного узла. |
| [IsNodeSelected](TreeListControlBase/IsNodeSelected.md)(…) | Возвращает, выделен ли указанный узел. |
| [MoveFirstNode](TreeListControlBase/MoveFirstNode.md)() | Перемещает фокус на первый узел. |
| [MoveLastNode](TreeListControlBase/MoveLastNode.md)() | Перемещает фокус на последний узел. |
| [MoveNextNode](TreeListControlBase/MoveNextNode.md)() | Перемещает фокус на следующий узел. |
| [MovePrevNode](TreeListControlBase/MovePrevNode.md)(…) | Перемещает фокус на предыдущий узел. |
| [RefreshData](TreeListControlBase/RefreshData.md)() | Обновляет данные контрола. |
| [RefreshNode](TreeListControlBase/RefreshNode.md)(…) | Обновляет отображаемые данные указанного узла. |
| [RefreshNodeChildren](TreeListControlBase/RefreshNodeChildren.md)(…) | Обновляет дочерние узлы указанного узла. |
| [ScrollIntoView](TreeListControlBase/ScrollIntoView.md)(…) | Прокручивает представление так, чтобы указанный узел стал видимым. |
| [SelectNode](TreeListControlBase/SelectNode.md)(…) | Выделяет указанный узел. |
| [SelectRange](TreeListControlBase/SelectRange.md)(…) | Выделяет все узлы между указанными начальным и конечным узлами. |
| [UncheckAllNodes](TreeListControlBase/UncheckAllNodes.md)() | Снимает отметку со всех видимых узлов. |
| [UnselectNode](TreeListControlBase/UnselectNode.md)(…) | Снимает выделение с указанного узла. |

## События

| имя | описание |
| --- | --- |
| event [CompleteDragDrop](TreeListControlBase/CompleteDragDrop.md) | Происходит после завершения операции перетаскивания. |
| event [CustomNodeFilter](TreeListControlBase/CustomNodeFilter.md) | Происходит при применении пользовательской фильтрации к узлам. |
| event [DragOver](TreeListControlBase/DragOver.md) | Происходит, когда перетаскиваемый элемент находится над контролом. |
| event [Drop](TreeListControlBase/Drop.md) | Происходит, когда перетаскиваемый элемент бросается на контрол. |
| event [FocusedColumnChanged](TreeListControlBase/FocusedColumnChanged.md) | Происходит при смене колонки с фокусом. |
| event [FocusedNodeChanged](TreeListControlBase/FocusedNodeChanged.md) | Происходит при смене узла с фокусом. |
| event [NodeChanged](TreeListControlBase/NodeChanged.md) | Происходит при изменении данных или состояния узла. |
| event [NodeCheckStateChanged](TreeListControlBase/NodeCheckStateChanged.md) | Происходит при изменении состояния флажка узла. |
| event [NodeClick](TreeListControlBase/NodeClick.md) | Происходит при щелчке по узлу. |
| event [NodeCollapsed](TreeListControlBase/NodeCollapsed.md) | Происходит после сворачивания узла. |
| event [NodeCollapsing](TreeListControlBase/NodeCollapsing.md) | Происходит перед сворачиванием узла. |
| event [NodeExpanded](TreeListControlBase/NodeExpanded.md) | Происходит после разворачивания узла. |
| event [NodeExpanding](TreeListControlBase/NodeExpanding.md) | Происходит перед разворачиванием узла. |
| event [SelectionChanged](TreeListControlBase/SelectionChanged.md) | Происходит при изменении выделения узлов. |
| event [StartDrag](TreeListControlBase/StartDrag.md) | Происходит при начале перетаскивания узла. |

## См. также

* класс [DataControlBase](../Eremex.AvaloniaUI.Controls.DataControl/DataControlBase.md)
* пространство имён [Eremex.AvaloniaUI.Controls.TreeList](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
