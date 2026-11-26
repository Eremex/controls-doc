---
title: 应用程序服务
order: 15000
seealso: []
---

# 应用程序服务 {#application-services}


应用程序服务（Application Services）提供了一种简洁、解耦的方式，让您可以在 ViewModel 和业务逻辑中处理窗口、对话框以及整个应用程序的外观设置。您无需直接引用窗口和对话框或访问系统功能，而是通过定义明确的服务接口来请求这些功能。服务负责处理平台相关的代码，而您的业务逻辑保持与平台无关。

以下代码片段演示了如何使用 [`IMessageBoxService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IMessageBoxService.md) 从 ViewModel 中显示消息框。

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
    
    有关如何在 [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md) 中注册内置服务的完整代码，请参阅[使用 ApplicationServicesContext 和 SimpleServiceProvider 访问内置服务](#access-built-in-services-using-the-applicationservicescontext-and-simpleserviceprovider)。





## 服务可以做什么？ {#what-can-you-do-with-services}

### 窗口管理 {#window-management}

- 在代码的任何位置获取活动窗口
- 自动为对话框设置所有者

### 用户交互 {#user-interaction}
- 显示带有预定义按钮集的标准消息框
- 创建带有应用程序自定义按钮标题的选择对话框
- 显示由 ViewModel 驱动的模态对话框
- 显示绑定到 ViewModel 的非模态窗口

### 文件操作 {#file-operations}
- 使用系统文件对话框打开文件
- 使用系统对话框保存文件
- 同时支持同步和异步操作

### 外观和主题 {#appearance-and-theming}

- 获取可用的主题选项 
- 在 UI 中创建主题选择器

## 可用服务 {#available-services}

Eremex Controls 库包含以下服务，每个服务提供特定的功能。

### 用户交互服务 {#user-interaction-services}

| 服务 | 说明 |
|---------|---------|
| [`IMessageBoxService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IMessageBoxService.md) | 显示标准消息框，其固定按钮集由 [`MessageBoxButtons`](../../API/Eremex.AvaloniaUI.Controls/MessageBoxButtons.md) 枚举定义（Ok、Ok&vert;Cancel、Yes&vert;No&vert;Cancel、Yes&vert;No、Abort&vert;Retry&vert;Ignore 和 Retry&vert;Cancel）。 |
| [`IDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IDialogService.md) | 从 ViewModel 代码中显示对话框，使 ViewModel 无需引用任何窗口类型即可向用户提问。对话框由_对话框 ViewModel_ 驱动。您还可以实现一个 View 作为对话框的内容显示。该 View 通过应用于对话框 ViewModel 的 [`ViewLocatorAttribute`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ViewLocatorAttribute.md) 进行定位。 |
| [`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) | 显示带有任意按钮集的对话框，并返回所按按钮的结果。 |
| [`IWindowService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowService.md) | 从 ViewModel 代码中显示非模态窗口，使 ViewModel 无需引用任何窗口类型即可打开窗口。模态对话框对应的服务是 [`IDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IDialogService.md)。 |

### 文件服务 {#file-services}

| 服务 | 说明 |
|---------|---------|
| [`IOpenFileDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IOpenFileDialogService.md) | 以同步或异步模式从 ViewModel 代码中显示平台的 `Open File` 对话框。 |
| [`ISaveFileDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ISaveFileDialogService.md) | 以同步或异步模式从 ViewModel 代码中显示平台的 `Save File` 对话框。 |

### 基础设施服务 {#infrastructure-services}

| 服务 | 说明 |
|---------|---------|
| [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) | 跟踪应用程序的活动窗口。对话框服务使用 [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) 服务为新创建的对话框获取默认所有者。 |
| [`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) | 列出视觉主题设置并应用所选的主题变体。 |

### 使用服务 {#use-services}

您可以使用 [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md) 和 [`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) 类来使用内置服务，也可以使用自定义 DI 容器。

#### 使用 ApplicationServicesContext 和 SimpleServiceProvider 访问内置服务 {#access-built-in-services-using-the-applicationservicescontext-and-simpleserviceprovider}

在应用程序启动时（在 `App` 类中），将内置服务注册到 [`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) 和 [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md)。然后在 ViewModel 中创建一个便捷的 `Service<T>()` 辅助方法，通过 `ApplicationServicesContext.GetRequiredService<T>` 方法访问这些服务。

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

[`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) 是 `IServiceProvider` 的最小实现，无需任何外部 NuGet 包。它是一个轻量级、线程安全的容器，适用于不需要完整 DI 容器的应用程序和测试。所有服务都是延迟创建的，并以单例形式存在（只创建一次，并在应用程序的整个生命周期内缓存）。实现了 `IDisposable` 的已创建实例由 [`Dispose`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider/Dispose.md) 方法释放。

 
#### 通过构造函数注入访问服务 {#access-services-through-constructor-injection}

需要时，您可以将应用程序服务直接传递给 ViewModel，然后在 ViewModel 中调用该服务的方法。

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



#### 自定义依赖注入容器支持 {#custom-dependency-injection-container-support}

如果您使用外部 DI 容器，请将内置服务注册到该容器中，并将得到的提供程序设置为当前提供程序。

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


- 自定义 `IServiceProvider` 实现

    您可以自行实现 `IServiceProvider`，并将其传递给 [`ApplicationServicesContext.SetCurrent`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext/SetCurrent.md)。


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
