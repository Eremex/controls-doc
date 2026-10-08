---
title: Date-Time Masks
order: 900
seealso: []
---

# Date-Time Masks

The `DateTime` mask type allows users to enter date-time values in editors according to a specified input mask. The input mask can also be used to format date-time values in display mode (when text editing is not active). The [`DateEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md) control has the [`DateTime`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/DateTime.md) mask type enabled by default. To enable this mask type for other text editors, set the editor's [`TextEditor.MaskType`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskType.md) property to [`DateTime`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/DateTime.md).

Use the editor's [`Mask`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Mask.md) property to specify an input mask. The input mask is a string that defines a pattern according to which a date-time value is entered or formatted.

The current culture affects most date-time masks. For example, the culture defines display names for the days of the week and months. You can forcibly assign a specific culture to a mask using the [`TextEditor.MaskCulture`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskCulture.md) property.

Eremex editors support standard and custom date-time masks.

## Standard Masks

Standard date-time masks supported by Eremex editors match the most common [standard date and time display formats](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings) that you can use to format values in .NET. 

### Example

The following example applies the `d` mask to a [`DateEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md). This mask formats the edit value according to the system short date pattern.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:DateEditor x:Name="DateEditor" Mask="d"/>
```

![dateeditor-mask-d-example](../../../images/dateeditor-mask-d-example.png)

### Standard Mask Specifiers

A standard date-time mask consists of one standard mask specifier. The table below shows available standard mask specifiers. 

| Mask specifier | Description | Example (ru-Ru) |
|---|---|---|
| `d` | Short date pattern. <br><br> See the `CultureInfo.DateTimeFormat.ShortDatePattern` property. | "05.07.2026" |
| `D` | Long date pattern. <br><br> See the `CultureInfo.DateTimeFormat.LongDatePattern` property. | "воскресенье, 5 июля 2026 г." |
| `t` | Short time pattern. <br><br> See the `CultureInfo.DateTimeFormat.ShortTimePattern` property. | "13:05" |
| `T` | Long time pattern. <br><br> See the `CultureInfo.DateTimeFormat.LongTimePattern` property. | "13:05:17" |
| `f` | Full date-time pattern (short time). <br><br> The mask combines the long date and short time patterns, separated by the space character.  | "пятница, 23 января 2026 г. 18:15" |
| `F` | Full date-time pattern (long time). <br><br> See the `CultureInfo.DateTimeFormat.FullDateTimePattern` property. | "пятница, 23 января 2026 г. 18:15:21" |
| `g` | General date-time pattern (short time). <br><br> The mask combines the short date and short time patterns, separated by the space character. | "30.09.2025 19:35" |
| `G` | General date-time pattern (long time). <br><br> The mask combines the short date and long time patterns, separated by the space character.  | "30.09.2025 19:35:07" |
| `M` or `m` | Month day pattern. <br><br> See the `CultureInfo.DateTimeFormat.MonthDayPattern` property. | "12 августа" |
| `R` or `r` | RFC1123 pattern. <br><br> See the `CultureInfo.DateTimeFormat.RFC1123Pattern` property. | "ср, 12 авг. 2026 06:19:57 GMT" |
| `s` | Sortable date-time pattern; conforms to ISO 8601. <br><br> See the `CultureInfo.DateTimeFormat.SortableDateTimePattern` property. | "2025-09-18T11:57:33" |
| `u` | Universal sortable date-time pattern. <br><br> See the `CultureInfo.DateTimeFormat.UniversalSortableDateTimePattern` property. | "2025-09-18 11:57:33Z" |
| `Y` or `y` | Year month pattern. <br><br> See the `CultureInfo.DateTimeFormat.YearMonthPattern` property. | "июль 2026 г." |

## Custom Masks

You can create custom masks if the standard masks do not meet your specific needs. A custom mask consists of one or more custom mask specifiers.

### Example

The following example applies the `'DATE:' yyyy MMMM dd, 'TIME:' HH:mm` mask to a [`DateEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md). This mask allows users to enter the date and time portions of a date-time value. The mask also displays the static (read-only) strings `DATE` and `TIME`.

![dateeditor-custommask-example](../../../images/dateeditor-custommask-example.png)

### Custom Mask Specifiers

The following table shows supported custom mask specifiers.

| Mask specifier | Description | Example |
|---|---|---|
| `d` | The day of the month (1,2...31). <br><br> Use the `%d` mask specifier to display the day of the month alone. Otherwise, the `d` specifier used alone is interpreted as the short date pattern. | 2026-07-08T15:11:35 &rarr; "8" |
| `dd` | The day of the month (01,02...31). | 2026-07-08T15:11:35 &rarr; "08" |
| `ddd` | The read-only abbreviated name of the day of the week. | 2026-07-08T15:11:35 &rarr; "ср" |
| `dddd` | The read-only full name of the day of the week. | 2026-07-08T15:11:35 &rarr; "среда" |
| `F` or `f` <br><br> `FF` or `ff` <br> `FFF` or `fff` <br> `FFFF` or `ffff` <br> `FFFFF` or `fffff` <br> `FFFFFF` or `ffffff` <br> `FFFFFFF` or `fffffff` <br>  | Fractional seconds represented in 1,2..7 digits. <br><br> Use the `%F` or `%f` mask specifier to display the tenths of a second alone. Otherwise, the `f`/`F` specifier used alone is interpreted as the full date-time pattern. | 2026-07-08T15:11:35.249850("fff") &rarr; 249 |
| `s` | The second (0,1..59). <br><br> Use the `%s` mask specifier to display the seconds part alone. Otherwise, the `s` specifier used alone is interpreted as the sortable date-time pattern. | 2030-02-07T01:04:08 &rarr; "8" |
| `ss` | The second (00,01..59). | 2030-02-07T01:04:08 &rarr; "08" |
| `h` | The hour, using a 12-hour clock (1..12). | 2030-02-07T01:04:08 &rarr; "1" |
| `hh` | The hour, using a 12-hour clock (01,02..12). | 2030-02-07T01:04:08 &rarr; "01" |
| `H` | The hour, using a 24-hour clock (1..23). | 2030-02-07T01:04:08 &rarr; "1" <br><br> 2029-10-04T14:01:02 &rarr; "14" |
| `HH` | The hour, using a 24-hour clock (01,02..23). | 2030-02-07T01:04:08 &rarr; "01" <br><br> 2029-10-04T14:01:02 &rarr; "14" |
| `m` | The minute (0..59). <br><br> Use the `%m` mask specifier to display the minutes part alone. Otherwise, the `m` specifier used alone is interpreted as the month day pattern. | 2030-02-07T01:04:08 &rarr; "4" |
| `mm` | The minute (00,01..59). | 2030-02-07T01:04:08 &rarr; "04" |
| `M` | The month number (1..12). | 2030-02-07T01:04:08 &rarr; "2" |
| `MM` | The month number (01,02..12). | 2030-02-07T01:04:08 &rarr; "02" |
| `MMM` | The abbreviated name of the month. | 2030-02-07T01:04:08 &rarr; "февр." |
| `MMMM` | The full name of the month. | 2030-02-07T01:04:08 &rarr; "февраль" |
| `y` | The last two digits of the year (0-99). <br><br> Use the `%y` mask specifier to display the year alone. Otherwise, the `y` specifier used alone is interpreted as the year month pattern. | 2001-01-08T09:02:07 &rarr; "1" |
| `yy` | The last two digits of the year (00-99). | 2001-01-08T09:02:07 &rarr; "01" |
| `yyyy` | The year as a four-digit number. | 2001-01-08T09:02:07 &rarr; "2001" |
| `g` or `gg` | The period or era. | 2001-01-08T09:02:07 &rarr; "н. э." |
| `t` | The first letter of the `AM/PM` designator. <br><br> Use the `%t` mask specifier to display the first letter of the `AM/PM` designator alone. Otherwise, the `t` specifier used alone is interpreted as the short time pattern. | 2001-01-08T09:02:07 &rarr; "A" |
| `tt` | The `AM/PM` designator. | 2001-01-08T09:02:07 &rarr; "AM" |
| `z` | Hours offset of the system's current time from UTC, with no leading zeros. | 2001-01-08T09:02:07 &rarr; "+3" |
| `zz` | Hours offset of the system's current time from UTC, with a leading zero for a single-digit value. | 2001-01-08T09:02:07 &rarr; "+03" |
| `zzzz` | Hours and minutes offset of the system's current time from UTC.  | 2001-01-08T09:02:07 &rarr; "+03:00" |
| `:` | The time separator. <br><br> See the `CultureInfo.DateTimeFormat.TimeSeparator` property. | 2001-01-08T09:02:07 (HH:mm) &rarr; "09:02" |
| `/` | The date separator. <br><br> See the `CultureInfo.DateTimeFormat.DateSeparator` property. | 2001-01-08T09:02:07 (yyyy/MM/dd) &rarr; "2001.01.08" |
| `\` | Escape character. The character that follows the escape character is interpreted as a literal rather than as a mask specifier. Use "&bsol;&bsol;" to insert a backslash character as a literal. | 2001-01-08T09:02:07(\t\m\: HH:mm) &rarr; "tm: 09:02" |
| `'`_string_ `'` <br> `"`_string_ `"` | A string enclosed in single or double quotation marks is displayed as is, in read-only mode. This string is not stored in an editor's edit value. | 2001-01-08T09:02:07("время:" HH:mm) &rarr; "время: 09:02" |
| All other characters | These characters are displayed as is, in read-only mode. They are not stored in an editor's edit value. | 2001-01-08T09:02:07(\Mn. № MM) &rarr; "Mn. № 01" |

