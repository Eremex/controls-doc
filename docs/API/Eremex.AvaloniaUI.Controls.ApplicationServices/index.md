## Eremex.AvaloniaUI.Controls.ApplicationServices namespace

| public type | description |
| --- | --- |
| class [AppearanceService](./AppearanceService.md) | The default IAppearanceService implementation, driving the appearance of the running Application. |
| static class [ApplicationServicesContext](./ApplicationServicesContext.md) | Ambient access to the application services and the description of their composition. |
| abstract class [AvaloniaStorageDialogBase](./AvaloniaStorageDialogBase.md) | Base class for the storage picker dialogs used by the file dialog services. It carries the settings every picker shares — caption and start folder — and turns them into the Avalonia storage provider options. |
| class [ChoiceDialogService](./ChoiceDialogService.md) | IChoiceDialogService implementation built on top of IDialogService. |
| class [DensityOption](./DensityOption.md) | A layout density offered by [`AppearanceService`](./AppearanceService.md). |
| abstract class [DialogAwareViewModel](./DialogAwareViewModel.md) | Base class for view models shown as modal dialogs by IDialogService. On top of [`WindowAwareViewModel`](./WindowAwareViewModel.md) it builds the dialog buttons when the window opens. |
| enum [DialogButtonType](./DialogButtonType.md) | Type of dialog button |
| class [DialogButtonViewModel](./DialogButtonViewModel.md) | The standard IDialogButtonViewModel implementation. Use the `Create*` factory methods for the common buttons — they apply the right caption, style classes and default/cancel behaviour — and return the results from CreateButtons. |
| class [DialogChoice&lt;T&gt;](./DialogChoice-1.md) | A single choice in a dialog: the button caption and the result returned when it is pressed. |
| enum [DialogResult](./DialogResult.md) | Identifies the button a modal dialog or message box was closed with. |
| class [DialogService](./DialogService.md) | The default IDialogService implementation. It hosts the view model in a [`DialogWindow`](./DialogWindow.md), attaches the view model for as long as the dialog is open, and picks the owner window through IWindowsManager. |
| class [DialogWindow](./DialogWindow.md) | The window that hosts a view model shown through IDialogService or IWindowService. It renders Content in the body and the buttons of ButtonsSource in the footer, sizing itself to its content. The services create it for you; there is normally no reason to instantiate it directly. |
| static class [DialogWindowClasses](./DialogWindowClasses.md) | Names of the style classes a dialog window recognises. Pass them to [`ViewLocatorAttribute`](./ViewLocatorAttribute.md) to pick the appearance of the window that hosts a view model, instead of repeating the literal strings at every call site. |
| enum [DockType](./DockType.md) | Docking direction for dialog buttons |
| class [FileDialogFileType](./FileDialogFileType.md) | One file type offered by a file dialog: a display name and the patterns it matches. |
| enum [FileDialogFolder](./FileDialogFolder.md) | A folder a file dialog can be pointed at without knowing its path. |
| interface [IActionWindow](./IActionWindow.md) | Marker interface for windows that support actions (dialogs, etc.) |
| interface [IAppearanceOption](./IAppearanceOption.md) | One choice offered by [`IAppearanceService`](./IAppearanceService.md): a light/dark variant, a colour palette or a layout density. |
| interface [IAppearanceService](./IAppearanceService.md) | Lists the appearance choices an application offers and applies the chosen one. |
| interface [IChoiceDialogService](./IChoiceDialogService.md) | Shows a dialog with an arbitrary set of buttons and returns the result of the pressed one. |
| interface [IDialogAwareViewModel](./IDialogAwareViewModel.md) | Implemented by view models shown as modal dialogs through [`IDialogService`](./IDialogService.md). It adds the dialog buttons to what [`IWindowAwareViewModel`](./IWindowAwareViewModel.md) already describes. |
| interface [IDialogButtonViewModel](./IDialogButtonViewModel.md) | Describes a single button in a dialog footer: what it looks like, where it sits, and what it does when pressed. A dialog exposes its buttons through [`ButtonsSource`](./IDialogAwareViewModel/ButtonsSource.md). |
| interface [IDialogService](./IDialogService.md) | Shows application dialogs from view model code, so that a view model can ask the user a question without referencing any window type. The view that hosts the view model is located through [`ViewLocatorAttribute`](./ViewLocatorAttribute.md), and the owner window is chosen by the implementation. |
| interface [IMessageBoxService](./IMessageBoxService.md) | Shows standard message boxes — a short piece of text, an icon and a fixed set of buttons — from view model code that must not reference any window type. |
| interface [IOpenFileDialogService](./IOpenFileDialogService.md) | Shows the platform open file dialog from view model code that must not reference any window type. |
| interface [ISaveFileDialogService](./ISaveFileDialogService.md) | Shows the platform save file dialog from view model code that must not reference any window type. |
| interface [IWindow](./IWindow.md) | An application window, as the services here see it. A view model receives one from [`IWindowsManager`](./IWindowsManager.md) and hands it back as the owner of the dialog it asks for, without ever naming a window type of the UI framework. |
| interface [IWindowAwareViewModel](./IWindowAwareViewModel.md) | Implemented by view models that are shown in a window of their own. The window services call [`Attach`](./IWindowAwareViewModel/Attach.md) before showing the window and [`Detach`](./IWindowAwareViewModel/Detach.md) after it closes, which lets the view model observe its window without depending on any window type. |
| interface [IWindowService](./IWindowService.md) | Shows non-modal application windows from view model code, so that a view model can open a window without referencing any window type. The counterpart for modal dialogs is [`IDialogService`](./IDialogService.md). |
| interface [IWindowsManager](./IWindowsManager.md) | Tracks the windows of the application so that the other services know which window a new dialog belongs to. Implementations follow window activation and closing, which is why a single instance should live for the whole application. |
| class [MessageBoxService](./MessageBoxService.md) | The default IMessageBoxService implementation. It resolves the owner window through IWindowsManager and shows the Eremex message box. |
| abstract class [OkCancelDialogAwareViewModel](./OkCancelDialogAwareViewModel.md) | Base class for a dialog with the usual OK and Cancel buttons already wired up: OK closes the dialog with Ok, Cancel closes it with Cancel. |
| class [OpenFileDialogOptions](./OpenFileDialogOptions.md) | Configures the open file dialog shown by [`IOpenFileDialogService`](./IOpenFileDialogService.md). Every property is optional; leaving one unset keeps the platform default. |
| class [OpenFileDialogService](./OpenFileDialogService.md) | The default IOpenFileDialogService implementation. It resolves the owner window through IWindowsManager and shows the platform open file dialog. |
| class [PaletteOption](./PaletteOption.md) | A colour palette offered by [`AppearanceService`](./AppearanceService.md). |
| class [SaveFileDialogOptions](./SaveFileDialogOptions.md) | Configures the save file dialog shown by [`ISaveFileDialogService`](./ISaveFileDialogService.md). Every property is optional; leaving one unset keeps the platform default. |
| class [SaveFileDialogService](./SaveFileDialogService.md) | The default ISaveFileDialogService implementation. It resolves the owner window through IWindowsManager and shows the platform save file dialog. |
| class [SimpleServiceProvider](./SimpleServiceProvider.md) | A minimal IServiceProvider implementation with no dependency on any DI container. Intended for applications and tests that do not need a full container. Applications with a container register the services their own way, see [`RegisterApplicationServices`](./ApplicationServicesContext/RegisterApplicationServices.md). |
| class [ThemeOption](./ThemeOption.md) | A light/dark variant offered by [`AppearanceService`](./AppearanceService.md). |
| class [ViewLocatorAttribute](./ViewLocatorAttribute.md) | Applied to a view model to declare which view renders it and how the hosting window should look. The window services read this attribute when a view model is shown, create the view and put it in [`Content`](./IWindowAwareViewModel/Content.md), so the view model never has to construct its own view. |
| class [WindowAwareViewModel](./WindowAwareViewModel.md) | Base class for view models that are shown in a window of their own by IWindowService or IDialogService. It tracks the window the view model is attached to, closes it on request, and creates the view declared by ViewLocatorAttribute. |
| static class [WindowInterop](./WindowInterop.md) | Translates between the framework free IWindow contract and the Avalonia window. |
| class [WindowManager](./WindowManager.md) | The default IWindowsManager implementation. It follows window activation to know which window is active, and disables the windows behind a modal dialog so that only the dialog can be interacted with — using the platform mechanism on Windows and X11 where one is available. |
| class [WindowService](./WindowService.md) | The default IWindowService implementation. It hosts the view model in a [`DialogWindow`](./DialogWindow.md) shown non-modally, and detaches the view model automatically once the window closes — including when the user closes it through the caption button. |

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.ApplicationServices.dll -->
<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Common.Contracts.dll -->
