---
title: Document Switcher
order: 58000
seealso: []
---

# Document Switcher

The Document Switcher provides a classic solution to switch to a specific document or panel using the keyboard. To open the Document Switcher, use the following shortcuts:

- Hold down the CTRL key and then press TAB

    or

- Hold down the CTRL key and then press SHIFT+TAB

A quick press of CTRL+TAB or CTRL+SHIFT+TAB immediately switches to the previous or next recently used document, respectively.

![docking-document-switcher](../../images/docking-document-switcher.png)



The Document Switcher displays a list of panels ([Dock Panes](dock-panes-and-containers.md)) on the left and a list of documents ([Document Panes](document-panes.md)) on the right. 

The Document Switcher stays opened while the CTRL key is being pressed.
To navigate between dock items in the active Document Switcher, keep the CTRL key pressed down and then use the following shortcuts:

- TAB and SHIFT+TAB — Navigates through the active list forward and backward.
- DOWN ARROW and UP ARROW keys — Equivalent to the TAB and SHIFT+TAB shortcuts.
- LEFT ARROW and RIGHT ARROW keys — Switches between the left list of panels and the right list of documents.

To close the Document Switcher and activate the selected panel or document, release the CTRL key or click the panel/document with the mouse.

## Disable the Document Switcher

Set the `DockManager.AllowDocumentSwitcher` property to `false` to disable the Document Switcher. This setting also disables the CTRL+TAB and CTRL+SHIFT+TAB shortcuts for navigation between dock items.

## Show Panes in the Document Switcher

To prevent a pane from being displayed in the Document Switcher, disable the `DockPane.ShowInDocumentSwitcher` option.

Closed panels are not accessible in the Document Switcher.

## Display Pane Descriptions in the Document Switcher

The Document Switcher supports two regions where it displays descriptions of the selected pane.

![docking-document-switcher-with-pane-descriptions](../../images/docking-document-switcher-with-pane-descriptions.png)

Use the following properties to specify pane descriptions to display in the Document Switcher: 

- `DockPane.DocumentSwitcherDescription` — Specifies the pane's description to display at the top of the Document Switcher.
- `DockPane.DocumentSwitcherFooterDescription` — Specifies the pane's description to display at the bottom of the Document Switcher.
