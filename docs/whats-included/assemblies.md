---
title: Assemblies
order: 1000
seealso: []
---

# Assemblies

This topic describes the assemblies with controls and [themes](../controls/themes/index.md) included in the Eremex Avalonia UI Controls library.



## NuGet Packages

The Eremex Controls assemblies and project templates are distributed as NuGet packages. You can find and download them from the [nuget.org](https://www.nuget.org) website using the link below:

- [Eremex Controls at NuGet.org](https://www.nuget.org/profiles/EremexControls)

## Included Assemblies

- **Eremex.Avalonia.Controls** — Contains the Eremex data shaping and editing controls and common utility classes. The main controls in this assembly include:

    - [DataGrid](../controls/datagrid/index.md)
    - [TreeList](../controls/treelist/index.md) and [TreeView](../controls/treelist/index.md)
    - [PropertyGrid](../controls/propertygrid/index.md)
    - [ListView](../controls/listview/index.md)
    - [CartesianChart](../controls/charts/index.md), [PolarChar`](../API/Eremex.AvaloniaUI.Charts/PolarChart.md) and [SmithChart](../API/Eremex.AvaloniaUI.Charts/SmithChart.md)
    - [Ribbon](../controls/ribbon/index.md)
    - [Toolbars and Menus](../controls/toolbars-and-menus/index.md)
    - [Docking UI](../controls/docking/index.md)
    - [Heatmap](../controls/charts/heatmap.md)
    - [Data Editors](../controls/editors/index.md) ([TextEditor](../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md), [ButtonEditor](../API/Eremex.AvaloniaUI.Controls.Editors/ButtonEditor.md), [ComboBoxEditor](../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md), [CheckEditor](../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md), [SpinEditor](../API/Eremex.AvaloniaUI.Controls.Editors/SpinEditor.md), and more)
    - [Utility Controls](../controls/utility-controls/index.md) ([MxTabControl](../controls/utility-controls/tabcontrol.md),  [SplitContainerControl](../controls/utility-controls/splitcontainercontrol.md), [CalendarControl](../controls/utility-controls/calendarcontrol.md), and more)
    - [Windows](../controls/windows-and-dialogs/index.md) ([MxMessageBox](../controls/windows-and-dialogs/messagebox.md) and [MxWindow](../controls/windows-and-dialogs/index.md))

- **Eremex.Avalonia.Controls3D** — Includes the controls and classes to render 3D models in your applications. 
    - [Graphics3DControl](../controls/graphics3dcontrol/index.md) — Allows you to display and interact with 3D models.

- **Eremex.Avalonia.Controls.ApplicationServices** — Contains a set of services that enable ViewModels in your MVVM applications to work with message boxes, windows, dialogs, and theme settings without referencing Avalonia types directly. See [Application Services](../controls/app-services/index.md).

- **Eremex.Avalonia.Themes.DeltaDesign** — Contains the 'DeltaDesign' paint theme for the Eremex controls. See [Themes](../controls/themes/index.md).

- **Eremex.DocumentProcessing** — A library of non-visual components to generate PDF and XLSX documents.

- **Eremex.Drawing** — Core drawing library for the Eremex Avalonia UI Controls, providing primitives and base abstractions for font and text handling, formatting and measurement.

- **Eremex.Drawing.Skia** — SkiaSharp-based implementation of the Eremex.Drawing abstractions: font loading, text rendering, formatting and measurement powered by the SkiaSharp graphics engine. 

- **Eremex.Avalonia.Templates** — Contains templates to create new Avalonia UI projects with Eremex controls from scratch. See [Project Templates](project-templates.md).

- **Eremex.Common.Contracts** — Contains Model-layer common interfaces and base classes with no UI dependencies.