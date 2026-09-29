---
title: 项目模板
order: 900
seealso: []
---

# 项目模板

**Eremex.Avalonia.Templates** [NuGet 包](https://www.nuget.org/profiles/EremexControls)包含用于使用 Eremex Controls 快速创建新 Avalonia UI 项目的模板。

## 安装 Eremex Avalonia 模板

运行以下命令：

<code>
dotnet new install Eremex.Avalonia.Templates
</code>

## 更新 Eremex Avalonia 模板

要更新到最新版本，请运行模板安装命令：

<code>
dotnet new install Eremex.Avalonia.Templates
</code>

## 包含的模板

### `eremex.avalonia.app`

该应用程序模板会创建一个引用 Eremex Controls 库的空 Avalonia UI 项目。此模板执行以下操作：

- 向项目中添加 Eremex 的 NuGet 包：
    
    - **Eremex.Avalonia.Controls**
    - **Eremex.Avalonia.Themes.DeltaDesign**

- 使用 `MxWindow` 类作为项目的主窗口。`MxWindow` 窗口提供对 Eremex 外观主题的支持。
- [注册](../controls/themes/register-an-eremex-paint-theme.md) Eremex 的 `DeltaDesign` 外观主题。


### `eremex.avalonia.mvvm`

该应用程序模板会创建一个支持 MVVM 模式、引用 Eremex Controls 库的 Avalonia UI 项目。该模板将代码分离为 View（_MainWindow_）和 ViewModel（_MainWindowViewModel_）。
此模板的其余功能与 `eremex.avalonia.app` 模板相同。

### `eremex.avalonia.window`


这是一个用于创建基于 `MxWindow` 的新 Avalonia 窗口的模板。此模板仅创建定义窗口的两个文件：_Window.axaml_ 和 _Window.axaml.cs_。


## 通过命令行从模板创建新项目

切换到需要创建项目的文件夹。使用 <code>dotnet new _template-name_</code> 命令从指定模板创建新项目。要为项目指定名称，请使用 <code>-n _name_</code> 命令选项。

以下命令基于 `eremex.avalonia.mvvm` 模板创建一个新的 _AvaloniaApplication1_ 项目。

<code>
dotnet new eremex.avalonia.mvvm -n AvaloniaApplication1 
</code>


在 Visual Studio 中打开创建的项目。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
