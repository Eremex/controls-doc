---
title: MxMessageBox
order: 100
seealso: []
---

# MxMessageBox

`MxMessageBox` 对话框允许您显示消息并向用户询问简单的问题。

![mxmessagebox](../../images/mxmessagebox.png)

`MxMessageBox` 使用 Eremex 绘制主题进行渲染。它同时支持浅色和深色主题变体。

使用静态方法 `MxMessageBox.Show` 和 `MxMessageBox.ShowAsync` 的重载来显示对话框。




## Show 方法重载

`MxMessageBox.Show` 方法的重载会返回对话框的结果(用户点击的按钮)。提供两个 `MxMessageBox.Show` 方法重载:

``` cs
public static MessageBoxResult MxMessageBox.Show(Window? owner, string text, string? title = null, MessageBoxButtons buttons = MessageBoxButtons.Ok, MessageBoxIcon icon = MessageBoxIcon.None, MessageBoxResult defaultButton = MessageBoxResult.None, Action<MxMessageBox>? configure = null)
```

- owner — 消息框的所有者窗口。如果该参数为 `null`,`MxMessageBox` 会自动确定所有者:所有者为最后一个活动窗口,或应用程序的主窗口。
- text — 要在对话框中显示的文本。
- title — 对话框的标题。
- buttons — 一个 `Eremex.AvaloniaUI.Controls.MessageBoxButtons` 枚举值,用于指定对话框中要显示的按钮。可用值包括:`Ok`、`OkCancel`、`YesNoCancel`、`YesNo`、`AbortRetryIgnore`、`RetryCancel`
- icon — 要在文本前显示的预定义图标之一。将该属性设置为 `MessageBoxIcon.None` 以隐藏图标。
- defaultButton — 指定默认按钮。默认按钮是对话框显示时最初获得焦点的按钮。当用户按下 ENTER 键时,将触发默认按钮。
- configure — 用于执行额外对话框自定义的委托(例如,标题栏中对话框的图标,或按钮的对齐方式)。


    ### 示例 

    以下示例显示了一个带有三个按钮(Yes、No 和 Cancel)的消息框。

    ![mxmessagebox-example](../../images/mxmessagebox-example.png)

    ``` cs
    MessageBoxResult result = MxMessageBox.Show(null, "The document has changed."+ Environment.NewLine+ "Do you want to save the changes?", "Save Changes", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Warning, MessageBoxResult.Yes);
    if (result == MessageBoxResult.Yes)
    {
        //...
    }
    ```

另一个 `MxMessageBox.Show` 方法重载只包含一个参数。

``` cs
public static MessageBoxResult MxMessageBox.Show(Action<MxMessageBox> configure)
```

- configure — 用于自定义对话框的委托。


    ### 示例

    ![mxmessagebox-error-example](../../images/mxmessagebox-error-example.png)

    ``` cs
    var res = MxMessageBox.Show(configure: msgBox =>
    {
        msgBox.Text = "Error opening the database";
        msgBox.Title = "Error";
        msgBox.Buttons = MessageBoxButtons.Ok;
        msgBox.ButtonAlignment = Avalonia.Layout.HorizontalAlignment.Center;
        msgBox.Window.Icon = new WindowIcon(AssetLoader.Open(new Uri("avares://DemoCenter/Assets/EMXControls.ico")));
    });
    ```


## ShowAsync 方法重载

您可以使用 `MxMessageBox.ShowAsync` 方法的重载来异步调用消息框,而不会阻塞 UI 线程。`ShowAsync` 方法返回一个表示异步操作的 `Task<MessageBoxResult>` 对象。当用户关闭消息框时,该操作完成。`ShowAsync` 方法重载的参数与 `Show` 方法的参数相同。

``` cs
public static Task<MessageBoxResult> ShowAsync(Window? owner, string text, string? title = null, MessageBoxButtons buttons = MessageBoxButtons.Ok, MessageBoxIcon icon = MessageBoxIcon.None, MessageBoxResult defaultButton = MessageBoxResult.None, Action<MxMessageBox>? configure = null)
```

``` cs
public static Task<MessageBoxResult> ShowAsync(Action<MxMessageBox> configure)
```

### 示例

以下示例异步显示一个消息框,并等待用户按下按钮。 

``` cs
async Task<MessageBoxResult> ShowMessageBoxAsync()
{
    Task<MessageBoxResult> resultTask = MxMessageBox.ShowAsync(
        owner: null,
        text: "Are you sure you want to cancel this task?",
        title: "Confirmation",
        buttons: MessageBoxButtons.YesNo,
        icon: MessageBoxIcon.Question
    );

    MessageBoxResult result = await resultTask;

    if (result == MessageBoxResult.Yes)
    {
        await CancelTaskAsync();
    }

    return result;
}

async Task CancelTaskAsync()
{
    await Task.Delay(3000);
}
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
