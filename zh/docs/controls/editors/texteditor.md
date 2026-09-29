---
title: TextEditor
order: 120000
seealso: []
---

# TextEditor

`TextEditor` 控件提供基本的文本编辑功能。它支持掩码，允许你限制用户输入并对值进行格式化。

![texteditor](../../images/texteditor.png)

该控件的主要功能包括：

- 支持单行和多行文本。
- 文本换行。
- 使用掩码指定数据输入的模式。
- 当编辑器未获得焦点时，使用掩码格式化值。
- 文本选择。
- 水印

## 指定文本并自定义文本选项

`TextEditor.EditorValue` 属性指定编辑器的文本。如果文本包含 _NewLine_ 字符，编辑器会将文本显示为多行。

### 文本换行

`TextEditor.TextWrapping` 属性允许你在编辑器右边缘启用自动文本换行。将该属性设置为 `Avalonia.Media.TextWrapping.Wrap` 值，即可启用常规文本换行模式。

### 输入时接受 _Tab_ 和 _Enter_ 键

用户可以按下 _Tab_ 和 _Enter_ 键在文本中插入 _Tab_ 和 _Return_ 字符。你可以使用以下选项更改此行为：

- `TextEditor.AcceptsReturn` — 指定按下 _Enter_ 键时是否插入 _NewLine_ 字符。如果该属性被禁用，编辑器会忽略 _Enter_ 键。
- `TextEditor.AcceptsTab` — 指定按下 _Tab_ 键时是否插入制表符。如果该属性被禁用，按下 _Tab_ 键时焦点会移动到 Tab 顺序中的下一个控件。

## 掩码

应用于文本编辑器的[掩码](masks/index.md)会引导用户按照指定的模式输入值。默认情况下，[DateEditor](dateeditor.md) 和 [SpinEditor](spineditor.md) 控件启用了掩码输入，而其他文本编辑器默认禁用该功能。

要启用掩码输入，请执行以下操作：

- 将 `TextEditor.MaskType` 属性设置为某个掩码类型。
- 将 `TextEditor.Mask` 属性设置为掩码字符串。

### 掩码类型

`TextEditor.MaskType` 属性允许你从以下选项中选择掩码模式：

- `MaskType.Numeric` — 专为接受数值而设计的掩码模式。
- `MaskType.DateTime` — 专为接受日期时间值而设计的掩码模式。
- `MaskType.None` — 禁用掩码输入。

### 掩码字符串

使用 `TextEditor.Mask` 属性设置指定掩码的字符串。掩码由特定于所选掩码类型的掩码说明符组成。

有关更多信息，请参见以下主题：

- [掩码](masks/index.md)
- [数字掩码](masks/numeric-masks.md)
- [日期时间掩码](masks/date-time-masks.md)

#### 示例 - 允许在文本编辑器中输入整数值

以下代码应用“_d_”数字掩码，将 TextEditor 中的数据输入限制为整数值。

![texteditor-numericmask-d](../../images/texteditor-numericmask-d.png)

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:TextEditor Name="textEditor1" MaskType="Numeric" Mask="d" 
 HorizontalContentAlignment="Right"/>
```

### 将掩码用作显示格式

`TextEditor.Mask` 属性指定的掩码可用于在显示模式下（即文本编辑未激活时）格式化编辑器的值。此设置由 `TextEditor.MaskUseAsDisplayFormat` 属性指定。该属性的默认值为 `true`。

### 掩码区域性设置

许多掩码依赖于当前的区域性。例如，数字掩码的小数分隔符在不同区域性下是不同的。日期时间值会使用特定区域性的模式，以及本地化的星期和月份名称进行格式化。

`TextEditor.MaskCulture` 属性允许你设置掩码所使用的区域性。如果未设置该属性，则使用应用程序的默认区域性。

#### 示例 

以下代码设置“c”数字掩码，用于在文本编辑器中输入货币值，并将该掩码应用为 _中文（简体）_ 区域性。

![texteditor-mask-currency-chinese](../../images/texteditor-mask-currency-chinese.png)

``` csharp
textEditor1.EditorValue = 12.34567;
textEditor1.MaskType = Eremex.AvaloniaUI.Controls.Editors.MaskType.Numeric;
textEditor1.MaskCulture = new CultureInfo("zh-CN");
textEditor1.Mask = "c";
```

## 文本选择

用户可以使用鼠标和键盘选择文本。

要在代码中选择部分文本或清除选择，请使用以下 API：

- `TextEditor.SelectionStart` — 文本选择起始字符的从零开始的索引。
- `TextEditor.SelectionEnd` — 文本选择结束字符的从零开始的索引。
- `TextEditor.SelectAll` — 选中全部文本。
- `TextEditor.ClearSelection` — 取消选中已选中的文本。

## 水印

`TextEditor` 控件及其派生类支持水印。水印是当编辑器的值为空或为 null 时显示的灰色提示文字。

![texteditor-watermark](../../images/texteditor-watermark.png)

使用 `TextEditor.Watermark` 属性指定水印。

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:TextEditor Name="textEditor1" Watermark="Type to search"/>
```


## 另请参阅

- [如何创建密码文本框](examples/How-to-create-a-password-text-box.md)


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
