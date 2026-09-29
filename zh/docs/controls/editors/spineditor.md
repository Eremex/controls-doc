---
title: SpinEditor
order: 102000
seealso: []
---

# SpinEditor

`SpinEditor` 是一个数值编辑器，带有内置微调按钮，用于按特定值（增量）增加和减少数字。用户可以通过单击这些按钮或按键盘上的向上和向下箭头来增加和减少数字。

![spineditor](../../images/spineditor.png)

control的主要特点包括：

- 内置微调按钮允许用户增加和减少值。
- 限制可用值范围。
- 自定义增量值。
- 在编辑框中显示自定义值前缀和后缀。

## 获取和设置编辑器的值

使用 `SpinEditor.Value` 属性返回并指定编辑器的数值。您还可以将 `EditorValue` 属性用于相同目的。这些属性是同步的。它们的不同之处在于值类型：`Value` 属性是十进制类型，而 `EditorValue` 属性是 `object` 类型，与所有 Eremex 编辑器一样。

另请参阅：[Increase and Decrease a Value in Code](#increase-and-decrease-a-value-in-code)。

## 设置

下面主要设置help you、`SpinEditor`、control的属性：

- `SpinEditor.Minimum` — 编辑器的最小值。
- `SpinEditor.Maximum` — 编辑器的最大值。
- `SpinEditor.Increment` — 当用户单击微调按钮或按向上和向下箭头键时编辑器的值增加或减少的值。
- `SpinEditor.ShowEditorButtons` — 指定是否显示内置微调按钮。

### 示例 - 如何创建 SpinEditor

以下示例初始化 SpinEditor 控件。

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:SpinEditor x:Name="SpinEditor" Width="200" 
    Value="7"
    Maximum="15"
    Minimum="1"
    Increment="1"
    />
```


## 显示值前缀和后缀

使用 `SpinEditor.Prefix` 和 `SpinEditor.Suffix` 属性指定在数值之前和之后显示的文本。用户无法编辑此文本。

### 示例 - 如何为 SpinEditor 的值指定前缀和后缀

以下示例将 `SpinEditor.Prefix` 和 `SpinEditor.Suffix` 属性用于 display text 之前和之后的编辑器值。

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:SpinEditor x:Name="SpinEditor1" Width="200" 
    Value="8.5"
    Maximum="35"
    Minimum="2"
    Increment="0.5"
    Prefix="V=" Suffix="m/s"
    />
```

## 增加和减少代码中的值

`SpinEditor.IncreaseCommand` 和 `SpinEditor.DecreaseCommand` 命令通过 increment value (`SpinEditor.Increment`) 增加和减少编辑器的值。

<!--TODO
Check:
The `SpinEditor.IncreaseCommand` and `SpinEditor.DecreaseCommand` commands increase and decrease the editor's value by the increment value (`SpinEditor.Increment`).
-->

您还可以使用 `SpinEditor.Value` 属性直接更改编辑器的值。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
