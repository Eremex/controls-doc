---
title: Migrate from WinForms and WPF Docking to Avalonia Docking UI
order: 64000
seealso: []
---

# Migrate from WinForms and WPF Docking to Avalonia Docking UI

If you have built IDE-style interfaces with a docking manager in Windows Forms or WPF and are moving to Avalonia UI, the Docking UI of the Eremex Avalonia UI Controls library will look familiar. The library is built for Avalonia UI only: it does not include controls for Windows Forms or WPF. The **Dock Manager** component creates tool panels that can be docked, auto-hidden and floated, plus tabbed document areas, all in a cross-platform Avalonia UI application (Windows, Linux, macOS).

This topic maps the concepts you already know to the building blocks of the library, and shows where to find the details.

## Concept Map

| What you want | Building block in the Eremex library |
| --- | --- |
| The component that manages the whole docking layout | [`DockManager`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager.md) - see [Dock Manager and Dock Items](dock-manager.md) |
| A tool window (Solution Explorer, Properties, Output, and so on) | [`DockPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane.md) - see [Dock Panes and Containers](dock-panes-and-containers.md) |
| A document tab in the main area (tabbed MDI) | [`DocumentPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentPane.md) - see [Document Panes](document-panes.md) |
| A group of tabs | [`TabbedGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/TabbedGroup.md) (tab container for Dock Panes) and [`DocumentGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentGroup.md) (tab container for Document Panes) |
| Panels side by side or stacked, separated by splitters | [`DockGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup.md) (split container) - see [Split Panels](dock-panes-and-containers.md#split-panels) |
| A panel that slides out from the window edge | Auto-hide - see [Auto-Hide Panels](dock-panes-and-containers.md#auto-hide-panels) |
| A panel in its own window | [`FloatGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup.md) - see [Floating Panels](dock-panes-and-containers.md#floating-panels) |
| Drag-and-drop guides that show where a panel will dock | Dock hints - see [Dock Manager and Dock Items](dock-manager.md#dock-hints), and the [`DockManager.CustomizeDockGuide`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/CustomizeDockGuide.md) event (version 1.5) to hide specific guides |
| Ctrl+Tab window switching | [Document Switcher](document-switcher.md) |
| Saving and restoring the layout between sessions | [Save and Restore the Layout of Panels](save-and-restore-layout.md) |
| Building the layout from code (arrange, split, float, activate, close) | [Perform Dock Operations in Code](perform-dock-operations-in-code.md) |
| A view-model-driven layout | [Use MVVM Pattern to Populate Dock Items](use-mvvm-pattern-to-populate-dock-items.md) |

## Differences Worth Knowing

- **XAML first.** A layout is declared in XAML (the Dock Manager contains Dock Panes, Document Panes and groups) and docking operations can also be performed in code.
- **MVVM support.** Panels can be created from a collection of view models, so a docking layout fits an MVVM application without code-behind.
- **Layout serialization.** The layout of dock panels and documents can be saved and restored with the [`DockManager.SaveLayout`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/SaveLayout.md) and [`DockManager.RestoreLayout`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/RestoreLayout.md) methods.
- **Cross-platform.** The same Docking UI works on every platform supported by Avalonia UI.

## A Minimal Layout

The following example shows the shape of a typical layout: a document area with an *Error List* panel below it, and a tab container with two tool panels beside them. See [Get Started with Docking](get-started-with-docking.md) for a step-by-step walk-through.

``` xml
xmlns:mxd="https://schemas.eremexcontrols.net/avalonia/docking"

<mxd:DockManager>
    <mxd:DockGroup>
        <mxd:DockGroup Orientation="Vertical">
            <mxd:DocumentGroup></mxd:DocumentGroup>
            <mxd:DockPane Header="Error List"/>
        </mxd:DockGroup>
        <mxd:TabbedGroup>
            <mxd:DockPane Header="Properties"/>
            <mxd:DockPane Header="Debug"/>
        </mxd:TabbedGroup>
    </mxd:DockGroup>
</mxd:DockManager>
```

## Where to Go Next

- [Get Started with Docking](get-started-with-docking.md)
- [Docking UI overview](index.md)
- [Examples](examples/index.md)
