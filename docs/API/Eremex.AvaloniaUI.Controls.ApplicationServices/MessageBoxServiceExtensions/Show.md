# MessageBoxServiceExtensions.Show method (1 of 6)

Shows a message box with the given text, no caption, an OK button and no icon.

**Namespace:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Assembly:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Declaration

```csharp
public static DialogResult Show(this IMessageBoxService service, string text)
```

## Parameters

| name | type | description |
| --- | --- | --- |
| service | `IMessageBoxService` | The message box service. |
| text | `string` | The message to show. |

## Returns

| type | description |
| --- | --- |
| `DialogResult` | The button the message box was closed with. |

## See Also

* class [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* namespace [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# MessageBoxServiceExtensions.Show method (2 of 6)

Shows a message box with the given text and caption, an OK button and no icon.

**Namespace:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Assembly:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Declaration

```csharp
public static DialogResult Show(this IMessageBoxService service, string text, string caption)
```

## Parameters

| name | type | description |
| --- | --- | --- |
| service | `IMessageBoxService` | The message box service. |
| text | `string` | The message to show. |
| caption | `string` | The window caption. |

## Returns

| type | description |
| --- | --- |
| `DialogResult` | The button the message box was closed with. |

## See Also

* class [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* namespace [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# MessageBoxServiceExtensions.Show method (3 of 6)

Shows a message box with the given text, caption and buttons, and no icon.

**Namespace:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Assembly:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Declaration

```csharp
public static DialogResult Show(this IMessageBoxService service, string text, string caption, 
    MessageBoxButtons buttons)
```

## Parameters

| name | type | description |
| --- | --- | --- |
| service | `IMessageBoxService` | The message box service. |
| text | `string` | The message to show. |
| caption | `string` | The window caption. |
| buttons | `MessageBoxButtons` | The buttons to offer. |

## Returns

| type | description |
| --- | --- |
| `DialogResult` | The button the message box was closed with. |

## See Also

* class [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* namespace [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# MessageBoxServiceExtensions.Show method (4 of 6)

Shows a modal message box with an OK button and no icon, owned by the given Avalonia top level.

**Namespace:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Assembly:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Declaration

```csharp
public static DialogResult Show(this IMessageBoxService service, TopLevel? owner, string text, 
    string caption = "")
```

## Parameters

| name | type | description |
| --- | --- | --- |
| service | `IMessageBoxService` | The message box service. |
| owner | `TopLevel?` | The window (top level) to show the message box over. |
| text | `string` | The message to show. |
| caption | `string` | The window caption. |

## Returns

| type | description |
| --- | --- |
| `DialogResult` | The button the message box was closed with. |

## See Also

* class [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* namespace [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# MessageBoxServiceExtensions.Show method (5 of 6)

Shows a modal message box with no icon, owned by the given Avalonia top level.

**Namespace:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Assembly:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Declaration

```csharp
public static DialogResult Show(this IMessageBoxService service, TopLevel? owner, string text, 
    string caption, MessageBoxButtons buttons)
```

## Parameters

| name | type | description |
| --- | --- | --- |
| service | `IMessageBoxService` | The message box service. |
| owner | `TopLevel?` | The window (top level) to show the message box over. |
| text | `string` | The message to show. |
| caption | `string` | The window caption. |
| buttons | `MessageBoxButtons` | The buttons to offer. |

## Returns

| type | description |
| --- | --- |
| `DialogResult` | The button the message box was closed with. |

## See Also

* class [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* namespace [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# MessageBoxServiceExtensions.Show method (6 of 6)

Shows a modal message box owned by the given Avalonia top level; when it is `null`, the active application window owns it.

**Namespace:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Assembly:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Declaration

```csharp
public static DialogResult Show(this IMessageBoxService service, TopLevel? owner, string text, 
    string caption, MessageBoxButtons buttons, MessageBoxIcon icon)
```

## Parameters

| name | type | description |
| --- | --- | --- |
| service | `IMessageBoxService` | The message box service. |
| owner | `TopLevel?` | The window (top level) to show the message box over. |
| text | `string` | The message to show. |
| caption | `string` | The window caption. |
| buttons | `MessageBoxButtons` | The buttons to offer. |
| icon | `MessageBoxIcon` | The icon to show. |

## Returns

| type | description |
| --- | --- |
| `DialogResult` | The button the message box was closed with. |

## See Also

* class [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* namespace [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.ApplicationServices.dll -->
