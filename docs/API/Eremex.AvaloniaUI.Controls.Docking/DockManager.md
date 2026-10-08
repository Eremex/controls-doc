# DockManager class

Manages a layout of docked, floating, and auto-hidden panes and documents.

**Namespace:** [`Eremex.AvaloniaUI.Controls.Docking`](./index.md)  
**Assembly:** `Eremex.Avalonia.Controls.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Declaration

```csharp
public class DockManager : TemplatedControl
```

## Public Members

| name | description |
| --- | --- |
| [DockManager](DockManager/DockManager.md)() | Initializes a new instance of the DockManager class. |
| static [GetDockManager](DockManager/GetDockManager.md)(…) |  |
| [ActiveDockItem](DockManager/ActiveDockItem.md) { get; } | Gets the currently active docking item. |
| [AllowDocumentSwitcher](DockManager/AllowDocumentSwitcher.md) { get; set; } | Gets or sets whether users can open the document switcher. |
| [AllowFreeDocumentLayout](DockManager/AllowFreeDocumentLayout.md) { get; set; } | Gets or sets whether document groups can be arranged in both horizontal and vertical directions within a document host. |
| [AutoHideGroups](DockManager/AutoHideGroups.md) { get; } | Gets the collection of auto-hide groups. |
| [AutoHideMode](DockManager/AutoHideMode.md) { get; set; } | Gets or sets whether expanded auto-hide panels overlay the docking layout or occupy space within it. |
| [AutoHideOnlyActivePane](DockManager/AutoHideOnlyActivePane.md) { get; set; } | Gets or sets whether the auto-hide and pin commands affect only the active pane in a tabbed group. |
| [ClosedPanes](DockManager/ClosedPanes.md) { get; } | Gets the collection of closed panes available for restoration. |
| [CloseOnlyActivePane](DockManager/CloseOnlyActivePane.md) { get; set; } | Gets or sets whether the close command closes only the active pane in a tabbed group. |
| [Commands](DockManager/Commands.md) { get; } | Gets the dock manager's commands. |
| [FloatGroups](DockManager/FloatGroups.md) { get; } | Gets the collection of floating groups. |
| [ItemAdapter](DockManager/ItemAdapter.md) { get; set; } | Gets or sets the adapter used to configure a generated docking item for its source item. |
| [ItemContentTemplate](DockManager/ItemContentTemplate.md) { get; set; } | Gets or sets the template used to display the content of generated docking panes. |
| [ItemsSource](DockManager/ItemsSource.md) { get; set; } | Gets or sets the collection whose items are used to generate docking items. |
| [ItemTemplate](DockManager/ItemTemplate.md) { get; set; } | Gets or sets the template used to create docking items from the data source. |
| [OwnsFloatingDockPanes](DockManager/OwnsFloatingDockPanes.md) { get; set; } | Gets or sets whether floating windows containing tool panes are owned by the dock manager's window. |
| [OwnsFloatingDocuments](DockManager/OwnsFloatingDocuments.md) { get; set; } | Gets or sets whether floating windows containing documents are owned by the dock manager's window. |
| [Root](DockManager/Root.md) { get; set; } | Gets or sets the root group of the docked layout. |
| [SerializationInfo](DockManager/SerializationInfo.md) { get; } | Gets the layout information used during serialization or deserialization. |
| event [CustomizeDockGuide](DockManager/CustomizeDockGuide.md) | Occurs when docking guides are prepared for a dragged item. Use the event to hide guides or guide items. |
| event [DockItemActivated](DockManager/DockItemActivated.md) | Occurs when the active docking item changes. |
| event [DockItemContextMenuOpening](DockManager/DockItemContextMenuOpening.md) | Occurs before a docking item context menu opens. Cancel the event to prevent the menu from opening. |
| event [DockItemEndFloatDragging](DockManager/DockItemEndFloatDragging.md) | Occurs when dragging a floating docking item ends. |
| event [DockItemStartFloatDragging](DockManager/DockItemStartFloatDragging.md) | Occurs when dragging a floating docking item starts. |
| event [DockOperationCompleted](DockManager/DockOperationCompleted.md) | Occurs after a docking operation completes. |
| event [DockOperationStarting](DockManager/DockOperationStarting.md) | Occurs before a docking operation starts. Cancel the event to prevent the operation. |
| event [RegisterDockItem](DockManager/RegisterDockItem.md) | Occurs when a docking item is registered with the dock manager. |
| [AutoHide](DockManager/AutoHide.md)(…) | Moves the panes in the specified item into an auto-hide group and returns whether the operation succeeded. |
| [Close](DockManager/Close.md)(…) | Closes the panes in the specified item and returns whether the operation succeeded. |
| [CollapseAutoHidePanel](DockManager/CollapseAutoHidePanel.md)(…) | Collapses the auto-hide panel for the specified pane and returns whether the operation succeeded. |
| [Dock](DockManager/Dock.md)(…) | Docks the specified item using its docking history and returns whether the operation succeeded. (2 methods) |
| [ExpandAutoHidePanel](DockManager/ExpandAutoHidePanel.md)(…) | Expands the auto-hide panel for the specified pane and returns whether the operation succeeded. |
| [Float](DockManager/Float.md)(…) | Moves the specified item into a floating window and returns whether the operation succeeded. |
| [Remove](DockManager/Remove.md)(…) | Removes the specified item and its docking history from the layout and returns whether the operation succeeded. |
| [Restore](DockManager/Restore.md)(…) | Restores a closed pane to its previous layout position and returns whether the operation succeeded. |
| [RestoreLayout](DockManager/RestoreLayout.md)(…) | Restores the docking layout from the specified stream using the default serialization settings. (2 methods) |
| [SaveLayout](DockManager/SaveLayout.md)(…) | Saves the docking layout to the specified stream using the default serialization settings. (2 methods) |
| static [GetDockItem](DockManager/GetDockItem.md)(…) | Gets the docking item associated with the specified object. |
| static [SetDockItem](DockManager/SetDockItem.md)(…) | Sets the docking item associated with the specified object. |
| static [SetDockManager](DockManager/SetDockManager.md)(…) | Sets the dock manager associated with the specified object. |

## See Also

* namespace [Eremex.AvaloniaUI.Controls.Docking](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->
