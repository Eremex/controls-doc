---
title: Masks
order: 1000
seealso: []
---

# Masks

掩码允许您限制文本编辑器中的数据输入。它们还可以用于在显示模式下格式化编辑器值（当编辑器没有焦点时）。

要启用屏蔽输入，请执行以下操作：

- 将编辑器的 `TextEditor.MaskType` 属性设置为掩码类型。
- 将编辑器的 `TextEditor.Mask` 属性设置为特定掩码。

支持以下掩码类型：

- `Numeric` — 专为接受数值而设计的掩码模式。
- `DateTime` — 专为接受日期时间值而设计的掩码模式。

以下主题为您提供有关支持的遮罩模式和遮罩的更多详细信息：

- [Numeric Masks](numeric-masks.md)
- [Date-Time Masks](date-time-masks.md)

## 使用遮罩作为显示格式

`TextEditor.Mask` 属性指定的掩码可用于在显示模式下格式化编辑器的值（当文本编辑未激活时）。 `TextEditor.MaskUseAsDisplayFormat` 属性指定此设置。该属性的默认值为 `true`。

## 掩模文化设置

许多面具都依赖于当前的文化。例如，数字掩码的小数分隔符在不同的文化中是不同的。日期时间值使用特定于文化的模式以及星期几和月份的本地化名称进行格式化。

`TextEditor.MaskCulture` 属性允许您设置掩码使用的区域性。如果未设置此属性，则使用应用程序的默认区域性。

### 例子

以下代码设置“c”数字掩码以在文本编辑器中输入货币值，并将_中文（简体）_ 区域性应用于该掩码。

![texteditor-mask-currency-chinese](../../../images/texteditor-mask-currency-chinese.png)

``` csharp
textEditor1.EditorValue = 12.34567;
textEditor1.MaskType = Eremex.AvaloniaUI.Controls.Editors.MaskType.Numeric;
textEditor1.MaskCulture = new CultureInfo("zh-CN");
textEditor1.Mask = "c";
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
