---
title: Редактирование данных
order: 700
seealso: []
---

# Редактирование данных

## Встроенные редакторы Eremex, используемые по умолчанию

Если вы не задаёте встроенные редакторы для строк явно, контрол PropertyGrid использует встроенные редакторы Eremex для отображения и редактирования значений строк распространённых типов данных.

![propertygrid-inplaceeditors](../../images/propertygrid-inplaceeditors.png)

Следующий список показывает редакторы Eremex, связанные с распространёнными типами данных:

- Значения Boolean — [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md)
- Значения Double — [`SpinEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md)
- Значения перечислений — [`ComboBoxEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md)
- Свойства с атрибутом `TypeConverter`, чей метод `TypeConverter.GetStandardValuesSupported` возвращает `true` — [`ComboBoxEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md)
- Другие значения — [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md)

Вы можете динамически обращаться к экземплярам встроенных редакторов Eremex и изменять их, когда эти редакторы активны. Подробнее смотрите в разделе [Доступ к активному встроенному редактору Eremex](#доступ-к-активному-встроенному-редактору-eremex).

## Назначение встроенных редакторов Eremex

Вы можете явно назначать встроенные редакторы Eremex строкам, если вам нужно переопределить назначение редактора по умолчанию или настроить редакторы строк в XAML или code-behind. 

Используйте для этого свойство [`PropertyGridRow.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridRow/EditorProperties.md) следующим образом:

1. Создайте и настройте экземпляр вспомогательного класса `...EditorProperties`, хранящего настройки, специфичные для нужного встроенного редактора. Все эти вспомогательные классы являются потомками [`BaseEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditorProperties.md): 
    - [`ButtonEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditorProperties.md) — содержит настройки, специфичные для контрола [`ButtonEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md).
    - [`CheckEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditorProperties.md) — содержит настройки, специфичные для контрола [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md).
    - `ColorEditorProperties` — содержит настройки, специфичные для контрола [`ColorEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ColorEditor.md).
    - [`ComboBoxEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditorProperties.md) — содержит настройки, специфичные для контрола [`ComboBoxEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md).
    - [`HyperlinkEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/HyperlinkEditorProperties.md) — содержит настройки, специфичные для контрола [`HyperlinkEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/HyperlinkEditor.md).
    - [`PopupColorEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupColorEditorProperties.md) — содержит настройки, специфичные для контрола [`PopupColorEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupColorEditor.md).
    - [`PopupEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditorProperties.md) — содержит настройки, специфичные для контрола [`PopupEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor.md).
    - [`SegmentedEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditorProperties.md) — содержит настройки, специфичные для контрола [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md).
    - [`SpinEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditorProperties.md) — содержит настройки, специфичные для контрола [`SpinEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md).
    - [`TextEditorProperties`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditorProperties.md) — содержит настройки, специфичные для контрола [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md).
    
2. Установите свойство [`PropertyGridRow.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridRow/EditorProperties.md) в созданный экземпляр `...EditorProperties`.

``` xml
xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxpg:PropertyGridRow FieldName="OrderNo">
    <mxpg:PropertyGridRow.EditorProperties >
        <mxe:ButtonEditorProperties TextWrapping="Wrap" />
    </mxpg:PropertyGridRow.EditorProperties>
</mxpg:PropertyGridRow>
```

Свойство [`PropertyGridRow.CellTemplate`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridRow/CellTemplate.md) — ещё один способ назначить редактор Eremex строке. Убедитесь, что у редактора Eremex свойство `x:Name` установлено в **"PART_Editor"**. В этом случае PropertyGrid автоматически привязывает свойство редактора [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) к привязанному полю строки. Кроме того, PropertyGrid начинает поддерживать настройки внешнего вида встроенного редактора (видимость рамок и цвета текста в активном и неактивном состояниях).

``` xml
xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
...
<mxpg:PropertyGridRow FieldName="Caption">
    <mxpg:PropertyGridRow.CellTemplate>
        <DataTemplate>
            <mxe:ButtonEditor x:Name="PART_Editor">
                <mxe:ButtonEditor.Buttons>
                    <mxe:ButtonSettings Content="..."/>
                </mxe:ButtonEditor.Buttons>
            </mxe:ButtonEditor>
        </DataTemplate>
    </mxpg:PropertyGridRow.CellTemplate>
</mxpg:PropertyGridRow>
```


## Пользовательские редакторы
PropertyGrid позволяет задавать пользовательские редакторы для ячеек строк. Вы можете назначить редактор непосредственно конкретной строке или динамически назначать редакторы строкам на основе типа данных базового объекта строки.
Дополнительную информацию смотрите в следующем разделе: [Пользовательские редакторы](custom-editors.md).

<!--TODO ## Get and Set Cell values

-->

## Доступ к активному встроенному редактору Eremex

- Свойство [`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) — возвращает активный встроенный редактор. 
  
  Для повышения производительности контрола PropertyGrid использует облегчённые версии встроенных редакторов Eremex, когда отрисовывает значения ячеек в режиме отображения (когда редактирование текста не активно). Когда в ячейке начинается операция редактирования текста, встроенный редактор переключается со своей облегчённой версии на полнофункциональную версию. В этом случае вы можете использовать свойство [`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) для доступа к экземпляру редактора Eremex. Когда ячейка строки теряет фокус, редактор переключается обратно на свою облегчённую версию, и свойство [`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) возвращает `null`.

- Событие [`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md) — позволяет получать уведомления о начале операций редактирования в ячейках строк. Вы можете безопасно обращаться к свойству [`ActiveEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ActiveEditor.md) в обработчике события [`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md).

## Показ редактора ячейки

- Метод [`ShowEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowEditor.md) — активирует редактор ячейки в сфокусированной строке.
- Событие [`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md) — позволяет в определённых случаях предотвратить активацию редактора ячейки пользователями. При обработке события [`ShowingEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/ShowingEditor.md) установите параметр события `Cancel` в `true`, чтобы отключить активацию редактора.

## Закрытие активного встроенного редактора

- Метод [`CloseEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CloseEditor.md) — сохраняет изменения, внесённые в редактор ячейки, и закрывает редактор.
- Метод [`HideEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/HideEditor.md) — закрывает редактор ячейки без сохранения изменений.

- Событие [`HiddenEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/HiddenEditor.md) — возникает после закрытия активного редактора ячейки.


## Сохранение изменений, внесённых во встроенный редактор

- Метод [`CloseEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/CloseEditor.md) — сохраняет изменения, внесённые в редактор ячейки, и закрывает редактор.
- Метод [`PostEditor`](../../API/Eremex.AvaloniaUI.Controls.PropertyGrid/PropertyGridControl/PostEditor.md) — сохраняет изменения, внесённые в активный редактор ячейки, не закрывая редактор.


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
