---
title: Perform Dock Operations in Code
order: 56000
seealso: []
---

# Perform Dock Operations in Code

This topic describes operations on dock panels in code behind.

## Create Dock Panels

You can create [`DockPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane.md) and [`DocumentPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentPane.md) objects using their constructors. After a panel is created you typically need to display it at a specific position relative to another panel or [container (group)](dock-panes-and-containers.md). The [`DockManager.Dock`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Dock.md) method allows you to dock a panel along an edge of another panel, add a panel to an existing container, and combine panels in a tabbed UI. To add a panel as a child of an existing container, you can also use the container's `Add` method.


The most frequently used overload of the [`DockManager.Dock`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Dock.md) method is defined as follows:

``` cs
public bool Dock(DockItemBase item, DockItemBase target, DockType dockType)
```

The `target` parameter specifies the panel or container relative to which the source item (passed as the `item` parameter) is docked.

The `dockType` parameter specifies how to dock an item relative to the target item:

- [`DockType.Fill`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md) — The source and target panels are combined in a tab container (`TabGroup`). If the target panel already belongs to a tab container, the source panel is added to this container; no extra tab container is created.

- [`DockType.Left`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md), [`DockType.Right`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md), [`DockType.Top`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md), [`DockType.Bottom`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md) — A source dock item is docked at the corresponding side of a target dock item. When required, an additional horizontal or vertical split container ([`DockGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup.md)) is created by the [`DockManager.Dock`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Dock.md) method, as described below. 

  Assume that you dock a source panel at the top or bottom of the target panel that belongs to a **vertical** split container. 
  
  ``` cs
  dockManager1.Dock(paneProperties, paneDebug, DockType.Top);
  ```

  In this case, the source panel is added as a child of the existing container. 

  ![docking-dock-verticalcontainer-dock-to-top](../../images/docking-dock-verticalcontainer-dock-to-top.png)
  
  If you dock a panel at the left or right of the target panel, an additional horizontal split container is created combining the source and target panels.

  ``` cs
  dockManager1.Dock(paneProperties, paneDebug, DockType.Left);
  ```

  ![docking-dock-verticalcontainer-dock-to-left](../../images/docking-dock-verticalcontainer-dock-to-left.png)

  The same reasoning applies when a panel is docked next to a target panel that resides in a **horizontal** split container. If you dock the source panel at the left or right of the target panel, the source panel is added as a child of the existing horizontal container. 
  
  ``` cs
  dockManager1.Dock(paneProperties, paneOutput, DockType.Right);
  ```

  ![docking-dock-horizontalcontainer-dock-to-right](../../images/docking-dock-horizontalcontainer-dock-to-right.png)

  If you dock a panel at the top or bottom of the target panel, an additional vertical split container is created combining the source and target panels.

  ``` cs
  dockManager1.Dock(paneProperties, paneOutput, DockType.Bottom);
  ```

  ![docking-dock-horizontalcontainer-dock-to-bottom](../../images/docking-dock-horizontalcontainer-dock-to-bottom.png)
  
  Use the [`DockPane.DockWidth`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/DockWidth.md) and [`DockPane.DockHeight`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/DockHeight.md) properties to set size of panels when they are hosted in a split container.




### Example - Create and Display Panels Side-by-side

The following code creates [`DockPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane.md) and [`DocumentPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentPane.md) objects and arranges them as shown in the image below. The [`DocumentPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentPane.md) objects are placed in a [`DocumentGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentGroup.md) container to present them as tabs.

![docking-code-behind-create-panels](../../images/docking-code-behind-create-panels.png)

``` cs
DockPane paneProperties = new DockPane()
{
    Header = "Properties",
    Glyph = ImageLoader.LoadSvgImage(Assembly.GetExecutingAssembly(), "Images/settings.svg"),
    GlyphSize = new Avalonia.Size(16, 16)
};
DockPane paneDebug = new DockPane()
{
    Header = "Debug",
    Glyph = ImageLoader.LoadSvgImage(Assembly.GetExecutingAssembly(), "Images/debug2.svg"),
    GlyphSize = new Avalonia.Size(16, 16)
};
DockPane paneOutput = new DockPane() { Header = "Output" };

dockManager1.Root = new DockGroup();
dockManager1.Dock(paneProperties, dockManager1.Root, DockType.Right);
paneProperties.DockWidth = new GridLength(150, GridUnitType.Pixel);

dockManager1.Dock(paneOutput, paneProperties, DockType.Left);
dockManager1.Dock(paneDebug, paneOutput, DockType.Bottom);
paneDebug.DockHeight = new GridLength(150, GridUnitType.Pixel);

```



See also:

- [Manage Auto-Hide Panels](#manage-auto-hide-panels)
- [Manage Floating Panels](#manage-floating-panels)

More examples: 

- [How to Create a Complex Docking Layout in Code Behind](examples/how-to-create-a-complex-docking-layout-in-code-behind.md)

### Access a Dock Item's Parent and Children

The [`DockPane.DockParent`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/DockParent.md) property allows you to return the immediate parent of any dock item (panel or container). For instance, when a panel resides in a split container ([`DockGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup.md)), the [`DockPane.DockParent`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/DockParent.md) returns this split container. For panels combined in a tab container, the [`DockPane.DockParent`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/DockParent.md) returns this parent tab container (a [`TabbedGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/TabbedGroup.md) or [`DocumentGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentGroup.md) object).

To get immediate children of a dock container, use its [`Items`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup/Items.md) property.

See also: [Access Dock Panels and Containers](#access-dock-panels-and-containers).

#### Example - Access a Parent and Set Its Size

The following code creates a docking UI that consists of three panels. The example sets the relative width for the 'Properties' panel and the vertical split container that combines the 'Output' and 'Debug' panels.

![docking-code-behind-access-parent-and-resize](../../images/docking-code-behind-access-parent-and-resize.png)

``` cs
DockPane paneProperties = new DockPane() { Header = "Properties" };
DockPane paneDebug = new DockPane() { Header = "Debug" };
DockPane paneOutput = new DockPane() { Header = "Output" };

dockManager1.Root = new DockGroup();
dockManager1.Root.Add(paneProperties);
dockManager1.Dock(paneDebug, paneProperties, DockType.Right);
dockManager1.Dock(paneOutput, paneDebug, DockType.Top);
paneProperties.DockWidth = new GridLength(1, GridUnitType.Star);
paneDebug.DockParent.DockWidth = new GridLength(2, GridUnitType.Star);
```


## Close Panels

The [`DockManager.Close`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Close.md) method allows you to temporarily hide a panel or container. This method is called when a user closes a panel by clicking its 'Close' ('x') button.

![docking-dockpane-closebutton](../../images/docking-dockpane-closebutton.png)

When called for a container (group), the [`Close`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Close.md) method hides all panes of this container.

Closed panels can be accessed from the [`DockManager.ClosedPanes`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/ClosedPanes.md) collection.

Use the [`DockPane.AllowClose`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/AllowClose.md) property to hide the 'Close' button for a panel, and thus prevent the panel from being closed using this button. This option does not prevent a panel from being closed with the [`DockManager.Close`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Close.md) method.

When a panel is closed, the [`DockPane.CloseCommand`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/CloseCommand.md) command is activated.

## Remove Panels

You can use the [`DockManager.Remove`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Remove.md) method to remove a panel from a [`DockManager`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager.md). This method does not dispose of the panel and its content.

[`DockManager`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager.md) does not store references to removed panels.

## Combine Panels in a Tab Container

You can combine panels in a tab container (`TabGroup`). For this purpose, use the following [`DockManager.Dock`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Dock.md) method overload:

``` cs
public bool Dock(DockItemBase item, DockItemBase target, DockType dockType)
```

The `target` parameter can be a panel or an existing tab container. 

The `dockType` parameter specifies how to dock a panel. Set this parameter to [`DockType.Fill`](../../API/Eremex.AvaloniaUI.Controls.ApplicationServices/DockType.md) to combine panels in a tabbed UI.

When you dock a [`DockPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane.md) object into another [`DockPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane.md) object, a `TabGroup` container is created. A [`DocumentGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentGroup.md) container is created when you dock a [`DocumentPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentPane.md) into another [`DocumentPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentPane.md) object.

You can also use a tab container's [`Add`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup/Add.md) method to add a new item as a tab.

### Example - Create a Tab Container

The following code uses the [`DockManager.Dock`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Dock.md) method to create a tab container from two panels.

![docking-code-behind-create-tab-container](../../images/docking-code-behind-create-tab-container.png)

``` cs
dockManager1.Root = new DockGroup();
DockPane paneDebug = new DockPane() 
{ 
    Header = "Debug", 
    DockWidth = new GridLength(250, GridUnitType.Pixel) 
};
dockManager1.Root.Add(paneDebug);
DockPane paneOutput = new DockPane() { Header = "Output" };
dockManager1.Dock(paneOutput, paneDebug, DockType.Fill);
```

### Access the Tab Container

To obtain a parent tab container for a pane, use the pane's [`DockParent`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/DockParent.md) property.

See also: [Access Dock Panels and Containers](#access-dock-panels-and-containers).

## Manage Auto-Hide Panels

Auto-hide panels are initially collapsed. A user can click a panel's button to expand the panel.

![docking-code-behind-create-autohide-panel.gif](../../images/docking-code-behind-create-autohide-panel.gif)


### Create Auto-Hide Panel

Use the [`DockManager.AutoHide`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/AutoHide.md) method to enable the auto-hide functionality for a panel in code-behind. This method hides a panel at its current or previous dock position.

``` cs
dockManager1.AutoHide(paneOutput);
```

When a panel is about to become auto-hidden, an [`AutoHideGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/AutoHideGroup.md) container is created, and the panel is moved to this container.

You can call the [`DockManager.AutoHide`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/AutoHide.md) method for a `TabGroup` container. In this case, all panels of the tab container become auto-hidden.

#### Example - Auto-Hide Tab Containers

The following code creates two tab containers at the right edge of the [`DockManager`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager.md), and then enables the auto-hide functionality for these tab containers. Two [`AutoHideGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/AutoHideGroup.md) containers are created as a result, each displaying panels from a corresponding tab container.

![docking-code-behind-autohide-two-tab-containers](../../images/docking-code-behind-autohide-two-tab-containers.png)


``` cs
dockManager1.Root = new DockGroup();
dockManager1.Root.Add(new DocumentGroup());
DockPane paneDebug = new DockPane() { Header = "Debug" };
dockManager1.Root.Add(paneDebug);
DockPane paneOutput = new DockPane() { Header = "Output" };
// Create a tab container that combines the 'Debug' and 'Output' panels
dockManager1.Dock(paneOutput, paneDebug, DockType.Fill);

DockPane paneTasks = new DockPane() { Header = "Tasks" };
dockManager1.Root.Add(paneTasks);
DockPane paneExplorer = new DockPane() { Header = "Explorer" };
//Create a tab container that combines the 'Tasks' and 'Explorer' panels
dockManager1.Dock(paneExplorer, paneTasks, DockType.Fill);

//Auto-hide the tab containers
dockManager1.AutoHide(paneDebug.DockParent);
dockManager1.AutoHide(paneTasks.DockParent);
```


### Restore a Panel from the Auto-Hidden State

Use the [`DockManager.Dock(DockItemBase item)`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Dock.md) method overload to restore a panel from the auto-hidden state to its previous dock position.

``` cs
dockManager1.Dock(paneOutput);
```

You can also use the `Dock(DockItemBase item, DockItemBase target, DockType dockType)` overload to restore an auto-hidden panel while moving it to a specific position in a layout.

``` cs
dockManager1.Dock(paneOutput, paneDebug, DockType.Right););
```

### Show and Collapse an Auto-Hide Panel

The [`DockManager.ExpandAutoHidePanel`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/ExpandAutoHidePanel.md) and [`DockManager.CollapseAutoHidePanel`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/CollapseAutoHidePanel.md) methods allow you to display and collapse an auto-hide panel. The [`DockPane.IsActive`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/IsActive.md) property allows you to focus any panel. For an auto-hide panel, this property expands the panel (if it is collapsed), and then focuses it.

### Access Auto-Hide Panels

You can use the [`DockManager.AutoHideGroups`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/AutoHideGroups.md) collection to access all existing [`AutoHideGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/AutoHideGroup.md) containers. The [`AutoHideGroup.Items`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup/Items.md) property allows you to retrieve all auto-hide panels displayed in a specific container.

To retrieve a parent container for an auto-hide panel, see the [`DockPane.AutoHideGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/AutoHideGroup.md) property.

See also: [Access Dock Panels and Containers](#access-dock-panels-and-containers).

## Manage Floating Panels


### Create Floating Panels

Use the [`DockManager.Float`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Float.md) method to make a panel floating in code-behind. When you make a panel floating, it is moved to a [`FloatGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup.md) container (a floating window). A floating panel's [`DockPane.FloatGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/FloatGroup.md) property allows you to access the parent floating window, and set its bounds (see [`FloatGroup.FloatLocation`](../../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup/FloatLocation.md), [`FloatGroup.FloatWidth`](../../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup/FloatWidth.md) and [`FloatGroup.FloatHeight`](../../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup/FloatHeight.md)).


![docking-code-behind-create-floating-panel](../../images/docking-code-behind-create-floating-panel.png)

``` cs
DockPane paneTasks = new DockPane() { Header = "Tasks" };
dockManager1.Float(paneTasks);
// Set the floating window's bounds
paneTasks.FloatGroup.FloatLocation = new Avalonia.PixelPoint(200, 200);
paneTasks.FloatGroup.FloatWidth = 300;
paneTasks.FloatGroup.FloatHeight = 200;
```

If a panel is floating, you can dock another panel next to it, and thus create a floating container.

![docking-code-behind-floating-split-container](../../images/docking-code-behind-floating-split-container.png)

``` cs
DockPane paneTasks = new DockPane() { Header = "Tasks" };
dockManager1.Float(paneTasks);
DockPane paneExplorer = new DockPane() { Header = "Explorer" };
dockManager1.Dock(paneExplorer, paneTasks, DockType.Right);
```

### Access Floating Panels

The [`DockManager.FloatGroups`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/FloatGroups.md) collection allows you to retrieve existing floating windows ([`FloatGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup.md) objects). Use the [`FloatGroup.Items`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup/Items.md) property to obtain a list of panels displayed in each floating window.

See also: [Access Dock Panels and Containers](#access-dock-panels-and-containers).

## Access Dock Panels and Containers

The following list summarizes properties and methods you can use to access dock panels and groups (containers).

- DockManager's `GetItems` extension method — Returns a linear list of all docked, auto-hidden and closed panels and groups.
- DockManager's `FindItem` extension method — Returns an item by name.
- [`DockGroup.Items`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup/Items.md) — Gets a list of a container's immediate children.
- [`DockPane.DockParent`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/DockParent.md) — Gets a dock item's immediate parent.
- [`DockPane.FloatGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/FloatGroup.md) — Returns the floating window that hosts a panel in the floating state. 
- [`DockPane.AutoHideGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/AutoHideGroup.md) — Returns the [`AutoHideGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/AutoHideGroup.md) container that hosts a panel in the auto-hidden state. 
- [`DockManager.Root`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/Root.md) — Returns the root group (container) that displays all docked panels and containers.
- [`DockManager.FloatGroups`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/FloatGroups.md) — Gets a collection of existing [`FloatGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup.md) objects (floating windows).
- [`DockManager.AutoHideGroups`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/AutoHideGroups.md) — Gets a collection of existing [`AutoHideGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/AutoHideGroup.md) objects.
- [`DockManager.ClosedPanes`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/ClosedPanes.md) — Returns a collection of closed panels.



## Control Dock Operations

If you need flexible control over dock operations performed by users, you can handle the following events:

- [`DockManager.DockOperationStarting`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/DockOperationStarting.md) — Fires when a dock operation is about to start.

- [`DockManager.DockOperationCompleted`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/DockOperationCompleted.md) — Fires after a dock operation is complete.

- [`DockManager.DockItemActivated`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/DockItemActivated.md) — Fires after a dock item is activated.

- [`DockManager.DockItemStartFloatDragging`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/DockItemStartFloatDragging.md) — Fires when a panel becomes floating, or a floating window is about to be moved.

- [`DockManager.DockItemEndFloatDragging`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/DockItemEndFloatDragging.md) — Fires after a floating window's dragging is complete.

### Example - Prevent a Panel from Being Closed

The following [`DockManager.DockOperationStarting`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/DockOperationStarting.md) event handler does not allow the 'Output' panel to be closed when a user clicks the panel's 'Close' ('x') button.

``` cs
private void DockManager1_DockOperationStarting(object? sender, DockOperationStartingEventArgs e)
{
    if(e.Item is DockPane pane)
    {
        e.Cancel = e.DockOperation == DockOperation.Close && pane.Header == "Output";
    }
    
}
```