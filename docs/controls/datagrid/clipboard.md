---
title: Clipboard
order: 1200
seealso: []
---

# Clipboard

The Data Grid control now supports the CTRL+C shortcut to copy the row selection to the clipboard.

In code, you can use the `CopyToClipboardAsync` method to copy the row selection. This method is asynchronous - it immediately returns a `Task` object without waiting for the copy operation to complete. 
Asynchronous methods do not block the UI thread.

- The `CopyToClipboardAsync` method copies display text of selected rows' cells. In single selection mode, the focused row is copied to the clipboard. In multiple selection mode, all selected rows are copied. 
- If a group row is selected, it's copied to the clipboard as well. Rows nested within the selected group row are not copied, unless they are selected.
- Column headers are copied to the clipboard, by default. Set the `DataGridControl.ClipboardCopyHeaders` option to false to prevent copying column headers.
- Column headers and cell values are separated in the clipboard by TAB characters.


## Related API

- `DataControlBase.SelectionMode` — Allows you to enable multiple row selection.
- `DataControlBase.SelectedItems` — Specifies the collection of data (business) objects that correspond to selected rows.
- `DataGridControl.GetCellDisplayText` — Returns the display text of a specific cell, addressed by a row and column (or field name).
- `DataGridControl.ClipboardCopyHeaders` — Gets or sets whether to copy column headers to the clipboard.


<!-- TODO
CTRL+C ??
example for CTRL+C ?
 -->

 <!-- TODO
 create Clipboard topic for TreeList
  -->