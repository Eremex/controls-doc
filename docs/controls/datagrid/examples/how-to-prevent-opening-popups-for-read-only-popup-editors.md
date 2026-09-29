---
title: How to Prevent Opening Popups for Read-only Popup Editors
order: 1000
seealso: []
---

# How to Prevent Opening Popups for Read-only Popup Editors


Starting with version 1.2, you can use a popup editor's `ShowPopupIfReadOnly` property to prevent popups from being opened for read-only popup editors.

In earlier versions, you can control this behavior using the `PopupEditor.PopupOpening` event. The current topic provides more information on using this event.


When bound to read-only columns, in-place popup editors (`DateEditor`, `ComboBoxEditor`, `MemoEditor`, and so on) still allow their popups to be displayed. 
The `PopupEditor.PopupOpening` event fires just before a popup appears, allowing you to conditionally disable it — for example, when the editor is bound to a read-only column. You can handle this event for a specific in-place editor, or globally (to apply the logic to all popup editors in the application).


## Disable Popups for a Specific Read-only Column

1. Associate an in-place editor with a grid column using the `GridColumn.CellTemplate` property. 
2. Handle the editor's `PopupEditor.PopupOpening` event to perform actions when a popup is displayed for this editor. 

In the following example, a grid column is associated with a `DateEditor` in-place editor. The `DateEditor.PopupOpening` event handler disables the editor's popup when the grid column is read-only.

``` xml
<mxdg:GridColumn FieldName="BirthDate" Width="*" MinWidth="80">
    <mxdg:GridColumn.CellTemplate>
        <DataTemplate>
            <mxe:DateEditor x:Name="PART_Editor" PopupOpening="DateEditor_PopupOpening"/>
        </DataTemplate>
    </mxdg:GridColumn.CellTemplate>
</mxdg:GridColumn>
```

``` cs
private void DateEditor_PopupOpening(object sender, OpeningPopupEventArgs e)
{
    e.Cancel = (sender as PopupEditor).ReadOnly;
}
```

## Disable Popups for all Popup Editors Bound to Read-only Columns

You can use Class Handlers or the Behavior mechanism to process editors' events globally.

### Use a Class Handler to Disable Popups for Read-only Editors Globally

Class Handlers in Avalonia enable event processing at the class level rather than the instance level. They allow you to attach event handlers to all instances of a control type without manually subscribing to each one. 

The following example adds a class handler for the `PopupEditor.PopupOpening` event. This code affects all `PopupEditor` descendants.


``` cs
public partial class MainWindow : MxWindow
{
    public MainWindow()
    {
        InitializeComponent();
        PopupEditor.PopupOpeningEvent.AddClassHandler<PopupEditor>(PopupEditor_PopupOpening);
    }

    private void PopupEditor_PopupOpening(object sender, OpeningPopupEventArgs e)
    {
        e.Cancel = (sender as PopupEditor).ReadOnly;
    }
}
```


### Use the Behavior Mechanism to Disable Popups for Read-only Editors Globally

This approach requires the use of the `Avalonia.Xaml.Interactivity` package, which provides the Behavior pattern implementation for Avalonia UI. `Behavior` objects allow you to customize properties and subscribe to events for all instances of a given control type.

The following code creates a global `Behavior` object for all `PopupEditor` class instances. The `Behavior` object handles the `PopupEditor.PopupOpening` event to disable popups in read-only columns.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:behaviors="using:DemoCenter.Behaviors"

<UserControl.Styles>
    <Style Selector=":is(mxe|PopupEditor)">
        <Setter Property="Interaction.Behaviors">
            <Setter.Value>
                <BehaviorCollectionTemplate>
                    <BehaviorCollection>
                        <behaviors:PopupEditorReadOnlyPopupBehavior/>
                    </BehaviorCollection>
                </BehaviorCollectionTemplate>
            </Setter.Value>
        </Setter>
    </Style>
</UserControl.Styles>
```

``` cs
using Avalonia.Xaml.Interactivity;
using Eremex.AvaloniaUI.Controls.Editors;

namespace DemoCenter.Behaviors
{
    public class PopupEditorReadOnlyPopupBehavior : Behavior<PopupEditor>
    {
        protected override void OnAttached()
        {
            base.OnAttached();
            AssociatedObject.PopupOpening += AssociatedObject_PopupOpening;
        }

        protected override void OnDetachedFromVisualTree()
        {
            base.OnDetachedFromVisualTree();
            AssociatedObject.PopupOpening -= AssociatedObject_PopupOpening;
        }

        void AssociatedObject_PopupOpening(object sender, OpeningPopupEventArgs e)
        {
            e.Cancel = AssociatedObject.ReadOnly;
        }
    }
}
```