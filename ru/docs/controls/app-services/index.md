---
title: Сервисы приложения
order: 15000
seealso: []
---

# Сервисы приложения


Сервисы приложения (Application Services) обеспечивают чистый и слабосвязанный способ работы с окнами, диалогами и настройками внешнего вида всего приложения из ваших ViewModel и бизнес-логики. Вместо того чтобы напрямую ссылаться на окна и диалоги или обращаться к системным функциям, вы запрашиваете эти возможности через чётко определённые интерфейсы сервисов. Сервисы берут на себя платформенно-зависимый код, а ваша бизнес-логика остаётся независимой от платформы.

Ниже приведён фрагмент кода, который показывает, как с помощью [`IMessageBoxService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IMessageBoxService.md) отобразить окно сообщения из ViewModel.

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
    
    Полный код, показывающий, как зарегистрировать встроенные сервисы в [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md), приведён в разделе [Доступ к встроенным сервисам с помощью ApplicationServicesContext и SimpleServiceProvider](#доступ-к-встроенным-сервисам-с-помощью-applicationservicescontext-и-simpleserviceprovider).





## Что можно делать с помощью сервисов?

### Управление окнами

- Получать активное окно из любого места кода
- Автоматически задавать владельца для диалогов

### Взаимодействие с пользователем
- Показывать стандартные окна сообщений с предопределёнными наборами кнопок
- Создавать диалоги выбора с заданными приложением подписями кнопок
- Отображать модальные диалоги, управляемые ViewModel
- Показывать немодальные окна, привязанные к ViewModel

### Операции с файлами
- Открывать файлы с помощью системного файлового диалога
- Сохранять файлы с помощью системных диалогов
- Поддерживать как синхронные, так и асинхронные операции

### Внешний вид и темы

- Получать доступные параметры темы 
- Создавать в интерфейсе селектор темы

## Доступные сервисы

Библиотека Eremex Controls содержит следующие сервисы, каждый из которых предоставляет определённую функциональность.

### Сервисы взаимодействия с пользователем

| Сервис | Описание |
|---------|---------|
| [`IMessageBoxService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IMessageBoxService.md) | Показывает стандартные окна сообщений с фиксированными наборами кнопок, определёнными перечислением [`MessageBoxButtons`](../../API/Eremex.AvaloniaUI.Controls/MessageBoxButtons.md) (Ok, Ok&vert;Cancel, Yes&vert;No&vert;Cancel, Yes&vert;No, Abort&vert;Retry&vert;Ignore и Retry&vert;Cancel). |
| [`IDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IDialogService.md) | Показывает диалоги из кода ViewModel, чтобы ViewModel могла задать пользователю вопрос, не ссылаясь ни на какой тип окна. Диалог управляется _ViewModel диалога_. Вы также можете реализовать View, которое отображается как содержимое диалога. Это View находится с помощью атрибута [`ViewLocatorAttribute`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ViewLocatorAttribute.md), примененного к ViewModel диалога. |
| [`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) | Показывает диалог с произвольным набором кнопок и возвращает результат нажатой кнопки. |
| [`IWindowService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowService.md) | Показывает немодальные окна из кода ViewModel, чтобы ViewModel могла открыть окно, не ссылаясь ни на какой тип окна. Аналог для модальных диалогов — [`IDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IDialogService.md). |

### Файловые сервисы

| Сервис | Описание |
|---------|---------|
| [`IOpenFileDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IOpenFileDialogService.md) | Показывает системный диалог `Open File` из кода ViewModel в синхронном или асинхронном режиме. |
| [`ISaveFileDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ISaveFileDialogService.md) | Показывает системный диалог `Save File` из кода ViewModel в синхронном или асинхронном режиме. |

### Инфраструктурные сервисы

| Сервис | Описание |
|---------|---------|
| [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md) | Отслеживает активное окно приложения. Сервисы диалогов используют сервис [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md), чтобы получить владельца по умолчанию для создаваемых диалогов. |
| [`IAppearanceService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IAppearanceService.md) | Предоставляет список настроек визуальной темы и применяет выбранный вариант темы. |

### Использование сервисов

Для работы со встроенными сервисами можно использовать классы [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md) и [`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) или собственные DI-контейнеры.

#### Доступ к встроенным сервисам с помощью ApplicationServicesContext и SimpleServiceProvider

Зарегистрируйте встроенные сервисы в [`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) и [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md) при запуске приложения (в классе `App`). Затем создайте в ViewModel удобный вспомогательный метод `Service<T>()`, который получает эти сервисы с помощью метода `ApplicationServicesContext.GetRequiredService<T>`.

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

[`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) — это минимальная реализация `IServiceProvider`, которая не требует внешних NuGet-пакетов. Это легковесный потокобезопасный контейнер для приложений и тестов, которым не нужен полноценный DI-контейнер. Все сервисы создаются отложенно и живут как синглтоны (создаются один раз и кэшируются на всё время работы приложения). Созданные экземпляры, реализующие `IDisposable`, освобождаются методом [`Dispose`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider/Dispose.md).

 
#### Доступ к сервисам через внедрение в конструктор

При необходимости сервис приложения можно передать в ViewModel напрямую. Затем можно вызывать методы этого сервиса в ViewModel.

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



#### Поддержка собственных DI-контейнеров 

Если вы используете внешний DI-контейнер, зарегистрируйте в нём встроенные сервисы и задайте полученный провайдер в качестве текущего.

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


- Собственные реализации `IServiceProvider`

    Вы можете самостоятельно реализовать `IServiceProvider` и передать его в [`ApplicationServicesContext.SetCurrent`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext/SetCurrent.md).


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
