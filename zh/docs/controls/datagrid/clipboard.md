---
title: 剪贴板
order: 1200
seealso: []
---

# 剪贴板

DataGrid 控件现已支持使用 CTRL+C 快捷键将选中的行复制到剪贴板。

在代码中,您可以使用 `CopyToClipboardAsync` 方法复制选中的行。该方法是异步的——它会立即返回一个 `Task` 对象,而不会等待复制操作完成。
异步方法不会阻塞 UI 线程。

- `CopyToClipboardAsync` 方法会复制所选行单元格的显示文本。在单选模式下,系统会复制获得焦点的行;在多选模式下,系统会复制所有选中的行。
- 如果选中了某个分组行,该行也会被一并复制到剪贴板。嵌套在所选分组行内的行不会被复制,除非它们本身也被选中。
- 默认情况下,列标题会被复制到剪贴板。将 `DataGridControl.ClipboardCopyHeaders` 选项设置为 false,可以阻止复制列标题。
- 列标题和单元格值在剪贴板中以制表符(TAB)分隔。


## Related API

- `DataControlBase.SelectionMode` — 允许您启用多行选择。
- `DataControlBase.SelectedItems` — 指定与所选行对应的数据(业务)对象集合。
- `DataGridControl.GetCellDisplayText` — 返回由行和列(或字段名称)寻址的特定单元格的显示文本。
- `DataGridControl.ClipboardCopyHeaders` — 获取或设置是否将列标题复制到剪贴板。


<!-- TODO
CTRL+C ??
example for CTRL+C ?
 -->

 <!-- TODO
 create Clipboard topic for TreeList
  -->

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
