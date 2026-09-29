---
title: SegmentedEditor
order: 104000
seealso: []
---

# SegmentedEditor

`SegmentedEditor` представляет набор элементов (вариантов) в виде горизонтально расположенных сегментов. Пользователь может щёлкнуть по одному из сегментов, чтобы выбрать соответствующий вариант, или CTRL+щёлкнуть по выбранному сегменту, чтобы очистить выбор.

![segmentededitor](../../images/segmentededitor.png)

Основные возможности контрола включают:

- Заполнение сегментов из списка строк, списка бизнес-объектов или типа перечисления.
- Шаблоны элементов позволяют отрисовывать сегменты произвольным образом.
- Использование контрола как встроенного редактора в контейнерных контролах (например, TreeList, TreeView и PropertyGrid).

## Источник объектов

Используйте свойство `SegmentedEditor.ItemsSource`, чтобы задать источник элементов, используемый для создания сегментов контрола. Вы можете привязать редактор к списку строк, списку бизнес-объектов или типу перечисления.

## Привязка к списку строк

Простейший источник элементов — список строк.

### Пример - как привязать к списку строк
Следующий пример заполняет контрол `SegmentedEditor` списком строк.

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

## Привязка к списку бизнес-объектов

Вы можете привязать контрол `SegmentedEditor` к списку бизнес-объектов. В этом случае поведение контрола по умолчанию следующее:

- Метод `ToString` бизнес-объекта задаёт текстовое представление элементов по умолчанию.
- Когда вы выбираете элемент, значение редактора (`SegmentedEditor.EditorValue`) устанавливается в соответствующий бизнес-объект.

Типичный бизнес-объект имеет несколько свойств. Вы можете задать, какие свойства бизнес-объекта предоставляют отображаемый текст элемента и значения редактирования. Используйте для этого следующие члены API:

- `SegmentedEditor.DisplayMember` — возвращает или задаёт имя свойства бизнес-объекта, задающего отображаемый текст элемента. 
- `SegmentedEditor.ValueMember` — возвращает или задаёт имя свойства бизнес-объекта, задающего значения элементов. Когда вы выбираете элемент, значение редактора (`SegmentedEditor.EditorValue`) устанавливается в значение свойства `ValueMember` элемента. 

### Пример - как привязать к списку бизнес-объектов

Следующий пример привязывает контрол SegmentedEditor к списку бизнес-объектов _Product_. Свойство _Product.ProductName_ задаёт отображаемый текст элемента. Свойство _Product.ProductID_ задаёт значения элементов.

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

## Привязка к перечислению

`SegmentedEditor` может заполнять свои сегменты значениями типа перечисления. 

Вспомогательный класс `Eremex.AvaloniaUI.Controls.Common.EnumItemsSource` облегчает привязку к перечислению. Его основные возможности:

- Изображения для членов перечисления. Примените атрибут `Eremex.AvaloniaUI.Controls.Common.ImageAttribute` к целевым членам перечисления, чтобы задать изображения.
- Пользовательские отображаемые имена для членов перечисления. Используйте атрибут `System.ComponentModel.DataAnnotations.DisplayAttribute` или пользовательский конвертер, чтобы изменить отображаемый текст элемента по умолчанию.
- Всплывающие подсказки для элементов. Всплывающая подсказка содержит описание целевого элемента, которое вы можете предоставить с помощью атрибута `System.ComponentModel.DataAnnotations.DisplayAttribute` или пользовательского конвертера.

Используйте следующие свойства `EnumItemsSource`, чтобы настроить привязку к типу перечисления:

- `EnumItemsSource.EnumType` — задаёт тип перечисления, значения которого отображаются в контроле `SegmentedEditor`.
- `EnumItemsSource.ShowImages` — задаёт, отображать ли изображения для членов перечисления. Вы можете предоставить изображения с помощью атрибута `Eremex.AvaloniaUI.Controls.Common.ImageAttribute`.
- `EnumItemsSource.ShowNames` — задаёт, отображать ли текст элемента. Установите `ShowNames` в `false`, а `ShowImages` в `true`, чтобы отрисовывать члены перечисления с помощью изображений без текста.
- `EnumItemsSource.ImageSize` — задаёт размер отображения изображений, назначенных членам перечисления.
- `EnumItemsSource.NameToDisplayTextConverter` — позволяет назначить конвертер, который получает пользовательский отображаемый текст для членов перечисления.
- `EnumItemsSource.NameToDescriptionConverter` — позволяет назначить конвертер, который получает описания членов перечисления, отображаемые как всплывающие подсказки при наведении курсора на сегменты.

### Пример - как отобразить значения перечисления и использовать атрибуты для предоставления отображаемого текста и изображений для членов перечисления.

Следующий пример отображает значения перечисления _ProductCategoryEnum_ в `SegmentedEditor`. Он использует класс `EnumItemsSource` для привязки данных.

Атрибуты `System.ComponentModel.DataAnnotations.DisplayAttribute` и `Eremex.AvaloniaUI.Controls.Common.ImageAttribute` задают пользовательский отображаемый текст, описания (всплывающие подсказки) и изображения для членов перечисления.

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

### Пример - как отобразить значения перечисления и использовать пользовательские конвертеры для предоставления отображаемого текста для членов перечисления.

Следующий пример использует класс `EnumItemsSource`, чтобы отобразить значения типа перечисления в контроле `SegmentedEditor`. Объекты `EnumItemsSource.NameToDisplayTextConverter` и `EnumItemsSource.NameToDescriptionConverter` предоставляют пользовательский отображаемый текст и описания (всплывающие подсказки) для членов перечисления.

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

## Получение и установка выбранного элемента и задание значения редактора

Когда пользователь выбирает сегмент или снимает с него выбор с помощью Ctrl+щелчка, свойства `SegmentedEditor.SelectedItem` и `SegmentedEditor.EditorValue` изменяются соответственно.
Вы можете использовать любое из этих свойств, чтобы получить и задать выбранное значение редактора.

Свойство `SegmentedEditor.SelectedItem` задаёт базовый объект данных выбранного сегмента.

Свойство `SegmentedEditor.EditorValue` имеет следующие значения:

- Если свойство `ValueMember` пусто, свойства `EditorValue` и `SelectedItem` эквивалентны.
- В противном случае свойство `EditorValue` синхронизировано со значением свойства `ValueMember` выбранного базового объекта данных.

Чтобы очистить выбор, установите свойство `SegmentedEditor.SelectedItem` в `null`.
 
### Пример - как выбрать элемент, когда SegmentedEditor привязан к списку строк

Следующий пример показывает, как использовать свойство `SelectedItem` или `EditorValue`, чтобы выбрать элемент в контроле `SegmentedEditor`, привязанном к списку строк.

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

### Пример - как выбрать элемент, когда SegmentedEditor привязан к списку бизнес-объектов

В следующем примере контрол `SegmentedEditor` привязан к списку объектов _Product_. Свойство `ValueMember` ссылается на член _Product.ProductID_. Таким образом, идентификаторы продуктов служат значениями элементов. Когда пользователь выбирает сегмент, свойство `EditorValue` устанавливается в соответствующий идентификатор продукта. Пример использует свойство `EditorValue`, чтобы выбрать элемент в коде.

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

## Шаблоны элементов

Когда `SegmentedEditor` привязан к списку строк или бизнес-объектов, сегменты контрола отображают текстовое представление элементов по умолчанию. Отображаемый текст элемента по умолчанию определяется следующим образом:

- Значение, возвращаемое методом `ToString` базового объекта данных, если свойство `ValueMember` не задано.
- В противном случае текстовое представление значения, хранящегося в свойстве `ValueMember` объекта данных.

Шаблоны элементов дают вам гибкость в задании того, что отображать в сегментах редактора. Они позволяют отображать изображения и значения нескольких свойств в сегментах. Используйте свойство `SegmentedEditor.ItemTemplate`, чтобы задать шаблон элемента.

### Пример - как отобразить изображение и текст для элементов SegmentedEditor

Следующий пример показывает, как создать шаблон элемента, отображающий изображения и текст в сегментах контрола `SegmentedEditor`.

В примере контрол `SegmentedEditor` привязан к коллекции объектов _CapitalInfo_, которые хранят информацию о странах, их столицах и национальных флагах. 
Созданный шаблон элемента (свойство `SegmentedEditor.ItemTemplate`) отображает флаг страны, за которым следует название столицы страны.

Свойство `SegmentedEditor.ValueMember` ссылается на свойство _CapitalInfo.Capital_. Когда пользователь выбирает сегмент, свойство редактора `EditorValue` устанавливается в название столицы соответствующей страны.

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


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
