---
title: Dock Manager and Dock Items
order: 100000
seealso: []
---

# Dock Manager and Dock Items

The [`DockManager`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager.md) component allows you to create the Visual Studio-inspired docking UI. Dock Panes and Document Panes are basic elements of a docking UI. Dock Panes are used to implement tool panels. Document Panes are tailored to display the main content of the window. You can combine multiple Document Panes in a special container to implement a tabbed MDI (Multiple Document Interface).


![docking-ui-dockpanes-and-documentpanes-v2](../../images/docking-ui-dockpanes-and-documentpanes-v2.png)

The Docking library supports runtime operations on dock items (panels and documents) by users and in code. Users can rearrange the layout of dock items and make them floating using drag-and-drop operations and context menus. Splitters between adjacent items allow runtime resizing operations. 'Pin' buttons in panel headers maintain the auto-hide feature, which lets a user to collapse and restore panels. 

See also: [Wayland Limitations](wayland-limitations.md).


With the Docking library, you can use the MVVM design pattern to populate the docking interface with Dock Panes and Document Panes, and provide content for the panes.


## Get Started with Docking UI

The following topics demonstrate how to create sample docking interfaces from scratch:

- [Get Started With a Docking Interface](get-started-with-docking.md) 
- [How to Create a Complex Docking Layout in Code Behind](examples/how-to-create-a-complex-docking-layout-in-code-behind.md)


## Dock Panes

Dock Panes ([`DockPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane.md) objects) allow you to create dockable and floating tool panels. Panels can be displayed side-by-side or as tabs. They also support the auto-hide feature.

![dockingui-dockpanes](../../images/dockingui-dockpanes.png)

To create a Docking UI in XAML or code-behind, Dock Panes need to be combined in containers (groups). For instance, you can combine items in a [`DockGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup.md) container to display them next to each other, either horizontally or vertically. If you combine panels in a [`TabbedGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/TabbedGroup.md) container, they are displayed as tabs. Containers can also include other containers as children.

See the following topic to learn more: [Dock Panes and Containers](dock-panes-and-containers.md)


## Document Panes

Use Document Panes ([`DocumentPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentPane.md) objects) to display the main content of your Window. If you create multiple Document Panes, you can combine them in a [`DocumentGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentGroup.md) container. [`DocumentGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentGroup.md) is a special container that presents Document Panes as tabs (similar to the [`TabbedGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/TabbedGroup.md) container used to present Dock Panes as tabs).

![dockingui-documentpanes](../../images/dockingui-documentpanes.png)

Document Panes can be made floating. Unlike Dock Panes, Document Panes do not support the auto-hide functionality.

You can create two or more [`DocumentGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentGroup.md) containers, each displaying its own set of Document Panes.

<animated gif>

See the following topic to learn more: [Document Panes](document-panes.md)

## Dock Guides

When a user drags a Dock Pane or Document Pane over another panel or container, the DockManager displays dock guides. Dock guides are visual arrow overlays that assist users during dock operations. Dropping a panel or container over a specific guide docks the item at the corresponding position.

![docking-dock-hints](../../images/docking-dock-hints.png)

If a user drops an item outside a dock guide, the item becomes floating.

See also: [Wayland Limitations](wayland-limitations.md).

### Customize Dock Guides

The [`CustomizeDockGuide`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/CustomizeDockGuide.md) event allows you to hide specific dock guides and individual items within the `Center` guide. When a guide element is hidden, users cannot perform the corresponding dock operation.

Use the following methods provided by the event arguments to hide guide elements:

- [`HideGuide(DockGuideType guide)`](../../API/Eremex.AvaloniaUI.Controls.Docking/CustomizeDockGuideEventArgs/HideGuide.md) — Hides a dock guide specified by the `DockGuideType` enumeration.

    The following image demonstrates the available dock guide types:

    ![docking-guide-types](../../images/docking-guide-types.png)

    - `SideLeft`, `SideRight`, `SideTop`, and `SideBottom` — A panel dropped over these guides is docked at the corresponding edge of the root container.
    - `Center` — This guide consists of 9 inner items, each of which can be hidden using the [`HideItem`](../../API/Eremex.AvaloniaUI.Controls.Docking/CustomizeDockGuideEventArgs/HideItem.md) method.


- [`HideItem(DockGuideItem item)`](../../API/Eremex.AvaloniaUI.Controls.Docking/CustomizeDockGuideEventArgs/HideItem.md) — Hides an item within the `Center` dock guide.

    The following image demonstrates the available items in the `Center` dock guide:

    ![docking-guide-item-types](../../images/docking-guide-item-types.png)

    - `Center` — The dropped panel and the destination panel are combined into the same tabbed container.  
    - `CenterLeft`, `CenterRight`, `CenterTop`, and `CenterBottom` — The dropped panel is placed at the corresponding edge of the destination panel, forming a split container. 
    - `TabLeft`, `TabRight`, `TabTop`, and `TabBottom` — The dropped panel is wrapped in a new tabbed container, which is placed at the corresponding edge of the destination panel.

#### Example - Hide Dock Guides

The following code handles the [`CustomizeDockGuide`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/CustomizeDockGuide.md) event to hide the `TabTop` and `TabBottom` items from the `Center` guide.

![docking-customizedockguide-example](../../images/docking-customizedockguide-example.png)

```csharp
private void DockManager1_CustomizeDockGuide(object sender, Eremex.AvaloniaUI.Controls.Docking.CustomizeDockGuideEventArgs e)
{
    DockGuideItem[] guideItems = new DockGuideItem[] { DockGuideItem.TabTop, DockGuideItem.TabBottom  };
    foreach (var item in guideItems)
    {
        e.HideItem(item);
    }
}
```


## Context Menus

The Docking library provides built-in context menus for Dock Panes and Document Panes. These menus contain commands to perform common dock operations on panes.

![dockingui-contextmenus](../../images/dockingui-contextmenus.png)

Handle the [`DockManager.DockItemContextMenuOpening`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/DockItemContextMenuOpening.md) event to customize the context menus, or to prevent them from being displayed.

<!-- TODO
example for the [`DockManager.DockItemContextMenuOpening`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/DockItemContextMenuOpening.md) event 
 -->

## Prevent Certain Operations on Dock Items

Dock Panes and Document Panes display predefined buttons in their headers used to perform common operations on the panes.

![dockpane-headerbuttons](../../images/dockpane-headerbuttons.png)

The DockManager provides options and events to control dock operations on panes. See the following section for more details: [Dock Panes and Containers - Runtime Options for Dock Panels](dock-panes-and-containers.md#runtime-options-for-dock-panels)

## Save and Restore the Layout of Panes

You can save the current dock layout to a stream, and then restore it when required. This feature allows you to save the layout when a user closes the application, and reload the saved layout the next time the application runs. See the following topic for more information: [Save and Restore the Layout of Panels](save-and-restore-layout.md)

## See Also

- [How to Create a Complex Docking Layout in Code Behind](examples/how-to-create-a-complex-docking-layout-in-code-behind.md)