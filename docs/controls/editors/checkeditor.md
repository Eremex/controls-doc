---
title: CheckEditor
order: 116000
seealso: []
---

# CheckEditor

The [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md) control displays a check box that a user can toggle with the mouse and keyboard. In default mode, the editor supports two check states (checked and unchecked). You can enable the indeterminate state when required.

![checkeditor](../../images/checkeditor.png)

The control's main features include:

- You can choose between two or three check states.
- Displaying a label next to the check box.
- A user can toggle the control with the mouse and keyboard.
- The validation mechanism modifies the appearance of the control to inform users about errors.

## Specify a Check State

A user can toggle a CheckEditor with the mouse. If the editor has focus the user can press the Space or Enter key on the keyboard to change the check state.

In code, you can specify a check state or read the current check state with the [`CheckEditor.IsChecked`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor/IsChecked.md) or [`CheckEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) property. These properties are in sync. They differ in the value type: the [`IsChecked`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor/IsChecked.md) property is of the nullable `bool` type, while the [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) property is of the `object` type as in all Eremex editors.

## Display Text

The [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md) control can display text to the right of the check box. Use the [`Content`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor/Content.md) property to assign the text.

### Example - How to create a CheckEditor

The following example defines a [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md) object that controls the Enabled state of a TreeList control. A user cannot edit the TreeList's data if the check box is unchecked.

![checkeditor-sample](../../images/checkeditor-sample.png)

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"

<mxe:CheckEditor IsChecked="{Binding IsEnabled, ElementName=treeList1}" Content="Edit Data"/>

<mxtl:TreeListControl Name="treeList1">...</mxtl:TreeListControl>
```

## Enable Three States

Enable the [`IsThreeState`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor/IsThreeState.md) property to allow the editor to have three states. 
Successive toggles of the editor switch between the checked, indeterminate and unchecked states.

In the indeterminate state the [`CheckEditor.IsChecked`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor/IsChecked.md) and [`CheckEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) properties return `null`.
