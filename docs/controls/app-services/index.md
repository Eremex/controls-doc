---
title: Application Services
order: 15000
seealso: []
---

# Application Services


Application Services provides a clean, decoupled way to work with windows, dialogs, and application-wide appearance settings from your ViewModels and business logic. Instead of directly referencing windows and dialogs, or accessing system features, you request these capabilities through well-defined service interfaces. The services handle platform-specific code, while your business logic remains platform-agnostic.

Here is a code snippet that demonstrates the use of the `IMessageBoxService` to display a message box from a View Model.

``` cs
using Eremex.AvaloniaUI.Controls.ApplicationServices;

public class MyViewModel
{
    public MyViewModel() { }
    
    [RelayCommand]
    private void ShowInformation()
    {
        // Access an IMessageBoxService and show a message box.
        var result = Service<IMessageBoxService>()
            .Show("Connection established", "Information", MessageBoxButtons.Ok, MessageBoxIcon.Information);
    }

    // Provides direct access to any service
    protected static T Service<T>() where T : class
        => ApplicationServicesContext.GetRequiredService<T>();
}
```

!!! Tip
    
    See [Access Built-in Services Using the ApplicationServicesContext and SimpleServiceProvider](#access-built-in-services-using-the-applicationservicescontext-and-simpleserviceprovider) for complete code, which shows how to register built-in services with `ApplicationServicesContext`.





## What Can You Do With Services?

### Window Management

- Get the active window from anywhere in your code
- Set the owner for dialogs automatically

### User Interaction
- Show standard message boxes with predefined button sets
- Create custom choice dialogs with application-defined button captions
- Display modal dialogs driven by ViewModels
- Show non-modal windows bound to ViewModels

### File Operations
- Open files using the system's file dialog
- Save files with system dialogs
- Support both synchronous and asynchronous operations

### Appearance and Theming

- Get available theme options 
- Allows you to create a theme selector in your UI

## Available Services

The Eremex Controls library contains the following services, each providing a specific functionality.

### User Interaction Services

| Service | Description |
|---------|---------|
| `IMessageBoxService` | Shows standard message boxes with fixed button sets defined by the `MessageBoxButtons` enumeration (Ok, Ok&vert;Cancel, Yes&vert;No&vert;Cancel, Yes&vert;No, Abort&vert;Retry&vert;Ignore, and Retry&vert;Cancel). |
| `IDialogService` | Shows dialogs from ViewModel code, so that a ViewModel can ask the user a question without referencing any window type. A dialog is driven by a _dialog ViewModel_. You can also implement a View to display as the dialog's content. This View is located through the `ViewLocatorAttribute` applied to the dialog ViewModel. |
| `IChoiceDialogService` | Shows a dialog with an arbitrary set of buttons and returns the result of the pressed one. |
| `IWindowService` | Shows non-modal windows from ViewModel code, so that a ViewModel can open a window without referencing any window type. The counterpart for modal dialogs is `IDialogService`. |

### File Services

| Service | Description |
|---------|---------|
| `IOpenFileDialogService` | Shows the platform `Open File` dialog from ViewModel code in sync or async mode. |
| `ISaveFileDialogService` | Shows the platform `Save File` dialog from ViewModel code in sync or async mode. |

### Infrastructure Services

| Service | Description |
|---------|---------|
| `IWindowsManager` | Tracks the active window of the application. Dialog services use the `IWindowsManager` service to get the default owner for newly created dialogs. |
| `IAppearanceService` | Lists visual theme settings and applies the chosen theme variant. |

### Use Services

You can use the `ApplicationServicesContext` and `SimpleServiceProvider` classes to work with built-in services, or use custom DI containers.

#### Access Built-in Services Using the ApplicationServicesContext and SimpleServiceProvider

Register the built-in services with the `SimpleServiceProvider` and `ApplicationServicesContext` when the application starts (in the `App` class). Then create a convenient `Service<T>()` helper method in your ViewModel to access these services using the `ApplicationServicesContext.GetRequiredService<T>` method.

```csharp
using Eremex.AvaloniaUI.Controls.ApplicationServices;

public abstract partial class ApplicationServicesPageViewModelBase : PageViewModelBase
{
    // Provides direct access to any service
    protected static T Service<T>() where T : class
        => ApplicationServicesContext.GetRequiredService<T>();
}

public partial class MyViewModel : ApplicationServicesPageViewModelBase
{
    [RelayCommand]
    private void ShowInformation()
    {
        // Access an IMessageBoxService and show a message box.
        var result = Service<IMessageBoxService>()
            .Show("Connection established", "Information", MessageBoxButtons.Ok, MessageBoxIcon.Information);
    }
}

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

The `SimpleServiceProvider` is a minimal `IServiceProvider` implementation that requires no external NuGet packages. It is a lightweight, thread-safe container intended for applications and tests that do not need a full DI container. All services are created lazily and live as singletons (created once and cached for the application lifetime). Created instances implementing `IDisposable` are disposed by the `Dispose` method.

 
#### Access Services Through Constructor Injection

When required, you can pass an application service to a ViewModel directly. They you can call a method of this service in the ViewModel.

```csharp
public partial class MyViewModel
{
    private readonly IMessageBoxService messageBoxService;
   
    public MyViewModel(IMessageBoxService messageBoxService)
    {
        this.messageBoxService = messageBoxService;
    }

    [RelayCommand]
    private void ShowInformation()
    {
        var result = messageBoxService.Show("Connection established", "Information", MessageBoxButtons.Ok, MessageBoxIcon.Information);
    }
}
``` 



#### Custom Dependency Injection Container Support 




- Microsoft.Extensions.DependencyInjection

    ```
    var services = new ServiceCollection();
    services.AddTransient<IDataService, DataService>();
    ApplicationServicesContext.RegisterApplicationServices(
        (type, factory) => services.AddSingleton(type, sp => factory(sp))
    );
    var provider = services.BuildServiceProvider();
    ApplicationServicesContext.SetCurrent(provider);
    ```

- Autofac

    ```
    var services = new ServiceCollection();
    services.AddTransient<IDataService, DataService>();
    //...
    var builder = new ContainerBuilder();
    builder.Populate(services);
    ApplicationServicesContext.RegisterApplicationServices(
        (type, factory) => builder
            .Register(c => factory(c.Resolve<IServiceProvider>()))
            .As(type)
            .SingleInstance()
    );
    var container = builder.Build();
    var serviceProvider = new AutofacServiceProvider(container);
    ApplicationServicesContext.SetCurrent(serviceProvider);
    ```


- Custom `IServiceProvider` implementations


