---
title: IChoiceDialogService
order: 800
seealso: []
---

# IChoiceDialogService

`IChoiceDialogService` provides a platform-agnostic way to show a modal dialog with an arbitrary set of buttons and return the result of the pressed one. The dialog result can be a `string`, `bool`, enumeration value, or any other type. From your ViewModel, you can use `IChoiceDialogService` to display a dialog and receive a strongly typed answer, without referencing any window type.

<!-- TODO
image
app-services-ichoicedialogservice
-->

Main features include:

- Dialog is automatically closed when one of its choice buttons (shown in the dialog's footer) is clicked.
- Any number of choice buttons — For each button you can specify a caption and associate it with a dialog result, returned when this button is pressed.
- Dialog result — The dialog result is specified by a clicked button's `Result` value, which can be a `string`, a `bool`, an enumeration, or any other type.
- Customizable button placement — Dialog buttons support the `Dock` property which allows you to forcibly place buttons first or last.
- Default button — You can mark a specific button as default. When the user presses ENTER, the dialog invokes this button's command.
- Cancel button — Mark any button with `IsCancel` to make it respond to ESC. 
- Automatic owner — The owner window is resolved by the underlying `IDialogService` through `IWindowsManager`, so it does not need to be specified explicitly.
- Choice buttons are always enabled — Unlike [IDialogService](dialogservice.md), which supports `CanOk` for validation, `IChoiceDialogService` has no mechanism to disable individual choices based on input state.

## Interface Definition

```csharp
public interface IChoiceDialogService
{
    // Show a modal dialog with the given choices.
    T Show<T>(string message, string? caption, IReadOnlyList<DialogChoice<T>> choices);
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `message` | `string` | The dialog's body content assigned to the dialog ViewModel's `Content` property. Cannot be `null`. |
| `caption` | `string?` | The dialog's caption. When set to `null`, the caption is taken from the dialog ViewModel's `Title` property. |
| `choices` | `IReadOnlyList<DialogChoice<T>>` | The available choices displayed as buttons in the dialog's footer. The order matches the button order. Cannot be `null` and must contain at least one item. |

**Returns:** 

- `T` — the result associated with the clicked choice button
- `default(T)` if the dialog was closed without a choice by clicking the dialog's caption 'x' button. `default(T)` is `null` for reference types (including `string`), `false` for the `bool` type, `0` for an enum without an explicit zero member.
- Pressing ENTER — If the dialog contains a choice button with `IsDefault = true`, pressing ENTER returns that button's `Result` value. If no choice button has `IsDefault = true`, pressing ENTER does nothing, and the dialog remains open.
- Pressing ESC — If the dialog contains a choice button with `IsCancel = true`, pressing Escape returns that button's `Result` value. If no choice button has `IsCancel = true`, pressing Escape does nothing, and the dialog remains open.

See also: [Handle a Dismissed Dialog](#handle-a-dismissed-dialog).

**Exceptions:**

- `ArgumentNullException` — The `message` or `choices` parameter  is `null`.
- `ArgumentException` — The `choices` list is empty. A dialog must contain at least one button.


## DialogChoice<T>

Each choice button in the dialog is described by a `DialogChoice<T>` instance:

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

## How to Use IChoiceDialogService

In your ViewModel, call the `IChoiceDialogService.Show` method to display the dialog with specified choice buttons. The method returns the `Result` value of the pressed choice button.

### Access the Service

There are two ways to access an `IChoiceDialogService` object in a ViewModel:

- Through the `Service<T>()` helper method. This is a convenient approach to obtain registered application services shipped with the Eremex Controls library.
- Through constructor injection.

#### Service<T>() Helper

Implement a helper `Service<T>()` method in your ViewModel to get a requested service using the static `ApplicationServicesContext.GetRequiredService<T>()` method.

##### Example - Show a Dialog Using Service<T>() Helper

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

In the App.axaml.cs file, ensure that Eremex application services are registered using `SimpleServiceProvider` and `ApplicationServicesContext` as follows:

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

Implement a constructor in your ViewModel with `IChoiceDialogService` as a parameter. When you instantiate the ViewModel, pass the service object to this constructor.

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



### Return a String Result

To return a string value when a dialog button is clicked, use `DialogChoice<string>` for that button. The value associated with this button is specified by the _result_ parameter of the `DialogChoice<T>` constructor.

The following example shows a dialog with three buttons. Specific dialog results (string values — "log", "retry", and "close") are associated with these buttons. The dialog's `Show` method returns a corresponding value when one of its buttons is clicked.

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



### Return a Boolean Result

To return a Boolean value when a dialog button is clicked, use `DialogChoice<bool>` for that button. The value associated with this button is specified by the _result_ parameter of the `DialogChoice<T>` constructor.

The following example shows a dialog with two buttons. Specific dialog results (`true` and `false`) are associated with these buttons. The dialog's `Show` method returns a corresponding value when one of its buttons is clicked.

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

See also: [Handle a Dismissed Dialog](#handle-a-dismissed-dialog).


### Return an Enum Result

To return an enumeration value when a dialog button is clicked, use `DialogChoice< enum >` for that button. The value associated with this button is specified by the _result_ parameter of the `DialogChoice<T>` constructor.

The following example shows a dialog with three buttons. Specific dialog results (`DialogResult.Abort`, `DialogResult.Retry`, and `DialogResult.Ignore`) are associated with these buttons. The dialog's `Show` method returns a corresponding value when one of its buttons is clicked.

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



### Set Button Placement

Use the `DialogChoice<T>.Dock` property to forcibly position specific buttons first (set the `Dock` property to `DockType.Left`) or last (set the `Dock` property to `DockType.Right`) among all buttons. The `Dock` property defaults to `DockType.Right`.

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




## Handle a Dismissed Dialog

When the user dismisses the dialog by clicking the caption 'x' button, the `Show` method returns `default(T)`:

- For reference types (`string`, etc.), the result is `null`.
- For value types (`bool`, enums, etc.), the result is the default value of the type (`false` for a Boolean type, `0` for an enumeration, etc.)


If the dialog contains a cancel button (a choice button whose `IsCancel` property is `true`), clicking it or pressing Escape closes the dialog with that button's result. The caption 'x' button still closes the dialog with the `default(T)` result.

### Example — Handle a Dialog's Dismissal

The following example creates a dialog with a cancel button associated with the `null` dialog result. In this case, you only need to check for the `null` dialog result to handle all dialog dismissal scenarios:

- The cancel button is clicked.
- The `x` caption button is clicked.
- The Escape key is pressed.

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

