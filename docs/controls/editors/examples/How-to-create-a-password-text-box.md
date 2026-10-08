---
title: How to create a password text box
order: 100
seealso: []
---

# How to create a password text box

This example shows how to mask user input with a password character (for example, '*'), and allow a user to reveal and hide the entered password with a button.

![texteditor-passwordchar](../../../images/texteditor-password.gif)

The [`TextEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) class currently does not contain the `PasswordChar` property. However, you can enable password mode for an internal text box (a `TextBox` control), which is embedded in the [`TextEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) control and provides the text editing functionality.

The following example creates the _PasswordBoxBehavior_ behavior which activates password mode for a text editor's internal text box (`TextBox`). The _PasswordBoxBehavior_ class exposes the `PasswordChar` and `ShowRevealButton` properties to specify the password mask character and the visibility of the password reveal button.

You need to add the `Avalonia.Xaml.Behaviors` NuGet package to your project to use behaviors.

``` cs
namespace DemoCenter.Views;

public class PasswordBoxBehavior : Avalonia.Xaml.Interactivity.Behavior<TextEditor>
{
    private const string revealButtonClassName = "revealPasswordButton";
    public char PasswordChar { get; set; } = '*';
    public bool ShowRevealButton { get; set; } = true;

    protected override void OnAttached()
    {
        base.OnAttached();
        if (AssociatedObject != null)
            AssociatedObject.Loaded += OnLoaded;
    }
    private void OnLoaded(object sender, RoutedEventArgs e)
    {
        var realEditor = AssociatedObject.FindVisualChild<TextBox>();
        if (realEditor == null)
            return;
        realEditor.PasswordChar = PasswordChar;
        if (ShowRevealButton)
            realEditor.Classes.Add(revealButtonClassName);
    }

    protected override void OnDetaching()
    {
        base.OnDetaching();
        if (AssociatedObject != null)
            AssociatedObject.Loaded -= OnLoaded;
    }
}
```

Attach the _PasswordBoxBehavior_ behavior to the [`TextEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) control in your project, as follows:

``` xml
xmlns:view="using:DemoCenter.Views"

<mxe:TextEditor>
    <Interaction.Behaviors>
        <view:PasswordBoxBehavior />
    </Interaction.Behaviors>
</mxe:TextEditor>
```