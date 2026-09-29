---
title: Начало работы с EMX Controls в ALT Linux
order: 1500
seealso: []
---

# Начало работы с Eremex Avalonia UI Controls в ALT Linux

Это руководство проведёт вас через создание приложения Avalonia UI с контролами Eremex в ALT Linux. Сначала мы настроим окружение для разработки .NET-приложений, а затем создадим проект с контролом EMX DataGrid.


## 1. Предварительные требования

Убедитесь, что в ALT Linux установлены .NET SDK и Visual Studio Code. В следующих разделах показано, как установить их из командной строки.

### 1.1 Установка .NET SDK

Для разработки .NET-приложений в ALT Linux установите пакет .NET SDK. Например, чтобы установить .NET 8 SDK, выполните в терминале следующую команду:

``` sh
sudo apt-get install dotnet-sdk-8.0
```

### 1.2 Установка Visual Studio Code и расширения C# Dev Kit

Инструкции по установке VS Code в ALT Linux смотрите здесь: [Education applications: VS Code](https://www.altlinux.org/Education_applications/Vscode).

Кроме того, можно загрузить RPM-пакет VS Code со страницы [Download Visual Studio Code](https://code.visualstudio.com/Download), а затем установить его следующей командой:

``` sh
sudo apt-get install code_xxx.rpm
```

(Замените `code_xxx.rpm` фактическим именем загруженного пакета.)

Запустите VS Code и установите дополнение `C# Dev Kit` на вкладке Extensions.

![get-started-alt-vscode-cDevkit](../images/get-started-alt-vscode-cDevkit.png)


## 2. Установка шаблонов проектов Eremex

Библиотека EMX Controls включает набор [шаблонов проектов](../whats-included/project-templates.md), которые помогают создавать новые проекты Avalonia с EMX Controls. Установите эти шаблоны, выполнив в терминале следующую команду:

``` sh
dotnet new install Eremex.Avalonia.Templates
```

## 3. Создание нового проекта

Перейдите в каталог, в котором вы хотите создать проект. Выполните команду ниже, чтобы создать проект с поддержкой MVVM под именем _AvaloniaApplication1_ по шаблону `eremex.avalonia.mvvm`. 

``` sh
dotnet new eremex.avalonia.mvvm -n AvaloniaApplication1
```

Если вы столкнётесь с предупреждениями о сертификатах для `nuget.org`, вам следует вручную добавить необходимые корневые сертификаты в вашу ОС. Чтобы временно обойти проверку сертификатов, выполните следующую команду:

``` sh
DOTNET_NUGET_SIGNATURE_VERIFICATION=false dotnet new eremex.avalonia.mvvm -n AvaloniaApplication1
```

Сгенерированный проект включает:

- Все необходимые ссылки на пакеты контролов Eremex
- Тему оформления _'DeltaDesign'_ [paint theme](../controls/themes/index.md), зарегистрированную в `App.axaml`.
- [MxWindow](../controls/windows-and-dialogs/mxwindow.md), используемый в качестве главного окна приложения. `MxWindow` — это специализированное окно, которое отрисовывает свои элементы (фон, рамку и заголовок) в соответствии с текущей визуальной темой Eremex. 

## 4. Открытие проекта в VS Code

В VS Code откройте сгенерированную папку _AvaloniaApplication1_.

Перейдите на вкладку `Run and Debug` (Ctrl+Shift+D) и нажмите кнопку `Run and Debug`:

![get-started-alt-vscode-runanddebug](../images/get-started-alt-vscode-runanddebug.png)

Выберите `c#` в качестве окружения отладки:

![get-started-alt-vscode-csharp-debugger](../images/get-started-alt-vscode-csharp-debugger.png)

Выберите `C#: Launch Startup Project`:

![get-started-alt-vscode-launch-conf](../images/get-started-alt-vscode-launch-conf.png)

Выберите `AvaloniaApplication1.csproj` в качестве стартового проекта:

![get-started-alt-vscode-startup-project](../images/get-started-alt-vscode-startup-project.png)

После этого VS Code соберёт и запустит проект.

![get-started-alt-empty-app](../images/get-started-alt-empty-app.png)

Проект также можно запустить из терминала следующей командой:

``` sh
dotnet run
```


## 5. Выбор светлого или тёмного варианта визуальной темы 

Шаблоны приложений Eremex автоматически добавляют в созданный проект код регистрации визуальной темы `DeltaDesign`. Откройте файл _App.axaml_, чтобы найти этот код в определении объекта `Application`.

Визуальная тема `DeltaDesign` поддерживает варианты `Light` и `Dark`. Используйте свойство `Application.RequestedThemeVariant`, чтобы задать нужный вариант темы.

``` xml
<Application xmlns="https://github.com/avaloniaui"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    x:Class="AvaloniaApplication1.App"
    xmlns:local="using:AvaloniaApplication1"
    xmlns:theme=
    "clr-namespace:Eremex.AvaloniaUI.Themes.DeltaDesign;assembly=Eremex.Avalonia.Themes.DeltaDesign"
    RequestedThemeVariant="Light">
  <!-- "Default" - The application's theme variant is defined by the system setting. 
       "Light" - Enables the Light theme variant.
       "Dark" - Enables the Dark theme variant. 
  -->
    <!-- .... -->
    <Application.Styles>
        <theme:DeltaDesignTheme/>
        <!-- .... -->
    </Application.Styles>
</Application>
```

<br>

В разделах ниже мы добавим контрол Eremex `DataGridControl` в View и привяжем его к коллекции _Employees_, определённой во View Model.

## 6. Определение данных для Data Grid

Откройте главную View Model (_MainWindowViewModel.cs_) и определите коллекцию _Employees_, к которой будет привязан Data Grid.

``` csharp
using CommunityToolkit.Mvvm.ComponentModel;
using System;
using System.Collections.Generic;

namespace AvaloniaApplication1.ViewModels;

public partial class MainWindowViewModel : ViewModelBase
{
    [ObservableProperty]
    IList<EmployeeInfo> employees;

    public MainWindowViewModel()
    {
        Employees = new List<EmployeeInfo>
        {
            new EmployeeInfo("Alex", "Smith", new DateTime(1990, 1, 1)),
            new EmployeeInfo("Samantha", "Brown", new DateTime(1988, 2, 5)),
            new EmployeeInfo("Nick", "Morris", new DateTime(2000, 8, 25)),
            new EmployeeInfo("Julia", "Lee", new DateTime(2005, 12, 3))
        };
    }
}

public partial class EmployeeInfo : ObservableObject
{
    [ObservableProperty]
    public string firstName;
    [ObservableProperty]
    public string lastName;
    [ObservableProperty]
    public DateTime birthDate;
    public EmployeeInfo(string firstName, string lastName, DateTime birthDate)
    {
        FirstName = firstName;
        LastName = lastName;
        BirthDate = birthDate;
    }
}
```

## 7. Добавление пространств имён контролов Eremex Avalonia в XAML

Прежде чем определять контролы Eremex Avalonia в XAML, сначала объявите пространства имён, содержащие эти контролы. Чтобы использовать `DataGridControl` в главном окне, добавьте следующее пространство имён в файл _MainWindow.axaml_:

``` xml
<mx:MxWindow 
...
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
>
```

Список пространств имён для контролов и вспомогательных классов Eremex приведён в таблице ниже:

Продукт/классы | Пространство имён
------|------
Data Grid | `xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"`
Tree List и Tree View | `xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"`
Редакторы и вспомогательные контролы | `xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"`
Диаграммы | `xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"`
Property Grid | `xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"`
Ribbon | `xmlns:mxr="https://schemas.eremexcontrols.net/avalonia/ribbon"`
Панели инструментов и меню | `xmlns:mxb="https://schemas.eremexcontrols.net/avalonia/bars"`
Докинг | `xmlns:mxd="https://schemas.eremexcontrols.net/avalonia/docking"`
Graphics3DControl | `xmlns:mx3d="https://schemas.eremexcontrols.net/avalonia/controls3d"`
Общие вспомогательные классы | `xmlns:mx="https://schemas.eremexcontrols.net/avalonia"`



## 8. Добавление Data Grid в XAML

В файле _MainWindow.axaml_ определите `DataGridControl` и привяжите его к коллекции _Employees_.

``` xml
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:AvaloniaApplication1.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="AvaloniaApplication1.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="AvaloniaApplication1">

    <Design.DataContext>
        <!-- This only sets the DataContext for the previewer in an IDE,
             to set the actual DataContext for runtime, 
             set the DataContext property in code (look at App.axaml.cs) -->
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <mxdg:DataGridControl AutoGenerateColumns="True" ItemsSource="{Binding Employees}"
     SearchPanelDisplayMode="Always"/>

</mx:MxWindow>
```

Параметр `DataGridControl.AutoGenerateColumns` включён, чтобы автоматически генерировать колонки из публичных свойств привязанного источника элементов. 

Свойство `DataGridControl.SearchPanelDisplayMode` задаёт видимость поля поиска, которое позволяет пользователю быстро находить строки грида по содержащимся в них значениям.

## 9. Запуск приложения

Теперь можно запустить приложение (нажмите F5). При запуске появляется окно с полностью функциональным контролом Data Grid. Грид позволяет сортировать и группировать данные «из коробки». Чтобы найти значения в ячейках, введите текст на панели поиска.

![gs-run-app](../images/gs-run-app.png)


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
