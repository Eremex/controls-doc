---
title: Версия 1.4
order: 14
seealso: []
---

# Версия 1.4

## 1.4.38

### DataGrid и TreeList

#### Исправленные проблемы

- Возникает исключение, если операция перетаскивания отменяется в обработчике события `StartDrag`.
- Объект, присвоенный `e.Data.DataTransfer` в обработчике события `StartDrag`, недоступен в обработчике события `DragOver`.
- В режиме `CheckedList` фильтр колонки не отображает подпись элемента "(Select All)".

### Диаграммы

#### Исправленные проблемы

- Если отображается перекрестие (crosshair), возникает исключение, когда серия содержит только точки со значениями `NaN`.
- PolarChart — внутренняя область не заливается, если начальная и конечная точки совпадают.
- Возникает исключение, если диаграмма отображает значения `DateTime` по оси _Y_ и параметр `AlwaysShowZeroLevel` установлен в `true`.
- PolarChart и SmithChart — параметр [`CrosshairSeriesLabelMode.None`](../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesLabelMode.md) не действует.

### Окна и окна сообщений

#### Исправленные проблемы

- `MxMessageBox` — отображается неверная иконка, если параметр [`MessageBoxIcon`](../API/Eremex.AvaloniaUI.Controls/MessageBoxIcon.md) имеет значение, отличное от `None`, `Question` или `Warning`.


## 1.4.34

### Поддержка Avalonia 12

Этот выпуск обеспечивает полную поддержку Avalonia 12 в библиотеке Eremex Controls. Avalonia 12 приносит существенные улучшения в производительности, стабильности и надёжности платформы. Это обновление гарантирует, что набор контролов Eremex плавно интегрируется с изменениями, внесёнными в новой версии фреймворка Avalonia.

Подробности о критических изменениях в Avalonia 12 смотрите здесь:
[https://docs.avaloniaui.net/docs/avalonia12-breaking-changes](https://docs.avaloniaui.net/docs/avalonia12-breaking-changes).




### DataGrid и TreeList

#### Улучшения перетаскивания строк

##### Превью строк


DataGrid и TreeList теперь показывают превью строк во время [операций перетаскивания](../controls/datagrid/row-drag-and-drop.md), давая визуальную обратную связь при переупорядочивании или перемещении данных.

![grid-dragdrop-row-previews-wn14](../images/grid-dragdrop-row-previews-wn14.png)

При перетаскивании нескольких строк превью показывает число перетаскиваемых объектов.

![grid-dragdrop-multiple-row-previews-wn14](../images/grid-dragdrop-multiple-row-previews-wn14.png)

##### Маркеры перетаскивания строк

В этой версии добавлен новый режим перетаскивания, в котором для перетаскивания строк используются специальные маркеры (Drag Handles). Маркеры перетаскивания отображаются в области индикатора строки слева от строк.

![grid-dragdrop-drag-handle](../images/grid-draganddrop-draghandle-mode.gif)

Маркеры перетаскивания упрощают активацию редактора ячейки при включённой функции перетаскивания. Ранее пользователи инициировали перетаскивание строк, щёлкая и перетаскивая любую ячейку строки. Однако такое поведение противоречит требованию (высказанному многими) активировать редактор ячейки при нажатии мышью внутри ячейки. Новый режим на основе маркеров перетаскивания решает эту проблему:

- Одиночный щелчок по ячейке по умолчанию активирует редактор ячейки.
- Для перетаскивания строк используйте специальные маркеры перетаскивания.

###### Связанный API

- [`DataGridControl.RowDragMode`](../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/RowDragMode.md)
- [`DataGridControl.RowIndicatorWidth`](../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/RowIndicatorWidth.md)
- [`TreeListControl.RowDragMode`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/RowDragMode.md)
- [`TreeListControl.RowIndicatorWidth`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/RowIndicatorWidth.md)

##### Критическое изменение — перетаскивание строк между приложениями

Начиная с версии 1.4, чтобы разрешить перетаскивание строк между приложениями, включите новое свойство `UsePlatformRowDragDrop` для контрола, в котором начинаются операции перетаскивания. Обратите внимание, что превью строк не отображаются во время перетаскивания строк на уровне платформы.

Версии до v1.4 не требуют никаких дополнительных параметров для включения перетаскивания строк между приложениями.

##### Документация

- [Data Grid — Перетаскивание строк](../controls/datagrid/row-drag-and-drop.md)
- [Tree List — Перетаскивание узлов](../controls/treelist/node-drag-and-drop.md)

#### Визуальные улучшения перетаскивания заголовков колонок

Чтобы скрыть колонку, пользователь может перетащить её заголовок на небольшое расстояние от панели заголовков и отпустить там. Чтобы дать чёткую визуальную подсказку об этом действии, над перетаскиваемым заголовком колонки теперь отображается подсказка «Hide Column».

![grid-column-drag-hidecolumn-hint](../images/grid-column-drag-hidecolumn-hint.png)

Кроме того, во время операции перетаскивания превью заголовка колонки теперь выглядит полупрозрачным с эффектом тени.

![grid-column-drag-shadow-effect](../images/grid-column-drag-shadow-effect.png)

#### Best-Fit 

Контролы DataGrid и TreeList теперь поддерживают функцию Best Fit. Эта функция позволяет пользователям автоматически изменять ширину колонок до их идеальной минимальной ширины, чтобы полностью показать содержимое ячеек.

![bestfit-feature](../images/bestfit-feature.png)

Чтобы применить Best Fit, пользователи могут дважды щёлкнуть правый край заголовка колонки или выбрать команду «Best Fit» в контекстном меню колонки. Пользователи также могут применить Best Fit сразу ко всем колонкам, чтобы всё содержимое оставалось полностью видимым.

![bestfit-feature-bestfitall](../images/bestfit-feature-bestfitall.png)

Контролы включают свойства [`BestFitMode`](../API/Eremex.AvaloniaUI.Controls.DataControl/BestFitMode.md), которые задают, какие значения строк измеряются во время операций Best Fit:

- Режим `Fast` — измеряет ширину уникальных значений строк. Это улучшает производительность Best Fit в большинстве стандартных сценариев.

- Режим `Full` — измеряет ширину всех значений строк, включая дубликаты. Этот режим медленнее, чем Fast, но правильно вычисляет ширину колонок, когда используются шаблоны ячеек или ошибки валидации.

##### Связанный API

- [`DataGridControl.AllowBestFit`](../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/AllowBestFit.md)
- [`DataGridControl.BestFitMode`](../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/BestFitMode.md)
- [`DataGridControl.BestFitMode`](../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/BestFitMode.md)
- [`DataGridControl.BestFit`](../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/BestFit.md)
- [`DataGridControl.BestFitAllColumns`](../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/BestFitAllColumns.md)
- [`GridColumn.AllowBestFit`](../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/AllowBestFit.md)
- [`GridColumn.BestFitMode`](../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/BestFitMode.md)
- [`GridColumn.BestFitMode`](../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/BestFitMode.md)
- [`TreeListControl.AllowBestFit`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AllowBestFit.md)
- [`TreeListControl.BestFitMode`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/BestFitMode.md)
- [`TreeListControl.BestFitMode`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/BestFitMode.md)
- [`TreeListControl.BestFit`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/BestFit.md)
- [`TreeListControl.BestFitAllColumns`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/BestFitAllColumns.md)
- [`TreeListColumn.AllowBestFit`](../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/AllowBestFit.md)
- [`TreeListColumn.BestFitMode`](../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/BestFitMode.md)
- [`TreeListColumn.BestFitMode`](../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/BestFitMode.md)

##### Документация

- [Data Grid — Best Fit](#best-fit)
- [Tree List — Best Fit](#best-fit)

#### Сброс пользовательских изменений ширины колонки

После того как пользователь изменит ширину колонок (перетаскиванием или с помощью Best Fit), в контекстных меню колонок появляется команда _Reset Column Width_. Эта команда сбрасывает сделанные пользователями изменения ширины колонок, восстанавливая исходную ширину, применённую к колонкам в XAML или code-behind до пользовательских изменений.

![columns-resetcolumnwidthmenu](../images/columns-resetcolumnwidthmenu.png)

##### Связанный API

- [`DataGridControl.AllowResetColumnWidth`](../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/AllowResetColumnWidth.md)
- [`DataGridControl.ResetColumnWidth`](../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ResetColumnWidth.md)
- [`TreeListControl.AllowResetColumnWidth`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AllowResetColumnWidth.md)
- [`TreeListControl.ResetColumnWidth`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ResetColumnWidth.md)

#### Исправленные проблемы

- TreeList — возникает `StackOverflowException` при фильтрации данных, если [`ExpandNodesOnFiltering`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/ExpandNodesOnFiltering.md) равно `true`.
- TreeList — активный редактор в строке автофильтра закрывается при изменении коллекции узлов.
- DataGrid и TreeList — сочетание клавиш `Cmd+A` не работает на Mac.

### Cartesian Chart — улучшения перекрестия (Crosshair)

Контрол Cartesian Chart расширяет свой публичный API, чтобы дать вам более точный контроль над поведением и внешним видом меток перекрестия. 

#### Новый режим отображения меток перекрестия

Свойство [`CrosshairOptions.SeriesLabelMode`](../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/SeriesLabelMode.md) задаёт, объединяются ли несколько меток перекрестия и как именно. Значение этого свойства по умолчанию теперь `Smart`:

- Режим `Smart` — каждая серия отображает собственную метку перекрестия. Когда метки перекрываются, они объединяются в одну метку.
  
  ![chart-CrosshairSeriesLabelMode-smart](../images/chart-CrosshairSeriesLabelMode-smart.png)

#### Сортировка серий в перекрестии

Когда несколько серий объединены в одну метку перекрестия, вы можете использовать новое свойство [`CrosshairOptions.SeriesLabelItemSortMode`](../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/SeriesLabelItemSortMode.md), чтобы задать порядок отображения серий в метке:

- Порядок `By Series` — сортирует серии по порядку, в котором эти серии добавлены в коллекцию [`CartesianChart.Series`](../API/Eremex.AvaloniaUI.Charts/CartesianChart/Series.md).

    ![chart-CrosshairSeriesLabelItemSortMode-BySeries](../images/chart-CrosshairSeriesLabelItemSortMode-BySeries.png)

- Порядок `By Value` — сортирует серии по их значениям _Y_.

    ![chart-CrosshairSeriesLabelItemSortMode-ByValue](../images/chart-CrosshairSeriesLabelItemSortMode-ByValue.png)

#### Включать только серии рядом с курсором

Следующее свойство позволяет показывать метки перекрестия только для точек данных вблизи курсора.

- [`CrosshairOptions.MaxPickDistance`](../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/MaxPickDistance.md) — задаёт диапазон, в пределах которого выполняется поиск точек данных для включения в метки перекрестия.

    ![chart-Crosshair-MaxPickDistance](../images/chart-Crosshair-MaxPickDistance.png)

#### Задержка показа перекрестия

- [`CrosshairOptions.SeriesLabelShowDelay`](../API/Eremex.AvaloniaUI.Charts/CrosshairOptions/SeriesLabelShowDelay.md) — задаёт задержку (в миллисекундах) перед отображением метки серии перекрестия.


#### API показа и скрытия перекрестия

- `ShowCrosshair(Point position)`
- [`HideCrosshair()`](../API/Eremex.AvaloniaUI.Charts/CartesianChart/HideCrosshair.md)

#### Обновлённый шаблон перекрестия

Шаблон перекрестия контрола диаграммы был переработан для оптимизации структуры, поддержки новой функции сортировки серий и достижения единообразного внешнего вида в различных сценариях.

![chart-crosshairtemplate-changes-v14](../images/chart-crosshairtemplate-changes-v14.png)

Изменения шаблона включают:

- Класс [`CrosshairAllSeriesLabelControlData`](../API/Eremex.AvaloniaUI.Charts/CrosshairAllSeriesLabelControlData.md) теперь содержит коллекцию `ObservableCollection<CrosshairSeriesLabelItem> SeriesItems` вместо коллекции `CrosshairAllSeriesLabelGroup`.
- Класс `CrosshairAllSeriesLabelGroup` был удалён.
- Класс `CrosshairAllSeriesLabelSeriesItem` был переименован в [`CrosshairSeriesLabelItem`](../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesLabelItem.md). Этот класс содержит информацию об аргументе серии и префиксе аргумента.
- Класс `CrosshairAllSeriesLabelSeriesValueItem` был переименован в [`CrosshairSeriesLabelSeriesValueItem`](../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesLabelSeriesValueItem.md).
- Класс [`CrosshairSingleSeriesLabelControlData`](../API/Eremex.AvaloniaUI.Charts/CrosshairSingleSeriesLabelControlData.md) больше не наследуется от `CrosshairAllSeriesLabelSeriesValueItem`. [`CrosshairSingleSeriesLabelControlData`](../API/Eremex.AvaloniaUI.Charts/CrosshairSingleSeriesLabelControlData.md) теперь предоставляет свойство [`SeriesItem`](../API/Eremex.AvaloniaUI.Charts/CrosshairSingleSeriesLabelControlData/SeriesItem.md) типа [`CrosshairSeriesLabelItem`](../API/Eremex.AvaloniaUI.Charts/CrosshairSeriesLabelItem.md).

#### Документация

- [Перекрестие (Crosshair)](../controls/charts/crosshair.md)


### Интерфейс Докинга

#### Исправленные проблемы

- В некоторых случаях возникает исключение при закреплении плавающей панели.
- Элемент докинга не активируется, когда отображается меню с включённым свойством `OverlayDismissEventPassThrough`.

### Критические изменения

- Зависимость от пакета `CommunityToolkit.Mvvm` была удалена. Если вашему проекту требуется этот пакет, добавьте ссылку на `CommunityToolkit.Mvvm` явно.
- [`DataControlCommands`](../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlCommands.md), [`DataGridControlCommands`](../API/Eremex.AvaloniaUI.Controls.DataControl/DataGridControlCommands.md), [`TreeListCommands`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListCommands.md) и команды редакторов теперь содержат `ICommand` вместо `IRelayCommand` из CommunityToolkit.


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
