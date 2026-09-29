---
title: DataGrid
order: 100000
seealso: []
---

# DataGrid

`DataGridControl` allows you to display data from an items source in columns and rows. It provides rich data shaping and editing functionality. Users can rearrange columns, edit, sort, group and search for data.

![data-grid](../../images/data-grid.png)

- [Data Binding](data-binding/index.md) — You can bind the control to an IList, IBindingList, DataTable or any IEnumerable data source.
- [Data Sorting](sorting.md) — Allows you to sort data against an unlimited number of columns.
- [Data Grouping](grouping.md) — The data grouping feature combines rows with identical column values into the same data groups. You can group the control's data against multiple columns.
- [Styles](styles.md) — Allow you to customize the appearance settings of the control's elements in various states.
- [Data Edit Operations](data-editing/index.md) — A user can edit cell values if data editing is enabled. You can embed Eremex and custom editors in cells to edit and present cell values in a specific manner.
- Data Validation — The validation mechanism helps you check a user's input and data source's values, and show errors in cells.
- [Built-in and Custom Context Menus](context-menus.md)
- [Unbound Columns](data-binding/unbound-columns.md) — You can add unbound columns (those that are not bound to data source fields) and populate them with data manually, using an event.
- Column Resize and Move Operations
- [Column Filter Menus](filter-and-search.md#column-filters) — You can filter grid data using dropdown menus that display unique column values. Click the filter button in any column header to access filtering options.
- [Search Panel](filter-and-search.md#search-panel) — Helps a user quickly locate rows by the data they contain.
- [Auto Filter Row](filter-and-search.md#auto-filter-row) — A special row that allows a user to filter data against columns.
- [Row Drag-and-Drop](row-drag-and-drop.md) - A user can drag a row within the control and to another control.
- [Column Bands](bands.md) — Allow you to visually group multiple columns under a common header.
- [Fixed Columns](columns.md#fixed-columns) — Allow specific columns to remain visible and anchored to the left or right edge of the grid while other columns scroll horizontally. 
- [Best Fit](columns.md#best-fit) — This feature resizes columns to their minimum widths required to fully display column contents (values and headers) without truncation. 
- Column Header Templates – Allow you to display custom content in column headers, including images.
- Multiple Row Selection (Highlight) — You can enable multiple row selection mode to allow a user to select (highlight) multiple rows at one time. 
- [Data Annotation Attribute Support](columns.md#automatic-column-generation) — The DataGrid control takes into account dedicated Data Annotation attributes applied to the data source's properties. You can use Data Annotation attributes to specify custom visibility, position, read-only state, and display name for auto-generated columns.
- [High Performance for Large Volumes of Data](performance-and-data-virtualization.md) — The data virtualization mechanism for vertical and horizontal scrolling boosts the control's performance when displaying large numbers of rows and columns.
- [Export to XLSX, PDF, CSV and Image Formats](export.md)