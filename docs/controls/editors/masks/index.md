---
title: Masks
order: 1000
seealso: []
---

# Masks

Masks allow you to restrict data input in text editors. They can also be used  to format editor values in display mode (when an editor does not have focus).

To enable masked input, do the following:

- Set an editor's [`TextEditor.MaskType`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskType.md) property to a mask type.
- Set the editor's [`TextEditor.Mask`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Mask.md) property to a specific mask.

The following mask types are supported:

- `Numeric` —  Mask mode tailored to accept numeric values.
- `DateTime` — Mask mode tailored to accept date-time values.

The following topics give you more details on supported mask modes and masks:

- [Numeric Masks](numeric-masks.md)
- [Date-Time Masks](date-time-masks.md)

## Using the Mask as a Display Format

The mask specified by the [`TextEditor.Mask`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Mask.md) property can be used to format the editor's value in display mode (when text editing is not active). The [`TextEditor.MaskUseAsDisplayFormat`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskUseAsDisplayFormat.md) property specifies this setting. The property's default value is `true`.

## Mask Culture Settings

Many masks are dependent on the current culture. For instance, the decimal separator for numeric masks is different in different cultures. Date-time values are formatted using culture-specific patterns and localized names for the days of the week and months.

The [`TextEditor.MaskCulture`](../../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskCulture.md) property allows you to set the culture to use by the mask. If this property is not set, the application's default culture is used.

### Example 

The following code sets the "c" numeric mask to enter currency values in a text editor, and applies the _Chinese (Simplified)_ culture to the mask.

![texteditor-mask-currency-chinese](../../../images/texteditor-mask-currency-chinese.png)

``` csharp
textEditor1.EditorValue = 12.34567;
textEditor1.MaskType = Eremex.AvaloniaUI.Controls.Editors.MaskType.Numeric;
textEditor1.MaskCulture = new CultureInfo("zh-CN");
textEditor1.Mask = "c";
```