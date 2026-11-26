# Класс TreeListControl

Отображает коллекцию элементов, упорядоченных в иерархию узлов.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.TreeList`](./index.md)  
**Сборка:** `Eremex.Avalonia.Controls.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Объявление

```csharp
public class TreeListControl : TreeListControlBase
```

## Конструкторы

| имя | описание |
| --- | --- |
| [TreeListControl](TreeListControl/TreeListControl.md)() | Конструктор по умолчанию. |

## Свойства

| имя | описание |
| --- | --- |
| [AllowBandResizing](TreeListControl/AllowBandResizing.md) { get; set; } | Возвращает или задаёт, могут ли пользователи изменять размер групп. |
| [AllowBestFit](TreeListControl/AllowBestFit.md) { get; set; } | Возвращает или задаёт, могут ли пользователи применять подгонку ширины колонок по содержимому. |
| [AllowColumnFiltering](TreeListControl/AllowColumnFiltering.md) { get; set; } | Возвращает или задаёт, могут ли пользователи фильтровать данные по колонке. |
| [AllowColumnMoving](TreeListControl/AllowColumnMoving.md) { get; set; } | Возвращает или задаёт, могут ли пользователи менять порядок колонок, перетаскивая их заголовки. |
| [AllowColumnResizing](TreeListControl/AllowColumnResizing.md) { get; set; } | Возвращает или задаёт, могут ли пользователи изменять размер колонок. |
| [AllowEditingTotalSummaries](TreeListControl/AllowEditingTotalSummaries.md) { get; set; } | Возвращает или задаёт, могут ли пользователи редактировать общие итоги. |
| [AllowHorizontalVirtualization](TreeListControl/AllowHorizontalVirtualization.md) { get; set; } | Возвращает или задаёт, виртуализируются ли колонки за пределами экрана. |
| [AllowResetColumnWidth](TreeListControl/AllowResetColumnWidth.md) { get; set; } | Возвращает или задаёт, могут ли пользователи сбрасывать ширину колонок до значений по умолчанию. |
| [AllowSorting](TreeListControl/AllowSorting.md) { get; set; } | Возвращает или задаёт, могут ли пользователи сортировать данные. |
| [AutoGenerateBands](TreeListControl/AutoGenerateBands.md) { get; set; } | Возвращает или задаёт, создаются ли группы автоматически. |
| [AutoGenerateColumns](TreeListControl/AutoGenerateColumns.md) { get; set; } | Возвращает или задаёт, создаются ли колонки автоматически на основе источника данных. |
| [AutoGenerateServiceColumns](TreeListControl/AutoGenerateServiceColumns.md) { get; set; } | Возвращает или задаёт, создаются ли служебные колонки автоматически. |
| [AutoMoveRowFocus](TreeListControl/AutoMoveRowFocus.md) { get; set; } | Возвращает или задаёт, перемещает ли навигация с клавиатуры фокус на следующую или предыдущую строку при переходе за последнюю или первую колонку. |
| [Bands](TreeListControl/Bands.md) { get; } | Возвращает коллекцию групп контрола. |
| [BandsSource](TreeListControl/BandsSource.md) { get; set; } | Возвращает или задаёт коллекцию, элементы которой используются для создания групп. |
| [BandTemplate](TreeListControl/BandTemplate.md) { get; set; } | Возвращает или задаёт шаблон, используемый для создания группы для каждого элемента BandsSource. |
| [BestFitMode](TreeListControl/BestFitMode.md) { get; set; } | Возвращает или задаёт способ вычисления оптимальной ширины колонки. |
| [CellTemplate](TreeListControl/CellTemplate.md) { get; set; } | Возвращает или задаёт шаблон по умолчанию, используемый для отображения содержимого ячеек, если колонка не задаёт собственный шаблон. |
| [ClipboardCopyHeaders](TreeListControl/ClipboardCopyHeaders.md) { get; set; } | Возвращает или задаёт, копируются ли заголовки колонок в буфер обмена вместе со значениями ячеек. |
| [ColumnFilterButtonDisplayMode](TreeListControl/ColumnFilterButtonDisplayMode.md) { get; set; } | Возвращает или задаёт, когда отображаются кнопки фильтра колонок. |
| [ColumnFilterPopupMode](TreeListControl/ColumnFilterPopupMode.md) { get; set; } | Возвращает или задаёт тип всплывающего окна фильтра колонки. |
| [ColumnMenu](TreeListControl/ColumnMenu.md) { get; set; } | Возвращает или задаёт контекстное меню, вызываемое для заголовков колонок. |
| [Columns](TreeListControl/Columns.md) { get; } | Возвращает коллекцию колонок контрола. |
| [ColumnsSource](TreeListControl/ColumnsSource.md) { get; set; } | Возвращает или задаёт коллекцию, элементы которой используются для создания колонок. |
| [ColumnTemplate](TreeListControl/ColumnTemplate.md) { get; set; } | Возвращает или задаёт шаблон, используемый для создания колонки для каждого элемента ColumnsSource. |
| [ExtendScrollbarToFixedColumns](TreeListControl/ExtendScrollbarToFixedColumns.md) { get; set; } | Возвращает или задаёт, распространяется ли горизонтальная полоса прокрутки под закреплённые колонки. |
| [FilterPanelDisplayMode](TreeListControl/FilterPanelDisplayMode.md) { get; set; } | Возвращает или задаёт, когда отображается панель фильтра. |
| [FilterPanelText](TreeListControl/FilterPanelText.md) { get; } | Возвращает текст, отображаемый на панели фильтра. |
| [FixedColumnSeparatorWidth](TreeListControl/FixedColumnSeparatorWidth.md) { get; set; } | Возвращает или задаёт ширину разделителя, обозначающего закреплённые колонки. |
| [FixedLeftColumnWidth](TreeListControl/FixedLeftColumnWidth.md) { get; } | Возвращает общую ширину колонок, закреплённых у левого края. |
| [FixedRightColumnWidth](TreeListControl/FixedRightColumnWidth.md) { get; } | Возвращает общую ширину колонок, закреплённых у правого края. |
| [FocusedColumn](TreeListControl/FocusedColumn.md) { get; set; } | Возвращает или задаёт колонку с фокусом. |
| [HeaderDropIndicatorWidth](TreeListControl/HeaderDropIndicatorWidth.md) { get; set; } | Возвращает или задаёт ширину индикатора, отображаемого между заголовками во время перетаскивания колонки. |
| [HeaderPanelMinHeight](TreeListControl/HeaderPanelMinHeight.md) { get; set; } | Возвращает или задаёт минимальную высоту панели заголовков колонок. |
| [IsFilterPanelVisible](TreeListControl/IsFilterPanelVisible.md) { get; } | Возвращает, отображается ли в данный момент панель фильтра. |
| [NavigationMode](TreeListControl/NavigationMode.md) { get; set; } | Возвращает или задаёт, перемещает ли навигация с клавиатуры фокус между ячейками или между строками. |
| [RowDragMode](TreeListControl/RowDragMode.md) { get; set; } | Возвращает или задаёт, перетаскиваются ли строки за саму строку или за маркер перетаскивания. |
| [RowIndicatorWidth](TreeListControl/RowIndicatorWidth.md) { get; set; } | Возвращает или задаёт ширину индикатора строки. |
| [SerializationInfo](TreeListControl/SerializationInfo.md) { get; } | Возвращает сведения о сериализации, хранящие сохранённое размещение контрола. |
| [ShowAutoFilterRow](TreeListControl/ShowAutoFilterRow.md) { get; set; } | Возвращает или задаёт, отображается ли строка автофильтра. |
| [ShowBands](TreeListControl/ShowBands.md) { get; set; } | Возвращает или задаёт, отображаются ли заголовки групп. |
| [ShowBandSeparators](TreeListControl/ShowBandSeparators.md) { get; set; } | Возвращает или задаёт, отображаются ли разделители между заголовками групп. |
| [ShowCheckAllNodesCheckBox](TreeListControl/ShowCheckAllNodesCheckBox.md) { get; set; } | Возвращает или задаёт, отображается ли флажок, отмечающий все узлы. |
| [ShowColumnHeaders](TreeListControl/ShowColumnHeaders.md) { get; set; } | Возвращает или задаёт, отображается ли панель заголовков колонок. |
| [ShowColumnMenuFixedItem](TreeListControl/ShowColumnMenuFixedItem.md) { get; set; } | Возвращает или задаёт, отображается ли пункт закрепления колонки в контекстном меню заголовка колонки. |
| [ShowConditionInAutoFilterRow](TreeListControl/ShowConditionInAutoFilterRow.md) { get; set; } | Возвращает или задаёт, отображает ли строка автофильтра применённое условие фильтра. |
| [ShowHorizontalLines](TreeListControl/ShowHorizontalLines.md) { get; set; } | Возвращает или задаёт, отображаются ли горизонтальные линии сетки. |
| [ShowRowIndicator](TreeListControl/ShowRowIndicator.md) { get; } | Возвращает, отображается ли индикатор строки. |
| [ShowTotalSummaries](TreeListControl/ShowTotalSummaries.md) { get; set; } | Возвращает или задаёт, отображается ли нижняя панель общих итогов. |
| [ShowVerticalLines](TreeListControl/ShowVerticalLines.md) { get; set; } | Возвращает или задаёт, отображаются ли вертикальные линии сетки. |
| [TotalSummaries](TreeListControl/TotalSummaries.md) { get; } | Возвращает коллекцию элементов общих итогов, вычисляемых по всем строкам. |
| [TotalSummaryPanelMinHeight](TreeListControl/TotalSummaryPanelMinHeight.md) { get; set; } | Возвращает или задаёт минимальную высоту нижней панели общих итогов. |
| [TreeColumnFieldName](TreeListControl/TreeColumnFieldName.md) { get; set; } | Возвращает или задаёт имя поля колонки, отображающей иерархию дерева. |

## Методы

| имя | описание |
| --- | --- |
| [BestFit](TreeListControl/BestFit.md)(…) | Подгоняет ширину указанной колонки по содержимому. |
| [BestFitAllColumns](TreeListControl/BestFitAllColumns.md)() | Подгоняет ширину всех видимых колонок по содержимому. |
| [ExportToImages](TreeListControl/ExportToImages.md)(…) | Экспортирует видимые данные контрола в файлы изображений в указанной папке. |
| [ExportToPdf](TreeListControl/ExportToPdf.md)(…) | Экспортирует видимые данные контрола в указанный файл в формате PDF. (перегрузок: 2) |
| [ExportToXlsx](TreeListControl/ExportToXlsx.md)(…) | Экспортирует видимые данные контрола в указанный файл в формате XLSX. (перегрузок: 2) |
| [GetCellDisplayText](TreeListControl/GetCellDisplayText.md)(…) | Возвращает отображаемый текст указанной ячейки. (перегрузок: 2) |
| [GetCellValue](TreeListControl/GetCellValue.md)(…) | Возвращает значение указанной ячейки. (перегрузок: 2) |
| [GetTotalSummaryValue](TreeListControl/GetTotalSummaryValue.md)(…) | Возвращает значение общего итога, вычисленное для указанного элемента итога. |
| [MoveNextCell](TreeListControl/MoveNextCell.md)() | Перемещает фокус на следующую ячейку. |
| [MovePrevCell](TreeListControl/MovePrevCell.md)() | Перемещает фокус на предыдущую ячейку. |
| [PopulateColumns](TreeListControl/PopulateColumns.md)() | Создаёт колонки на основе полей источника данных. |
| [ResetColumnWidth](TreeListControl/ResetColumnWidth.md)() | Сбрасывает ширину всех колонок до значений по умолчанию. |
| [RestoreLayout](TreeListControl/RestoreLayout.md)(…) | Восстанавливает размещение контрола из указанного потока. (перегрузок: 2) |
| [SaveLayout](TreeListControl/SaveLayout.md)(…) | Сохраняет размещение контрола в указанный поток. (перегрузок: 2) |
| [SetCellValue](TreeListControl/SetCellValue.md)(…) | Задаёт значение указанной ячейки. (перегрузок: 2) |

## События

| имя | описание |
| --- | --- |
| event [AutoGeneratedColumns](TreeListControl/AutoGeneratedColumns.md) | Происходит после автоматического создания колонок. |
| event [AutoGeneratingColumn](TreeListControl/AutoGeneratingColumn.md) | Происходит при автоматическом создании колонки. |
| event [CellValueChanged](TreeListControl/CellValueChanged.md) | Происходит после изменения значения ячейки. |
| event [CellValueChanging](TreeListControl/CellValueChanging.md) | Происходит во время изменения значения ячейки до его передачи в источник данных. |
| event [CustomColumnDisplayText](TreeListControl/CustomColumnDisplayText.md) | Происходит, когда требуется отображаемый текст ячейки. |
| event [CustomColumnSort](TreeListControl/CustomColumnSort.md) | Происходит при сравнении значений колонки с использованием пользовательской логики во время сортировки данных. |
| event [CustomSummary](TreeListControl/CustomSummary.md) | Происходит при вычислении элемента итога с типом итога Custom. |
| event [CustomUnboundColumnData](TreeListControl/CustomUnboundColumnData.md) | Происходит при запросе или передаче значения ячейки несвязанной колонки. |
| event [HiddenEditor](TreeListControl/HiddenEditor.md) | Происходит после закрытия встроенного редактора. |
| event [ShowingEditor](TreeListControl/ShowingEditor.md) | Происходит перед активацией встроенного редактора. |
| event [ShownEditor](TreeListControl/ShownEditor.md) | Происходит после активации встроенного редактора. |
| event [ValidateCellValue](TreeListControl/ValidateCellValue.md) | Происходит при проверке значения ячейки. |

## См. также

* класс [TreeListControlBase](./TreeListControlBase.md)
* пространство имён [Eremex.AvaloniaUI.Controls.TreeList](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
