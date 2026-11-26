---
title: IWindowsManager
order: 650
seealso: []
---

# IWindowsManager

[`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) возвращает текущее активное окно. Сервис позволяет получить окно-владельца для окон сообщений, окон и диалогов, которые показывают другие сервисы приложения.

Основные возможности:

- Доступ к активному окну — Свойство `ActiveWindow` возвращает текущее активное окно, а если активного окна нет — главное окно приложения.
- Контракт, не зависящий от фреймворка — Активное окно возвращается как интерфейс [`Eremex.AvaloniaUI.Controls.ApplicationServices.IWindow`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindow.md), который не ссылается на типы Avalonia UI.

!!! Tip

    Коду, которому нужны типы окон, специфичные для Avalonia, следует использовать собственные API Avalonia.

    Следующий код получает текущее активное (сфокусированное) окно в desktop-приложении Avalonia и безопасно откатывается на главное окно приложения, если ни одно окно не активно, или на `null`, если у приложения ещё нет окон.

    ``` cs
    var lifetime = Avalonia.Application.Current?.ApplicationLifetime as IClassicDesktopStyleApplicationLifetime;
    Avalonia.Controls.Window? activeWindow = lifetime?.Windows.FirstOrDefault(w => w.IsActive) ?? lifetime?.MainWindow;
    ```


## Определение интерфейса

```csharp
public interface IWindowsManager
{
    // The window a new dialog should be shown on top of: the currently active window,
    // falling back to the application main window. null when the application has no window yet.
    IWindow? ActiveWindow { get; }
}
```

## Использование IWindowsManager

В ViewModel используйте свойство [`IWindowsManager.ActiveWindow`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager/ActiveWindow.md), чтобы получить текущее активное окно, и передайте его сервису приложения, который принимает явного владельца (например, при вызове [`IMessageBoxService.Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IMessageBoxService/Show.md)).


### Доступ к сервису

Получить объект [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) в ViewModel можно двумя способами:

- Через вспомогательный метод `Service<T>()`. Это удобный способ получить зарегистрированные сервисы приложения, поставляемые с библиотекой Eremex Controls.
- Через внедрение зависимости в конструктор.

#### Вспомогательный метод Service<T>()

Реализуйте в ViewModel вспомогательный метод `Service<T>()`, который возвращает запрошенный сервис через статический метод `ApplicationServicesContext.GetRequiredService<T>()`.

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

В файле App.axaml.cs убедитесь, что сервисы приложения Eremex зарегистрированы с помощью [`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) и [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md) следующим образом:

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

#### Внедрение через конструктор

Реализуйте в ViewModel конструктор с параметром [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md). При создании ViewModel передайте в этот конструктор объект сервиса.

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

[Сервисы приложения](index.md), показывающие окна сообщений, окна и диалоги, могут определять владельца автоматически через [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md). Для этого используйте их перегрузки [`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IMessageBoxService/Show.md) без параметра `owner`.
