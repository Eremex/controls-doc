---
title: Редактирование данных
order: 6000
seealso: []
---

# Редактирование данных

## Встроенные редакторы Eremex по умолчанию

Поведение по умолчанию элементов управления TreeList и TreeView заключается в использовании встроенных редакторов Eremex для отображения и редактирования значений ячеек стандартных типов данных:
Если вы явно не указали редакторы ячеек, элементы управления TreeList и TreeView используют встроенные редакторы Eremex для отображения и редактирования значений ячеек следующих типов данных:

- Логические значения (Boolean) — `CheckEditor`
- Значения типа Double — `SpinEditor`
- Значения перечислений (Enumeration) — `ComboBoxEditor`
- Свойства с атрибутом `TypeConverter`, метод `TypeConverter.GetStandardValuesSupported` которого возвращает `true` — `ComboBoxEditor`
- Прочие значения — `TextEditor`

Вы можете явно указать редакторы ячеек для колонок, чтобы переопределить назначение редактора по умолчанию, а также настроить параметры встроенных редакторов. Текущий раздел содержит более подробную информацию о назначении редакторов.

Когда в ячейке начинается операция редактирования, вы можете получить доступ к активному встроенному редактору и изменить его. Дополнительную информацию смотрите в разделе [Доступ к активному встроенному редактору Eremex](#доступ-к-активному-встроенному-редактору-eremex).

## Назначение встроенных редакторов Eremex

Элементы управления TreeList и TreeView позволяют явно назначать встроенные редакторы Eremex ячейкам (колонкам), чтобы переопределить назначение редактора по умолчанию, либо настроить редакторы ячеек в XAML или code-behind. Используйте для этого следующие свойства:

- Элемент управления TreeView: `TreeViewControl.EditorProperties` 

  Элемент управления TreeView отображает одну колонку данных. Таким образом, свойство `TreeViewControl.EditorProperties` задаёт встроенный редактор, используемый для редактирования ячеек этой колонки.

- Элемент управления TreeList: `TreeListColumn.EditorProperties`
  
  Каждая колонка в элементе управления TreeList может иметь собственный встроенный редактор. Создайте колонку TreeList (объект `TreeListColumn`) в коллекции `TreeListControl.Columns` и задайте редактор колонки с помощью свойства `TreeListColumn.EditorProperties`.

Вы можете установить свойство `EditorProperties` в один из следующих объектов, задающих тип встроенного редактора (все эти объекты являются потомками `BaseEditorProperties`):

- `ButtonEditorProperties` — содержит параметры, специфичные для элемента управления `ButtonEditor`.
- `CheckEditorProperties` — содержит параметры, специфичные для элемента управления `CheckEditor`.
- `ComboBoxEditorProperties` — содержит параметры, специфичные для элемента управления `ComboBoxEditor`.
- `DateEditorProperties` — содержит параметры, специфичные для элемента управления `DateEditor`.
- `HyperlinkEditorProperties` — содержит параметры, специфичные для элемента управления `HyperlinkEditor`.
- `MemoEditorProperties` — содержит параметры, специфичные для элемента управления `MemoEditor`.
- `PopupColorEditorProperties` — содержит параметры, специфичные для элемента управления `PopupColorEditor`.
- `SegmentedEditorProperties` — содержит параметры, специфичные для элемента управления `SegmentedEditor`.
- `SpinEditorProperties` — содержит параметры, специфичные для элемента управления `SpinEditor`.
- `TextEditorProperties` — содержит параметры, специфичные для элемента управления `TextEditor`.
    
Предположим, что вы установили свойство `EditorProperties` в объект `SpinEditorProperties`. В режиме отображения (когда редактирование ячейки не активно) элемент управления TreeList/TreeView эмулирует `SpinEditor` в ячейках целевой колонки, используя параметры объекта `SpinEditorProperties`. Реальный `SpinEditor` не создаётся до тех пор, пока в ячейке не начнётся операция редактирования. Когда пользователь начинает редактирование ячейки, элемент управления TreeList/TreeView создаёт реальный встроенный редактор `SpinEditor` в фокусированной ячейке. После завершения операции редактирования контрол уничтожает реальный `SpinEditor` и снова начинает эмулировать `SpinEditor` в этой ячейке. Информацию о том, как получить доступ к реальному редактору ячейки, смотрите в разделе [Доступ к активному встроенному редактору Eremex](#доступ-к-активному-встроенному-редактору-eremex).

### Пример — как использовать ButtonEditor в качестве встроенного редактора в колонке treelist

Следующий код назначает встроенный редактор `ButtonEditor` колонке TreeList.

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

Следующий код назначает встроенный редактор `ComboBoxEditor` элементу управления TreeView.

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

- `TreeListColumn.CellTemplate`
- `TreeViewControl.CellTemplate`

Установите свойство `x:Name` в значение **"PART_Editor"** для редактора Eremex, определённого в шаблоне. Это обеспечивает автоматическую привязку значения редактора (`BaseEditor.EditorValue`) к полю колонки. Кроме того, 
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

- `TreeListControl.GetCellDisplayText`
- `TreeListControl.GetCellValue`
- `TreeListControl.SetCellValue`
- `TreeViewControl.GetCellDisplayText`
- `TreeViewControl.GetCellValue`
- `TreeViewControl.SetCellValue`



## Доступ к активному встроенному редактору Eremex

- Свойство `ActiveEditor` — возвращает активный встроенный редактор. 
  
  Когда встроенный редактор Eremex назначен колонке TreeList/TreeView (неявно или явно с помощью свойства `EditorSettings` и шаблонов), контрол эмулирует указанный встроенный редактор в ячейках этой колонки в режиме отображения (когда редактирование ячейки не активно). В этот момент реального встроенного редактора не существует. Эмуляция редакторов ячеек в режиме отображения повышает производительность приложения.

  Когда пользователь начинает редактирование ячейки, контрол создаёт реальный встроенный редактор. В этот момент вы можете использовать свойство контрола `ActiveEditor`, чтобы получить доступ к реальному экземпляру редактора Eremex. Когда ячейка теряет фокус, реальный редактор уничтожается, и свойство `ActiveEditor` возвращает `null`.

- Событие `ShownEditor` — возникает после того, как для ячейки был создан встроенный редактор и началась операция редактирования. Доступ к активному редактору можно получить через параметр события `Editor` или свойство контрола `ActiveEditor`.

## Отображение редакторов ячеек

- Метод `ShowEditor` — активирует редактор в фокусированной ячейке.
- Событие `ShowingEditor` — позволяет предотвратить активацию редактора ячейки пользователями в определённых случаях. При обработке события `ShowingEditor` установите параметр события `Cancel` в `true`, чтобы отключить активацию редактора.


### Отображение редакторов ячеек пользователями

Когда редактирование ячеек включено, щелчок по ячейке узла активирует редактор ячейки. Используйте свойство `DataControlBase.EditorShowMode`, чтобы указать, какое действие мыши запускает редактор. Вы можете установить это свойство в одно из следующих значений:

- `EditorShowMode.PointerPressed` (по умолчанию) — редактор ячейки активируется при нажатии кнопки мыши.

    Когда включено [перетаскивание узлов](../node-drag-and-drop.md) и `RowDragMode` установлен в `RowDragMode.Row`, режим `EditorShowMode.PointerPressed` не поддерживается. В этой конфигурации режим по умолчанию — `EditorShowMode.PointerPressedInFocusedCell`.

- `EditorShowMode.PointerPressedInFocusedCell` — редактор ячейки активируется при нажатии кнопки мыши в фокусированной ячейке.

    Этот режим используется по умолчанию, если перетаскивание узлов активно, а свойство контрола `RowDragMode` установлено в `RowDragMode.Row`.

- `EditorShowMode.PointerReleased` — редактор ячейки активируется при отпускании кнопки мыши.
- `EditorShowMode.PointerReleasedInFocusedCell` — редактор ячейки активируется при отпускании кнопки мыши в фокусированной ячейке.

## Закрытие активного встроенного редактора

- Метод `CloseEditor` — сохраняет изменения, внесённые в редакторе ячейки, и закрывает редактор.
- Метод `HideEditor` — закрывает редактор ячейки без сохранения изменений.

- Событие `HiddenEditor` — возникает после закрытия активного редактора ячейки.


## Сохранение изменений, внесённых во встроенном редакторе

- Метод `CloseEditor` — сохраняет изменения, внесённые в редакторе ячейки, и закрывает редактор.
- Метод `PostEditor` — сохраняет изменения, внесённые в активном редакторе ячейки, без закрытия редактора.

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
