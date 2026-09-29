---
title: Регистрация визуальной темы Eremex
order: 200
seealso: []
---

# Регистрация визуальной темы Eremex

Вам необходимо добавить визуальные темы Eremex в ваш проект и зарегистрировать их, чтобы контролы Eremex отрисовывались корректно. Если визуальная тема Eremex не найдена, соответствующие контролы Eremex отображаются пустыми.

Библиотека контролов Eremex включает следующие визуальные темы:

| Тема&nbsp;оформления | Описание | Пакет |
| --- | --- | --- |
| `DeltaDesign` | Содержит визуальные настройки для контролов Eremex (кроме `Graphics3DControl`) и набора стандартных контролов Avalonia UI. | пакет `Eremex.Avalonia.Themes.DeltaDesign` |
| `Controls3D` | Содержит визуальные настройки для `Graphics3DControl`. | пакет `Eremex.Avalonia.Controls3D` |


## Добавление NuGet-пакета с темой в ваш проект

- Если вы используете любой контрол Eremex (кроме `Graphics3DControl`), добавьте пакет `Eremex.Avalonia.Themes.DeltaDesign` в ваш проект. 

- Если вы используете `Graphics3DControl`, дополнительный пакет с темой не требуется. Тема `Controls3D` реализована в пакете `Eremex.Avalonia.Controls3D`, который содержит сам контрол.

## Какую тему регистрировать

- Если вы используете любой контрол Eremex, кроме `Graphics3DControl`, вам нужно зарегистрировать только тему `DeltaDesign`. 

- Если вы используете только `Graphics3DControl`, вам нужно зарегистрировать только тему `Controls3D`.

- Если вы используете `Graphics3DControl` вместе с другими контролами Eremex, зарегистрируйте обе темы.

- Визуальная тема `DeltaDesign` также включает стили для распространённых стандартных контролов Avalonia. Если вы используете стандартные контролы Avalonia, не поддерживаемые темой `DeltaDesign`, вам также необходимо зарегистрировать тему `Fluent`. См. [Регистрация темы 'FluentTheme' для стандартных контролов Avalonia](#регистрация-темы-fluenttheme-для-стандартных-контролов-avalonia).


## Регистрация визуальных тем Eremex


- Откройте файл _App.axaml_ в вашем проекте.
- Добавьте необходимые пространства имён тем в объект `Application`:

    ``` xml
    <!-- App.axaml file -->
    <Application ...
        xmlns:theme="clr-namespace:Eremex.AvaloniaUI.Themes.DeltaDesign;assembly=Eremex.Avalonia.Themes.DeltaDesign"

        xmlns:theme3D="clr-namespace:Eremex.AvaloniaUI.Themes.Controls3D;assembly=Eremex.Avalonia.Controls3D"
    >
    ```
  
- Зарегистрируйте тему `DeltaDesign` и/или `Controls3D` в коллекции `Application.Styles`:

    ``` xml
    <Application 
        xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        x:Class="DemoCenter.App"
        xmlns:theme="clr-namespace:Eremex.AvaloniaUI.Themes.DeltaDesign;assembly=Eremex.Avalonia.Themes.DeltaDesign"
        xmlns:theme3D="clr-namespace:Eremex.AvaloniaUI.Themes.Controls3D;assembly=Eremex.Avalonia.Controls3D"
        RequestedThemeVariant="Light"
    >
    <!-- "Default" - The application's theme variant is defined by the system setting. 
        "Light" - Enables the Light theme variant.
        "Dark" - Enables the Dark theme variant. 
    -->
        <!-- .... -->
        <Application.Styles>
            <FluentTheme/>
            <theme:DeltaDesignTheme/>
            <theme3D:Controls3DTheme />
            <!-- .... -->
        </Application.Styles>
    </Application>
    ```

## Регистрация темы 'FluentTheme' для стандартных контролов Avalonia

Визуальная тема `Eremex.Avalonia.Themes.DeltaDesign` определяет стили для распространённых стандартных контролов Avalonia, обеспечивая их единообразную отрисовку с визуальной темой `DeltaDesign`. Стандартные контролы Avalonia, поддерживаемые темой `DeltaDesign`, включают, но не ограничиваются: 
Button, 
Calendar, 
CheckBox, 
ContextMenu, 
Label, 
ListBox, 
NotificationCard, 
ProgressBar, 
RadioButton, 
ScrollBar, 
ScrollViewer, 
Separator, 
Slider, 
TextBox, 
ToggleButton, 
ToggleSwitch, 
ToolTip, 
UserControl и 
WindowNotificationManager.

Полный список поддерживаемых стандартных контролов Avalonia смотрите в исходном коде темы: [Eremex Controls Themes](https://github.com/Eremex/controlthemes)

Чтобы обеспечить корректную отрисовку стандартных контролов Avalonia, не поддерживаемых темой `DeltaDesign`, включите тему `FluentTheme` в ваш проект. Визуальные темы Eremex должны быть зарегистрированы после темы `FluentTheme`:

``` xml
<!-- App.axaml file -->
<Application.Styles>
    <FluentTheme/>
    <theme:DeltaDesignTheme/>
</Application.Styles>
```

## Выбор светлого или тёмного варианта темы

Визуальные темы Eremex поддерживают два цветовых варианта — светлый и тёмный.

Установите свойство `Application.RequestedThemeVariant` (например, в файле _App.axaml_), чтобы задать цветовой вариант темы.

``` xml
<Application 
    RequestedThemeVariant="Default" ... >
    <!-- "Default" - The application's theme is defined by the system setting. 
         "Light" - Enables the Light theme.
         "Dark" - Enables the Dark theme. 
    -->
</Application>
```


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
