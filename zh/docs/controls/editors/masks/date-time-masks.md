---
title: 日期时间掩码
order: 900
seealso: []
---

# 日期时间掩码

`DateTime` 掩码类型允许用户根据指定的输入掩码在编辑器中输入日期时间值。输入掩码还可用于在显示模式下格式化日期时间值（当文本编辑未激活时）。 `DateEditor` control 默认启用 `DateTime` 掩码类型。要为其他文本编辑器启用此掩码类型，请将编辑器的 `TextEditor.MaskType` 属性设置为 `DateTime`。

使用编辑器的 `Mask` 属性指定输入掩码。输入掩码是一个字符串，它定义了输入或格式化日期时间值所依据的模式。

当前的文化影响大多数日期时间掩码。例如，区域性定义星期几和月份的显示名称。您可以使用 `TextEditor.MaskCulture` 属性将特定区域性强制分配给掩码。

Eremex 编辑器支持标准和自定义日期时间掩码。

## 标准口罩

Eremex 编辑器支持的标准日期时间掩码与可用于格式化 .NET 中的值的最常见 [standard date and time display formats](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings) 相匹配。

### 例子

以下示例将 `d` 掩码应用于 `DateEditor`。该掩码根据系统短日期模式格式化 the edit value。

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:DateEditor x:Name="DateEditor" Mask="d"/>
```

![dateeditor-mask-d-example](../../../images/dateeditor-mask-d-example.png)

### 标准掩码说明符

标准日期时间掩码由一个标准掩码说明符组成。下表显示了可用的标准掩码说明符。

|掩码说明符|描述 |示例 (ru-Ru) |
|---|---|---|
| `d` |短日期模式。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.ShortDatePattern` 属性。 | “2026 年 7 月 5 日”|
| `D` |长日期模式。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.LongDatePattern` 属性。 | “2026 年 5 月 5 日。” |
| `t` |短时间模式。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.ShortTimePattern` 属性。 | “13:05”|
| `T` |长时间模式。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.LongTimePattern` 属性。 | “13:05:17” |
| `f` |完整的日期时间模式（短时间）。 <br><br> 该掩码组合了长日期和短时间模式，并用空格字符分隔。  | “2026 年 23 月 18:15”|
| `F` |完整的日期时间模式（长时间）。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.FullDateTimePattern` 属性。 | “2026 年 23 月 18:15:21”|
| `g` |一般日期时间模式（短时间）。 <br><br> 该掩码组合了短日期和短时间模式，并用空格字符分隔。 | “2025 年 9 月 30 日 19:35” |
| `G` |一般日期时间模式（长时间）。 <br><br> 该掩码组合了短日期和长时间模式，并用空格字符分隔。  | “2025 年 9 月 30 日 19:35:07”|
| `M` 或 `m` |月日模式。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.MonthDayPattern` 属性。 | “12 августа”|
| `R` 或 `r` | RFC1123 模式。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.RFC1123Pattern` 属性。 | “2026 年 12 月 12 日 06:19:57 GMT”|
| `s` |可排序的日期时间模式；符合 ISO 8601。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.SortableDateTimePattern` 属性。 | “2025-09-18T11:57:33” |
| `u` |通用可排序日期时间模式。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.UniversalSortableDateTimePattern` 属性。 | “2025-09-18 11:57:33Z” |
| `Y` 或 `y` |年月模式。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.YearMonthPattern` 属性。 | “2026 年 г”。 |

## 定制面具

如果标准蒙版不能满足您的特定需求，您可以创建自定义蒙版。自定义掩码由一个或多个自定义掩码说明符组成。

### 例子

以下示例将 `'DATE:' yyyy MMMM dd, 'TIME:' HH:mm` 掩码应用于 `DateEditor`。此掩码允许用户输入日期时间值的日期和时间部分。该掩码还显示静态（只读）字符串 `DATE` 和 `TIME`。

![dateeditor-custommask-example](../../../images/dateeditor-custommask-example.png)

### 自定义掩码说明符

下表显示了支持的自定义掩码说明符。

|掩码说明符|描述 |示例|
|---|---|---|
| `d` |该月的某一天 (1,2...31)。 <br><br> 使用 `%d` 掩码说明符单独显示月份中的某一天。否则，单独使用的 `d` 说明符将被解释为短日期模式。 | 2026-07-08T15:11:35 &rarr; “8” |
| `dd` |该月的某一天 (01,02...31)。 | 2026-07-08T15:11:35 &rarr;“08”|
| `ddd` |星期几的只读缩写名称。 | 2026-07-08T15:11:35 &rarr;“ср” |
| `dddd` |星期几的只读全名。 | 2026-07-08T15:11:35 &rarr;“среда”|
| `F` 或 `f` <br><br> `FF` 或 `ff` <br> `FFF` 或 `fff` <br> `FFFF` 或 `ffff` <br> `FFFFF` 或`fffff` <br> `FFFFFF` 或 `ffffff` <br> `FFFFFFF` 或 `fffffff` <br> |以 1,2..7 数字表示的秒小数部分。 <br><br> 使用 `%F` 或 `%f` 掩码说明符单独显示十分之一秒。否则，单独使用的 `f`/`F` 说明符将被解释为完整的日期时间模式。 | 2026-07-08T15：11：35.249850（“fff”）&rarr; 249 |
| `s` |第二个 (0,1..59)。 <br><br> 使用 `%s` 掩码说明符单独显示秒部分。否则，单独使用的 `s` 说明符将被解释为可排序的日期时间模式。 | 2030-02-07T01:04:08 &rarr;“8”|
| `ss` |第二个（00,01..59）。 | 2030-02-07T01:04:08 &rarr;“08”|
| `h` |小时，使用 12 小时制 (1..12)。 | 2030-02-07T01:04:08 &rarr;“1”|
| `hh` |小时，使用 12 小时制 (01,02..12)。 | 2030-02-07T01:04:08 &rarr;“01”|
| `H` |小时，使用 24 小时制 (1..23)。 | 2030-02-07T01:04:08 &rarr;“1”<br><br> 2029-10-04T14:01:02 &rarr;“14”|
| `HH` |小时，采用 24 小时制 (01,02..23)。 | 2030-02-07T01:04:08 &rarr;“01”<br><br> 2029-10-04T14:01:02 &rarr;“14”|
| `m` |分钟 (0..59)。 <br><br> 使用 `%m` 掩码说明符单独显示分钟部分。否则，单独使用的 `m` 说明符将被解释为月日模式。 | 2030-02-07T01:04:08 &rarr;“4”|
| `mm` |分钟 (00,01..59)。 | 2030-02-07T01:04:08 &rarr;“04”|
| `M` |月份号 (1..12)。 | 2030-02-07T01:04:08 &rarr;“2”|
| `MM` |月份编号 (01,02..12)。 | 2030-02-07T01:04:08 &rarr;“02”|
| `MMM` |月份的缩写名称。 | 2030-02-07T01:04:08 &rarr;“февр。” |
| `MMMM` |月份的全名。 | 2030-02-07T01:04:08 &rarr;“февраль”|
| `y` |年份的最后两位数字 (0-99)。 <br><br> 使用 `%y` 掩码说明符单独显示年份。否则，单独使用的 `y` 说明符将被解释为年月模式。 | 2001-01-08T09:02:07 &rarr;“1”|
| `yy` |年份的最后两位数字 (00-99)。 | 2001-01-08T09:02:07 &rarr;“01”|
| `yyyy` |年份为四位数。 | 2001-01-08T09:02:07 &rarr;“2001”|
| `g` 或 `gg` |时期或时代。 | 2001-01-08T09:02:07 &rarr;“н.э.” |
| `t` | `AM/PM` 指示符的第一个字母。 <br><br> 使用 `%t` 掩码说明符单独显示 `AM/PM` 指示符的第一个字母。否则，单独使用的 `t` 说明符将被解释为短时间模式。 | 2001-01-08T09:02:07 &rarr; “A” |
| `tt` | `AM/PM` 指示符。 | 2001-01-08T09:02:07 &rarr;“上午”|
| `z` |系统当前时间相对于 UTC 的小时偏移量，不带前导零。 | 2001-01-08T09:02:07 &rarr;“+3”|
| `zz` |系统当前时间相对于 UTC 的小时偏移量，单位值前导零。 | 2001-01-08T09:02:07 &rarr;“+03”|
| `zzzz` |系统当前时间相对于 UTC 的小时和分钟偏移量。  | 2001-01-08T09:02:07 &rarr;“+03:00”|
| `:` |时间分隔符。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.TimeSeparator` 属性。 | 2001-01-08T09:02:07 (HH:mm) &rarr;“09:02”|
| `/` |日期分隔符。 <br><br> 请参阅 `CultureInfo.DateTimeFormat.DateSeparator` 属性。 | 2001-01-08T09:02:07（年/月/日）&rarr;“2001.01.08”|
| `\` |逃脱角色。转义字符后面的字符被解释为文字而不是掩码说明符。使用“&bsol;&bsol;”插入反斜杠字符作为文字。 | 2001-01-08T09:02:07(\t\m\: HH:mm) &rarr;“tm: 09:02”|
| `'`_string_ `'` <br> `"`_string_ `"` |用单引号或双引号括起来的字符串在只读模式下按原样显示。该字符串不存储在编辑器的编辑值中。 | 2001-01-08T09:02:07("время:" HH:mm) &rarr; "время: 09:02" |
|所有其他角色 |这些字符以只读模式按原样显示。它们不存储在编辑器的编辑值中。 | 2001-01-08T09:02:07(\Mn. № MM) &rarr;“Mn. № 01”|

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
