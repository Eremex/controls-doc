---
title: 如何创建密码文本框
order: 100
seealso: []
---

# 如何创建密码文本框

本示例演示如何使用密码字符（例如“*”）遮盖用户输入，并允许用户通过按钮显示和隐藏已输入的密码。

![texteditor-passwordchar](../../../images/texteditor-password.gif)

`TextEditor` 类目前不包含 `PasswordChar` 属性。但是，你可以为内部文本框（`TextBox` 控件）启用密码模式，该文本框内嵌于 `TextEditor` 控件中，并提供文本编辑功能。

以下示例创建了 _PasswordBoxBehavior_ 行为，用于为文本编辑器内部的文本框（`TextBox`）启用密码模式。_PasswordBoxBehavior_ 类公开了 `PasswordChar` 和 `ShowRevealButton` 属性，用于指定密码掩码字符以及密码显示按钮的可见性。

你需要在项目中添加 `Avalonia.Xaml.Behaviors` NuGet 包才能使用行为（behavior）。

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

按照以下方式，将 _PasswordBoxBehavior_ 行为附加到项目中的 `TextEditor` 控件上：

``` xml
xmlns:view="using:DemoCenter.Views"

<mxe:TextEditor>
    <Interaction.Behaviors>
        <view:PasswordBoxBehavior />
    </Interaction.Behaviors>
</mxe:TextEditor>
```


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
