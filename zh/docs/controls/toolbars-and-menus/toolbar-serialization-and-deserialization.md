---
title: 工具栏序列化和反序列化
order: 10000
seealso: []
---

# 工具栏序列化和反序列化

用户可以在运行时自定义工具栏的layout。参见 [Runtime Toolbar Customization](toolbars.md#runtime-toolbar-customization)。

工具栏的 layout（包括工具栏命令的 layout）可以保存到流中，并在以后（例如，应用程序下次运行时）从中加载。为此，请使用以下 layout 序列化和反序列化方法：

- `ToolbarManager.SaveLayout` — 将工具栏 layout 保存到流中。
- `ToolbarManager.RestoreLayout` — 从流中加载之前保存的 layout。

!!!笔记

所有工具栏和工具栏项必须具有唯一的名称，您可以使用 `Name` 属性指定该名称。唯一的名称确保工具栏及其项目的正确识别和序列化。

``` xml
<mxb:Toolbar x:Name="FileToolbar" ...>

<mxb:ToolbarButtonItem Name="btnNew" .../>
```

以下示例显示如何将工具栏 layout 保存到文件或从文件恢复。

``` cs
string fileName = "bars_layout.xml";
private void BtnSave_Click(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    using (var stream = new FileStream(fileName, FileMode.Create, FileAccess.Write))
    {
        toolbarManager1.SaveLayout(stream);
    }
}

private void BtnLoad_Click(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    if (!File.Exists(fileName)) return;
    using (FileStream fileStream = File.OpenRead(fileName))
    {
        toolbarManager1.RestoreLayout(fileStream);
    }
}
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
