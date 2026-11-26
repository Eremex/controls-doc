---
title: Часто используемый API
order: 100
seealso: []
---

# Часто используемый API

## Свойства

Свойство | Описание 
---|---
[`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) | Возвращает активный редактор ячейки Eremex. Свойство возвращает `null`, если в данный момент нет активного редактора или когда в сфокусированной ячейке активен не-Eremex редактор.
[`AllowEditing`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/AllowEditing.md) | Возвращает или задаёт, включены ли операции редактирования ячеек.
[`AutoGenerateRows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/AutoGenerateRows.md) | Возвращает или задаёт, генерирует ли пустой контрол автоматически строки для всех публичных свойств, доступных в привязанном объекте (объектах), при инициализации контрола. Если контрол уже содержит строки, автоматическая генерация строк отключается. Чтобы вручную заполнить контрол строками, вы можете использовать метод [`RetrieveFields`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/RetrieveFields.md) или добавлять строки в коллекцию [`Rows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/Rows.md).
[`CellTemplate`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CellTemplate.md)  | Возвращает или задаёт шаблон для отрисовки редакторов во всех ячейках. Вы можете использовать свойство [`PropertyGridRow.CellTemplate`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridRow/CellTemplate.md), чтобы задать редактор ячейки для конкретных строк.
[`FocusedRow`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/FocusedRow.md) | Возвращает или задаёт сфокусированную строку. Это свойство позволяет сфокусировать конкретную строку.
[`Rows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/Rows.md) | Возвращает строки контрола, отображаемые на корневом уровне. Для категориальных строк (объектов [`PropertyGridCategoryRow`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridCategoryRow.md)), хранящихся в этой коллекции, вы можете использовать свойство [`PropertyGridCategoryRow.Rows`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridCategoryRow/Rows.md), чтобы обратиться к их дочерним строкам.
[`RowsDataTemplates`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/RowsDataTemplates.md) | Задаёт шаблоны данных, используемые для отрисовки строк из источника строк (свойство [`RowsSource`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridExpandableRowBase/RowsSource.md)).
[`RowsSource`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridExpandableRowBase/RowsSource.md) | Задаёт источник данных для генерации строк с помощью шаблонов данных ([`RowsDataTemplates`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/RowsDataTemplates.md)).
[`SelectedObject`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObject.md) | Возвращает или задаёт объект, свойства которого отображаются в контроле.
[`SelectedObjects`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObjects.md) | Возвращает или задаёт список объектов, свойства которых отображаются в контроле.

## Методы

Метод | Описание
------|------
[`CloseEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CloseEditor.md) | Скрывает активный редактор и сохраняет внесённые изменения.
[`HideEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/HideEditor.md) | Скрывает активный редактор и отменяет внесённые изменения.
[`RetrieveFields`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/RetrieveFields.md) | Генерирует строки для публичных свойств, предоставляемых привязанным объектом (объектами) (свойства [`SelectedObject`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObject.md) и [`SelectedObjects`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/SelectedObjects.md)). Перед началом генерации строк существующие строки очищаются.
[`PostEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/PostEditor.md) | Сохраняет изменения, внесённые в ячейку, в привязанный объект (объекты).
[`ShowEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowEditor.md) | Активирует редактор сфокусированной строки. 

## События

Событие | Описание
------|------
[`CellValueChanged`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CellValueChanged.md) | Возникает при изменении значения ячейки.
[`CustomCellTemplateData`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CustomCellTemplateData.md) | Позволяет предоставить пользовательский объект в качестве значения шаблона ячейки. Дополнительную информацию смотрите в следующем разделе: [Пользовательские редакторы](custom-editors.md#динамическое-назначение-редакторов-на-основе-типа-данных-строки).
[`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md) | Возникает при активации редактора ячейки.


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
