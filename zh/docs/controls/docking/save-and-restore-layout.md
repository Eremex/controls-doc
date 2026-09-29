---
title: 保存和恢复面板布局
order: 50000
seealso: []
---

# 保存和恢复面板布局

Dock Manager 允许您保存停靠面板和文档的布局，并在之后恢复该布局。使用 `DockManager.SaveLayout` 和 `DockManager.RestoreLayout` 方法进行布局的序列化和反序列化。

所有面板和文档都必须具有唯一的名称，您可以通过 `Name` 属性指定该名称。唯一的名称可确保正确识别和序列化 Docking 元素。

``` xml
<mxd:DockGroup Orientation="Horizontal" DockHeight="*">
    <mxd:DockPane Name="dockPaneErrors" Header="Error List"/>
    <mxd:DockPane Name="dockPaneOutput" Header="Output"/>
</mxd:DockGroup>
```

`DockManager.SaveLayout` 方法按原样使用指定的流——在保存布局之前，它既不会清空该流，也不会更改流的当前位置。


## 示例

以下示例展示了如何将 Docking 元素的布局保存到文件中，并恢复已保存的布局。

``` cs
string fileName = "docking_layout.xml";

private void BtnSave_Click(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    using (var stream = new FileStream(fileName, FileMode.Create, FileAccess.Write))
    {
        dockManager1.SaveLayout(stream);
    }
}

private void BtnRestore_Click(object? sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    if (!File.Exists(fileName)) return;
    using (FileStream fileStream = File.OpenRead(fileName))
    {
        dockManager1.RestoreLayout(fileStream);
    }
}
```


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
