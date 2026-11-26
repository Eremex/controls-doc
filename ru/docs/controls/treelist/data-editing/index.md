---
title: Редактирование данных
order: 6000
seealso: []
---

# Редактирование данных

## Встроенные редакторы Eremex по умолчанию

Поведение по умолчанию элементов управления TreeList и TreeView заключается в использовании встроенных редакторов Eremex для отображения и редактирования значений ячеек стандартных типов данных:
Если вы явно не указали редакторы ячеек, элементы управления TreeList и TreeView используют встроенные редакторы Eremex для отображения и редактирования значений ячеек следующих типов данных:

- Логические значения (Boolean) — [`CheckEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md)
- Значения типа Double — [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md)
- Значения перечислений (Enumeration) — [`ComboBoxEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md)
- Свойства с атрибутом `TypeConverter`, метод `TypeConverter.GetStandardValuesSupported` которого возвращает `true` — [`ComboBoxEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md)
- Прочие значения — [`TextEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md)

Вы можете явно указать редакторы ячеек для колонок, чтобы переопределить назначение редактора по умолчанию, а также настроить параметры встроенных редакторов. Текущий раздел содержит более подробную информацию о назначении редакторов.

Когда в ячейке начинается операция редактирования, вы можете получить доступ к активному встроенному редактору и изменить его. Дополнительную информацию смотрите в разделе [Доступ к активному встроенному редактору Eremex](#доступ-к-активному-встроенному-редактору-eremex).

## Назначение встроенных редакторов Eremex

Элементы управления TreeList и TreeView позволяют явно назначать встроенные редакторы Eremex ячейкам (колонкам), чтобы переопределить назначение редактора по умолчанию, либо настроить редакторы ячеек в XAML или code-behind. Используйте для этого следующие свойства:

- Элемент управления TreeView: [`TreeViewControl.EditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/EditorProperties.md) 

  Элемент управления TreeView отображает одну колонку данных. Таким образом, свойство [`TreeViewControl.EditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/EditorProperties.md) задаёт встроенный редактор, используемый для редактирования ячеек этой колонки.

- Элемент управления TreeList: [`TreeListColumn.EditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md)
  
  Каждая колонка в элементе управления TreeList может иметь собственный встроенный редактор. Создайте колонку TreeList (объект [`TreeListColumn`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListColumn.md)) в коллекции [`TreeListControl.Columns`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/Columns.md) и задайте редактор колонки с помощью свойства [`TreeListColumn.EditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md).

Вы можете установить свойство `EditorProperties` в один из следующих объектов, задающих тип встроенного редактора (все эти объекты являются потомками [`BaseEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditorProperties.md)):

- [`ButtonEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditorProperties.md) — содержит параметры, специфичные для элемента управления [`ButtonEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md).
- [`CheckEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditorProperties.md) — содержит параметры, специфичные для элемента управления [`CheckEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md).
- [`ComboBoxEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditorProperties.md) — содержит параметры, специфичные для элемента управления [`ComboBoxEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md).
- [`DateEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditorProperties.md) — содержит параметры, специфичные для элемента управления [`DateEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md).
- [`HyperlinkEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/HyperlinkEditorProperties.md) — содержит параметры, специфичные для элемента управления [`HyperlinkEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/HyperlinkEditor.md).
- [`MemoEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/MemoEditorProperties.md) — содержит параметры, специфичные для элемента управления [`MemoEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/MemoEditor.md).
- [`PopupColorEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupColorEditorProperties.md) — содержит параметры, специфичные для элемента управления [`PopupColorEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupColorEditor.md).
- [`SegmentedEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditorProperties.md) — содержит параметры, специфичные для элемента управления [`SegmentedEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md).
- [`SpinEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditorProperties.md) — содержит параметры, специфичные для элемента управления [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md).
- [`TextEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditorProperties.md) — содержит параметры, специфичные для элемента управления [`TextEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md).
    
Предположим, что вы установили свойство `EditorProperties` в объект [`SpinEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditorProperties.md). В режиме отображения (когда редактирование ячейки не активно) элемент управления TreeList/TreeView эмулирует [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) в ячейках целевой колонки, используя параметры объекта [`SpinEditorProperties`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditorProperties.md). Реальный [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) не создаётся до тех пор, пока в ячейке не начнётся операция редактирования. Когда пользователь начинает редактирование ячейки, элемент управления TreeList/TreeView создаёт реальный встроенный редактор [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) в фокусированной ячейке. После завершения операции редактирования контрол уничтожает реальный [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) и снова начинает эмулировать [`SpinEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md) в этой ячейке. Информацию о том, как получить доступ к реальному редактору ячейки, смотрите в разделе [Доступ к активному встроенному редактору Eremex](#доступ-к-активному-встроенному-редактору-eremex).

### Пример — как использовать ButtonEditor в качестве встроенного редактора в колонке treelist

Следующий код назначает встроенный редактор [`ButtonEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md) колонке TreeList.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist" 
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxtl:TreeListControl.Columns>
    <mxtl:TreeListColumn Header="Name" FieldName="Name">
        <mxtl:TreeListColumn.EditorProperties>
            <mxe:ButtonEditorProperties>
                <mxe:ButtonEditorProperties.Buttons>
                    <mxe:ButtonSettings Content="Clear" 
                     Command="{Binding $parent[mxtl:CellControl].DataControl.
                               DataContext.ClearValueCommand}"/>
                </mxe:ButtonEditorProperties.Buttons>
            </mxe:ButtonEditorProperties>
        </mxtl:TreeListColumn.EditorProperties>
    </mxtl:TreeListColumn>
</mxtl:TreeListControl.Columns>
```

### Пример — как использовать ComboBoxEditor в качестве встроенного редактора в treeview

Следующий код назначает встроенный редактор [`ComboBoxEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md) элементу управления TreeView.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist" 
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxtl:TreeViewControl.EditorProperties>
    <mxe:ComboBoxEditorProperties ItemsSource="{Binding Families}"/>
</mxtl:TreeViewControl.EditorProperties>
```

## Назначение встроенных редакторов Eremex с помощью шаблонов

Вы можете использовать шаблоны для назначения редакторов Eremex колонкам TreeList и TreeView. Шаблоны ячеек позволяют предоставлять разные редакторы для разных строк в одном и том же колонке.

!!! Note 

    Использование шаблонов имеет следующие ограничения:

    - Отображаемый текст, предоставляемый через шаблоны ячеек, не используется для сортировки, группировки и фильтрации данных.
    - Шаблоны ячеек не [экспортируются](../export.md).


Чтобы предоставить встроенный редактор для колонки в шаблоне ячейки, используйте следующие свойства:

- [`TreeListColumn.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md)
- [`TreeViewControl.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/CellTemplate.md)

Установите свойство `x:Name` в значение **"PART_Editor"** для редактора Eremex, определённого в шаблоне. Это обеспечивает автоматическую привязку значения редактора ([`BaseEditor.EditorValue`](../../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md)) к полю колонки. Кроме того, 
параметры внешнего вида редактора (видимость рамки и цвета переднего плана в активном и неактивном состояниях) будут управляться элементом управления TreeList/TreeView.

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
...
<mxtl:TreeListColumn Header="Phone" FieldName="Phone">
    <mxtl:TreeListColumn.CellTemplate>
        <DataTemplate>
            <mxe:ButtonEditor x:Name="PART_Editor">
                <mxe:ButtonEditor.Buttons>
                    <mxe:ButtonSettings Content="..."/>
                </mxe:ButtonEditor.Buttons>
            </mxe:ButtonEditor>
        </DataTemplate>
    </mxtl:TreeListColumn.CellTemplate>
</mxtl:TreeListColumn>
```


## Пользовательские редакторы

Вы можете использовать шаблоны ячеек, чтобы встраивать пользовательские редакторы в колонки TreeList и TreeView. Доступны следующие подходы:

- Назначить редактор напрямую конкретной колонке.
- Динамически назначать редакторы колонкам на основе типа данных базового объекта колонки. Этот подход применим к элементу управления TreeList.

Дополнительную информацию смотрите в разделе [Пользовательские редакторы](custom-editors.md).



## Получение и установка значений ячеек

Элементы управления TreeList и TreeView предоставляют следующий API для получения и установки значений ячеек:

- [`TreeListControl.GetCellDisplayText`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/GetCellDisplayText.md)
- [`TreeListControl.GetCellValue`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/GetCellValue.md)
- [`TreeListControl.SetCellValue`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/SetCellValue.md)
- [`TreeViewControl.GetCellDisplayText`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/GetCellDisplayText.md)
- [`TreeViewControl.GetCellValue`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/GetCellValue.md)
- [`TreeViewControl.SetCellValue`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/SetCellValue.md)



## Доступ к активному встроенному редактору Eremex

- Свойство [`ActiveEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ActiveEditor.md) — возвращает активный встроенный редактор. 
  
  Когда встроенный редактор Eremex назначен колонке TreeList/TreeView (неявно или явно с помощью свойства `EditorSettings` и шаблонов), контрол эмулирует указанный встроенный редактор в ячейках этой колонки в режиме отображения (когда редактирование ячейки не активно). В этот момент реального встроенного редактора не существует. Эмуляция редакторов ячеек в режиме отображения повышает производительность приложения.

  Когда пользователь начинает редактирование ячейки, контрол создаёт реальный встроенный редактор. В этот момент вы можете использовать свойство контрола [`ActiveEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ActiveEditor.md), чтобы получить доступ к реальному экземпляру редактора Eremex. Когда ячейка теряет фокус, реальный редактор уничтожается, и свойство [`ActiveEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ActiveEditor.md) возвращает `null`.

- Событие [`ShownEditor`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShownEditor.md) — возникает после того, как для ячейки был создан встроенный редактор и началась операция редактирования. Доступ к активному редактору можно получить через параметр события [`Editor`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewEditorEventArgs/Editor.md) или свойство контрола [`ActiveEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ActiveEditor.md).

## Отображение редакторов ячеек

- Метод [`ShowEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ShowEditor.md) — активирует редактор в фокусированной ячейке.
- Событие [`ShowingEditor`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowingEditor.md) — позволяет предотвратить активацию редактора ячейки пользователями в определённых случаях. При обработке события [`ShowingEditor`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowingEditor.md) установите параметр события [`Cancel`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewShowingEditorEventArgs/Cancel.md) в `true`, чтобы отключить активацию редактора.


### Отображение редакторов ячеек пользователями

Когда редактирование ячеек включено, щелчок по ячейке узла активирует редактор ячейки. Используйте свойство [`DataControlBase.EditorShowMode`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/EditorShowMode.md), чтобы указать, какое действие мыши запускает редактор. Вы можете установить это свойство в одно из следующих значений:

- [`EditorShowMode.PointerPressed`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md) (по умолчанию) — редактор ячейки активируется при нажатии кнопки мыши.

    Когда включено [перетаскивание узлов](../node-drag-and-drop.md) и [`RowDragMode`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/RowDragMode.md) установлен в [`RowDragMode.Row`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/RowDragMode.md), режим [`EditorShowMode.PointerPressed`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md) не поддерживается. В этой конфигурации режим по умолчанию — [`EditorShowMode.PointerPressedInFocusedCell`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md).

- [`EditorShowMode.PointerPressedInFocusedCell`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md) — редактор ячейки активируется при нажатии кнопки мыши в фокусированной ячейке.

    Этот режим используется по умолчанию, если перетаскивание узлов активно, а свойство контрола [`RowDragMode`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/RowDragMode.md) установлено в [`RowDragMode.Row`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/RowDragMode.md).

- [`EditorShowMode.PointerReleased`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md) — редактор ячейки активируется при отпускании кнопки мыши.
- [`EditorShowMode.PointerReleasedInFocusedCell`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/EditorShowMode.md) — редактор ячейки активируется при отпускании кнопки мыши в фокусированной ячейке.

## Закрытие активного встроенного редактора

- Метод [`CloseEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/CloseEditor.md) — сохраняет изменения, внесённые в редакторе ячейки, и закрывает редактор.
- Метод [`HideEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/HideEditor.md) — закрывает редактор ячейки без сохранения изменений.

- Событие [`HiddenEditor`](../../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/HiddenEditor.md) — возникает после закрытия активного редактора ячейки.


## Сохранение изменений, внесённых во встроенном редакторе

- Метод [`CloseEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/CloseEditor.md) — сохраняет изменения, внесённые в редакторе ячейки, и закрывает редактор.
- Метод [`PostEditor`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/PostEditor.md) — сохраняет изменения, внесённые в активном редакторе ячейки, без закрытия редактора.

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
