---
title: Toolbar Serialization and Deserialization
order: 10000
seealso: []
---

# Toolbar Serialization and Deserialization

Users can customize the layout of toolbars at runtime. See [Runtime Toolbar Customization](toolbars.md#runtime-toolbar-customization).

The layout of toolbars (including the layout of toolbar commands) can be saved to a stream, and loaded from it later (for instance, the next time your application runs). To do this, use the following layout serialization and deserialization methods:

- `ToolbarManager.SaveLayout` — Saves the layout of toolbars to a stream.
- `ToolbarManager.RestoreLayout` — Loads the previously saved layout from a stream.

!!! note

    All toolbars and toolbar items must have unique names, which you can specify with the `Name` property. Unique names ensure correct identification and serialization of toolbars and their items.

``` xml
<mxb:Toolbar x:Name="FileToolbar" ...>

<mxb:ToolbarButtonItem Name="btnNew" .../>
```

The following example shows how you can save and restore the layout of toolbars to/from a file.

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