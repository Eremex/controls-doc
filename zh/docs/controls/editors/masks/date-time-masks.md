---
title: 日期时间掩码
order: 900
seealso: []
---

# 日期时间掩码 {#date-time-masks}

[`DateTime`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/DateTime.md) 掩码类型允许用户按照指定的输入掩码在编辑器中输入日期时间值。输入掩码还可用于在显示模式下（文本编辑未激活时）格式化日期时间值。[`DateEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md) 控件默认启用 [`DateTime`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/DateTime.md) 掩码类型。要为其他文本编辑器启用此掩码类型，请将编辑器的 [`TextEditor.MaskType`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskType.md) 属性设置为 [`DateTime`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor/DateTime.md)。

使用编辑器的 [`Mask`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Mask.md) 属性指定输入掩码。输入掩码是一个字符串，它定义了输入或格式化日期时间值所依据的模式。

当前区域性会影响大多数日期时间掩码。例如，区域性定义了星期和月份的显示名称。您可以使用 [`TextEditor.MaskCulture`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskCulture.md) 属性为掩码强制指定特定的区域性。

Eremex 编辑器支持标准日期时间掩码和自定义日期时间掩码。

## 标准掩码 {#standard-masks}

Eremex 编辑器支持的标准日期时间掩码与 .NET 中用于格式化值的最常用[标准日期和时间格式](https://learn.microsoft.com/zh-cn/dotnet/standard/base-types/standard-date-and-time-format-strings)相对应。

### 示例 {#example}

以下示例将 `d` 掩码应用于 [`DateEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md)。此掩码按照系统的短日期模式格式化编辑值。

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:DateEditor x:Name="DateEditor" Mask="d"/>
```

![dateeditor-mask-d-example](../../../images/dateeditor-mask-d-example.png)

### 标准掩码说明符 {#standard-mask-specifiers}

标准日期时间掩码由一个标准掩码说明符组成。下表列出了可用的标准掩码说明符。

| 掩码说明符 | 说明 | 示例 (ru-Ru) |
|---|---|---|
| `d` | 短日期模式。<br><br> 请参阅 `CultureInfo.DateTimeFormat.ShortDatePattern` 属性。 | "05.07.2026" |
| `D` | 长日期模式。<br><br> 请参阅 `CultureInfo.DateTimeFormat.LongDatePattern` 属性。 | "воскресенье, 5 июля 2026 г." |
| `t` | 短时间模式。<br><br> 请参阅 `CultureInfo.DateTimeFormat.ShortTimePattern` 属性。 | "13:05" |
| `T` | 长时间模式。<br><br> 请参阅 `CultureInfo.DateTimeFormat.LongTimePattern` 属性。 | "13:05:17" |
| `f` | 完整日期时间模式（短时间）。<br><br> 该掩码组合了长日期模式和短时间模式，中间用空格分隔。 | "пятница, 23 января 2026 г. 18:15" |
| `F` | 完整日期时间模式（长时间）。<br><br> 请参阅 `CultureInfo.DateTimeFormat.FullDateTimePattern` 属性。 | "пятница, 23 января 2026 г. 18:15:21" |
| `g` | 常规日期时间模式（短时间）。<br><br> 该掩码组合了短日期模式和短时间模式，中间用空格分隔。 | "30.09.2025 19:35" |
| `G` | 常规日期时间模式（长时间）。<br><br> 该掩码组合了短日期模式和长时间模式，中间用空格分隔。 | "30.09.2025 19:35:07" |
| `M` 或 `m` | 月日模式。<br><br> 请参阅 `CultureInfo.DateTimeFormat.MonthDayPattern` 属性。 | "12 августа" |
| `R` 或 `r` | RFC1123 模式。<br><br> 请参阅 `CultureInfo.DateTimeFormat.RFC1123Pattern` 属性。 | "ср, 12 авг. 2026 06:19:57 GMT" |
| `s` | 可排序的日期时间模式，符合 ISO 8601。<br><br> 请参阅 `CultureInfo.DateTimeFormat.SortableDateTimePattern` 属性。 | "2025-09-18T11:57:33" |
| `u` | 通用可排序日期时间模式。<br><br> 请参阅 `CultureInfo.DateTimeFormat.UniversalSortableDateTimePattern` 属性。 | "2025-09-18 11:57:33Z" |
| `Y` 或 `y` | 年月模式。<br><br> 请参阅 `CultureInfo.DateTimeFormat.YearMonthPattern` 属性。 | "июль 2026 г." |

## 自定义掩码 {#custom-masks}

如果标准掩码无法满足您的特定需求，可以创建自定义掩码。自定义掩码由一个或多个自定义掩码说明符组成。

### 示例 {#example_1}

以下示例将 `'DATE:' yyyy MMMM dd, 'TIME:' HH:mm` 掩码应用于 [`DateEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md)。此掩码允许用户输入日期时间值的日期部分和时间部分。该掩码还会显示静态（只读）字符串 `DATE` 和 `TIME`。

![dateeditor-custommask-example](../../../images/dateeditor-custommask-example.png)

### 自定义掩码说明符 {#custom-mask-specifiers}

下表列出了支持的自定义掩码说明符。

| 掩码说明符 | 说明 | 示例 |
|---|---|---|
| `d` | 月份中的日期 (1,2...31)。<br><br> 使用 `%d` 掩码说明符可单独显示月份中的日期。否则，单独使用的 `d` 说明符会被解释为短日期模式。 | 2026-07-08T15:11:35 &rarr; "8" |
| `dd` | 月份中的日期 (01,02...31)。 | 2026-07-08T15:11:35 &rarr; "08" |
| `ddd` | 只读的星期缩写名称。 | 2026-07-08T15:11:35 &rarr; "ср" |
| `dddd` | 只读的星期完整名称。 | 2026-07-08T15:11:35 &rarr; "среда" |
| `F` 或 `f` <br><br> `FF` 或 `ff` <br> `FFF` 或 `fff` <br> `FFFF` 或 `ffff` <br> `FFFFF` 或 `fffff` <br> `FFFFFF` 或 `ffffff` <br> `FFFFFFF` 或 `fffffff` <br>  | 以 1、2...7 位数字表示的秒的小数部分。<br><br> 使用 `%F` 或 `%f` 掩码说明符可单独显示十分之一秒。否则，单独使用的 `f`/`F` 说明符会被解释为完整日期时间模式。 | 2026-07-08T15:11:35.249850("fff") &rarr; 249 |
| `s` | 秒 (0,1..59)。<br><br> 使用 `%s` 掩码说明符可单独显示秒部分。否则，单独使用的 `s` 说明符会被解释为可排序的日期时间模式。 | 2030-02-07T01:04:08 &rarr; "8" |
| `ss` | 秒 (00,01..59)。 | 2030-02-07T01:04:08 &rarr; "08" |
| `h` | 小时，采用 12 小时制 (1..12)。 | 2030-02-07T01:04:08 &rarr; "1" |
| `hh` | 小时，采用 12 小时制 (01,02..12)。 | 2030-02-07T01:04:08 &rarr; "01" |
| `H` | 小时，采用 24 小时制 (1..23)。 | 2030-02-07T01:04:08 &rarr; "1" <br><br> 2029-10-04T14:01:02 &rarr; "14" |
| `HH` | 小时，采用 24 小时制 (01,02..23)。 | 2030-02-07T01:04:08 &rarr; "01" <br><br> 2029-10-04T14:01:02 &rarr; "14" |
| `m` | 分钟 (0..59)。<br><br> 使用 `%m` 掩码说明符可单独显示分钟部分。否则，单独使用的 `m` 说明符会被解释为月日模式。 | 2030-02-07T01:04:08 &rarr; "4" |
| `mm` | 分钟 (00,01..59)。 | 2030-02-07T01:04:08 &rarr; "04" |
| `M` | 月份数字 (1..12)。 | 2030-02-07T01:04:08 &rarr; "2" |
| `MM` | 月份数字 (01,02..12)。 | 2030-02-07T01:04:08 &rarr; "02" |
| `MMM` | 月份的缩写名称。 | 2030-02-07T01:04:08 &rarr; "февр." |
| `MMMM` | 月份的完整名称。 | 2030-02-07T01:04:08 &rarr; "февраль" |
| `y` | 年份的后两位数字 (0-99)。<br><br> 使用 `%y` 掩码说明符可单独显示年份。否则，单独使用的 `y` 说明符会被解释为年月模式。 | 2001-01-08T09:02:07 &rarr; "1" |
| `yy` | 年份的后两位数字 (00-99)。 | 2001-01-08T09:02:07 &rarr; "01" |
| `yyyy` | 四位数字表示的年份。 | 2001-01-08T09:02:07 &rarr; "2001" |
| `g` 或 `gg` | 时期或纪元。 | 2001-01-08T09:02:07 &rarr; "н. э." |
| `t` | `AM/PM` 指示符的第一个字母。<br><br> 使用 `%t` 掩码说明符可单独显示 `AM/PM` 指示符的第一个字母。否则，单独使用的 `t` 说明符会被解释为短时间模式。 | 2001-01-08T09:02:07 &rarr; "A" |
| `tt` | `AM/PM` 指示符。 | 2001-01-08T09:02:07 &rarr; "AM" |
| `z` | 系统当前时间相对于 UTC 的小时偏移量，不带前导零。 | 2001-01-08T09:02:07 &rarr; "+3" |
| `zz` | 系统当前时间相对于 UTC 的小时偏移量，个位数值带前导零。 | 2001-01-08T09:02:07 &rarr; "+03" |
| `zzzz` | 系统当前时间相对于 UTC 的小时和分钟偏移量。 | 2001-01-08T09:02:07 &rarr; "+03:00" |
| `:` | 时间分隔符。<br><br> 请参阅 `CultureInfo.DateTimeFormat.TimeSeparator` 属性。 | 2001-01-08T09:02:07 (HH:mm) &rarr; "09:02" |
| `/` | 日期分隔符。<br><br> 请参阅 `CultureInfo.DateTimeFormat.DateSeparator` 属性。 | 2001-01-08T09:02:07 (yyyy/MM/dd) &rarr; "2001.01.08" |
| `\` | 转义字符。转义字符后面的字符会被解释为文本字面量，而不是掩码说明符。使用 "&bsol;&bsol;" 可插入反斜杠字面量。 | 2001-01-08T09:02:07(\t\m\: HH:mm) &rarr; "tm: 09:02" |
| `'`_string_ `'` <br> `"`_string_ `"` | 用单引号或双引号括起来的字符串按原样以只读方式显示。此字符串不会存储在编辑器的编辑值中。 | 2001-01-08T09:02:07("время:" HH:mm) &rarr; "время: 09:02" |
| 所有其他字符 | 这些字符按原样以只读方式显示，不会存储在编辑器的编辑值中。 | 2001-01-08T09:02:07(\Mn. № MM) &rarr; "Mn. № 01" |


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
