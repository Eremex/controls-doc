---
title: HyperlinkEditor
order: 110000
seealso: []
---

# HyperlinkEditor

The `HyperlinkEditor` control displays a hyperlink that a user can click. The editor does not execute the link when it's touched. Instead, it raises an associated command that you can handle to process link clicks.

![hyperlink-editor](../../images/hyperlink-editor.png)

The editor's text is not editable by users.

## Specify a Display Hyperlink

Use the control's `EditorValue` property to specify the editor's display text. The editor underlines the text to imitate a hyperlink.

If no command is assigned to the editor (see below), a click on the displayed link has no effect.

## Process Hyperlink Clicks

Assign a command to the editor's `Command` property to handle clicks on the hyperlink. Use the `CommandParameter` to supply additional data to the command.

## Example

The following example defines a `HyperlinkEditor` that displays a link to a web page. A click on the link raises the _ShowWebPageCommand_ command. The link address to invoke is passed as the command's parameter.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:HyperlinkEditor EditorValue="https://www.w3.org" Command="{Binding ShowWebPageCommand}" 
                     CommandParameter="https://www.w3.org"/>
```

``` csharp
using CommunityToolkit.Mvvm.ComponentModel;
using System.Diagnostics;

public partial class HyperlinkEditorPageViewModel : ObservableObject
{
    [RelayCommand]
    public void ShowWebPage(string parameter)
    {
        try
        {
            Process.Start(new ProcessStartInfo(parameter) 
            { 
                UseShellExecute = true 
            });
        }
        catch { };
    }
}
```