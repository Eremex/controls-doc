---
title: CheckEditor
order: 116000
seealso: []
---

# CheckEditor

`CheckEditor` 控件显示一个复选框，用户可以通过鼠标和键盘来切换其状态。在默认模式下，编辑器支持两种选中状态（选中和未选中）。您可以在需要时启用不确定状态。

![checkeditor](../../images/checkeditor.png)

该控件的主要功能包括：

- 您可以在两种或三种选中状态之间进行选择。
- 在复选框旁边显示标签文本。
- 用户可以使用鼠标和键盘切换控件。
- 验证机制会修改控件的外观，以向用户提示错误。

## 指定选中状态

用户可以使用鼠标切换 CheckEditor。如果编辑器处于焦点状态，用户可以按键盘上的空格键或回车键来更改选中状态。

在代码中，您可以通过 `CheckEditor.IsChecked` 或 `CheckEditor.EditorValue` 属性指定或读取当前的选中状态。这些属性是同步的。它们的区别在于值类型：`IsChecked` 属性是可为 null 的 `bool` 类型，而 `EditorValue` 属性与所有 Eremex 编辑器一样是 `object` 类型。

## 显示文本

`CheckEditor` 控件可以在复选框右侧显示文本。使用 `Content` 属性来指定该文本。

### 示例 - 如何创建 CheckEditor

以下示例定义了一个 `CheckEditor` 对象，用于控制 TreeList 控件的 Enabled 状态。如果复选框未选中，用户将无法编辑 TreeList 的数据。

![checkeditor-sample](../../images/checkeditor-sample.png)

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"

<mxe:CheckEditor IsChecked="{Binding IsEnabled, ElementName=treeList1}" Content="Edit Data"/>

<mxtl:TreeListControl Name="treeList1">...</mxtl:TreeListControl>
```

## 启用三种状态

启用 `IsThreeState` 属性，以允许编辑器具有三种状态。 
连续切换编辑器会在选中、不确定和未选中状态之间循环。

在不确定状态下，`CheckEditor.IsChecked` 和 `CheckEditor.EditorValue` 属性返回 `null`。


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
</content>
