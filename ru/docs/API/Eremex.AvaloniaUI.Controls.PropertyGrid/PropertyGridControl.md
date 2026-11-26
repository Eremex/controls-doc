# Класс PropertyGridControl

Отображает и редактирует свойства выбранного объекта.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.PropertyGrid`](./index.md)  
**Сборка:** `Eremex.Avalonia.Controls.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Объявление

```csharp
public class PropertyGridControl : TemplatedControl, IPropertyGridEditableNode, 
    IPropertyGridRowsOwner
```

## Конструкторы

| имя | описание |
| --- | --- |
| [PropertyGridControl](PropertyGridControl/PropertyGridControl.md)() | Инициализирует новый экземпляр класса PropertyGridControl. |

## Свойства

| имя | описание |
| --- | --- |
| [ActiveEditor](PropertyGridControl/ActiveEditor.md) { get; } | Возвращает редактор, активный в данный момент для строки с фокусом. |
| [AllowEditing](PropertyGridControl/AllowEditing.md) { get; set; } | Возвращает или задаёт, могут ли пользователи редактировать значения строк. |
| [AllowImmediateEditorValuePosting](PropertyGridControl/AllowImmediateEditorValuePosting.md) { get; set; } | Возвращает или задаёт, передаются ли значения редактора немедленно при их изменении. |
| [AllowResizing](PropertyGridControl/AllowResizing.md) { get; set; } | Возвращает или задаёт, могут ли пользователи изменять размер колонок заголовков и редакторов. |
| [AutoGenerateRows](PropertyGridControl/AutoGenerateRows.md) { get; set; } | Возвращает или задаёт, создаются ли строки автоматически из свойств выбранного объекта. |
| [CaptionColumnWidth](PropertyGridControl/CaptionColumnWidth.md) { get; set; } | Возвращает или задаёт ширину колонки заголовков. |
| [CaptionHorizontalAlignment](PropertyGridControl/CaptionHorizontalAlignment.md) { get; set; } | Возвращает или задаёт горизонтальное выравнивание заголовков строк. |
| [CellTemplate](PropertyGridControl/CellTemplate.md) { get; set; } | Возвращает или задаёт шаблон, отображающий значения строк, если строка не задаёт собственный шаблон. |
| [EditorButtonShowMode](PropertyGridControl/EditorButtonShowMode.md) { get; set; } | Возвращает или задаёт, когда отображаются кнопки редактора. |
| [EditorColumnWidth](PropertyGridControl/EditorColumnWidth.md) { get; set; } | Возвращает или задаёт ширину колонки редакторов. |
| [EditorShowMode](PropertyGridControl/EditorShowMode.md) { get; set; } | Возвращает или задаёт действие мыши, активирующее редактор. |
| [FocusedRow](PropertyGridControl/FocusedRow.md) { get; set; } | Возвращает или задаёт строку с фокусом. |
| [IgnoreValidationAttributesOnCommit](PropertyGridControl/IgnoreValidationAttributesOnCommit.md) { get; set; } | Возвращает или задаёт, игнорируются ли атрибуты валидации при фиксации значения редактора. |
| [IsResizerVisible](PropertyGridControl/IsResizerVisible.md) { get; } | Возвращает, отображается ли маркер изменения размера колонок. |
| [Rows](PropertyGridControl/Rows.md) { get; } | Возвращает коллекцию строк. |
| [RowsDataTemplates](PropertyGridControl/RowsDataTemplates.md) { get; set; } | Возвращает или задаёт шаблоны, используемые для создания строк из элементов RowsSource. |
| [RowsSource](PropertyGridControl/RowsSource.md) { get; set; } | Возвращает или задаёт коллекцию, элементы которой используются для создания строк. |
| [SearchText](PropertyGridControl/SearchText.md) { get; set; } | Возвращает или задаёт текст, используемый для фильтрации строк. |
| [SelectedObject](PropertyGridControl/SelectedObject.md) { get; set; } | Возвращает или задаёт объект, свойства которого отображаются и редактируются. |
| [SelectedObjects](PropertyGridControl/SelectedObjects.md) { get; set; } | Возвращает или задаёт коллекцию объектов, свойства которых отображаются и редактируются. Поддерживает одновременное редактирование нескольких объектов. |
| [ShowDataErrors](PropertyGridControl/ShowDataErrors.md) { get; set; } | Возвращает или задаёт, отображаются ли ошибки проверки данных для строк. |
| [ShowSearchPanel](PropertyGridControl/ShowSearchPanel.md) { get; set; } | Возвращает или задаёт, отображается ли панель поиска. |
| [ValidateRowValuesOnShowAndUpdate](PropertyGridControl/ValidateRowValuesOnShowAndUpdate.md) { get; set; } | Возвращает или задаёт, проверяются ли значения строк при отображении и обновлении, а не при фиксации значения редактора. |

## Методы

| имя | описание |
| --- | --- |
| [CloseEditor](PropertyGridControl/CloseEditor.md)() | Сохраняет значение активного редактора в объект данных и скрывает редактор. |
| [CollapseAllRows](PropertyGridControl/CollapseAllRows.md)() | Сворачивает все строки. |
| [ExpandAllRows](PropertyGridControl/ExpandAllRows.md)() | Разворачивает все строки. |
| [HideEditor](PropertyGridControl/HideEditor.md)() | Скрывает активный редактор без передачи его значения. |
| [PostEditor](PropertyGridControl/PostEditor.md)() | Сохраняет значение активного редактора в объект данных. |
| [Refresh](PropertyGridControl/Refresh.md)() | Повторно считывает значения из выбранного объекта и обновляет значения строк. |
| [RetrieveFields](PropertyGridControl/RetrieveFields.md)() | Заново создаёт строки из свойств выбранного объекта. |
| [ShowEditor](PropertyGridControl/ShowEditor.md)() | Активирует редактор для строки с фокусом и выделяет его содержимое. |

## События

| имя | описание |
| --- | --- |
| event [CellValueChanged](PropertyGridControl/CellValueChanged.md) | Происходит после изменения значения строки. |
| event [CellValueChanging](PropertyGridControl/CellValueChanging.md) | Происходит, когда пользователь изменяет значение строки в редакторе, до фиксации изменения. |
| event [CustomCellTemplateData](PropertyGridControl/CustomCellTemplateData.md) | Происходит, когда требуются данные для шаблона ячейки строки. Задайте свойство Data, чтобы предоставить пользовательские данные. |
| event [HiddenEditor](PropertyGridControl/HiddenEditor.md) | Происходит после закрытия редактора. |
| event [InvalidRowValueException](PropertyGridControl/InvalidRowValueException.md) | Происходит при возникновении исключения во время сохранения значения строки в объект данных. Задайте свойство ErrorContent, чтобы изменить сообщение об ошибке. |
| event [ShowingEditor](PropertyGridControl/ShowingEditor.md) | Происходит перед активацией редактора для строки. Отмените событие, чтобы запретить редактирование. |
| event [UsingComplexDataContext](PropertyGridControl/UsingComplexDataContext.md) | Происходит перед тем, как значение строки сложного типа будет использовано в качестве DataContext для содержимого ячейки. Отмените событие, чтобы вместо этого привязаться к свойству родительского объекта. |
| event [ValidateRowValue](PropertyGridControl/ValidateRowValue.md) | Происходит при проверке значения строки. Задайте свойство ErrorContent, чтобы указать на ошибку. |

## См. также

* пространство имён [Eremex.AvaloniaUI.Controls.PropertyGrid](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
