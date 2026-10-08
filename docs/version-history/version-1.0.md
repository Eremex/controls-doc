---
title: Version 1.0
order: 10
seealso: []
---

# Version 1.0

## 1.0.96

### What's New

#### DataGridControl and TreeListControl

- Fixed issue: When using a popup UserControl as a cell editor, the UserControl unexpectedly loses focus.

- Feature: Provide a capability to handle navigation keys (Arrow keys, Tab, Enter, F2, Esc, Home, End, PgUp and PgDown) in in-place editors. 
    
    Grid/treelist controls intercept specific navigation keys (Arrow keys, Tab, Enter, F2, Esc, Home, End, PgUp and PgDown) to perform navigation between cells. To handle these keys in in-place editors, do the following:
    - Create a class that implements the [`IInplaceEditorNavigationHandler`](../API/Eremex.AvaloniaUI.Editors.InplaceEditing/IInplaceEditorNavigationHandler.md) interface. 
    - Implement the [`IInplaceEditorNavigationHandler.NeedsKey`](../API/Eremex.AvaloniaUI.Editors.InplaceEditing/IInplaceEditorNavigationHandler/NeedsKey.md) method. The method should return `true` for the keys that need to be processed in an in-place editor.
    - Associate your [`IInplaceEditorNavigationHandler`](../API/Eremex.AvaloniaUI.Editors.InplaceEditing/IInplaceEditorNavigationHandler.md) object with a specific in-place editor type using the [`EditorNavigationHandlers.RegisterHandler`](../API/Eremex.AvaloniaUI.Editors.InplaceEditing/EditorNavigationHandlers/RegisterHandler.md) static method. For instance: `EditorNavigationHandlers.RegisterHandler<TextBox, MyTextBoxNavigationHandler>();`.

- Fixed issue: When cell editing is disabled, a control placed in a cell's template is activated on a click.
- Fixed issue: Updating a cell value in a sorted grid column results in value changes in other cells.
- Fixed issue: The Esc key does not roll back changes in a cell when a CellTemplate is used.

#### PropertyGrid

- Feature: Add the `HiddenEditor` event.
- Feature: Add the `Row` parameter to the `ShowingEditor` event.

#### Editors

- Incorrect popup editor size when using a large DPI setting.


#### Charts
- Fixed issue: Crosshair crash in some cases.
- Fixed issue: Exception when using the [`SortedDateTimeDataAdapter`](../API/Eremex.AvaloniaUI.Charts/SortedDateTimeDataAdapter.md) with empty data.


## 1.0.93


### What's New

#### ListView

- Fixed issue: The current item selection is not cleared when an item is clicked.
- Fixed issue: The CTRL+A shortcut does not select all items in multiple selection mode.
- ListViewControl.GroupWidth property is not supported and has been removed.
- ListViewControl.GetGroupValueDisplayText method is now internal.

#### PropertyGrid

- Fixed issue: Unable to move focus away from an in-place editor when a validation error occurs and a CellTemplate is used



## 1.0

### What's New

#### Charts

[`PolarChart`](../API/Eremex.AvaloniaUI.Charts/PolarChart.md) control - A new chart control that plots a diagram on a polar coordinate system.

- Crosshair
- Strips and constant lines
- Sweep direction and start angle (for the X axis)
- Point Series View
- Line Series View
- Scatter Line Series View
- Area Series View
- Range Area Series View

[`SmithChart`](../API/Eremex.AvaloniaUI.Charts/SmithChart.md) control - A new control that plots a Smith chart.

- Crosshair
- Point Series View
- Scatter Line Series View

##### `CartesianChart` Updates

- Strips and constant lines
- Point Series View (with SVG marker support)
- Area Series View
- Scatter Line Series View
- Step Line Series View
- Step Area Series View
- Range Area Series View
- Bar Series View
- Range Bar Series View 

##### Common Features

- Using the MVVM design pattern to supply data and customize chart options.
- Dark theme variant support.
- New `DiagramPointToScreenPoint` and `ScreenPointToDiagramPoint` methods are helpful when you need to display custom graphics or tooltips, and need to identify coordinates of target chart elements.


#### Docking
* [`DockPane.ShowGlyphMode`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/ShowGlyphMode.md) property - Specifies the visibility and position of a glyph in a panel's header.
* [`DockPane.ShowTabGlyphMode`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/ShowTabGlyphMode.md) property - Specifies the visibility and position of a glyph in a panel's header (tab) when the panel is hosted within a tabbed group.
- [`FloatGroup.ShowGlyphMode`](../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup/ShowGlyphMode.md) property -  Specifies the visibility and position of a glyph in a floating window's header
- [`DockItemBase.FloatGroup`](../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/FloatGroup.md) property - Allows you to retrieve the floating window ([`FloatGroup`](../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup.md)) that hosts the current dock item (panel) in floating mode.
- [`DockItemBase.AutoHideGroup`](../API/Eremex.AvaloniaUI.Controls.Docking/DockItemBase/AutoHideGroup.md) property - Allows you to retrieve the auto-hide container ([`AutoHideGroup`](../API/Eremex.AvaloniaUI.Controls.Docking/AutoHideGroup.md)) that hosts the current dock item (panel) in auto-hide mode.
- [`DockManager.ExpandAutoHidePanel`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/ExpandAutoHidePanel.md) - Expands a collapsed auto-hidden panel.
- [`DockManager.CollapseAutoHidePanel`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/CollapseAutoHidePanel.md) - Collapses an expanded auto-hidden panel. 
- [`DockManager.SaveLayout`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/SaveLayout.md) and [`DockManager.RestoreLayout`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/RestoreLayout.md) methods - Allow you to save and restore a control's layout to/from a stream.

#### DataGridControl and TreeListControl

- [`SaveLayout`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/SaveLayout.md) and [`RestoreLayout`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/RestoreLayout.md) methods - Allow you to save and restore a control's layout to/from a stream.

#### TreeListControl and TreeViewControl

- `ShowBranchesWithMatches` filter mode - You can set the [`TreeListControlBase.FilterMode`](../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/FilterMode.md) property to `ShowBranchesWithMatches` to display entire branches when they contain nodes that match filter criteria.

#### Editors

* [`BaseEditor.Validate`](../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/Validate.md) event - Eremex editors now support the [`Validate`](../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/Validate.md) event that allows you to implement custom validation rules.
* [`BaseEditor.DoValidate`](../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/DoValidate.md) method - Allows you to forcibly invoke the validation.

#### Common Classes

- `ImageLoader` - The new `Eremex.AvaloniaUI.Controls.Utils.ImageLoader` class provides methods to load images (SVG, PNG, etc) by URIs from resources.


### Breaking Changes


#### DataGridControl and TreeListControl
* `ColumnBase.HeaderContentTemplate` property renamed to `HeaderTemplate`
* `ColumnBase.HeaderHorizontalContentAlignment`  property renamed to [`HeaderHorizontalAlignment`](../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlColumnBase/HeaderHorizontalAlignment.md)
* `ColumnBase.HeaderVerticalContentAlignment`  property renamed to [`HeaderVerticalAlignment`](../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlColumnBase/HeaderVerticalAlignment.md)

#### DataGridControl
* `GetRowIndexBySourceIndex` method renamed to `GetRowIndexBySourceItemIndex`
* `GetRowIndexByVisibleIndex` method renamed to `GetRowIndexByVisibleRowIndex`
* `GetSourceIndexByRowIndex` method renamed to `GetSourceItemIndexByRowIndex`
* `GetSourceIndexByVisibleIndex` method renamed to `GetSourceItemIndexByVisibleRowIndex`
* `GetVisibleIndexByRowIndex` method renamed to `GetVisibleRowIndexByRowIndex`
* `GetVisibleIndexBySourceIndex` method renamed to `GetVisibleRowIndexBySourceItemIndex`
* `GetItemByVisibleIndex` method renamed to `GetSourceItemByVisibleRowIndex`
* `GetItemByRowIndex` method renamed to `GetSourceItemByRowIndex`
* `CustomColumnSort` event: The `SourceIndex1` event argument is renamed to `SourceItemIndex1`. The `SourceIndex2` event argument is renamed to `SourceItemIndex2`

#### Docking

* `TabbedGroup.TabHeader` attached property is replaced with the [`DockPane.TabHeader`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/TabHeader.md) property
* `TabbedGroup.TabHeaderTemplate` attached property is replaced with the [`DockPane.TabHeaderTemplate`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/TabHeaderTemplate.md) property
* `TabbedGroup.TabGlyph` attached property  is replaced with the  [`DockPane.TabGlyph`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/TabGlyph.md) property
* `TabbedGroup.TabGlyphSize` attached property is replaced with the [`DockPane.TabGlyphSize`](../API/Eremex.AvaloniaUI.Controls.Docking/DockPane/TabGlyphSize.md) property
* `TabbedGroup.ShowTabPanelForSinglePage` renamed to  [`ShowTabStripForSingleChild`](../API/Eremex.AvaloniaUI.Controls.Docking/TabbedGroup/ShowTabStripForSingleChild.md)
* `DockManager.Hide` method renamed to [`DockManager.AutoHide`](../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/AutoHide.md)

#### Common Classes
* The `SerializationHelper` class renamed to `SerializationManager`