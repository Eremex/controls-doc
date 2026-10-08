---
title: TextEditor
order: 120000
seealso: []
---

# TextEditor

The [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) control provides base text editing features. It supports masks that allow you to restrict user input and to format values.

![texteditor](../../images/texteditor.png)

The control's main features include:

- Support for single-line and multi-line text.
- Text wrapping.
- Using masks to specify a pattern for data input.
- Using masks to format values when the editor does not have focus.
- Text selection.
- Watermarks

## Specify Text and Customize Text Options

The [`TextEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) property specifies the editor's text. If the text contains _NewLine_ characters, the editor displays the text on multiple lines. 

### Text Wrapping

The [`TextEditor.TextWrapping`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/TextWrapping.md) property allows you to activate automatic text wrapping at the editor's right edge. Set this property to the `Avalonia.Media.TextWrapping.Wrap` value to enable regular text wrapping mode.

### Accept _Tab_ and _Enter_ keys During Input

Users can press the _Tab_ and _Enter_ keys to insert _Tab_ and _Return_ characters in the text. You can use the following options to change this behavior:

- [`TextEditor.AcceptsReturn`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/AcceptsReturn.md) — Specifies whether a _NewLine_ character is inserted when the _Enter_ key is pressed. If this property is disabled, the editor ignores the _Enter_ key.
- `TextEditor.AcceptsTab`— Specifies whether a tab character is inserted when the _Tab_ key is pressed. If this property is disabled, focus is moved to the next control in the tab order when the _Tab_ key is pressed.

## Masks

A [mask](masks/index.md) applied to a text editor guides a user to enter values according to a specified pattern. Masked input is enabled for the [DateEditor](dateeditor.md) and [SpinEditor](spineditor.md) controls, and disabled for other text editors, by default. 

To enable masked input, do the following:

- Set the [`TextEditor.MaskType`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskType.md) property to a mask type.
- Set the [`TextEditor.Mask`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Mask.md) property to a mask.

### Mask Type 

The [`TextEditor.MaskType`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskType.md) property allows you to select mask mode from the following options:

- [`MaskType.Numeric`](../../API/Eremex.AvaloniaUI.Controls.Editors/MaskType.md) — Mask mode tailored to accept numeric values.
- [`MaskType.DateTime`](../../API/Eremex.AvaloniaUI.Controls.Editors/MaskType.md) — Mask mode tailored to accept date-time values.
- [`MaskType.None`](../../API/Eremex.AvaloniaUI.Controls.Editors/MaskType.md) — Masked input is disabled.

### Mask Strings

Use the [`TextEditor.Mask`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Mask.md) property to set a string that specifies a mask. The mask is composed of mask specifiers which are specific to the selected mask type.

See the following topics for more information:

- [Masks](masks/index.md)
- [Numeric Masks](masks/numeric-masks.md)
- [Date-Time Masks](masks/date-time-masks.md)

#### Example - Allow input of integer values in a Text Editor

The following code applies the "_d_" numeric mask to restrict data input to integer values in a TextEditor.

![texteditor-numericmask-d](../../images/texteditor-numericmask-d.png)

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:TextEditor Name="textEditor1" MaskType="Numeric" Mask="d" 
 HorizontalContentAlignment="Right"/>
```

### Using the Mask as a Display Format

The mask specified by the [`TextEditor.Mask`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Mask.md) property can be used to format the editor's value in display mode (when text editing is not active). The [`TextEditor.MaskUseAsDisplayFormat`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskUseAsDisplayFormat.md) property specifies this setting. The property's default value is `true`.

### Mask Culture Settings

Many masks are dependent on the current culture. For instance, the decimal separator for numeric masks is different in different cultures. Date-time values are formatted using culture-specific patterns and localized names for the days of the week and months.

The [`TextEditor.MaskCulture`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskCulture.md) property allows you to set the culture to use by the mask. If this property is not set, the application's default culture is used.

#### Example 

The following code sets the "c" numeric mask to enter currency values in a text editor, and applies the _Chinese (Simplified)_ culture to the mask.

![texteditor-mask-currency-chinese](../../images/texteditor-mask-currency-chinese.png)

``` csharp
textEditor1.EditorValue = 12.34567;
textEditor1.MaskType = Eremex.AvaloniaUI.Controls.Editors.MaskType.Numeric;
textEditor1.MaskCulture = new CultureInfo("zh-CN");
textEditor1.Mask = "c";
```

## Text Selection

A user can select text using the mouse and keyboard. 

To select a portion of text and clear the selection in code, use the following API:

- [`TextEditor.SelectionStart`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/SelectionStart.md) — The zero-based index of the starting character of the text selection.
- [`TextEditor.SelectionEnd`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/SelectionEnd.md) — The zero-based index of the end character of the text selection.
- [`TextEditor.SelectAll`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/SelectAll.md) — Selects all text.
- [`TextEditor.ClearSelection`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/ClearSelection.md) — Deselects the selected text.

## Watermarks

The [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) control and its descendants support watermarks. A watermark is a grayed out hint displayed when the editor's value is empty or null.

![texteditor-watermark](../../images/texteditor-watermark.png)

Use the [`TextEditor.Watermark`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Watermark.md) property to specify a watermark.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:TextEditor Name="textEditor1" Watermark="Type to search"/>
```


## See Also

- [How to create a password text box](examples/How-to-create-a-password-text-box.md)