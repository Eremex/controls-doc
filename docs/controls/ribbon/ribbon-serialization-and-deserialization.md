---
title: Ribbon Serialization and Deserialization
order: 300
seealso: []
---

# Ribbon Serialization and Deserialization

End-users can use context menus to add commands to the [Quick Access Toolbar](quick-access-toolbar.md) and remove commands from it at runtime.

![ribbon-qat-add-items-menu](../../images/ribbon-qat-add-items-menu.png) 

![ribbon-qat-remove-items-menu](../../images/ribbon-qat-remove-items-menu.png)

The layout of commands in the Quick Access Toolbar can be saved to a stream, and loaded from it later (for instance, the next time your application runs). To do this, use the following layout serialization and deserialization methods:

- [`RibbonControl.SaveLayout`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonControl/SaveLayout.md) — Saves the layout of ribbon items in the Quick Access Toolbar to a stream.
- [`RibbonControl.RestoreLayout`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonControl/RestoreLayout.md) — Reads the previously saved layout from a stream and applies it to the Quick Access Toolbar.

!!! note

    All ribbon items must have unique names, which you can specify with the `Name` property (or alternatively, with the `SerializationName` property). Unique names ensure correct identification and serialization of ribbon items.

``` xml
<mxb:ToolbarButtonItem Name="btnNew" .../>
```

The following example shows how you can save and restore the layout of ribbon items to/from a file.

``` cs
string fileName = "ribbon_layout.xml";
private void BtnSave_Click(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    using (var stream = new FileStream(fileName, FileMode.Create, FileAccess.Write))
    {
        ribbon.SaveLayout(stream);
    }
}

private void BtnLoad_Click(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    if (!File.Exists(fileName)) return;
    using (FileStream fileStream = File.OpenRead(fileName))
    {
        ribbon.RestoreLayout(fileStream);
    }
}
```