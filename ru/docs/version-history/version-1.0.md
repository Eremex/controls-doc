---
title: Версия 1.0
order: 10
seealso: []
---

# Версия 1.0

## 1.0.96

### Что нового

#### DataGridControl и TreeListControl

- Исправлено: при использовании всплывающего UserControl в качестве редактора ячейки UserControl неожиданно теряет фокус.

- Возможность: предоставить способность обрабатывать навигационные клавиши (клавиши со стрелками, Tab, Enter, F2, Esc, Home, End, PgUp и PgDown) во встроенных редакторах. 
    
    Контролы grid/treelist перехватывают определённые навигационные клавиши (клавиши со стрелками, Tab, Enter, F2, Esc, Home, End, PgUp и PgDown) для выполнения навигации между ячейками. Чтобы обрабатывать эти клавиши во встроенных редакторах, сделайте следующее:
    - Создайте класс, реализующий интерфейс [`IInplaceEditorNavigationHandler`](../API/Eremex.AvaloniaUI.Editors.InplaceEditing/IInplaceEditorNavigationHandler.md). 
    - Реализуйте метод [`IInplaceEditorNavigationHandler.NeedsKey`](../API/Eremex.AvaloniaUI.Editors.InplaceEditing/IInplaceEditorNavigationHandler/NeedsKey.md). Метод должен возвращать `true` для клавиш, которые нужно обрабатывать во встроенном редакторе.
    - Свяжите ваш объект [`IInplaceEditorNavigationHandler`](../API/Eremex.AvaloniaUI.Editors.InplaceEditing/IInplaceEditorNavigationHandler.md) с конкретным типом встроенного редактора с помощью статического метода [`EditorNavigationHandlers.RegisterHandler`](../API/Eremex.AvaloniaUI.Editors.InplaceEditing/EditorNavigationHandlers/RegisterHandler.md). Например: `EditorNavigationHandlers.RegisterHandler<TextBox, MyTextBoxNavigationHandler>();`.

- Исправлено: когда редактирование ячейки отключено, контрол, помещённый в шаблон ячейки, активируется при щелчке.
- Исправлено: обновление значения ячейки в отсортированной колонке грида приводит к изменению значений в других ячейках.
- Исправлено: клавиша Esc не откатывает изменения в ячейке, когда используется CellTemplate.

#### PropertyGrid

- Возможность: добавлено событие `HiddenEditor`.
- Возможность: добавлен параметр `Row` в событие `ShowingEditor`.

#### Редакторы

- Некорректный размер всплывающего редактора при использовании большой настройки DPI.


#### Диаграммы
- Исправлено: сбой перекрестия в некоторых случаях.
- Исправлено: исключение при использовании [`SortedDateTimeDataAdapter`](../API/Eremex.AvaloniaUI.Charts/SortedDateTimeDataAdapter.md) с пустыми данными.


## 1.0.93


### Что нового

#### ListView

- Исправлено: текущее выделение элемента не очищается при щелчке по элементу.
- Исправлено: сочетание клавиш CTRL+A не выбирает все элементы в режиме множественного выбора.
- Свойство ListViewControl.GroupWidth не поддерживается и было удалено.
- Метод ListViewControl.GetGroupValueDisplayText теперь internal.

#### PropertyGrid

- Исправлено: невозможно увести фокус со встроенного редактора при возникновении ошибки валидации и использовании CellTemplate.



## 1.0

### Что нового

#### Диаграммы

Контрол [`PolarChart`](../API/Eremex.AvaloniaUI.Charts/PolarChart.md) — новый контрол диаграммы, который строит диаграмму в полярной системе координат.

- Перекрестие (Crosshair)
- Полосы и постоянные линии
- Направление обхода и начальный угол (для оси X)
- Point Series View
- Line Series View
- Scatter Line Series View
- Area Series View
- Range Area Series View

Контрол [`SmithChart`](../API/Eremex.AvaloniaUI.Charts/SmithChart.md) — новый контрол, который строит диаграмму Смита.

- Перекрестие (Crosshair)
- Point Series View
- Scatter Line Series View

##### Обновления `CartesianChart`

- Полосы и постоянные линии
- Point Series View (с поддержкой SVG-маркеров)
- Area Series View
- Scatter Line Series View
- Step Line Series View
- Step Area Series View
- Range Area Series View
- Bar Series View
- Range Bar Series View 

##### Общие функции

- Использование паттерна проектирования MVVM для предоставления данных и настройки параметров диаграммы.
- Поддержка тёмного варианта темы.
- Новые методы `DiagramPointToScreenPoint` и `ScreenPointToDiagramPoint` полезны, когда нужно отобразить пользовательскую графику или всплывающие подсказки и определить координаты целевых элементов диаграммы.


#### Докинг
* Свойство [`DockPane.ShowGlyphMode`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/ShowGlyphMode.md) — задаёт видимость и положение глифа в заголовке панели.
* Свойство [`DockPane.ShowTabGlyphMode`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/ShowTabGlyphMode.md) — задаёт видимость и положение глифа в заголовке панели (вкладке), когда панель размещена в составе группы вкладок.
- Свойство [`FloatGroup.ShowGlyphMode`](../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup/ShowGlyphMode.md) — задаёт видимость и положение глифа в заголовке плавающего окна.
- Свойство [`DockItemBase.FloatGroup`](../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/FloatGroup.md) — позволяет получить плавающее окно ([`FloatGroup`](../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup.md)), в котором размещён текущий элемент докинга (панель) в плавающем режиме.
- Свойство [`DockItemBase.AutoHideGroup`](../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/AutoHideGroup.md) — позволяет получить контейнер автоскрытия ([`AutoHideGroup`](../API/Eremex.AvaloniaUI.Controls.Docking/AutoHideGroup.md)), в котором размещён текущий элемент докинга (панель) в режиме автоскрытия.
- [`DockManager.ExpandAutoHidePanel`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/ExpandAutoHidePanel.md) — разворачивает свёрнутую автоскрытую панель.
- [`DockManager.CollapseAutoHidePanel`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/CollapseAutoHidePanel.md) — сворачивает развёрнутую автоскрытую панель. 
- Методы [`DockManager.SaveLayout`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/SaveLayout.md) и [`DockManager.RestoreLayout`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/RestoreLayout.md) — позволяют сохранять и восстанавливать размещение контрола в поток и из потока.

#### DataGridControl и TreeListControl

- Методы [`SaveLayout`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/SaveLayout.md) и [`RestoreLayout`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/RestoreLayout.md) — позволяют сохранять и восстанавливать размещение контрола в поток и из потока.

#### TreeListControl и TreeViewControl

- Режим фильтра `ShowBranchesWithMatches` — вы можете установить свойство [`TreeListControlBase.FilterMode`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/FilterMode.md) в `ShowBranchesWithMatches`, чтобы отображать целые ветви, когда они содержат узлы, соответствующие критериям фильтра.

#### Редакторы

* Событие [`BaseEditor.Validate`](../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/Validate.md) — редакторы Eremex теперь поддерживают событие [`Validate`](../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/Validate.md), которое позволяет реализовывать пользовательские правила валидации.
* Метод [`BaseEditor.DoValidate`](../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/DoValidate.md) — позволяет принудительно вызвать валидацию.

#### Общие классы

- `ImageLoader` — новый класс `Eremex.AvaloniaUI.Controls.Utils.ImageLoader` предоставляет методы для загрузки изображений (SVG, PNG и т. д.) по URI из ресурсов.


### Критические изменения


#### DataGridControl и TreeListControl
* Свойство `ColumnBase.HeaderContentTemplate` переименовано в `HeaderTemplate`
* Свойство `ColumnBase.HeaderHorizontalContentAlignment` переименовано в [`HeaderHorizontalAlignment`](../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlColumnBase/HeaderHorizontalAlignment.md)
* Свойство `ColumnBase.HeaderVerticalContentAlignment` переименовано в [`HeaderVerticalAlignment`](../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlColumnBase/HeaderVerticalAlignment.md)

#### DataGridControl
* Метод `GetRowIndexBySourceIndex` переименован в `GetRowIndexBySourceItemIndex`
* Метод `GetRowIndexByVisibleIndex` переименован в `GetRowIndexByVisibleRowIndex`
* Метод `GetSourceIndexByRowIndex` переименован в `GetSourceItemIndexByRowIndex`
* Метод `GetSourceIndexByVisibleIndex` переименован в `GetSourceItemIndexByVisibleRowIndex`
* Метод `GetVisibleIndexByRowIndex` переименован в `GetVisibleRowIndexByRowIndex`
* Метод `GetVisibleIndexBySourceIndex` переименован в `GetVisibleRowIndexBySourceItemIndex`
* Метод `GetItemByVisibleIndex` переименован в `GetSourceItemByVisibleRowIndex`
* Метод `GetItemByRowIndex` переименован в `GetSourceItemByRowIndex`
* Событие `CustomColumnSort`: аргумент события `SourceIndex1` переименован в `SourceItemIndex1`. Аргумент события `SourceIndex2` переименован в `SourceItemIndex2`

#### Докинг

* Присоединённое свойство `TabbedGroup.TabHeader` заменено свойством [`DockPane.TabHeader`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/TabHeader.md)
* Присоединённое свойство `TabbedGroup.TabHeaderTemplate` заменено свойством [`DockPane.TabHeaderTemplate`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/TabHeaderTemplate.md)
* Присоединённое свойство `TabbedGroup.TabGlyph` заменено свойством [`DockPane.TabGlyph`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/TabGlyph.md)
* Присоединённое свойство `TabbedGroup.TabGlyphSize` заменено свойством [`DockPane.TabGlyphSize`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/TabGlyphSize.md)
* `TabbedGroup.ShowTabPanelForSinglePage` переименовано в [`ShowTabStripForSingleChild`](../API/Eremex.AvaloniaUI.Controls.Docking/TabbedGroup/ShowTabStripForSingleChild.md)
* Метод `DockManager.Hide` переименован в [`DockManager.AutoHide`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/AutoHide.md)

#### Общие классы
* Класс `SerializationHelper` переименован в `SerializationManager`


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
