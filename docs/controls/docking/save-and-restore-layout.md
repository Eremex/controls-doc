---
title: Save and Restore the Layout of Panels
order: 50000
seealso: []
---

# Save and Restore the Layout of Panels

Dock Manager allows you to save the layout of dock panels and documents and then restore it later. Use the [`DockManager.SaveLayout`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/SaveLayout.md) and [`DockManager.RestoreLayout`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/RestoreLayout.md) methods for the layout serialization and deserialization.

All panels and documents must have unique names, which you can specify with the `Name` property. Unique names ensure correct identification and serialization of dock items.

``` xml
<mxd:DockGroup Orientation="Horizontal" DockHeight="*">
    <mxd:DockPane Name="dockPaneErrors" Header="Error List"/>
    <mxd:DockPane Name="dockPaneOutput" Header="Output"/>
</mxd:DockGroup>
```

The [`DockManager.SaveLayout`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/SaveLayout.md) method uses the specified stream as is - it neither clears the stream nor changes the current stream position before saving the layout.


## Example

The following example shows how you can save the layout of dock items to a file, and restore the saved layout. 

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