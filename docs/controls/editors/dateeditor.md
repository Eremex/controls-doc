---
title: DateEditor
order: 112000
seealso: []
---

# DateEditor

The `DateEditor` control contains a dropdown calendar that allows users to select a date. The editor supports multiple display formats for the date value displayed in the edit box.

![dateeditor](../../images/dateeditor.png)

The dropdown calendar contains the navigation header used to browse through months and years. The Today and Clear buttons help users quickly select the Today's date and clear the current value, respectively.

The control's main features include:

- Date selection in the dropdown calendar with the mouse.
- Browsing through months and years using the navigation bar.
- Three calendar views: month view, year view, and year range view.
- Built-in Today and Clear buttons.
- Limiting the available date range.
- Numerous display formats for the selected date value in the edit box.


## Select a Date

A user can select a date by opening the dropdown window and picking a date in the calendar that appears.

The dropdown calendar's navigation header allows a user to browse through months and years:

![DateEditor - select date](../../images/dateeditor-selectdate-animation.gif)

In code, you can specify a date or read the currently selected date with the `DateEditor.DateTime` or `DateEditor.EditorValue` property. These properties are in sync. They differ in the value type: the `DateTime` property is of the nullable `System.DateTime` type, while the `EditorValue` property is of the `object` type as in all Eremex editors.

## Customize the Dropdown Calendar

The following properties allow you to set up a `DateEditor`'s calendar:

- `ShowToday` — Gets or sets whether to highlight the Today's date in the calendar. 
- `NullValueButtonPosition` — Gets or sets whether the (_'x'_) (clear value) button is visible. 
- `MinValue` — Specifies the minimum allowed date. The `MinValue` and `MaxValue` properties allow you to specify the range of values displayed in the calendar.
- `MaxValue` — Specifies the maximum allowed date.

<!--TODO
`ShowToday` — `HighlightTodayDate`?
`NullValueButtonPosition` — `ShowClearButton`? 
-->

You can also handle the `PopupOpened` event to perform additional customizations of the dropdown calendar. In a `PopupOpened` event handler, the calendar object can be accessed using the `DateEditor.PopupContent` property. Typecast this property to a `CalendarControl` class object to modify its properties. See the following example: [Example - Enable the Year View When the Calendar is Opened](#example-enable-the-year-view-when-the-calendar-is-opened)




### Example - How to create a DateEditor

The following example defines a DateEditor, sets the initial value and specifies the allowed date range.

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

## Specify the Value's Display Format

Use the `DisplayFormatString` property to set the display format for the date/time value displayed in the edit box.

## Prevent Popups in Read-only Editors

In read-only mode, the default behavior of any popup editor is to allow users to open the editor's dropdown. However, they cannot modify values through either the edit box or dropdown. To disable popups for read-only editors, set the `ShowPopupIfReadOnly` property to `false`.

## Prevent Popups From Opening and Closing

You can handle the following inherited events to cancel popup opening and closing operations:

- `PopupEditor.PopupOpening` — Fires when a popup is about to be created. 
- `PopupEditor.PopupClosing` — Fires when the popup is about to be closed. 

These events provide the `e.Cancel` parameter. Set it to `true` to cancel the current operation.

## Customize the Popup When It Appears

Handle the following inherited event to modify the popup or its nested controls:

- `PopupEditor.PopupOpened` — Fires after the popup has been created and immediately before it is displayed. This is a notification event. It does not allow you to cancel popup opening. Handle the `PopupOpened` event to customize the popup or its child controls.

When handling the `PopupEditor.PopupOpened` event, use the editor's `PopupContent` property to safely access the control inside the editor's popup. The `PopupOpened` event ensures that the popup control exists when you access it. For the DateEditor control, the `PopupContent` property returns an instance of the `CalendarControl` class. 

### Example - Enable the Year View When the Calendar is Opened

This example shows how to set a DateEditor's dropdown calendar to the Year view on opening.

![dateeditor-popupopened-example](../../images/dateeditor-popupopened-example.png)

The `DateEditor` class does not provide a public property to change the current view of its calendar. However, the embedded calendar (a `CalendarControl` object) exposes a public property called `DisplayMode`. This property specifies the calendar's view mode (`Month`, `Year`, or `Decade`).

This example handles the `PopupOpened` event to access the embedded calendar when it is created. The handler typecasts the `DateEditor.PopupContent` property to a `CalendarControl` object, and then sets the `CalendarControl.DisplayMode` property  to `Year`.

``` cs
using Eremex.AvaloniaUI.Controls.Editors;

dateEditor1.PopupOpened += DateEditor_PopupOpened;

private void DateEditor_PopupOpened(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    DateEditor editor = sender as DateEditor;
    (editor.PopupContent as CalendarControl).DisplayMode = CalendarMode.Year;
}
```

## Respond to Popup Closing

Use the following inherited event to perform actions after the popup has been closed:

- `PopupEditor.PopupClosed` — Fires immediately after the popup has been closed. This is a notification event. It does not allow you to cancel popup closing.
