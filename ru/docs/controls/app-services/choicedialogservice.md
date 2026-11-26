---
title: IChoiceDialogService
order: 800
seealso: []
---

# IChoiceDialogService

[`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) предоставляет платформенно-независимый способ показать модальный диалог с произвольным набором кнопок и вернуть результат нажатой кнопки. Результатом диалога может быть `string`, `bool`, значение перечисления или любой другой тип. С помощью [`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) ViewModel может отобразить диалог и получить строго типизированный ответ, не ссылаясь ни на какой тип окна.

<!-- TODO
image
app-services-ichoicedialogservice
-->

Основные возможности:

- Диалог автоматически закрывается при нажатии одной из его кнопок выбора (расположенных в нижней части диалога).
- Любое количество кнопок выбора — Для каждой кнопки можно задать подпись и связать её с результатом диалога, который возвращается при нажатии этой кнопки.
- Результат диалога — Результат диалога определяется значением `Result` нажатой кнопки, которое может быть `string`, `bool`, перечислением или любым другим типом.
- Настраиваемое расположение кнопок — Кнопки диалога поддерживают свойство [`Dock`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/Dock.md), которое позволяет принудительно разместить кнопки первыми или последними.
- Кнопка по умолчанию — Любую кнопку можно отметить как кнопку по умолчанию. Когда пользователь нажимает ENTER, диалог вызывает команду этой кнопки.
- Кнопка отмены — Отметьте любую кнопку с помощью [`IsCancel`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/IsCancel.md), чтобы она реагировала на ESC. 
- Автоматический владелец — Окно-владелец определяется базовым сервисом [`IDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IDialogService.md) через [`IWindowsManager`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IWindowsManager.md), поэтому его не нужно задавать явно.
- Кнопки выбора всегда доступны — В отличие от [IDialogService](dialogservice.md), который поддерживает `CanOk` для валидации, в [`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) нет механизма, позволяющего отключать отдельные варианты выбора в зависимости от состояния ввода.

## Определение интерфейса

```csharp
public interface IChoiceDialogService
{
    // Show a modal dialog with the given choices.
    T Show<T>(string message, string? caption, IReadOnlyList<DialogChoice<T>> choices);
}
```

| Параметр | Тип | Описание |
|-----------|------|-------------|
| `message` | `string` | Основное содержимое диалога, присваиваемое свойству `Content` ViewModel диалога. Не может быть `null`. |
| `caption` | `string?` | Заголовок диалога. Если задано значение `null`, заголовок берётся из свойства `Title` ViewModel диалога. |
| `choices` | `IReadOnlyList<DialogChoice<T>>` | Доступные варианты выбора, отображаемые в виде кнопок в нижней части диалога. Порядок соответствует порядку кнопок. Не может быть `null` и должен содержать хотя бы один элемент. |

**Возвращаемое значение:** 

- `T` — результат, связанный с нажатой кнопкой выбора
- `default(T)`, если диалог был закрыт без выбора нажатием кнопки закрытия ('x') диалога. `default(T)` равно `null` для ссылочных типов (включая `string`), `false` для типа `bool`, `0` для перечисления без явного нулевого члена.
- Нажатие ENTER — Если в диалоге есть кнопка выбора с `IsDefault = true`, нажатие ENTER возвращает значение `Result` этой кнопки. Если ни у одной кнопки выбора нет `IsDefault = true`, нажатие ENTER ничего не делает, и диалог остаётся открытым.
- Нажатие ESC — Если в диалоге есть кнопка выбора с `IsCancel = true`, нажатие Escape возвращает значение `Result` этой кнопки. Если ни у одной кнопки выбора нет `IsCancel = true`, нажатие Escape ничего не делает, и диалог остаётся открытым.

См. также: [Обработка закрытия диалога без выбора](#обработка-закрытия-диалога-без-выбора).

**Исключения:**

- `ArgumentNullException` — Параметр `message` или `choices` равен `null`.
- `ArgumentException` — Список `choices` пуст. Диалог должен содержать хотя бы одну кнопку.


## DialogChoice<T>

Каждая кнопка выбора в диалоге описывается экземпляром [`DialogChoice<T>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md):

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

## Как использовать IChoiceDialogService

В ViewModel вызовите метод [`IChoiceDialogService.Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService/Show.md), чтобы отобразить диалог с указанными кнопками выбора. Метод возвращает значение `Result` нажатой кнопки выбора.

### Доступ к сервису

Получить объект [`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md) в ViewModel можно двумя способами:

- С помощью вспомогательного метода `Service<T>()`. Это удобный способ получить зарегистрированные сервисы приложения, входящие в библиотеку Eremex Controls.
- Через внедрение в конструктор.

#### Вспомогательный метод Service<T>()

Реализуйте в ViewModel вспомогательный метод `Service<T>()`, который получает запрошенный сервис с помощью статического метода `ApplicationServicesContext.GetRequiredService<T>()`.

##### Пример - отображение диалога с помощью вспомогательного метода Service<T>()

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

Убедитесь, что в файле App.axaml.cs сервисы приложения Eremex зарегистрированы с помощью [`SimpleServiceProvider`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/SimpleServiceProvider.md) и [`ApplicationServicesContext`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/ApplicationServicesContext.md) следующим образом:

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

#### Внедрение в конструктор

Реализуйте в ViewModel конструктор с параметром типа [`IChoiceDialogService`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService.md). При создании ViewModel передайте объект сервиса в этот конструктор.

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



### Возврат строкового результата

Чтобы при нажатии кнопки диалога возвращалось строковое значение, используйте для этой кнопки [`DialogChoice<string>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md). Значение, связанное с кнопкой, задаётся параметром _result_ конструктора [`DialogChoice<T>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md).

В этом примере показан диалог с тремя кнопками. С этими кнопками связаны определённые результаты диалога (строковые значения "log", "retry" и "close"). Метод [`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService/Show.md) диалога возвращает соответствующее значение при нажатии одной из его кнопок.

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



### Возврат логического результата

Чтобы при нажатии кнопки диалога возвращалось логическое значение, используйте для этой кнопки [`DialogChoice<bool>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md). Значение, связанное с кнопкой, задаётся параметром _result_ конструктора [`DialogChoice<T>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md).

В этом примере показан диалог с двумя кнопками. С этими кнопками связаны определённые результаты диалога (`true` и `false`). Метод [`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService/Show.md) диалога возвращает соответствующее значение при нажатии одной из его кнопок.

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

См. также: [Обработка закрытия диалога без выбора](#обработка-закрытия-диалога-без-выбора).


### Возврат значения перечисления

Чтобы при нажатии кнопки диалога возвращалось значение перечисления, используйте для этой кнопки [`DialogChoice< enum >`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md). Значение, связанное с кнопкой, задаётся параметром _result_ конструктора [`DialogChoice<T>`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T.md).

В этом примере показан диалог с тремя кнопками. С этими кнопками связаны определённые результаты диалога ([`DialogResult.Abort`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogResult.md), [`DialogResult.Retry`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogResult.md) и [`DialogResult.Ignore`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogResult.md)). Метод [`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService/Show.md) диалога возвращает соответствующее значение при нажатии одной из его кнопок.

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



### Расположение кнопок

Используйте свойство [`DialogChoice<T>.Dock`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/Dock.md), чтобы принудительно разместить определённые кнопки первыми (задайте свойству [`Dock`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/Dock.md) значение [`DockType.Left`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md)) или последними (задайте свойству [`Dock`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/Dock.md) значение [`DockType.Right`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md)) среди всех кнопок. По умолчанию свойство [`Dock`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/Dock.md) имеет значение [`DockType.Right`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md).

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




## Обработка закрытия диалога без выбора

Когда пользователь закрывает диалог кнопкой закрытия ('x'), метод [`Show`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/IChoiceDialogService/Show.md) возвращает `default(T)`:

- Для ссылочных типов (`string` и т. д.) результат равен `null`.
- Для значимых типов (`bool`, перечисления и т. д.) результатом является значение типа по умолчанию (`false` для логического типа, `0` для перечисления и т. д.)


Если в диалоге есть кнопка отмены (кнопка выбора, у которой свойство [`IsCancel`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DialogChoice-T/IsCancel.md) равно `true`), нажатие на неё или клавиши Escape закрывает диалог с результатом этой кнопки. Кнопка закрытия ('x') по-прежнему закрывает диалог с результатом `default(T)`.

### Пример — обработка закрытия диалога

В этом примере создаётся диалог с кнопкой отмены, связанной с результатом диалога `null`. В этом случае достаточно проверить результат на `null`, чтобы обработать все сценарии закрытия диалога:

- Нажата кнопка отмены.
- Нажата кнопка `x` в заголовке.
- Нажата клавиша Escape.

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

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
