---
title: Начало работы с EMX Controls
order: 3000
seealso: []
---

# Начало работы с Eremex Avalonia UI Controls

Это руководство демонстрирует, как создать новое приложение Avalonia UI в Visual Studio 2022 с Eremex Avalonia UI Controls. В нём показан код регистрации визуальной темы Eremex, необходимый для отрисовки контролов.

В этом руководстве контрол Eremex [Data Grid](../controls/datagrid/index.md) добавляется в окно и привязывается к источнику элементов. Источником элементов в этом примере является коллекция бизнес-объектов, реализованная с помощью библиотеки CommunityToolkit.Mvvm.

![gs-run-app](../images/gs-run-app.png)


## 1. Создание нового проекта Avalonia UI

В этом руководстве для создания нового проекта используется **шаблон Eremex Avalonia App**. 
Этот шаблон создаёт новый проект, добавляет в него библиотеку Eremex Controls и регистрирует визуальную тему Eremex, необходимую для отрисовки контролов. 

Для создания проектов можно также использовать стандартные шаблоны Avalonia UI. Дополнительную информацию смотрите в следующем разделе: [Используйте стандартные шаблоны Avalonia UI для создания нового проекта с контролами Eremex](create-new-avalonia-project-using-avalonia-templates.md)


### 1.1 Установка шаблонов Eremex Avalonia

Выполните следующую команду:

<code>
dotnet new install Eremex.Avalonia.Templates
</code>


Установленные шаблоны включают:

#### eremex.avalonia.app

Этот шаблон приложения создаёт пустой проект Avalonia UI, ссылающийся на библиотеку Eremex Controls. Шаблон выполняет следующее:

- Добавляет в проект NuGet-пакеты Eremex: 
    
    - **Eremex.Avalonia.Controls** — содержит контролы и библиотеки Eremex.
    - **Eremex.Avalonia.Themes.DeltaDesign** — содержит визуальную тему `DeltaDesign` для контролов Eremex.
- Использует класс `MxWindow` в качестве главного окна проекта. `MxWindow` обеспечивает поддержку визуальных тем Eremex.
- Регистрирует визуальную тему Eremex `DeltaDesign`. 

    !!! note
        Если в вашем приложении не зарегистрирована ни одна визуальная тема Eremex, контролы Eremex отображаются пустыми.


#### eremex.avalonia.mvvm

Этот шаблон приложения создаёт проект Avalonia UI с поддержкой MVVM, ссылающийся на библиотеку Eremex Controls. Шаблон разделяет код на View (_MainWindow_) и ViewModel (_MainWindowViewModel_).
Остальные возможности этого шаблона совпадают с шаблоном `eremex.avalonia.app`.

#### eremex.avalonia.window

Шаблон, создающий новое окно Avalonia на основе `MxWindow`. Этот шаблон создаёт только два файла, определяющих окно: _Window.axaml_ и _Window.axaml.cs_.

### 1.2 Создание нового проекта

Перейдите в папку, в которой нужно создать проект. Используйте команду <code>dotnet new eremex.avalonia.mvvm</code>, чтобы создать новый проект с поддержкой MVVM. Чтобы задать имя проекта, используйте параметр команды <code>-n _name_</code>.

Следующая команда создаёт новый проект _AvaloniaApplication1_.

<code>
dotnet new eremex.avalonia.mvvm -n AvaloniaApplication1 
</code>


Откройте созданный проект в Visual Studio.


### 1.3. Выбор светлого или тёмного варианта визуальной темы 

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

## 2. Определение данных для Data Grid

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

## 3. Добавление пространств имён контролов Eremex Avalonia в XAML

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



## 4. Добавление Data Grid в XAML

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

## 5. Запуск приложения

Теперь можно запустить приложение. При запуске появляется окно с полностью функциональным контролом Data Grid. Грид позволяет сортировать и группировать данные «из коробки». Чтобы найти значения в ячейках, введите текст на панели поиска.

![gs-run-app](../images/gs-run-app.png)


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
