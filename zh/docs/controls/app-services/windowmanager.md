---
title: IWindowsManager
order: 650
seealso: []
---

# IWindowsManager {#iwindowsmanager}

[`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) 返回当前活动窗口。您可以使用此服务为通过其他应用程序服务显示的消息框、窗口和对话框获取所有者。

主要功能：

- 活动窗口访问 — `ActiveWindow` 属性返回当前活动窗口，如果不存在活动窗口，则回退到应用程序主窗口。
- 与框架无关的契约 — 返回的活动窗口是 [`Eremex.AvaloniaUI.Controls.ApplicationServices.IWindow`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindow.md) 接口，该接口不引用 Avalonia UI 框架。

!!! Tip

    需要 Avalonia 特定窗口类型的代码应改用 Avalonia 自身的 API。

    以下代码在 Avalonia 桌面应用程序中获取当前活动（聚焦）的窗口，如果没有窗口获得焦点，则安全地回退到应用程序的主窗口；如果应用程序还没有窗口，则返回 `null`。

    ``` cs
    var lifetime = Avalonia.Application.Current?.ApplicationLifetime as IClassicDesktopStyleApplicationLifetime;
    Avalonia.Controls.Window? activeWindow = lifetime?.Windows.FirstOrDefault(w => w.IsActive) ?? lifetime?.MainWindow;
    ```


## 接口定义 {#interface-definition}

```csharp
public interface IWindowsManager
{
    // The window a new dialog should be shown on top of: the currently active window,
    // falling back to the application main window. null when the application has no window yet.
    IWindow? ActiveWindow { get; }
}
```

## 使用 IWindowsManager {#use-iwindowsmanager}

在 ViewModel 中，使用 [`IWindowsManager.ActiveWindow`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager/ActiveWindow.md) 属性获取当前活动窗口，并将其传递给接受显式所有者的应用程序服务（例如调用 [`IMessageBoxService.Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IMessageBoxService/Show.md) 时）。


### 访问服务 {#access-the-service}

在 ViewModel 中有两种方式获取 [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) 对象：

- 通过 `Service<T>()` 辅助方法。这是获取 Eremex Controls 库所提供的已注册应用程序服务的便捷方式。
- 通过构造函数注入。

#### Service<T>() 辅助方法 {#servicet-helper}

在 ViewModel 中实现 `Service<T>()` 辅助方法，通过静态方法 `ApplicationServicesContext.GetRequiredService<T>()` 返回请求的服务。

```csharp
using Eremex.AvaloniaUI.Controls.ApplicationServices;
using CommunityToolkit.Mvvm.Input;

public partial class MyViewModel : ObservableObject
{
    // Provides access to any registered service
    protected static T Service<T>() where T : class
        => ApplicationServicesContext.GetRequiredService<T>();

    [RelayCommand]
    private void ShowOverActiveWindow()
    {
        // Resolve the manager directly from the Service<T>() method
        var owner = Service<IWindowsManager>().ActiveWindow;
        var result = Service<IMessageBoxService>()
            .Show(owner, "Save changes?", "Question",
                  MessageBoxButtons.OkCancel, MessageBoxIcon.None);
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

在 ViewModel 中实现一个以 [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) 为参数的构造函数。创建 ViewModel 时，将服务对象传递给该构造函数。

```csharp
public partial class MyViewModel
{
    private readonly IWindowsManager _windowsManager;
    private readonly IMessageBoxService _messageBoxService;

    public MyViewModel(IWindowsManager windowsManager, IMessageBoxService messageBoxService)
    {
        _windowsManager = windowsManager;
        _messageBoxService = messageBoxService;
    }

    [RelayCommand]
    private void ShowOverActiveWindow()
    {
        var owner = _windowsManager.ActiveWindow;
        var result = _messageBoxService.Show(
            owner, "Save changes?", "Question",
            MessageBoxButtons.OkCancel, MessageBoxIcon.None
        );
        //...
    }
}
```

用于显示消息框、窗口和对话框的[应用程序服务](index.md)可以通过 [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) 自动解析所有者。为此，请使用其不带 `owner` 参数的 [`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IMessageBoxService/Show.md) 重载。
