---
title: PropertyGrid Overview
order: 1900
seealso: []
---

# PropertyGrid Overview

The `PropertyGridControl` displays public properties and their values of a bound object(s) as a vertical list. Each list item is rendered as a row that contains two cells: "property name" and "property value".

![propertygrid1](../../images/propertygrid1.png)

The PropertyGrid can automatically populate rows from the bound object(s). You can also manually create rows in code. Dedicated attributes applied to the bound object's properties allow you to specify custom visibility, read-only state, display name, category, and type converter.

The control supports category rows that allow you to combine rows into expandable groups.

## Data Binding and Row Customization

When you bind a control to an object(s), the control automatically generates rows for all public properties. Dedicated attributes allow you to customize row generation options.

The control also supports manual generation of regular and category rows. See the following topics for information:

- [Bind to One Object](data-binding.md#bind-to-one-object)
- [Bind to Multiple Object](data-binding.md#bind-to-multiple-objects)
- [Row Creation](data-binding.md#row-creation)
- [Rows](rows.md)

## Data Editing

Users can edit the "value" part of rows if data editing is enabled. The control uses default editors to display and edit row values of common data types (Boolean, Double, Integer, Enumerations, etc.). You can also specify custom editors for specific rows when required.

See the following topics to learn how to specify and access editors, obtain and set cell values:

- [Data Editing](data-editing.md)
- [Custom Editors](custom-editors.md)

## Built-In Search

The PropertyGrid's Search Panel allows users to quickly locate rows by names.

Refer to the following topic to learn more: 

- [Data Searching](data-search.md)

## Frequently Used API

See the following topic to find out the API members that help you accomplish most popular customization tasks:

- [Frequently Used API](frequently-used-api.md)