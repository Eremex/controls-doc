---
title: IWindowsManager
order: 650
seealso: []
---

# IWindowsManager

[`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) returns the currently active window. You can use this service to obtain the owner for message boxes, windows, and dialogs shown using other application services.

Main features:

- Active window access — The `ActiveWindow` property returns the currently active window, falling back to the application main window.
- Framework-agnostic contract — The active window returned is of an [`Eremex.AvaloniaUI.Controls.ApplicationServices.IWindow`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindow.md) interface, which has no reference to the Avalonia UI framework.

!!! Tip

    Code that needs Avalonia-specific window types should use Avalonia's own APIs instead.

    The following code retrieves the currently active (focused) window in an Avalonia desktop application, safely falling back to the application's main window if no window currently has focus, or `null` when the application has no window.

    ``` cs
    var lifetime = Avalonia.Application.Current?.ApplicationLifetime as IClassicDesktopStyleApplicationLifetime;
    Avalonia.Controls.Window? activeWindow = lifetime?.Windows.FirstOrDefault(w => w.IsActive) ?? lifetime?.MainWindow;
    ```


## Interface Definition

```csharp
public interface IWindowsManager
{
    // The window a new dialog should be shown on top of: the currently active window,
    // falling back to the application main window. null when the application has no window yet.
    IWindow? ActiveWindow { get; }
}
```

## Use IWindowsManager

In your ViewModel, use the [`IWindowsManager.ActiveWindow`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager/ActiveWindow.md) property to obtain the currently active window, and pass it to an application service that accepts an explicit owner (for example, when calling [`IMessageBoxService.Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IMessageBoxService/Show.md)). 


### Access the Service

There are two ways to access an [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) object in a ViewModel:

- Through the `Service<T>()` helper method. This is a convenient approach to obtain registered application services shipped with the Eremex Controls library.
- Through constructor injection.

#### Service<T>() Helper

Implement a helper `Service<T>()` method in your ViewModel to return a requested service using the static `ApplicationServicesContext.GetRequiredService<T>()` method.

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

In the App.axaml.cs file, ensure that Eremex application services are registered using [`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) and [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md) as follows:

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

#### Constructor Injection

Implement a constructor in your ViewModel with [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) as a parameter. When you instantiate the ViewModel, pass the service object to this constructor.

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

The [application services](index.md) that show message boxes, windows, and dialogs can resolve the owner automatically through [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md). To do this, use their [`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IMessageBoxService/Show.md) overloads that have no `owner` parameter.
