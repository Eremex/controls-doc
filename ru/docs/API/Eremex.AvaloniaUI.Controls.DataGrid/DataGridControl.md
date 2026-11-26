# Класс DataGridControl

Отображает данные из источника данных в виде строк и колонок с поддержкой сортировки, группировки, фильтрации и редактирования.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.DataGrid`](./index.md)  
**Сборка:** `Eremex.Avalonia.Controls.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Объявление

```csharp
public class DataGridControl : DataControlBase, IDataControl
```

## Конструкторы

| имя | описание |
| --- | --- |
| [DataGridControl](DataGridControl/DataGridControl.md)() | Инициализирует новый экземпляр класса DataGridControl. |

## Свойства

| имя | описание |
| --- | --- |
| [AllowBandResizing](DataGridControl/AllowBandResizing.md) { get; set; } | Возвращает или задаёт, могут ли пользователи изменять размер групп. |
| [AllowBestFit](DataGridControl/AllowBestFit.md) { get; set; } | Возвращает или задаёт, могут ли пользователи применять подгонку ширины колонок по содержимому. |
| [AllowColumnFiltering](DataGridControl/AllowColumnFiltering.md) { get; set; } | Возвращает или задаёт, могут ли пользователи фильтровать данные по колонке. |
| [AllowColumnMoving](DataGridControl/AllowColumnMoving.md) { get; set; } | Возвращает или задаёт, могут ли пользователи менять порядок колонок, перетаскивая их заголовки. |
| [AllowColumnResizing](DataGridControl/AllowColumnResizing.md) { get; set; } | Возвращает или задаёт, могут ли пользователи изменять размер колонок. |
| [AllowDragDrop](DataGridControl/AllowDragDrop.md) { get; set; } | Возвращает или задаёт, включено ли перетаскивание строк. |
| [AllowDragDropSortedRows](DataGridControl/AllowDragDropSortedRows.md) { get; set; } | Возвращает или задаёт, можно ли перетаскивать строки, когда данные отсортированы. |
| [AllowEditingGroupSummaries](DataGridControl/AllowEditingGroupSummaries.md) { get; set; } | Возвращает или задаёт, могут ли пользователи редактировать групповые итоги. |
| [AllowEditingTotalSummaries](DataGridControl/AllowEditingTotalSummaries.md) { get; set; } | Возвращает или задаёт, могут ли пользователи редактировать общие итоги. |
| [AllowGrouping](DataGridControl/AllowGrouping.md) { get; set; } | Возвращает или задаёт, могут ли пользователи группировать данные. |
| [AllowHorizontalVirtualization](DataGridControl/AllowHorizontalVirtualization.md) { get; set; } | Возвращает или задаёт, виртуализируются ли колонки за пределами экрана. |
| [AllowResetColumnWidth](DataGridControl/AllowResetColumnWidth.md) { get; set; } | Возвращает или задаёт, могут ли пользователи сбрасывать ширину колонок до значений по умолчанию. |
| [AllowScrollingOnDrag](DataGridControl/AllowScrollingOnDrag.md) { get; set; } | Возвращает или задаёт, прокручивается ли представление автоматически, когда перетаскиваемый элемент приближается к его краю. |
| [AllowSorting](DataGridControl/AllowSorting.md) { get; set; } | Возвращает или задаёт, могут ли пользователи сортировать данные. |
| [AutoExpandAllGroups](DataGridControl/AutoExpandAllGroups.md) { get; set; } | Возвращает или задаёт, разворачиваются ли все группы автоматически. |
| [AutoExpandDelayOnDrag](DataGridControl/AutoExpandDelayOnDrag.md) { get; set; } | Возвращает или задаёт задержку перед автоматическим разворачиванием группы при перетаскивании над ней. |
| [AutoExpandOnDrag](DataGridControl/AutoExpandOnDrag.md) { get; set; } | Возвращает или задаёт, разворачивается ли свёрнутая группа автоматически, когда над ней находится перетаскиваемый элемент. |
| [AutoGenerateBands](DataGridControl/AutoGenerateBands.md) { get; set; } | Возвращает или задаёт, создаются ли группы автоматически. |
| [AutoGenerateColumns](DataGridControl/AutoGenerateColumns.md) { get; set; } | Возвращает или задаёт, создаются ли колонки автоматически на основе источника данных. |
| [Bands](DataGridControl/Bands.md) { get; } | Возвращает коллекцию групп сетки. |
| [BandsSource](DataGridControl/BandsSource.md) { get; set; } | Возвращает или задаёт коллекцию, элементы которой используются для создания групп. |
| [BandTemplate](DataGridControl/BandTemplate.md) { get; set; } | Возвращает или задаёт шаблон, используемый для создания группы для каждого элемента BandsSource. |
| [BestFitMode](DataGridControl/BestFitMode.md) { get; set; } | Возвращает или задаёт способ вычисления оптимальной ширины колонки. |
| [CellTemplate](DataGridControl/CellTemplate.md) { get; set; } | Возвращает или задаёт шаблон по умолчанию, используемый для отображения содержимого ячеек, если колонка не задаёт собственный шаблон. |
| [ClipboardCopyHeaders](DataGridControl/ClipboardCopyHeaders.md) { get; set; } | Возвращает или задаёт, копируются ли заголовки колонок в буфер обмена вместе со значениями ячеек. |
| [ColumnFilterButtonDisplayMode](DataGridControl/ColumnFilterButtonDisplayMode.md) { get; set; } | Возвращает или задаёт, когда отображаются кнопки фильтра колонок. |
| [ColumnFilterPopupMode](DataGridControl/ColumnFilterPopupMode.md) { get; set; } | Возвращает или задаёт тип всплывающего окна фильтра колонки. |
| [ColumnMenu](DataGridControl/ColumnMenu.md) { get; set; } | Возвращает или задаёт контекстное меню, вызываемое для заголовков колонок. |
| [Columns](DataGridControl/Columns.md) { get; } | Возвращает коллекцию колонок сетки. |
| [ColumnsSource](DataGridControl/ColumnsSource.md) { get; set; } | Возвращает или задаёт коллекцию, элементы которой используются для создания колонок. |
| [ColumnTemplate](DataGridControl/ColumnTemplate.md) { get; set; } | Возвращает или задаёт шаблон, используемый для создания колонки для каждого элемента ColumnsSource. |
| [Commands](DataGridControl/Commands.md) { get; } | Возвращает команды сетки. |
| [ExtendScrollbarToFixedColumns](DataGridControl/ExtendScrollbarToFixedColumns.md) { get; set; } | Возвращает или задаёт, распространяется ли горизонтальная полоса прокрутки под закреплённые колонки. |
| [FilterPanelDisplayMode](DataGridControl/FilterPanelDisplayMode.md) { get; set; } | Возвращает или задаёт, когда отображается панель фильтра. |
| [FilterPanelText](DataGridControl/FilterPanelText.md) { get; } | Возвращает текст, отображаемый на панели фильтра. |
| [FixedColumnSeparatorWidth](DataGridControl/FixedColumnSeparatorWidth.md) { get; set; } | Возвращает или задаёт ширину разделителя, обозначающего закреплённые колонки. |
| [FixedLeftColumnWidth](DataGridControl/FixedLeftColumnWidth.md) { get; } | Возвращает общую ширину колонок, закреплённых у левого края. |
| [FixedRightColumnWidth](DataGridControl/FixedRightColumnWidth.md) { get; } | Возвращает общую ширину колонок, закреплённых у правого края. |
| [FocusedColumn](DataGridControl/FocusedColumn.md) { get; set; } | Возвращает или задаёт колонку с фокусом. |
| [FocusedRowIndex](DataGridControl/FocusedRowIndex.md) { get; set; } | Возвращает или задаёт индекс строки с фокусом. |
| [GroupCount](DataGridControl/GroupCount.md) { get; set; } | Возвращает или задаёт количество первых сортируемых колонок, используемых для группировки данных. |
| [GroupSummaries](DataGridControl/GroupSummaries.md) { get; set; } | Возвращает коллекцию элементов групповых итогов, вычисляемых по строкам групп. |
| [GroupSummaryRowMinHeight](DataGridControl/GroupSummaryRowMinHeight.md) { get; set; } | Возвращает или задаёт минимальную высоту строк нижнего колонтитула групп, отображающих групповые итоги. |
| [HeaderDropIndicatorWidth](DataGridControl/HeaderDropIndicatorWidth.md) { get; set; } | Возвращает или задаёт ширину индикатора, отображаемого между заголовками во время перетаскивания колонки. |
| [HeaderPanelMinHeight](DataGridControl/HeaderPanelMinHeight.md) { get; set; } | Возвращает или задаёт минимальную высоту панели заголовков колонок. |
| [IsFilterPanelVisible](DataGridControl/IsFilterPanelVisible.md) { get; } | Возвращает, отображается ли в данный момент панель фильтра. |
| [NavigationMode](DataGridControl/NavigationMode.md) { get; set; } | Возвращает или задаёт, перемещает ли навигация с клавиатуры фокус между ячейками или между строками. |
| [RowCellMenu](DataGridControl/RowCellMenu.md) { get; set; } | Возвращает или задаёт контекстное меню, вызываемое для ячеек данных. |
| [RowDragMode](DataGridControl/RowDragMode.md) { get; set; } | Возвращает или задаёт, перетаскиваются ли строки за саму строку или за маркер перетаскивания. |
| [RowIndicatorWidth](DataGridControl/RowIndicatorWidth.md) { get; set; } | Возвращает или задаёт ширину индикатора строки. |
| [SerializationInfo](DataGridControl/SerializationInfo.md) { get; } | Возвращает сведения о сериализации сетки. |
| [ShowAutoFilterRow](DataGridControl/ShowAutoFilterRow.md) { get; set; } | Возвращает или задаёт, отображается ли строка автофильтра. |
| [ShowBands](DataGridControl/ShowBands.md) { get; set; } | Возвращает или задаёт, отображаются ли заголовки групп. |
| [ShowBandSeparators](DataGridControl/ShowBandSeparators.md) { get; set; } | Возвращает или задаёт, отображаются ли разделители между заголовками групп. |
| [ShowColumnHeaders](DataGridControl/ShowColumnHeaders.md) { get; set; } | Возвращает или задаёт, отображается ли панель заголовков колонок. |
| [ShowColumnMenuFixedItem](DataGridControl/ShowColumnMenuFixedItem.md) { get; set; } | Возвращает или задаёт, отображается ли пункт закрепления колонки в контекстном меню заголовка колонки. |
| [ShowConditionInAutoFilterRow](DataGridControl/ShowConditionInAutoFilterRow.md) { get; set; } | Возвращает или задаёт, отображает ли строка автофильтра применённое условие фильтра. |
| [ShowGroupedColumns](DataGridControl/ShowGroupedColumns.md) { get; set; } | Возвращает или задаёт, остаются ли сгруппированные колонки видимыми среди колонок данных. |
| [ShowGroupPanel](DataGridControl/ShowGroupPanel.md) { get; set; } | Возвращает или задаёт, отображается ли панель группировки. |
| [ShowGroupSummaries](DataGridControl/ShowGroupSummaries.md) { get; set; } | Возвращает или задаёт, отображаются ли строки нижнего колонтитула групп с групповыми итогами. |
| [ShowHorizontalLines](DataGridControl/ShowHorizontalLines.md) { get; set; } | Возвращает или задаёт, отображаются ли горизонтальные линии сетки. |
| [ShowRowIndicator](DataGridControl/ShowRowIndicator.md) { get; } | Возвращает, отображается ли индикатор строки. |
| [ShowTotalSummaries](DataGridControl/ShowTotalSummaries.md) { get; set; } | Возвращает или задаёт, отображается ли нижняя панель общих итогов. |
| [ShowVerticalLines](DataGridControl/ShowVerticalLines.md) { get; set; } | Возвращает или задаёт, отображаются ли вертикальные линии сетки. |
| [TotalSummaries](DataGridControl/TotalSummaries.md) { get; } | Возвращает коллекцию элементов общих итогов, вычисляемых по всем строкам. |
| [TotalSummaryPanelMinHeight](DataGridControl/TotalSummaryPanelMinHeight.md) { get; set; } | Возвращает или задаёт минимальную высоту нижней панели общих итогов. |
| [UsePlatformRowDragDrop](DataGridControl/UsePlatformRowDragDrop.md) { get; set; } | Возвращает или задаёт, используется ли перетаскивание платформы при перетаскивании строк. |
| [VisibleRowCount](DataGridControl/VisibleRowCount.md) { get; } | Возвращает количество видимых в данный момент строк. |

## Методы

| имя | описание |
| --- | --- |
| override [BeginDataUpdate](DataGridControl/BeginDataUpdate.md)() |  |
| [BestFit](DataGridControl/BestFit.md)(…) | Подгоняет ширину указанной колонки по её содержимому. |
| [BestFitAllColumns](DataGridControl/BestFitAllColumns.md)() | Подгоняет ширину всех колонок по их содержимому. |
| [CollapseAllGroups](DataGridControl/CollapseAllGroups.md)() | Сворачивает все строки групп. |
| [CollapseGroupRow](DataGridControl/CollapseGroupRow.md)(…) | Сворачивает строку группы с указанным индексом. |
| override [CommitEditing](DataGridControl/CommitEditing.md)() |  |
| [ExpandAllGroups](DataGridControl/ExpandAllGroups.md)() | Разворачивает все строки групп. |
| [ExpandGroupRow](DataGridControl/ExpandGroupRow.md)(…) | Разворачивает строку группы с указанным индексом. |
| [ExportToImages](DataGridControl/ExportToImages.md)(…) | Экспортирует сетку в файлы изображений, сохраняемые в указанной папке. |
| [ExportToPdf](DataGridControl/ExportToPdf.md)(…) | Экспортирует сетку в указанный файл в формате PDF. (перегрузок: 2) |
| [ExportToXlsx](DataGridControl/ExportToXlsx.md)(…) | Экспортирует сетку в указанный файл в формате XLSX. (перегрузок: 2) |
| [FindRowByDisplayText](DataGridControl/FindRowByDisplayText.md)(…) | Находит первую строку, отображаемый текст ячейки которой в указанном поле равен указанному тексту. Возвращает InvalidRowIndex, если строка не найдена. (перегрузок: 2) |
| [FindRowByItem](DataGridControl/FindRowByItem.md)(…) | Находит строку, соответствующую указанному элементу источника данных. Возвращает InvalidRowIndex, если элемент не найден. |
| [FindRowByValue](DataGridControl/FindRowByValue.md)(…) | Находит первую строку, значение ячейки которой в указанном поле равно указанному значению. Возвращает InvalidRowIndex, если строка не найдена. (перегрузок: 2) |
| [GetCellDisplayText](DataGridControl/GetCellDisplayText.md)(…) | Возвращает отображаемый текст ячейки на пересечении указанной строки и колонки, привязанной к указанному полю. (перегрузок: 2) |
| [GetCellValue](DataGridControl/GetCellValue.md)(…) | Возвращает значение ячейки на пересечении указанных строки и колонки. (перегрузок: 2) |
| [GetGroupChildRowCount](DataGridControl/GetGroupChildRowCount.md)() | Возвращает количество строк групп верхнего уровня. |
| [GetGroupChildRowCount](DataGridControl/GetGroupChildRowCount.md)(…) | Возвращает количество дочерних строк строки группы с указанным индексом. |
| [GetGroupChildRowIndex](DataGridControl/GetGroupChildRowIndex.md)(…) | Возвращает индекс дочерней строки в указанной позиции внутри строки группы с указанным индексом. (перегрузок: 2) |
| [GetGroupRowValue](DataGridControl/GetGroupRowValue.md)(…) | Возвращает значение строки группы с указанным индексом. |
| [GetGroupSummaryValue](DataGridControl/GetGroupSummaryValue.md)(…) |  |
| [GetParentRowIndex](DataGridControl/GetParentRowIndex.md)(…) | Возвращает индекс родительской строки группы для строки с указанным индексом. |
| [GetRowIndexBySourceItemIndex](DataGridControl/GetRowIndexBySourceItemIndex.md)(…) | Возвращает индекс строки, соответствующей элементу источника данных с указанным индексом. |
| [GetRowIndexByVisibleRowIndex](DataGridControl/GetRowIndexByVisibleRowIndex.md)(…) | Возвращает индекс строки с указанным видимым индексом. |
| [GetRowLevel](DataGridControl/GetRowLevel.md)(…) | Возвращает уровень вложенности строки с указанным индексом. |
| [GetSelectedRowIndexes](DataGridControl/GetSelectedRowIndexes.md)() | Возвращает индексы выделенных строк. |
| [GetSourceItem](DataGridControl/GetSourceItem.md)(…) | Возвращает элемент источника данных с указанным индексом. |
| [GetSourceItemByRowIndex](DataGridControl/GetSourceItemByRowIndex.md)(…) | Возвращает элемент источника данных, соответствующий строке с указанным индексом. |
| [GetSourceItemByVisibleRowIndex](DataGridControl/GetSourceItemByVisibleRowIndex.md)(…) | Возвращает элемент источника данных, соответствующий строке с указанным видимым индексом. |
| [GetSourceItemIndexByRowIndex](DataGridControl/GetSourceItemIndexByRowIndex.md)(…) | Возвращает индекс в источнике данных строки с указанным индексом. |
| [GetSourceItemIndexByVisibleRowIndex](DataGridControl/GetSourceItemIndexByVisibleRowIndex.md)(…) | Возвращает индекс в источнике данных строки с указанным видимым индексом. |
| [GetSourceItemValue](DataGridControl/GetSourceItemValue.md)(…) | Возвращает значение поля указанной колонки для элемента источника данных с указанным индексом. (перегрузок: 2) |
| [GetTotalSummaryValue](DataGridControl/GetTotalSummaryValue.md)(…) | Возвращает вычисленное значение указанного общего итога. |
| [GetVisibleRowIndexByRowIndex](DataGridControl/GetVisibleRowIndexByRowIndex.md)(…) | Возвращает видимый индекс строки с указанным индексом. |
| [GetVisibleRowIndexBySourceItemIndex](DataGridControl/GetVisibleRowIndexBySourceItemIndex.md)(…) | Возвращает видимый индекс строки, соответствующей элементу источника данных с указанным индексом. |
| [IsGroupFooterRow](DataGridControl/IsGroupFooterRow.md)(…) | Определяет, является ли строка с указанным индексом строкой нижнего колонтитула группы. |
| [IsGroupRow](DataGridControl/IsGroupRow.md)(…) | Определяет, является ли строка с указанным индексом строкой группы. |
| [IsGroupRowExpanded](DataGridControl/IsGroupRowExpanded.md)(…) | Определяет, развёрнута ли строка группы с указанным индексом. |
| [IsRowSelected](DataGridControl/IsRowSelected.md)(…) | Определяет, выделена ли строка с указанным индексом. |
| [MoveNextCell](DataGridControl/MoveNextCell.md)() | Перемещает фокус на следующую ячейку. |
| [MoveNextRow](DataGridControl/MoveNextRow.md)() | Перемещает фокус на следующую строку. |
| [MovePrevCell](DataGridControl/MovePrevCell.md)() | Перемещает фокус на предыдущую ячейку. |
| [MovePrevRow](DataGridControl/MovePrevRow.md)(…) | Перемещает фокус на предыдущую строку, при необходимости разрешая перемещение фокуса в строку автофильтра. |
| [PopulateColumns](DataGridControl/PopulateColumns.md)() | Создаёт колонки на основе источника данных. |
| [RefreshData](DataGridControl/RefreshData.md)() | Повторно считывает источник данных и обновляет содержимое сетки. |
| [RefreshRow](DataGridControl/RefreshRow.md)(…) | Обновляет видимые ячейки строки с указанным индексом. |
| [ResetColumnWidth](DataGridControl/ResetColumnWidth.md)() | Сбрасывает ширину всех колонок до значений по умолчанию. |
| [RestoreLayout](DataGridControl/RestoreLayout.md)(…) | Восстанавливает размещение сетки из указанного потока. (перегрузок: 2) |
| [SaveLayout](DataGridControl/SaveLayout.md)(…) | Сохраняет размещение сетки в указанный поток. (перегрузок: 2) |
| [SelectRange](DataGridControl/SelectRange.md)(…) | Выделяет все строки между указанными начальным и конечным индексами строк. |
| [SelectRow](DataGridControl/SelectRow.md)(…) | Выделяет строку с указанным индексом. |
| [SetCellValue](DataGridControl/SetCellValue.md)(…) | Задаёт значение ячейки на пересечении указанных строки и колонки. (перегрузок: 2) |
| [UnselectRow](DataGridControl/UnselectRow.md)(…) | Снимает выделение со строки с указанным индексом. |

## События

| имя | описание |
| --- | --- |
| event [AutoGeneratedColumns](DataGridControl/AutoGeneratedColumns.md) | Происходит после автоматического создания колонок из источника данных. |
| event [AutoGeneratingColumn](DataGridControl/AutoGeneratingColumn.md) | Происходит, когда колонка вот-вот будет создана автоматически. Отмените событие, чтобы колонка не создавалась. |
| event [CellValueChanged](DataGridControl/CellValueChanged.md) | Происходит после изменения значения ячейки. |
| event [CellValueChanging](DataGridControl/CellValueChanging.md) | Происходит, когда пользователь изменяет значение ячейки в редакторе, до фиксации изменения. |
| event [CompleteDragDrop](DataGridControl/CompleteDragDrop.md) | Происходит после завершения операции перетаскивания. |
| event [CustomColumnDisplayText](DataGridControl/CustomColumnDisplayText.md) | Происходит, когда требуется отображаемый текст ячейки. Задайте свойство DisplayText, чтобы изменить текст. |
| event [CustomColumnGroup](DataGridControl/CustomColumnGroup.md) | Происходит при сравнении двух строк во время группировки. Задайте свойство Result, чтобы указать, принадлежат ли строки к одной группе. |
| event [CustomColumnSort](DataGridControl/CustomColumnSort.md) | Происходит при сравнении двух строк во время сортировки. Задайте свойство Result, чтобы реализовать пользовательскую сортировку. |
| event [CustomGroupValueDisplayText](DataGridControl/CustomGroupValueDisplayText.md) | Происходит, когда требуется отображаемый текст значения строки группы. Задайте свойство DisplayText, чтобы изменить текст. |
| event [CustomRowFilter](DataGridControl/CustomRowFilter.md) | Происходит при фильтрации строки. Задайте свойство Visible, чтобы показать или скрыть строку. |
| event [CustomSummary](DataGridControl/CustomSummary.md) | Происходит при вычислении значения итога. Задайте свойство SummaryValue, чтобы реализовать пользовательский итог. |
| event [CustomUnboundColumnData](DataGridControl/CustomUnboundColumnData.md) | Происходит, когда значение ячейки несвязанной колонки запрашивается или фиксируется. Задайте свойство Value, чтобы предоставить значение. |
| event [DragOver](DataGridControl/DragOver.md) | Происходит, пока перетаскиваемая строка находится над сеткой. Задайте свойства Effects и DropPosition, чтобы настроить операцию сброса. |
| event [Drop](DataGridControl/Drop.md) | Происходит, когда перетаскиваемая строка бросается над сеткой. Обработайте событие, чтобы выполнить пользовательскую операцию сброса. |
| event [HiddenEditor](DataGridControl/HiddenEditor.md) | Происходит после закрытия редактора. |
| event [RowClick](DataGridControl/RowClick.md) | Происходит при щелчке по строке. |
| event [SelectionChanged](DataGridControl/SelectionChanged.md) | Происходит при изменении выделения строк. |
| event [ShowingEditor](DataGridControl/ShowingEditor.md) | Происходит перед активацией редактора для ячейки. Отмените событие, чтобы запретить редактирование. |
| event [ShownEditor](DataGridControl/ShownEditor.md) | Происходит после активации редактора для ячейки. |
| event [StartDrag](DataGridControl/StartDrag.md) | Происходит при начале перетаскивания строки. Задайте свойства Effects и Data, чтобы настроить операцию перетаскивания. |
| event [ValidateCellValue](DataGridControl/ValidateCellValue.md) | Происходит при проверке значения ячейки. Задайте свойство ErrorContent, чтобы указать на ошибку. |

## Поля

| имя | описание |
| --- | --- |
| const [InvalidRowIndex](DataGridControl/InvalidRowIndex.md) | Представляет недопустимый индекс строки. |

## См. также

* класс [DataControlBase](../Eremex.AvaloniaUI.Controls.DataControl/DataControlBase.md)
* пространство имён [Eremex.AvaloniaUI.Controls.DataGrid](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
