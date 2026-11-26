# MessageBoxServiceExtensions.Show 方法（1/6）

显示一个带有给定文本、无标题、带“确定”按钮且无图标的消息框。

**命名空间：** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**程序集：** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## 声明

```csharp
public static DialogResult Show(this IMessageBoxService service, string text)
```

## 参数

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| service | `IMessageBoxService` | 消息框服务。 |
| text | `string` | 要显示的消息。 |

## 返回值

| 类型 | 说明 |
| --- | --- |
| `DialogResult` | 关闭消息框所用的按钮。 |

## 另请参阅

* 类 [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* 命名空间 [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# MessageBoxServiceExtensions.Show 方法（2/6）

显示一个带有给定文本和标题、带“确定”按钮且无图标的消息框。

**命名空间：** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**程序集：** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## 声明

```csharp
public static DialogResult Show(this IMessageBoxService service, string text, string caption)
```

## 参数

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| service | `IMessageBoxService` | 消息框服务。 |
| text | `string` | 要显示的消息。 |
| caption | `string` | 窗口标题。 |

## 返回值

| 类型 | 说明 |
| --- | --- |
| `DialogResult` | 关闭消息框所用的按钮。 |

## 另请参阅

* 类 [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* 命名空间 [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# MessageBoxServiceExtensions.Show 方法（3/6）

显示一个带有给定文本、标题和按钮且无图标的消息框。

**命名空间：** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**程序集：** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## 声明

```csharp
public static DialogResult Show(this IMessageBoxService service, string text, string caption, 
    MessageBoxButtons buttons)
```

## 参数

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| service | `IMessageBoxService` | 消息框服务。 |
| text | `string` | 要显示的消息。 |
| caption | `string` | 窗口标题。 |
| buttons | `MessageBoxButtons` | 要提供的按钮。 |

## 返回值

| 类型 | 说明 |
| --- | --- |
| `DialogResult` | 关闭消息框所用的按钮。 |

## 另请参阅

* 类 [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* 命名空间 [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# MessageBoxServiceExtensions.Show 方法（4/6）

显示一个带“确定”按钮且无图标的模态消息框，其所有者为给定的 Avalonia 顶级窗口。

**命名空间：** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**程序集：** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## 声明

```csharp
public static DialogResult Show(this IMessageBoxService service, TopLevel? owner, string text, 
    string caption = "")
```

## 参数

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| service | `IMessageBoxService` | 消息框服务。 |
| owner | `TopLevel?` | 消息框所依附的窗口（顶级窗口）。 |
| text | `string` | 要显示的消息。 |
| caption | `string` | 窗口标题。 |

## 返回值

| 类型 | 说明 |
| --- | --- |
| `DialogResult` | 关闭消息框所用的按钮。 |

## 另请参阅

* 类 [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* 命名空间 [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# MessageBoxServiceExtensions.Show 方法（5/6）

显示一个无图标的模态消息框，其所有者为给定的 Avalonia 顶级窗口。

**命名空间：** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**程序集：** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## 声明

```csharp
public static DialogResult Show(this IMessageBoxService service, TopLevel? owner, string text, 
    string caption, MessageBoxButtons buttons)
```

## 参数

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| service | `IMessageBoxService` | 消息框服务。 |
| owner | `TopLevel?` | 消息框所依附的窗口（顶级窗口）。 |
| text | `string` | 要显示的消息。 |
| caption | `string` | 窗口标题。 |
| buttons | `MessageBoxButtons` | 要提供的按钮。 |

## 返回值

| 类型 | 说明 |
| --- | --- |
| `DialogResult` | 关闭消息框所用的按钮。 |

## 另请参阅

* 类 [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* 命名空间 [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# MessageBoxServiceExtensions.Show 方法（6/6）

显示一个模态消息框，其所有者为给定的 Avalonia 顶级窗口；如果为 `null`，则由活动应用程序窗口作为所有者。

**命名空间：** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**程序集：** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## 声明

```csharp
public static DialogResult Show(this IMessageBoxService service, TopLevel? owner, string text, 
    string caption, MessageBoxButtons buttons, MessageBoxIcon icon)
```

## 参数

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| service | `IMessageBoxService` | 消息框服务。 |
| owner | `TopLevel?` | 消息框所依附的窗口（顶级窗口）。 |
| text | `string` | 要显示的消息。 |
| caption | `string` | 窗口标题。 |
| buttons | `MessageBoxButtons` | 要提供的按钮。 |
| icon | `MessageBoxIcon` | 要显示的图标。 |

## 返回值

| 类型 | 说明 |
| --- | --- |
| `DialogResult` | 关闭消息框所用的按钮。 |

## 另请参阅

* 类 [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* 命名空间 [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.ApplicationServices.dll -->

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
