# Метод MessageBoxServiceExtensions.Show (1 из 6)

Показывает окно сообщения с заданным текстом, без заголовка, с кнопкой OK и без значка.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Сборка:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Объявление

```csharp
public static DialogResult Show(this IMessageBoxService service, string text)
```

## Параметры

| имя | тип | описание |
| --- | --- | --- |
| service | `IMessageBoxService` | Сервис окна сообщения. |
| text | `string` | Показываемое сообщение. |

## Возвращаемое значение

| тип | описание |
| --- | --- |
| `DialogResult` | Кнопка, которой было закрыто окно сообщения. |

## См. также

* класс [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* пространство имён [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# Метод MessageBoxServiceExtensions.Show (2 из 6)

Показывает окно сообщения с заданными текстом и заголовком, с кнопкой OK и без значка.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Сборка:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Объявление

```csharp
public static DialogResult Show(this IMessageBoxService service, string text, string caption)
```

## Параметры

| имя | тип | описание |
| --- | --- | --- |
| service | `IMessageBoxService` | Сервис окна сообщения. |
| text | `string` | Показываемое сообщение. |
| caption | `string` | Заголовок окна. |

## Возвращаемое значение

| тип | описание |
| --- | --- |
| `DialogResult` | Кнопка, которой было закрыто окно сообщения. |

## См. также

* класс [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* пространство имён [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# Метод MessageBoxServiceExtensions.Show (3 из 6)

Показывает окно сообщения с заданными текстом, заголовком и кнопками, без значка.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Сборка:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Объявление

```csharp
public static DialogResult Show(this IMessageBoxService service, string text, string caption, 
    MessageBoxButtons buttons)
```

## Параметры

| имя | тип | описание |
| --- | --- | --- |
| service | `IMessageBoxService` | Сервис окна сообщения. |
| text | `string` | Показываемое сообщение. |
| caption | `string` | Заголовок окна. |
| buttons | `MessageBoxButtons` | Предлагаемые кнопки. |

## Возвращаемое значение

| тип | описание |
| --- | --- |
| `DialogResult` | Кнопка, которой было закрыто окно сообщения. |

## См. также

* класс [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* пространство имён [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# Метод MessageBoxServiceExtensions.Show (4 из 6)

Показывает модальное окно сообщения с кнопкой OK и без значка, владельцем которого является указанное окно верхнего уровня Avalonia.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Сборка:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Объявление

```csharp
public static DialogResult Show(this IMessageBoxService service, TopLevel? owner, string text, 
    string caption = "")
```

## Параметры

| имя | тип | описание |
| --- | --- | --- |
| service | `IMessageBoxService` | Сервис окна сообщения. |
| owner | `TopLevel?` | Окно (верхнего уровня), поверх которого показывается окно сообщения. |
| text | `string` | Показываемое сообщение. |
| caption | `string` | Заголовок окна. |

## Возвращаемое значение

| тип | описание |
| --- | --- |
| `DialogResult` | Кнопка, которой было закрыто окно сообщения. |

## См. также

* класс [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* пространство имён [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# Метод MessageBoxServiceExtensions.Show (5 из 6)

Показывает модальное окно сообщения без значка, владельцем которого является указанное окно верхнего уровня Avalonia.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Сборка:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Объявление

```csharp
public static DialogResult Show(this IMessageBoxService service, TopLevel? owner, string text, 
    string caption, MessageBoxButtons buttons)
```

## Параметры

| имя | тип | описание |
| --- | --- | --- |
| service | `IMessageBoxService` | Сервис окна сообщения. |
| owner | `TopLevel?` | Окно (верхнего уровня), поверх которого показывается окно сообщения. |
| text | `string` | Показываемое сообщение. |
| caption | `string` | Заголовок окна. |
| buttons | `MessageBoxButtons` | Предлагаемые кнопки. |

## Возвращаемое значение

| тип | описание |
| --- | --- |
| `DialogResult` | Кнопка, которой было закрыто окно сообщения. |

## См. также

* класс [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* пространство имён [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

---

# Метод MessageBoxServiceExtensions.Show (6 из 6)

Показывает модальное окно сообщения, владельцем которого является указанное окно верхнего уровня Avalonia; если оно равно `null`, владельцем становится активное окно приложения.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.ApplicationServices`](../index.md)  
**Сборка:** `Eremex.Avalonia.Controls.ApplicationServices.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls.ApplicationServices](https://www.nuget.org/packages/Eremex.Avalonia.Controls.ApplicationServices)

## Объявление

```csharp
public static DialogResult Show(this IMessageBoxService service, TopLevel? owner, string text, 
    string caption, MessageBoxButtons buttons, MessageBoxIcon icon)
```

## Параметры

| имя | тип | описание |
| --- | --- | --- |
| service | `IMessageBoxService` | Сервис окна сообщения. |
| owner | `TopLevel?` | Окно (верхнего уровня), поверх которого показывается окно сообщения. |
| text | `string` | Показываемое сообщение. |
| caption | `string` | Заголовок окна. |
| buttons | `MessageBoxButtons` | Предлагаемые кнопки. |
| icon | `MessageBoxIcon` | Показываемый значок. |

## Возвращаемое значение

| тип | описание |
| --- | --- |
| `DialogResult` | Кнопка, которой было закрыто окно сообщения. |

## См. также

* класс [MessageBoxServiceExtensions](../MessageBoxServiceExtensions.md)
* пространство имён [Eremex.AvaloniaUI.Controls.ApplicationServices](../index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.ApplicationServices.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
