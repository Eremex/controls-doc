---
title: DateEditor
order: 112000
seealso: []
---

# DateEditor

Контрол [`DateEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md) содержит выпадающий календарь, позволяющий пользователям выбирать дату. Редактор поддерживает несколько форматов отображения значения даты в поле ввода.

![dateeditor](../../images/dateeditor.png)

Выпадающий календарь содержит навигационный заголовок, используемый для перемещения по месяцам и годам. Кнопки Today и Clear помогают пользователям быстро выбрать сегодняшнюю дату и очистить текущее значение соответственно.

Основные возможности контрола включают:

- Выбор даты в выпадающем календаре с помощью мыши.
- Перемещение по месяцам и годам с помощью панели навигации.
- Три представления календаря: представление месяца, представление года и представление диапазона лет.
- Встроенные кнопки Today и Clear.
- Ограничение доступного диапазона дат.
- Множество форматов отображения выбранного значения даты в поле ввода.


## Выбор даты

Пользователь может выбрать дату, открыв выпадающее окно и выбрав дату в появившемся календаре.

Навигационный заголовок выпадающего календаря позволяет пользователю перемещаться по месяцам и годам:

![DateEditor - select date](../../images/dateeditor-selectdate-animation.gif)

В коде вы можете задать дату или прочитать текущую выбранную дату с помощью свойства [`DateEditor.DateTime`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/DateTime.md) или [`DateEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md). Эти свойства синхронизированы. Они различаются типом значения: свойство [`DateTime`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/DateTime.md) имеет тип nullable `System.DateTime`, тогда как свойство [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) имеет тип `object`, как во всех редакторах Eremex.

## Настройка всплывающего календаря

Следующие свойства позволяют настроить календарь [`DateEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md):

- [`ShowToday`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/ShowToday.md) — возвращает или задаёт, выделять ли сегодняшнюю дату в календаре. 
- [`NullValueButtonPosition`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor/NullValueButtonPosition.md) — возвращает или задаёт, видима ли кнопка (_'x'_) (очистки значения). 
- [`MinValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/MinValue.md) — задаёт минимальную допустимую дату. Свойства [`MinValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/MinValue.md) и [`MaxValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/MaxValue.md) позволяют задать диапазон значений, отображаемых в календаре.
- [`MaxValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/MaxValue.md) — задаёт максимальную допустимую дату.

<!--TODO
[`ShowToday`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/ShowToday.md) — `HighlightTodayDate`?
[`NullValueButtonPosition`](../../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor/NullValueButtonPosition.md) — `ShowClearButton`? 
-->

Вы также можете обработать событие [`PopupOpened`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpened.md), чтобы выполнить дополнительные настройки выпадающего календаря. В обработчике события [`PopupOpened`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpened.md) к объекту календаря можно обратиться с помощью свойства [`DateEditor.PopupContent`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupContent.md). Приведите это свойство к объекту класса [`CalendarControl`](../../API/Eremex.AvaloniaUI.Controls.Editors/CalendarControl.md), чтобы изменить его свойства. См. этот пример: [Пример - включение представления года при открытии календаря](#пример---включение-представления-года-при-открытии-календаря)




### Пример - как создать DateEditor

Этот пример определяет DateEditor, задаёт начальное значение и указывает допустимый диапазон дат.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<Window.DataContext>
    <local:MainViewModel/>
</Window.DataContext>

<mxe:DateEditor 
    DateTime="{Binding SelectedDate, Mode=TwoWay}" 
    MinValue="{Binding MinimumDate}" 
    MaxValue="{Binding MaximumDate}" />
```
``` csharp
using CommunityToolkit.Mvvm.ComponentModel;
using System.Collections.ObjectModel;

[ObservableObject]
public partial class MainViewModel
{
    [ObservableProperty]
    DateTime selectedDate = DateTime.Now;
    [ObservableProperty]
    DateTime minimumDate = DateTime.Now.AddDays(-15);
    [ObservableProperty] 
    DateTime maximumDate = DateTime.Now.AddDays(15);
}
```

## Формат отображения значения

Используйте свойство [`DisplayFormatString`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/DisplayFormatString.md), чтобы задать формат отображения значения даты/времени, отображаемого в поле ввода.

## Предотвращение всплывающих окон в редакторах только для чтения

В режиме «только для чтения» поведение любого всплывающего редактора по умолчанию — позволять пользователям открывать выпадающий список редактора. Однако они не могут изменять значения ни через поле ввода, ни через выпадающий список. Чтобы отключить всплывающие окна для редакторов только для чтения, установите свойство [`ShowPopupIfReadOnly`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/ShowPopupIfReadOnly.md) в `false`.

## Предотвращение открытия и закрытия всплывающих окон

Вы можете обработать следующие унаследованные события, чтобы отменить операции открытия и закрытия всплывающего окна:

- [`PopupEditor.PopupOpening`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpening.md) — возникает, когда всплывающее окно собирается создаться. 
- [`PopupEditor.PopupClosing`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupClosing.md) — возникает, когда всплывающее окно собирается закрыться. 

Эти события предоставляют параметр `e.Cancel`. Установите его в `true`, чтобы отменить текущую операцию.

## Настройка всплывающего окна при его появлении

Обработайте следующее унаследованное событие, чтобы изменить всплывающее окно или его вложенные контролы:

- [`PopupEditor.PopupOpened`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpened.md) — возникает после создания всплывающего окна и непосредственно перед его отображением. Это уведомляющее событие. Оно не позволяет отменить открытие всплывающего окна. Обработайте событие [`PopupOpened`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpened.md), чтобы настроить всплывающее окно или его дочерние контролы.

При обработке события [`PopupEditor.PopupOpened`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpened.md) используйте свойство [`PopupContent`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupContent.md) редактора, чтобы безопасно обратиться к контролу внутри всплывающего окна редактора. Событие [`PopupOpened`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpened.md) гарантирует, что контрол всплывающего окна существует, когда вы к нему обращаетесь. Для контрола DateEditor свойство [`PopupContent`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupContent.md) возвращает экземпляр класса [`CalendarControl`](../../API/Eremex.AvaloniaUI.Controls.Editors/CalendarControl.md). 

### Пример - включение представления года при открытии календаря

Этот пример показывает, как установить выпадающий календарь DateEditor в представление года при открытии.

![dateeditor-popupopened-example](../../images/dateeditor-popupopened-example.png)

Класс [`DateEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md) не предоставляет публичного свойства для изменения текущего представления своего календаря. Однако встроенный календарь (объект [`CalendarControl`](../../API/Eremex.AvaloniaUI.Controls.Editors/CalendarControl.md)) предоставляет публичное свойство `DisplayMode`. Это свойство задаёт режим представления календаря (`Month`, `Year` или `Decade`).

Этот пример обрабатывает событие [`PopupOpened`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpened.md), чтобы обратиться к встроенному календарю при его создании. Обработчик приводит свойство [`DateEditor.PopupContent`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupContent.md) к объекту [`CalendarControl`](../../API/Eremex.AvaloniaUI.Controls.Editors/CalendarControl.md), а затем устанавливает свойство `CalendarControl.DisplayMode` в `Year`.

``` cs
using Eremex.AvaloniaUI.Controls.Editors;

dateEditor1.PopupOpened += DateEditor_PopupOpened;

private void DateEditor_PopupOpened(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    DateEditor editor = sender as DateEditor;
    (editor.PopupContent as CalendarControl).DisplayMode = CalendarMode.Year;
}
```

## Реакция на закрытие всплывающего окна

Используйте следующее унаследованное событие, чтобы выполнять действия после закрытия всплывающего окна:

- [`PopupEditor.PopupClosed`](../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupClosed.md) — возникает сразу после закрытия всплывающего окна. Это уведомляющее событие. Оно не позволяет отменить закрытие всплывающего окна.


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
