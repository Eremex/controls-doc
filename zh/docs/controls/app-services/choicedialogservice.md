---
title: IChoiceDialogService
order: 800
seealso: []
---

# IChoiceDialogService {#ichoicedialogservice}

[`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) 提供了一种与平台无关的方式，用于显示带有任意按钮集的模态对话框，并返回所按按钮的结果。对话框结果可以是 `string`、`bool`、枚举值或任何其他类型。在 ViewModel 中，您可以使用 [`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) 显示对话框并获得强类型的答案，而无需引用任何窗口类型。

<!-- TODO
image
app-services-ichoicedialogservice
-->

主要功能包括：

- 单击对话框中的某个选择按钮（显示在对话框底部）时，对话框会自动关闭。
- 任意数量的选择按钮 — 您可以为每个按钮指定标题，并将其与按下该按钮时返回的对话框结果相关联。
- 对话框结果 — 对话框结果由所单击按钮的 `Result` 值指定，可以是 `string`、`bool`、枚举或任何其他类型。
- 可自定义的按钮位置 — 对话框按钮支持 [`Dock`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/Dock.md) 属性，可用于强制将按钮放在最前或最后。
- 默认按钮 — 您可以将特定按钮标记为默认按钮。当用户按下 ENTER 键时，对话框会调用该按钮的命令。
- 取消按钮 — 使用 [`IsCancel`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/IsCancel.md) 标记任意按钮，使其响应 ESC 键。 
- 自动设置所有者 — 所有者窗口由底层 [`IDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IDialogService.md) 通过 [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) 解析，因此无需显式指定。
- 选择按钮始终可用 — 与支持使用 `CanOk` 进行验证的 [IDialogService](dialogservice.md) 不同，[`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) 没有根据输入状态禁用单个选项的机制。

## 接口定义 {#interface-definition}

```csharp
public interface IChoiceDialogService
{
    // Show a modal dialog with the given choices.
    T Show<T>(string message, string? caption, IReadOnlyList<DialogChoice<T>> choices);
}
```

| 参数 | 类型 | 说明 |
|-----------|------|-------------|
| `message` | `string` | 对话框的正文内容，赋值给对话框 ViewModel 的 `Content` 属性。不能为 `null`。 |
| `caption` | `string?` | 对话框的标题。设置为 `null` 时，标题取自对话框 ViewModel 的 `Title` 属性。 |
| `choices` | `IReadOnlyList<DialogChoice<T>>` | 以按钮形式显示在对话框底部的可用选项。顺序与按钮顺序一致。不能为 `null`，并且必须至少包含一项。 |

**返回值：** 

- `T` — 与所单击的选择按钮关联的结果
- 如果通过单击对话框的关闭（'x'）按钮关闭对话框而未作选择，则返回 `default(T)`。对于引用类型（包括 `string`），`default(T)` 为 `null`；对于 `bool` 类型为 `false`；对于没有显式零成员的枚举为 `0`。
- 按下 ENTER — 如果对话框包含 `IsDefault = true` 的选择按钮，按下 ENTER 将返回该按钮的 `Result` 值。如果没有任何选择按钮的 `IsDefault = true`，按下 ENTER 不会执行任何操作，对话框保持打开。
- 按下 ESC — 如果对话框包含 `IsCancel = true` 的选择按钮，按下 Escape 将返回该按钮的 `Result` 值。如果没有任何选择按钮的 `IsCancel = true`，按下 Escape 不会执行任何操作，对话框保持打开。

另请参阅：[处理未作选择即关闭的对话框](#handle-a-dismissed-dialog)。

**异常：**

- `ArgumentNullException` — `message` 或 `choices` 参数为 `null`。
- `ArgumentException` — `choices` 列表为空。对话框必须至少包含一个按钮。


## DialogChoice<T> {#dialogchoice}

对话框中的每个选择按钮都由一个 [`DialogChoice<T>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md) 实例描述：

```csharp
public sealed class DialogChoice<T>
{
    // The button caption.
    public string Caption { get; }

    // The result returned by the `IChoiceDialogService.Show` method when the button is pressed.
    public T Result { get; }

    // Whether the current button is the default button, invoked by Enter.
    public bool IsDefault { get; set; }

    // Whether the current button is the cancel button, invoked by Escape.
    public bool IsCancel { get; set; }

    // The side to which the button is docked. Defaults to `DockType.Right`.
    public DockType Dock { get; set; } = DockType.Right;

    // The button order within its side. Use the `Index` property when you need to reorder buttons without changing the button array.
    public int? Index { get; set; }

    public DialogChoice(string caption, T result);
}
```

## 如何使用 IChoiceDialogService {#how-to-use-ichoicedialogservice}

在 ViewModel 中，调用 [`IChoiceDialogService.Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService/Show.md) 方法以显示带有指定选择按钮的对话框。该方法返回所按选择按钮的 `Result` 值。

### 访问服务 {#access-the-service}

在 ViewModel 中访问 [`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) 对象有两种方式：

- 通过 `Service<T>()` 辅助方法。这是获取 Eremex Controls 库附带的已注册应用程序服务的便捷方法。
- 通过构造函数注入。

#### Service<T>() 辅助方法 {#service-helper}

在 ViewModel 中实现一个 `Service<T>()` 辅助方法，通过静态方法 `ApplicationServicesContext.GetRequiredService<T>()` 获取所请求的服务。

##### 示例 - 使用 Service<T>() 辅助方法显示对话框 {#example-show-a-dialog-using-service-helper}

```csharp
using Eremex.AvaloniaUI.Controls.ApplicationServices;
using CommunityToolkit.Mvvm.Input;

public partial class MyViewModel : ObservableObject
{
    // Provides access to any registered service
    protected static T Service<T>() where T : class
        => ApplicationServicesContext.GetRequiredService<T>();

    [RelayCommand]
    private void ShowChoiceDialog()
    {
        // Resolve the service and show the dialog
        var result = Service<IChoiceDialogService>().Show(
            "The license server did not respond.",
            "Activation failed",
            new[]
            {
                new DialogChoice<string>("Show log", "log") { IsDefault = true },
                new DialogChoice<string>("Retry", "retry"),
                new DialogChoice<string>("Close", "close") { IsCancel = true },
            });
        if(result == "retry") 
        {
            //...
        }
        else 
        {
            //...
        }
    }
}
```

在 App.axaml.cs 文件中，确保按如下方式使用 [`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) 和 [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md) 注册 Eremex 应用程序服务：

```csharp
public class App : Application
{
    public override void OnFrameworkInitializationCompleted()
    {
        RegisterApplicationServices();
        //...
    }

    static void RegisterApplicationServices()
    {
        // Register built-in services.
        var serviceProvider = new SimpleServiceProvider();
        ApplicationServicesContext.RegisterApplicationServices(serviceProvider.AddSingleton);
        ApplicationServicesContext.SetCurrent(serviceProvider);
    }
}
```

#### 构造函数注入 {#constructor-injection}

在 ViewModel 中实现一个以 [`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) 为参数的构造函数。实例化 ViewModel 时，将服务对象传递给该构造函数。

```csharp
public partial class MyViewModel
{
    private readonly IChoiceDialogService _choiceDialogService;

    public MyViewModel(IChoiceDialogService choiceDialogService)
    {
        _choiceDialogService = choiceDialogService;
    }

    [RelayCommand]
    private void ShowChoiceDialog()
    {
        var result = _choiceDialogService.Show(
            "The license server did not respond.",
            "Activation failed",
            new[]
            {
                new DialogChoice<string>("Show log", "log") { IsDefault = true },
                new DialogChoice<string>("Retry", "retry"),
                new DialogChoice<string>("Close", "close") { IsCancel = true },
            });
        //...
    }
}
```



### 返回字符串结果 {#return-a-string-result}

要在单击对话框按钮时返回字符串值，请为该按钮使用 [`DialogChoice<string>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md)。与该按钮关联的值由 [`DialogChoice<T>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md) 构造函数的 _result_ 参数指定。

以下示例显示一个带有三个按钮的对话框。特定的对话框结果（字符串值 "log"、"retry" 和 "close"）与这些按钮相关联。单击其中某个按钮时，对话框的 [`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService/Show.md) 方法会返回相应的值。

<!-- TODO image
app-services-ichoicedialogservice-custom-captions
-->

```csharp
[RelayCommand]
private void ShowDialogWithCustomCaptions()
{
    var result = Service<IChoiceDialogService>().Show(
        DialogMessage,
        DialogTitle,
        new[]
        {
            new DialogChoice<string>("Show log", "log") { IsDefault = true },
            new DialogChoice<string>("Retry", "retry"),
            new DialogChoice<string>("Close", "close") { IsCancel = true },
        });
}
```



### 返回布尔结果 {#return-a-boolean-result}

要在单击对话框按钮时返回布尔值，请为该按钮使用 [`DialogChoice<bool>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md)。与该按钮关联的值由 [`DialogChoice<T>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md) 构造函数的 _result_ 参数指定。

以下示例显示一个带有两个按钮的对话框。特定的对话框结果（`true` 和 `false`）与这些按钮相关联。单击其中某个按钮时，对话框的 [`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService/Show.md) 方法会返回相应的值。

<!-- TODO image
app-services-ichoicedialogservice-boolean-result
-->

```csharp
[RelayCommand]
private void ShowDialogWithBooleanResult()
{
    var result = Service<IChoiceDialogService>().Show(
        DialogMessage,
        DialogTitle,
        new[]
        {
            new DialogChoice<bool>("Show log", true) { IsDefault = true },
            new DialogChoice<bool>("Close", false) { IsCancel = true },
        });
}
```

另请参阅：[处理未作选择即关闭的对话框](#handle-a-dismissed-dialog)。


### 返回枚举结果 {#return-an-enum-result}

要在单击对话框按钮时返回枚举值，请为该按钮使用 [`DialogChoice< enum >`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md)。与该按钮关联的值由 [`DialogChoice<T>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md) 构造函数的 _result_ 参数指定。

以下示例显示一个带有三个按钮的对话框。特定的对话框结果（[`DialogResult.Abort`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogResult.md)、[`DialogResult.Retry`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogResult.md) 和 [`DialogResult.Ignore`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogResult.md)）与这些按钮相关联。单击其中某个按钮时，对话框的 [`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService/Show.md) 方法会返回相应的值。

<!-- TODO image
app-services-ichoicedialogservice-enum-result
-->

```csharp
[RelayCommand]
private void ShowDialogWithEnumResult()
{
    var result = Service<IChoiceDialogService>().Show(
        DialogMessage,
        DialogTitle,
        new[]
        {
            new DialogChoice<DialogResult>("Abort", DialogResult.Abort) { IsCancel = true },
            new DialogChoice<DialogResult>("Retry", DialogResult.Retry) { IsDefault = true },
            new DialogChoice<DialogResult>("Ignore", DialogResult.Ignore),
        });
}
```



### 设置按钮位置 {#set-button-placement}

使用 [`DialogChoice<T>.Dock`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/Dock.md) 属性可以强制将特定按钮放在所有按钮的最前（将 [`Dock`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/Dock.md) 属性设置为 [`DockType.Left`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md)）或最后（将 [`Dock`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/Dock.md) 属性设置为 [`DockType.Right`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md)）。[`Dock`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/Dock.md) 属性默认为 [`DockType.Right`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md)。

<!-- TODO image
app-services-ichoicedialogservice-docked-choices
-->


```csharp
[RelayCommand]
private void ShowDialogWithCustomButtonPlacement()
{
    var result = Service<IChoiceDialogService>().Show(
        DialogMessage,
        DialogTitle,
        new[]
        {
            new DialogChoice<string>("Help", "help") { Dock = DockType.Left },
            new DialogChoice<string>("Retry", "retry") { IsDefault = true },
            new DialogChoice<string>("Cancel", "cancel") { IsCancel = true },
        });
}
```




## 处理未作选择即关闭的对话框 {#handle-a-dismissed-dialog}

当用户单击关闭（'x'）按钮关闭对话框时，[`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService/Show.md) 方法返回 `default(T)`：

- 对于引用类型（`string` 等），结果为 `null`。
- 对于值类型（`bool`、枚举等），结果为该类型的默认值（布尔类型为 `false`，枚举为 `0` 等）。


如果对话框包含取消按钮（[`IsCancel`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/IsCancel.md) 属性为 `true` 的选择按钮），单击该按钮或按下 Escape 键会以该按钮的结果关闭对话框。关闭（'x'）按钮仍以 `default(T)` 结果关闭对话框。

### 示例 — 处理对话框的关闭 {#example-handle-a-dialogs-dismissal}

以下示例创建一个对话框，其中的取消按钮与 `null` 对话框结果相关联。在这种情况下，只需检查对话框结果是否为 `null`，即可处理所有关闭对话框的情形：

- 单击了取消按钮。
- 单击了标题栏的 `x` 按钮。
- 按下了 Escape 键。

<!-- TODO image
app-services-ichoicedialogservice-dismissal-example 
-->

```csharp
var result = Service<IChoiceDialogService>().Show(
    "Save the document?",
    "Confirmation",
    new[]
    {
        new DialogChoice<bool?>("Yes", true) { IsDefault = true },
        new DialogChoice<bool?>("No", false),
        new DialogChoice<bool?>("Cancel", null) { IsCancel = true },
    });

if (result is null)
{
    // Dialog was dismissed or Cancel was clicked, or Escape was pressed.
}
else if (result.Value)
{
    // Yes was pressed.
}
else
{
    // No was pressed.
}
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
