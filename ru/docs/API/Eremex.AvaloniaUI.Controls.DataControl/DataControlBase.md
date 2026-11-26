# Класс DataControlBase

Предоставляет базовый класс для контролов данных, отображающих коллекцию элементов в виде строк.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.DataControl`](./index.md)  
**Сборка:** `Eremex.Avalonia.Controls.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Объявление

```csharp
public abstract class DataControlBase : TemplatedControl, IBandsOwner, ISortedInfoCollectionOwner
```

## Свойства

| имя | описание |
| --- | --- |
| [ActiveEditor](DataControlBase/ActiveEditor.md) { get; } | Возвращает активный в данный момент встроенный редактор. |
| [AllowEditing](DataControlBase/AllowEditing.md) { get; set; } | Возвращает или задаёт, могут ли пользователи редактировать значения ячеек. |
| [AllowImmediateEditorValuePosting](DataControlBase/AllowImmediateEditorValuePosting.md) { get; set; } | Возвращает или задаёт, передаются ли значения редактора немедленно при их изменении. |
| [AutoScrollToFocusedRow](DataControlBase/AutoScrollToFocusedRow.md) { get; set; } | Возвращает или задаёт, прокручивается ли представление автоматически, чтобы строка с фокусом оставалась видимой. |
| [EditorButtonShowMode](DataControlBase/EditorButtonShowMode.md) { get; set; } | Возвращает или задаёт, когда отображаются кнопки редактора. |
| [EditorShowMode](DataControlBase/EditorShowMode.md) { get; set; } | Возвращает или задаёт, когда активируются встроенные редакторы. |
| [FilterString](DataControlBase/FilterString.md) { get; set; } | Возвращает или задаёт строку критериев фильтра, применяемую к данным. |
| [FocusedItem](DataControlBase/FocusedItem.md) { get; set; } | Возвращает или задаёт элемент данных, имеющий фокус. |
| virtual [HeaderDropIndex](DataControlBase/HeaderDropIndex.md) { get; set; } | Возвращает или задаёт индекс, по которому бросается перетаскиваемый заголовок колонки. |
| [IgnoreValidationAttributesOnCommit](DataControlBase/IgnoreValidationAttributesOnCommit.md) { get; set; } | Возвращает или задаёт, игнорируются ли атрибуты валидации при фиксации значений ячеек. |
| [IsColumnChooserVisible](DataControlBase/IsColumnChooserVisible.md) { get; set; } | Возвращает или задаёт, отображается ли окно выбора колонок. |
| [IsFilterEnabled](DataControlBase/IsFilterEnabled.md) { get; set; } | Возвращает или задаёт, включена ли фильтрация. |
| [IsSearchPanelVisible](DataControlBase/IsSearchPanelVisible.md) { get; set; } | Возвращает или задаёт, видна ли панель поиска. |
| [ItemsSource](DataControlBase/ItemsSource.md) { get; set; } | Возвращает или задаёт источник данных, элементы которого контрол отображает в виде строк. |
| [KeepSelectedOnClick](DataControlBase/KeepSelectedOnClick.md) { get; set; } | Возвращает или задаёт, остаётся ли выделенная строка выделенной при повторном щелчке. |
| [RowLevelIndent](DataControlBase/RowLevelIndent.md) { get; set; } | Возвращает или задаёт отступ, применяемый для каждого уровня вложенности строк. |
| [RowMinHeight](DataControlBase/RowMinHeight.md) { get; set; } | Возвращает или задаёт минимальную высоту строк. |
| [SearchPanelDisplayMode](DataControlBase/SearchPanelDisplayMode.md) { get; set; } | Возвращает или задаёт, когда отображается панель поиска. |
| [SearchPanelHighlightResults](DataControlBase/SearchPanelHighlightResults.md) { get; set; } | Возвращает или задаёт, выделяются ли результаты поиска. |
| [SearchText](DataControlBase/SearchText.md) { get; set; } | Возвращает или задаёт текст поиска, введённый в панели поиска. |
| [SelectedItems](DataControlBase/SelectedItems.md) { get; set; } | Возвращает или задаёт коллекцию выделенных элементов данных. |
| [SelectionMode](DataControlBase/SelectionMode.md) { get; set; } | Возвращает или задаёт, могут ли пользователи выделять одну строку или несколько строк. |
| [ShowItemsSourceErrors](DataControlBase/ShowItemsSourceErrors.md) { get; set; } | Возвращает или задаёт, отображаются ли ошибки валидации исходных элементов. |
| [ShowSearchPanelCloseButton](DataControlBase/ShowSearchPanelCloseButton.md) { get; set; } | Возвращает или задаёт, отображает ли панель поиска кнопку закрытия. |
| [TextSortMode](DataControlBase/TextSortMode.md) { get; set; } | Возвращает или задаёт способ сравнения текстовых значений при сортировке. |
| [ValidateCellValuesOnShowAndUpdate](DataControlBase/ValidateCellValuesOnShowAndUpdate.md) { get; set; } | Возвращает или задаёт, проверяются ли значения ячеек при отображении и обновлении. |

## Методы

| имя | описание |
| --- | --- |
| virtual [BeginDataUpdate](DataControlBase/BeginDataUpdate.md)() | Запрещает контролу обновлять данные до вызова EndDataUpdate или CancelDataUpdate. |
| [BeginSelection](DataControlBase/BeginSelection.md)() | Запрещает обновление выделения до вызова EndSelection. |
| [CancelDataUpdate](DataControlBase/CancelDataUpdate.md)() | Возобновляет обновление данных после BeginDataUpdate без обновления данных контрола. |
| [ClearAllColumnsFilter](DataControlBase/ClearAllColumnsFilter.md)() | Сбрасывает условия фильтра, применённые всеми колонками. |
| [ClearSelection](DataControlBase/ClearSelection.md)() | Снимает текущее выделение. |
| [ClearSorting](DataControlBase/ClearSorting.md)() | Сбрасывает сортировку, применённую ко всем колонкам. |
| [CloseEditor](DataControlBase/CloseEditor.md)() | Закрывает активный встроенный редактор. |
| virtual [CommitEditing](DataControlBase/CommitEditing.md)() | Завершает текущий сеанс редактирования, закрывая активный встроенный редактор. |
| [CopyToClipboardAsync](DataControlBase/CopyToClipboardAsync.md)() | Копирует заголовки колонок и выделенные строки в буфер обмена. |
| virtual [EndDataUpdate](DataControlBase/EndDataUpdate.md)() | Возобновляет обновление данных после BeginDataUpdate и обновляет данные контрола. |
| [EndSelection](DataControlBase/EndSelection.md)() | Применяет изменения выделения, внесённые после BeginSelection. |
| [ExportToCsv](DataControlBase/ExportToCsv.md)(…) | Экспортирует видимые данные контрола в указанный файл в формате CSV. (перегрузок: 2) |
| [HideColumnChooser](DataControlBase/HideColumnChooser.md)() | Скрывает окно выбора колонок. |
| [HideEditor](DataControlBase/HideEditor.md)() | Скрывает активный встроенный редактор. |
| [MoveNextPage](DataControlBase/MoveNextPage.md)() | Перемещает фокус на первую строку следующей страницы. |
| [MovePrevPage](DataControlBase/MovePrevPage.md)() | Перемещает фокус на последнюю строку предыдущей страницы. |
| [PostEditor](DataControlBase/PostEditor.md)() | Передаёт отредактированное значение в источник данных. |
| [ResizeBand](DataControlBase/ResizeBand.md)(…) | Задаёт одинаковую ширину для всех колонок, отображаемых в указанной группе. |
| [ResizeColumn](DataControlBase/ResizeColumn.md)(…) | Задаёт ширину указанной колонки. |
| [SelectAll](DataControlBase/SelectAll.md)() | Выделяет все строки. |
| [ShowColumnChooser](DataControlBase/ShowColumnChooser.md)() | Отображает окно выбора колонок. |
| [ShowEditor](DataControlBase/ShowEditor.md)() | Активирует встроенный редактор для ячейки с фокусом и выделяет её содержимое. |
| static [GetIsFocusWithin](DataControlBase/GetIsFocusWithin.md)(…) | Возвращает, находится ли фокус клавиатуры внутри указанного элемента. |

## События

| имя | описание |
| --- | --- |
| event [EndSorting](DataControlBase/EndSorting.md) | Происходит после завершения сортировки данных. |
| event [FilterChanged](DataControlBase/FilterChanged.md) | Происходит при изменении фильтра данных. |
| event [InvalidCellValueException](DataControlBase/InvalidCellValueException.md) | Происходит при возникновении исключения во время передачи недопустимого значения ячейки. |
| event [StartSorting](DataControlBase/StartSorting.md) | Происходит перед началом сортировки данных. |

## Поля

| имя | описание |
| --- | --- |
| const [AutoFilterRowIndex](DataControlBase/AutoFilterRowIndex.md) | Представляет видимый индекс, идентифицирующий строку автофильтра. |

## См. также

* пространство имён [Eremex.AvaloniaUI.Controls.DataControl](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
