# Класс DockManager

Управляет размещением закреплённых, плавающих и автоскрытых панелей и документов.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.Docking`](./index.md)  
**Сборка:** `Eremex.Avalonia.Controls.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Объявление

```csharp
public class DockManager : TemplatedControl
```

## Конструкторы

| имя | описание |
| --- | --- |
| [DockManager](DockManager/DockManager.md)() | Инициализирует новый экземпляр класса DockManager. |

## Свойства

| имя | описание |
| --- | --- |
| [ActiveDockItem](DockManager/ActiveDockItem.md) { get; } | Возвращает активный в данный момент элемент докинга. |
| [AllowDocumentSwitcher](DockManager/AllowDocumentSwitcher.md) { get; set; } | Возвращает или задаёт, могут ли пользователи открывать переключатель документов. |
| [AllowFreeDocumentLayout](DockManager/AllowFreeDocumentLayout.md) { get; set; } | Возвращает или задаёт, можно ли располагать группы документов как в горизонтальном, так и в вертикальном направлении внутри хоста документов. |
| [AutoHideGroups](DockManager/AutoHideGroups.md) { get; } | Возвращает коллекцию групп автоскрытия. |
| [AutoHideMode](DockManager/AutoHideMode.md) { get; set; } | Возвращает или задаёт, перекрывают ли развёрнутые автоскрываемые панели размещение докинга или занимают в нём место. |
| [AutoHideOnlyActivePane](DockManager/AutoHideOnlyActivePane.md) { get; set; } | Возвращает или задаёт, влияют ли команды автоскрытия и закрепления только на активную панель в группе вкладок. |
| [ClosedPanes](DockManager/ClosedPanes.md) { get; } | Возвращает коллекцию закрытых панелей, доступных для восстановления. |
| [CloseOnlyActivePane](DockManager/CloseOnlyActivePane.md) { get; set; } | Возвращает или задаёт, закрывает ли команда закрытия только активную панель в группе вкладок. |
| [Commands](DockManager/Commands.md) { get; } | Возвращает команды менеджера докинга. |
| [FloatGroups](DockManager/FloatGroups.md) { get; } | Возвращает коллекцию плавающих групп. |
| [ItemAdapter](DockManager/ItemAdapter.md) { get; set; } | Возвращает или задаёт адаптер, используемый для настройки созданного элемента докинга для его исходного элемента. |
| [ItemContentTemplate](DockManager/ItemContentTemplate.md) { get; set; } | Возвращает или задаёт шаблон, используемый для отображения содержимого созданных Dock-панелей. |
| [ItemsSource](DockManager/ItemsSource.md) { get; set; } | Возвращает или задаёт коллекцию, элементы которой используются для создания элементов докинга. |
| [ItemTemplate](DockManager/ItemTemplate.md) { get; set; } | Возвращает или задаёт шаблон, используемый для создания элементов докинга из источника данных. |
| [OwnsFloatingDockPanes](DockManager/OwnsFloatingDockPanes.md) { get; set; } | Возвращает или задаёт, принадлежат ли плавающие окна с панелями инструментов окну менеджера докинга. |
| [OwnsFloatingDocuments](DockManager/OwnsFloatingDocuments.md) { get; set; } | Возвращает или задаёт, принадлежат ли плавающие окна с документами окну менеджера докинга. |
| [Root](DockManager/Root.md) { get; set; } | Возвращает или задаёт корневую группу закреплённого размещения. |
| [SerializationInfo](DockManager/SerializationInfo.md) { get; } | Возвращает сведения о размещении, используемые при сериализации или десериализации. |

## Методы

| имя | описание |
| --- | --- |
| static [GetDockManager](DockManager/GetDockManager.md)(…) |  |
| [AutoHide](DockManager/AutoHide.md)(…) | Перемещает панели указанного элемента в группу автоскрытия и возвращает, успешно ли выполнена операция. |
| [Close](DockManager/Close.md)(…) | Закрывает панели указанного элемента и возвращает, успешно ли выполнена операция. |
| [CollapseAutoHidePanel](DockManager/CollapseAutoHidePanel.md)(…) | Сворачивает автоскрываемую панель для указанной панели и возвращает, успешно ли выполнена операция. |
| [Dock](DockManager/Dock.md)(…) | Закрепляет указанный элемент с использованием его истории докинга и возвращает, успешно ли выполнена операция. (перегрузок: 2) |
| [ExpandAutoHidePanel](DockManager/ExpandAutoHidePanel.md)(…) | Разворачивает автоскрываемую панель для указанной панели и возвращает, успешно ли выполнена операция. |
| [Float](DockManager/Float.md)(…) | Перемещает указанный элемент в плавающее окно и возвращает, успешно ли выполнена операция. |
| [Remove](DockManager/Remove.md)(…) | Удаляет указанный элемент и его историю докинга из размещения и возвращает, успешно ли выполнена операция. |
| [Restore](DockManager/Restore.md)(…) | Восстанавливает закрытую панель в её прежнюю позицию в размещении и возвращает, успешно ли выполнена операция. |
| [RestoreLayout](DockManager/RestoreLayout.md)(…) | Восстанавливает размещение докинга из указанного потока с параметрами сериализации по умолчанию. (перегрузок: 2) |
| [SaveLayout](DockManager/SaveLayout.md)(…) | Сохраняет размещение докинга в указанный поток с параметрами сериализации по умолчанию. (перегрузок: 2) |
| static [GetDockItem](DockManager/GetDockItem.md)(…) | Возвращает элемент докинга, связанный с указанным объектом. |
| static [SetDockItem](DockManager/SetDockItem.md)(…) | Задаёт элемент докинга, связанный с указанным объектом. |
| static [SetDockManager](DockManager/SetDockManager.md)(…) | Задаёт менеджер докинга, связанный с указанным объектом. |

## События

| имя | описание |
| --- | --- |
| event [CustomizeDockGuide](DockManager/CustomizeDockGuide.md) | Происходит при подготовке направляющих докинга для перетаскиваемого элемента. Используйте событие, чтобы скрыть направляющие или их элементы. |
| event [DockItemActivated](DockManager/DockItemActivated.md) | Происходит при смене активного элемента докинга. |
| event [DockItemContextMenuOpening](DockManager/DockItemContextMenuOpening.md) | Происходит перед открытием контекстного меню элемента докинга. Отмените событие, чтобы меню не открывалось. |
| event [DockItemEndFloatDragging](DockManager/DockItemEndFloatDragging.md) | Происходит по окончании перетаскивания плавающего элемента докинга. |
| event [DockItemStartFloatDragging](DockManager/DockItemStartFloatDragging.md) | Происходит при начале перетаскивания плавающего элемента докинга. |
| event [DockOperationCompleted](DockManager/DockOperationCompleted.md) | Происходит после завершения операции докинга. |
| event [DockOperationStarting](DockManager/DockOperationStarting.md) | Происходит перед началом операции докинга. Отмените событие, чтобы предотвратить операцию. |
| event [RegisterDockItem](DockManager/RegisterDockItem.md) | Происходит при регистрации элемента докинга в менеджере докинга. |

## См. также

* пространство имён [Eremex.AvaloniaUI.Controls.Docking](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
