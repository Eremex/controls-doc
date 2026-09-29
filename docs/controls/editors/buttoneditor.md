---
title: ButtonEditor
order: 118000
seealso: []
---

# ButtonEditor

The `ButtonEditor` is a text editor that can display multiple built-in regular and toggle buttons. 

![buttoneditor](../../images/buttoneditor.png)

The control's main features include:

- Regular and toggle buttons.
- Displaying text and images in buttons.
- Right and left button alignment.
- Tooltips.
- Predefined 'x' button to clear the editor's value.
- Watermarks.

## Built-in Buttons

To add a built-in button, add a `ButtonSettings` object to the `ButtonEditor.Buttons` collection. A `ButtonSettings` object contains button display and behavior options.

### Main Properties and Events

- `ButtonKind` — Specifies whether the button is a regular or toggle button.
- `Content` — The button's text or custom data. Use the `ContentTemplate` property to specify the template to render the custom data.
- `Glyph` — The button's image.
- `GlyphSize` — The button's image size.
- `IsLeft` — Specifies whether the button is aligned to the left or right (default) edge of the edit box.
- `Click` — The event that allows you to respond to button clicks.
- `Command` — Specifies a command raised when the button is clicked.
- `CommandParameter` — Specifies the command's parameter.
- `IsChecked` — Gets or sets whether the toggle button is checked.


### Example - How to add regular and toggle buttons

The following example defines a `ButtonEditor` control with two buttons:

- A regular button associated with the _ResetValue_ command that sets the editor's value to '0'.
- A check button that toggles the parent editor's `IsTextEditable` setting. Text editing is disabled when the button is checked.

It is assumed that the project contains the '_dot.svg_', '_locked.svg_' and '_unlocked.svg_' images in the '_Images_' folder. The regular button displays the '_dot.svg_' image. The check button displays either '_locked.svg_' or '_unlocked.svg_' image depending on the check state.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:local="clr-namespace:EditorsSample"

<Window.DataContext>
    <local:MainViewModel/>
</Window.DataContext>

<mxe:ButtonEditor Name="btnEditor1" 
                  EditorValue="{Binding Quantity, Mode=TwoWay}"
                  IsTextEditable="True">
    <mxe:ButtonEditor.Buttons>
        <mxe:ButtonSettings ButtonKind="Simple"
                            Glyph="{SvgImage 'avares://EditorsSample/Images/dot.svg'}"
                            Command="{Binding ResetValueCommand}"
                            CommandParameter="{Binding #btnEditor1}"
                            ToolTip.Tip = "Reset value"
                            >
        </mxe:ButtonSettings>
        <mxe:ButtonSettings ButtonKind="Toggle"
                            Glyph="{Binding $self.IsChecked, 
                             Converter={local:LockedStateToSvgNameConverter}}"
                            IsChecked="{Binding !$parent.IsTextEditable}"
                            ToolTip.Tip = "Toggle text editing mode"
                >
        </mxe:ButtonSettings>
    </mxe:ButtonEditor.Buttons>
</mxe:ButtonEditor>
```

```csharp
using Eremex.AvaloniaUI.Controls.Utils;

namespace EditorsSample;

[ObservableObject]
public partial class MainViewModel
{
    [ObservableProperty]
    decimal quantity = 0;

    // Sets the editor's value to '0'.
    [RelayCommand]
    void ResetValue(TextEditor editor)
    {
        // You can access the current editor from the command parameter, 
        // and change its value.
        editor.EditorValue = 0;
    }
}

public class LockedStateToSvgNameConverter : MarkupExtension, IValueConverter
{
    public object? Convert(object? value, Type targetType, object? parameter, CultureInfo culture)
    {
        if (value == null)
            return null;
        bool isLocked = (bool)value;
        string lockedState = isLocked ? "locked" : "unlocked";
        if (isLocked)
            lockedState = "locked";
        return ImageLoader.LoadSvgImage(Assembly.GetExecutingAssembly(), $"Images/{lockedState}.svg");
    }

    public object? ConvertBack(object? value, Type targetType, object? parameter, CultureInfo culture)
    {
        throw new NotImplementedException();
    }

    public override object ProvideValue(IServiceProvider serviceProvider)
    {
        return this;
    }
}
```

<!--TODO ## Provide Custom Template to Render Buttons

### Example - How to display an Image and Text in a Button

 -->

## Clear Value ('x') Button

Set the `ButtonEditor.NullValueButtonPosition` property to `ComponentPlacement.EditorBox` to enable the built-in 'x' button which allows a user to set the current value to null. 

![buttoneditor-clearbutton](../../images/buttoneditor-clearbutton.png)

## Watermark

As all `TextEditor` descendants, the `ButtonEditor` control supports a watermark (a grayed out hint displayed when the editor's value is empty or null). 

![buttoneditor-watermark](../../images/buttoneditor-watermark.png)

Use the inherited `TextEditor.Watermark` property to specify a watermark.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:ButtonEditor Name="buttonEditor1" Watermark="User Name or Email" Margin="5">
    ...
</mxe:ButtonEditor>
```


