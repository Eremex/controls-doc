---
title: SegmentedEditor
order: 104000
seealso: []
---

# SegmentedEditor

[`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) presents a set of items (options) as horizontally arranged segments. A user can click one of the segments to select a corresponding option, or CTRL-click on a selected segment to clear the selection.

![segmentededitor](../../images/segmentededitor.png)

The control's main features include:

- Populating segments from a list of strings, a list of business objects, or an enumeration type.
- Item templates allow you to render segments in a custom manner.
- Use of the control as an in-place editor within container controls (for instance, TreeList, TreeView, and PropertyGrid).

## Specify the Items Source

Use the [`SegmentedEditor.ItemsSource`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ItemsSource.md) property to specify the items source used to create the control's segments. You can bind the editor to a list of strings, a list of business objects, or an enumeration type.

## Bind to a List of Strings

The simplest items source is a list of strings.

### Example - How to bind to a string list
The following example populates a [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) control with a list of strings.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:sys="clr-namespace:System;assembly=mscorlib"
xmlns:col="using:System.Collections"

<mxe:SegmentedEditor>
    <mxe:SegmentedEditor.ItemsSource>
        <col:ArrayList>
            <sys:String>Montevideo</sys:String>
            <sys:String>Havana</sys:String>
            <sys:String>Santiago</sys:String>
            <sys:String>La Paz</sys:String>
        </col:ArrayList>
    </mxe:SegmentedEditor.ItemsSource>
</mxe:SegmentedEditor>
```

## Bind to a List of Business Objects

You can bind a [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) control to a list of business objects. In this case, the control's default behavior is as follows:

- A business object's `ToString` method specifies the default text representation of items.
- When you select an item, the editor's value ([`SegmentedEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md)) is set to the corresponding business object.

A typical business object has multiple properties. You can specify which business object properties supply item display text and edit values. Use the following API members for this purpose:

- [`SegmentedEditor.DisplayMember`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/DisplayMember.md) - Gets or sets the name of the business object's property that specifies item display text. 
- [`SegmentedEditor.ValueMember`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ValueMember.md) - Gets or sets the name of the business object's property that specifies item values. When you select an item, the editor's value ([`SegmentedEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md)) is set to the item's [`ValueMember`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ValueMember.md) property value. 

### Example - How to bind to a business object list

The following example binds a SegmentedEditor control to a list of _Product_ business objects. The _Product.ProductName_ property specifies item display text. The _Product.ProductID_ property specifies item values.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:sys="clr-namespace:System;assembly=mscorlib"

<Window.DataContext>
    <local:MainViewModel/>
</Window.DataContext>

<mxe:SegmentedEditor
    Name="segmEditor1"
    ItemsSource="{Binding Products}"
    DisplayMember="ProductName"
    ValueMember="ProductID" />
```
``` csharp
public MainViewModel()
{
    Products = new ObservableCollection<Product>();
    Products.Add(new Product(0, "Chai", "Beverages", 200));
    Products.Add(new Product(1, "Chang", "Beverages", 100))
    Products.Add(new Product(3, "Ikura", "Seafood", 500));
    Products.Add(new Product(5, "Tofu", "Produce", 430));
    //...
}

public partial class Product :ObservableObject
{
    public Product(int productID, string productName, string category, int productPrice)
    {
        ProductID = productID;
        ProductName = productName;
        Category = category;
        ProductPrice = productPrice;
    }

    [ObservableProperty]
    public int productID;

    [ObservableProperty]
    public string productName;

    [ObservableProperty]
    public string category;

    [ObservableProperty]
    public decimal productPrice;
}
```

## Bind to an Enumeration

[`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) can populate its segments with values of an enumeration type. 

The `Eremex.AvaloniaUI.Controls.Common.EnumItemsSource` helper class facilitates binding to an enumeration. Its main features include:

- Images for enumeration members. Apply the `Eremex.AvaloniaUI.Controls.Common.ImageAttribute` attribute to the target enumeration members to specify images.
- Custom display names for enumeration members. Use the `System.ComponentModel.DataAnnotations.DisplayAttribute` attribute or custom converter to change the default item display text.
- Tooltips for items. A tooltip contains a target item's description that you can supply with the `System.ComponentModel.DataAnnotations.DisplayAttribute` attribute or custom converter.

Use the following `EnumItemsSource` properties to set up binding to an enumeration type:

- `EnumItemsSource.EnumType` — Specifies the enumeration type whose values are displayed in the [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) control.
- `EnumItemsSource.ShowImages` — Specifies whether to display images for enumeration members. You can supply images using the `Eremex.AvaloniaUI.Controls.Common.ImageAttribute` attribute.
- `EnumItemsSource.ShowNames` — Specifies whether to display item text. Set `ShowNames` to `false` and `ShowImages` to `true` to render enumeration members using images without text.
- `EnumItemsSource.ImageSize` — Specifies the display size of images assigned to enumeration members.
- `EnumItemsSource.NameToDisplayTextConverter` — Allows you to assign a converter that retrieves custom display text for enumeration members.
- `EnumItemsSource.NameToDescriptionConverter` — Allows you to assign a converter that retrieves enumeration member descriptions, which are displayed as tooltips when a user hovers the mouse over segments.

### Example - How to display enumeration values, and use attributes to supply display text and images for enumeration members.

The following example displays values of a _ProductCategoryEnum_ enumeration in [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md). It uses the `EnumItemsSource` class for data binding.

The `System.ComponentModel.DataAnnotations.DisplayAttribute` and `Eremex.AvaloniaUI.Controls.Common.ImageAttribute` attributes specify custom display text, descriptions (tooltips) and images for the enumeration members.

``` xml
xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:SegmentedEditor Name="segmentedEditorEnum"
        ItemsSource="{mx:EnumItemsSource EnumType=local:ProductCategoryEnum, 
         ImageSize='16, 16', ShowImages=True, ShowNames=True}">
</mxe:SegmentedEditor>
```
``` csharp
using Eremex.AvaloniaUI.Controls.Common;
using System.ComponentModel.DataAnnotations;

public enum ProductCategoryEnum
{
    // The images assigned to the enumeration values below are placed 
    // in the EditorsSample/Images folder.
    // They have their "Build Action" properties set to "AvaloniaResource".
    [Image($"avares://EditorsSample/Images/Products/DairyProducts.svg")]
    [Display(Name = "Dairy Products", Description = "Products made from milk")]
    DairyProducts,

    [Image($"avares://EditorsSample/Images/Products/Beverages.svg")]
    [Display(Description = "Edible drinks")]
    Beverages,

    [Image($"avares://EditorsSample/Images/Products/Condiments.svg")]
    [Display(Description = "Flavor Enhancers")]
    Condiments,

    [Image($"avares://EditorsSample/Images/Products/Confections.svg")]
    [Display(Description = "Sweets")]
    Confections
}
```

### Example - How to display enumeration values, and use custom converters to supply display text for enumeration members.

The following example uses the `EnumItemsSource` class to display values of an enumeration type in a [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) control. The `EnumItemsSource.NameToDisplayTextConverter` and `EnumItemsSource.NameToDescriptionConverter` objects supply custom display text and descriptions (tooltips) for enumeration members.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
xmlns:local="clr-namespace:EditorsSample"

<mxe:SegmentedEditor Name="segmentedEditorEnumWithConverters"
        ItemsSource="{mx:EnumItemsSource EnumType=local:ProductCategoryEnum, 
         ImageSize='16, 16', ShowImages=True, ShowNames=True, 
         NameToDisplayTextConverter={local:EnumMemberNameToDisplayTextConverter}, 
         NameToDescriptionConverter={local:EnumMemberNameToDescriptionConverter}}"
        >
</mxe:SegmentedEditor>
```

``` csharp
using Eremex.AvaloniaUI.Controls.Common;

public enum ProductCategoryEnum
{
    // The images assigned to the enumeration values below are placed 
    // in the EditorsSample/Images folder.
    // They have their "Build Action" properties set to "AvaloniaResource".
    [Image($"avares://EditorsSample/Images/Products/DairyProducts.svg")]
    DairyProducts,

    [Image($"avares://EditorsSample/Images/Products/Beverages.svg")]
    Beverages,

    [Image($"avares://EditorsSample/Images/Products/Condiments.svg")]
    Condiments,

    [Image($"avares://EditorsSample/Images/Products/Confections.svg")]
    Confections
}

public class EnumMemberNameToDisplayTextConverter : BaseEnumConverter
{
    protected override void PopulateDictionary()
    {
        TextValueDictionary.Add("ProductCategoryEnum_DairyProducts", "Dairy");
    }
}
public class EnumMemberNameToDescriptionConverter : BaseEnumConverter
{
    protected override void PopulateDictionary()
    {
        TextValueDictionary.Add("ProductCategoryEnum_DairyProducts", "Milk Products");
    }
}

public abstract class BaseEnumConverter : MarkupExtension, IValueConverter
{
    protected Dictionary<string, string> TextValueDictionary;

    public BaseEnumConverter()
    {
        TextValueDictionary = new Dictionary<string, string>();
        PopulateDictionary();
    }

    protected abstract void PopulateDictionary();

    public override object ProvideValue(IServiceProvider serviceProvider)
    {
        return this;
    }
    public object? Convert(object? value, Type targetType, object? parameter, 
     System.Globalization.CultureInfo culture)
    {
        var type = value?.GetType();
        var memberName = value?.ToString();
        if (type == null || !type.IsEnum || string.IsNullOrEmpty(memberName))
            return null;
        return EnumMemberToString(type.Name, memberName);
    }
        
    protected virtual string EnumMemberToString(string enumName, string enumMemberName)
    {
        string fullMemberName = enumName + "_" + enumMemberName;
        if (TextValueDictionary.ContainsKey(fullMemberName))
            return TextValueDictionary[fullMemberName];
        else 
            return enumMemberName;
    }
        
    public object? ConvertBack(object? value, Type targetType, object? parameter, 
     System.Globalization.CultureInfo culture)
    {
        return null;
    }
}
```

## Get and Set the Selected Item, and Specify the Editor Value

When a user selects a segment or deselects it with a Ctrl-click, the [`SegmentedEditor.SelectedItem`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/SelectedItem.md) and [`SegmentedEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) properties are changed accordingly.
You can use any of these properties to get and set the editor's selected value.

The [`SegmentedEditor.SelectedItem`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/SelectedItem.md) property specifies the selected segment's underlying data object.

The [`SegmentedEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) property has the following meanings:

- If the [`ValueMember`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ValueMember.md) property is empty, the [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) and [`SelectedItem`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/SelectedItem.md) properties are equivalent.
- Otherwise, the [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) property is synced with the [`ValueMember`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ValueMember.md) property value of the selected underlying data object.

To clear the selection, set the [`SegmentedEditor.SelectedItem`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/SelectedItem.md) property to `null`.
 
### Example - How to select an item when SegmentedEditor is bound to a string list

The following example shows how to use the [`SelectedItem`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/SelectedItem.md) or [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) property to select an item in a [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) control that is bound to a list of strings.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:sys="clr-namespace:System;assembly=mscorlib"
xmlns:col="using:System.Collections"

<mxe:SegmentedEditor Name="segmEditorStrings">
    <mxe:SegmentedEditor.ItemsSource>
        <col:ArrayList>
            <sys:String>Montevideo</sys:String>
            <sys:String>Havana</sys:String>
            <sys:String>Santiago</sys:String>
            <sys:String>La Paz</sys:String>
        </col:ArrayList>
    </mxe:SegmentedEditor.ItemsSource>
</mxe:SegmentedEditor>
```
``` csharp
// Use the SelectedItem property:
segmEditorStrings.SelectedItem = "Santiago";
//or the EditorValue property:
segmEditorStrings.EditorValue = "Santiago";
```

### Example - How to select an item when SegmentedEditor is bound to a business object list

In the following example, a [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) control is bound to a list of _Product_ objects. The [`ValueMember`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ValueMember.md) property refers to the _Product.ProductID_ member. Thus, product IDs serve as item values. When a user selects a segment, the [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) property is set to a correponding product ID. The example uses the [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) property to select an item in code.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:sys="clr-namespace:System;assembly=mscorlib"
xmlns:local="clr-namespace:EditorsSample"

<Window.DataContext>
    <local:MainViewModel/>
</Window.DataContext>

<mxe:SegmentedEditor
    Name="segmEditor1"
    ItemsSource="{Binding Products}"
    DisplayMember="ProductName"
    ValueMember="ProductID" />
```

``` csharp
// Select an item by its product ID:
var itemSource = segmEditor1.ItemsSource as ObservableCollection<Product>;
if (itemSource != null)
    segmEditor1.EditorValue = itemSource[3].ProductID;
//The SelectedItem property will return the itemSource[3] object.

//...
[ObservableObject]
public partial class MainViewModel : ViewModelBase
{
    [ObservableProperty]
    public ObservableCollection<Product> products;

    public MainViewModel()
    {
        Products = new ObservableCollection<Product>();
        Products.Add(new Product(0, "Chai", "Beverages", 200));
        Products.Add(new Product(1, "Chang", "Beverages", 100))
        Products.Add(new Product(3, "Ikura", "Seafood", 500));
        Products.Add(new Product(5, "Tofu", "Produce", 430));
    }
}

public partial class Product :ObservableObject
{
    public Product(int productID, string productName, string category, int productPrice)
    {
        ProductID = productID;
        ProductName = productName;
        Category = category;
        ProductPrice = productPrice;
    }

    [ObservableProperty]
    public int productID;

    [ObservableProperty]
    public string productName;

    [ObservableProperty]
    public string category;

    [ObservableProperty]
    public decimal productPrice;
}
```

## Specify Item Templates

When a [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) is bound to a list of strings or business objects, the control's segments display the default text representation of items. The default item display text is defined as follows:

- The value returned by an underlying data object's `ToString` method, if the [`ValueMember`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ValueMember.md) property is not set.
- Otherwise, the text representation of the value stored in the data object's [`ValueMember`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ValueMember.md) property.

Item templates give you the flexiblity to specify what to display in the editor's segments. They allow you to display images, and values of multiple properties in the segments. Use the [`SegmentedEditor.ItemTemplate`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ItemTemplate.md) property to specify an item template.

### Example - How to display an image and text for SegmentedEditor items

The following example shows how to create an item template that displays images and text in a [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) control's segments.

In the example, the [`SegmentedEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor.md) control is bound to a collection of _CapitalInfo_ objects which store information on countries, capitals of the countries, and national flags. 
The created item template (the [`SegmentedEditor.ItemTemplate`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ItemTemplate.md) property) displays a country flag followed by the name of the country's capital.

The [`SegmentedEditor.ValueMember`](../../API/Eremex.AvaloniaUI.Controls.Editors/SegmentedEditor/ValueMember.md) property refers to the _CapitalInfo.Capital_ property. When a user selects a segment, the editor's [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) property is set to the name of the corresponding country's capital.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:local="clr-namespace:EditorsSample"

<Window.DataContext>
    <local:MainViewModel/>
</Window.DataContext>

<Window.Resources>
    <DataTemplate x:Key="CapitalItemTemplate">
        <Grid>
            <Grid.ColumnDefinitions>
                <ColumnDefinition Width="Auto"/>
                <ColumnDefinition Width="*"/>
            </Grid.ColumnDefinitions>
            <Image Width="16" Height="16" Source="{Binding Path=Flag}"/>
            <TextBlock VerticalAlignment="Center" Grid.Column="1" 
             Margin="6,0,0,0" Text="{Binding Path=Capital}"/>
        </Grid>
    </DataTemplate>
</Window.Resources>

<mxe:SegmentedEditor
    Name="segmentedEditorCapitals"
    ItemsSource="{Binding Capitals}"
    ItemTemplate="{StaticResource CapitalItemTemplate}"
    ValueMember="Capital"
/>
```

``` csharp
using CommunityToolkit.Mvvm.ComponentModel;
using Avalonia.Media;
using Avalonia.Svg.Skia;
using Eremex.AvaloniaUI.Controls.Utils;

public partial class MainViewModel 
{
    [ObservableProperty]
    public ObservableCollection<CapitalInfo> capitals;

    public MainViewModel()
    {
        var capitalDictionary = new List<(string capital, string country)>();
        capitalDictionary.Add(("Havana", "Cuba"));
        capitalDictionary.Add(("Santiago", "Chile"));
        capitalDictionary.Add(("La Paz", "Bolivia"));
        Capitals = new ObservableCollection<CapitalInfo>();
        foreach (var item in capitalDictionary)
        {
            string country = item.country.ToLower();
            // Load .SVG images that are stored in the Images/Flags folder as Avalonia Resources.
            IImage image = ImageLoader.LoadSvgImage(Assembly.GetExecutingAssembly(), $"Images/Flags/{country}.svg");
            Capitals.Add(new CapitalInfo(item.capital, item.country, image));
        }
    }
}

public partial class CapitalInfo : ObservableObject
{
    public CapitalInfo(string capital, string country, IImage flag)
    {
        Capital = capital;
        Flag = flag;
        Country = country;
    }

    [ObservableProperty]
    public string capital;

    [ObservableProperty]
    public string country;

    [ObservableProperty]
    public IImage flag;
}
```

