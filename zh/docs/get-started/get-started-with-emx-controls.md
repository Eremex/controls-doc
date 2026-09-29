---
title: EMX Controls 入门指南
order: 3000
seealso: []
---

# Eremex Avalonia UI Controls 入门指南

本教程演示了如何在 Visual Studio 2022 中使用 Eremex Avalonia 控件创建一个新的 Avalonia UI 应用程序，并展示了渲染控件所需的 Eremex 绘制主题注册代码。

在本教程中，一个 Eremex [Data Grid 控件](../controls/datagrid/index.md)被添加到窗口中，并绑定到一个项源。本示例中的项源是使用 CommunityToolkit.Mvvm 库实现的业务对象集合。

![gs-run-app](../images/gs-run-app.png)


## 1. 创建新的 Avalonia UI 项目

本教程使用 **Eremex Avalonia App 模板** 创建新项目。
该模板会创建一个新项目，将 Eremex Controls 库添加到项目中，并注册渲染控件所需的 Eremex 绘制主题。

您也可以使用标准 Avalonia UI 模板来创建项目。有关更多信息，请参见以下主题：[使用标准 Avalonia UI 模板结合 Eremex Controls 创建新项目](create-new-avalonia-project-using-avalonia-templates.md)


### 1.1 安装 Eremex Avalonia 模板

运行以下命令：

<code>
dotnet new install Eremex.Avalonia.Templates
</code>


安装的模板包括：

#### eremex.avalonia.app

此应用程序模板会创建一个引用 Eremex Controls 库的空 Avalonia UI 项目。该模板执行以下操作：

- 将 Eremex 的 NuGet 包添加到项目中：

    - **Eremex.Avalonia.Controls** —— 包含 Eremex 控件和库。
    - **Eremex.Avalonia.Themes.DeltaDesign** —— 包含用于 Eremex 控件的 `DeltaDesign` 绘制主题。
- 使用 `MxWindow` 类作为项目的主窗口。`MxWindow` 提供对 Eremex 绘制主题的支持。
- 注册 Eremex `DeltaDesign` 绘制主题。

    !!! note
        如果您的应用程序中未注册任何 Eremex 绘制主题，则 Eremex 控件将显示为空白。


#### eremex.avalonia.mvvm

此应用程序模板会创建一个支持 MVVM 的、引用 Eremex Controls 库的 Avalonia UI 项目。该模板将代码分离为 View（_MainWindow_）和 ViewModel（_MainWindowViewModel_）。
该模板的其余功能与 `eremex.avalonia.app` 模板相同。

#### eremex.avalonia.window

一个用于创建基于 `MxWindow` 的新 Avalonia 窗口的模板。该模板仅创建定义窗口所需的两个文件：_Window.axaml_ 和 _Window.axaml.cs_。

### 1.2 创建新项目

切换到需要创建项目的文件夹。使用 <code>dotnet new eremex.avalonia.mvvm</code> 命令创建一个支持 MVVM 的新项目。若要为项目指定名称，请使用 <code>-n _name_</code> 命令选项。

以下命令会创建一个新的 _AvaloniaApplication1_ 项目。

<code>
dotnet new eremex.avalonia.mvvm -n AvaloniaApplication1 
</code>


在 Visual Studio 中打开创建的项目。


### 1.3. 选择浅色或深色绘制主题变体

Eremex 应用程序模板会自动将 `DeltaDesign` 绘制主题的注册代码添加到创建的项目中。打开 _App.axaml_ 文件，在 `Application` 对象定义中查找该代码。

`DeltaDesign` 绘制主题支持 `Light`（浅色）和 `Dark`（深色）两种主题变体。使用 `Application.RequestedThemeVariant` 属性指定所需的主题变体。

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

在下面的各节中，我们将向 View 添加一个 Eremex `DataGridControl` 控件，并将其绑定到 View Model 中定义的 _Employees_ 集合。

## 2. 为 Data Grid 定义数据

打开主 View Model（_MainWindowViewModel.cs_），定义将要绑定到 Data Grid 的 _Employees_ 集合。

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

## 3. 在 XAML 中添加 Eremex Avalonia 控件命名空间

在 XAML 中定义 Eremex Avalonia 控件之前，需要先声明包含这些控件的命名空间。若要在主窗口中使用 `DataGridControl`，请将以下命名空间添加到 _MainWindow.axaml_ 文件中：

``` xml
<mx:MxWindow 
...
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"
>
```

下表列出了 Eremex 控件和辅助类对应的命名空间：

产品/类 | 命名空间
------|------
Data Grid | `xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"`
Tree List 和 Tree View | `xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"`
编辑器和实用控件 | `xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"`
图表 | `xmlns:mxc="https://schemas.eremexcontrols.net/avalonia/charts"`
Property Grid | `xmlns:mxpg="https://schemas.eremexcontrols.net/avalonia/propertygrid"`
Ribbon | `xmlns:mxr="https://schemas.eremexcontrols.net/avalonia/ribbon"`
工具栏和菜单 | `xmlns:mxb="https://schemas.eremexcontrols.net/avalonia/bars"`
Docking | `xmlns:mxd="https://schemas.eremexcontrols.net/avalonia/docking"`
Graphics3DControl | `xmlns:mx3d="https://schemas.eremexcontrols.net/avalonia/controls3d"`
通用辅助类 | `xmlns:mx="https://schemas.eremexcontrols.net/avalonia"`



## 4. 在 XAML 中添加 Data Grid

在 _MainWindow.axaml_ 文件中，定义一个 `DataGridControl` 并将其绑定到 _Employees_ 集合。

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

启用 `DataGridControl.AutoGenerateColumns` 选项后，将根据绑定的项源的公共属性自动生成列。

`DataGridControl.SearchPanelDisplayMode` 属性用于指定搜索框的可见性，该搜索框允许用户根据单元格中包含的值快速定位网格中的行。

## 5. 运行应用程序

现在您可以运行应用程序了。应用程序启动后会出现一个包含功能完整的 Data Grid 控件的窗口。该网格默认即可对数据进行排序和分组。若要定位单元格的值，请在搜索面板中输入文本。

![gs-run-app](../images/gs-run-app.png)


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
