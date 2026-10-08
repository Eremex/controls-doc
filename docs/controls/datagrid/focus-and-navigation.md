---
title: Focus and Navigation
order: 49500
seealso: []
---

# Focus and Navigation


## Cell and Row Navigation Modes

The DataGrid's default behavior allows users to navigate between cells using the keyboard, or focus them using the mouse.
Use the [`DataGridControl.NavigationMode`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/NavigationMode.md) property to switch between Cell Navigation and Row Navigation modes.

**Cell Navigation** (default)

Users can focus any cell using the keyboard or mouse.

![grid-navigationmode-cell](../../images/grid-navigationmode-cell.png)

**Row Navigation**

Users cannot focus individual cells, and cell edit operations are disabled. Clicking a cell highlights the entire row.

``` xml
<mxdg:DataGridControl x:Name="dataGrid" NavigationMode="Row">
```

![grid-navigationmode-row](../../images/grid-navigationmode-row.png)



## Focused Column

Use the [`DataGridControl.FocusedColumn`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/FocusedColumn.md) property to obtain the focused column. To move focus to a specific column, assign a corresponding [`GridColumn`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/GridColumn.md) object to the [`FocusedColumn`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/FocusedColumn.md) property.

!!! note

    You can only focus a column in [Cell Navigation mode](#cell-and-row-navigation-modes).

## Focused Row

Use the [`DataGridControl.FocusedRowIndex`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/FocusedRowIndex.md) property to retrieve the focused row's [index](rows.md#identify-and-get-rows). The [`DataGridControl.FocusedItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/FocusedItem.md) property allows you to retrieve the focused row's underlying data object.

To move focus to a specific row, you can assign this row's index to the [`DataGridControl.FocusedRowIndex`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/FocusedRowIndex.md) property.

## Focused Cell

The focused cell is determined by the intersection of the focused row and focused column. To move focus to a specific cell, focus the target [row](#focused-row) and [column](#focused-column).

<!-- TODO
Example - focus a specific cell
 -->