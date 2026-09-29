---
title: Шаблоны проектов
order: 900
seealso: []
---

# Шаблоны проектов

[NuGet-пакет](https://www.nuget.org/profiles/EremexControls) **Eremex.Avalonia.Templates** содержит шаблоны для быстрого создания новых проектов Avalonia UI с использованием контролов Eremex.

## Установка шаблонов Eremex Avalonia

Выполните следующую команду:

<code>
dotnet new install Eremex.Avalonia.Templates
</code>

## Обновление шаблонов Eremex Avalonia

Чтобы обновиться до последней версии, выполните команду установки шаблонов:

<code>
dotnet new install Eremex.Avalonia.Templates
</code>

## Включённые шаблоны

### `eremex.avalonia.app`

Этот шаблон приложения создаёт пустой проект Avalonia UI, ссылающийся на библиотеку Eremex Controls. Шаблон выполняет следующее:

- Добавляет в проект NuGet-пакеты Eremex: 
    
    - **Eremex.Avalonia.Controls**
    - **Eremex.Avalonia.Themes.DeltaDesign**

- Использует класс `MxWindow` в качестве главного окна проекта. Окно `MxWindow` обеспечивает поддержку визуальных тем Eremex.
- [Регистрирует](../controls/themes/register-an-eremex-paint-theme.md) визуальную тему Eremex `DeltaDesign`. 


### `eremex.avalonia.mvvm`

Этот шаблон приложения создаёт проект Avalonia UI с поддержкой MVVM, ссылающийся на библиотеку Eremex Controls. Шаблон разделяет код на View (_MainWindow_) и ViewModel (_MainWindowViewModel_).
Остальные возможности этого шаблона совпадают с шаблоном `eremex.avalonia.app`.

### `eremex.avalonia.window`


Шаблон, создающий новое окно Avalonia на основе `MxWindow`. Этот шаблон создаёт только два файла, определяющих окно: _Window.axaml_ и _Window.axaml.cs_.


## Создание нового проекта из шаблона с помощью командной строки

Перейдите в папку, в которой нужно создать проект. Используйте команду <code>dotnet new _template-name_</code>, чтобы создать новый проект из указанного шаблона. Чтобы задать имя проекта, используйте параметр команды <code>-n _name_</code>.

Следующая команда создаёт новый проект _AvaloniaApplication1_ на основе шаблона `eremex.avalonia.mvvm`.

<code>
dotnet new eremex.avalonia.mvvm -n AvaloniaApplication1 
</code>


Откройте созданный проект в Visual Studio.


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
