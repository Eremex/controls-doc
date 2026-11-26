---
title: Galleries
order: 700
seealso: []
---

# Галереи

Галерея — это [элемент Ribbon](ribbon-items.md), который может отображать набор графически насыщенных элементов (например, форматированный текст с изображениями), отрисованных в соответствии с заданными шаблонами данных. Элементы галереи располагаются слева направо, затем вниз, образуя многоколоночный список. 

Следующее изображение демонстрирует встроенную в Ribbon галерею, отображающую 3 столбца элементов.

![ribbon-inplace-gallery](../../images/ribbon-inplace-gallery.png)

Встроенная в Ribbon галерея содержит две кнопки для вертикальной прокрутки. Под этими кнопками находится кнопка выпадающего списка, которая отображает всё содержимое галереи во всплывающем окне.

![ribbon-dropdown-gallery](../../images/ribbon-dropdown-gallery.png)


## Создание галереи Ribbon

Используйте элемент [`RibbonGalleryItem`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem.md), чтобы добавить галерею в интерфейс Ribbon. Вы можете добавить объект [`RibbonGalleryItem`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem.md) в [группу страниц](page-groups.md), во всплывающие меню, в [область заголовков страниц](page-header-items.md) или на [панель быстрого доступа](quick-access-toolbar.md) так же, как и другие [элементы Ribbon](ribbon-items.md). Например, чтобы добавить элементы Ribbon в группу страниц, определите их между открывающим и закрывающим тегами &lt;RibbonPageGroup&gt;. В code-behind вы можете добавлять элементы с помощью коллекции [`RibbonPageGroup.Items`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonPageGroup/Items.md).

Следующий фрагмент кода из демо _WordPad Example_ добавляет галерею в группу страниц _Styles_. Источник элементов галереи задаётся коллекцией _FontStyles_, определённой во View Model.

![ribbon-create-gallery-example](../../images/ribbon-create-gallery-example.png)

``` xml
<mxr:RibbonPageGroup Header="Styles" IsHeaderButtonVisible="True">
    <mxr:RibbonGalleryItem MaxColumnCount="3" ItemWidth="108" StretchItemVertically="True"
                           ItemHeight="80"
                           Header="Styles"
                           MaxDropDownColumnCount="3"
                           ItemsSource="{Binding FontStyles}">
</mxr:RibbonPageGroup>
```

## Элементы галереи

Используйте свойство [`RibbonGalleryItem.ItemsSource`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ItemsSource.md), чтобы предоставить коллекцию бизнес-объектов для отображения в виде элементов галереи. Чтобы отрисовать эти бизнес-объекты в галерее, определите соответствующие шаблоны данных. 

Чтобы определить шаблоны элементов галереи, вы также можете использовать свойство [`RibbonGalleryItem.ItemTemplate`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ItemTemplate.md).

### Пример - использование нескольких шаблонов для элементов галереи

В следующем коде из демо _WordPad Example_ элементы галереи заполняются из коллекции _FontStyles_, определённой во View Model. Элементы коллекции _FontStyles_ — это бизнес-объекты (_NormalGalleryItem_, _HeadingGalleryItem_ и _TitleGalleryItem_), для которых шаблоны данных определены в коллекции `UserControl.DataTemplates`.

![ribbon-gallery-itemssource-example](../../images/ribbon-gallery-itemssource-example.png)


``` xml
<mxr:RibbonGalleryItem 
  ItemsSource="{Binding FontStyles}"
  ...
  >
```

``` cs
public partial class WordPadExampleViewModel : PageViewModelBase
{
    [ObservableProperty] private ObservableCollection<FontStyleGalleryItem> fontStyles;
    //...
    fontStyles = new ObservableCollection<FontStyleGalleryItem>();
    fontStyles.Add(new NormalGalleryItem() { Header = "Normal" });
    fontStyles.Add(new HeadingGalleryItem() { Header = "Heading" });
    fontStyles.Add(new TitleGalleryItem() { Header = "Title" });
}
```

``` xml
<!-- Define data templates -->
<UserControl.DataTemplates>
    <DataTemplate DataType="vm:NormalGalleryItem">
        <Grid>
            <TextBlock Text="{Binding Header}"
                        FontSize="14"
                        HorizontalAlignment="Center"
                        VerticalAlignment="Center" />
        </Grid>
    </DataTemplate>
    <DataTemplate DataType="vm:HeadingGalleryItem">
        <Grid>
            <TextBlock Text="{Binding Header}"
                        FontSize="22"
                        Foreground="SteelBlue"
                        HorizontalAlignment="Center"
                        VerticalAlignment="Center" />
        </Grid>
    </DataTemplate>
    <DataTemplate DataType="vm:TitleGalleryItem">
        <Grid>
            <TextBlock Text="{Binding Header}"
                        FontSize="24"
                        HorizontalAlignment="Center"
                        VerticalAlignment="Center" />
        </Grid>
    </DataTemplate>
</UserControl.DataTemplates>
```

Полный код смотрите в демо _WordPad Example_.


### Пример - использование одного шаблона для всех элементов галереи

Пример ниже использует свойство [`RibbonGalleryItem.ItemTemplate`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ItemTemplate.md), чтобы определить шаблон данных для отрисовки всех элементов галереи. Этот шаблон рисует текстовый блок, текст и цвета которого задаются настройками объектов элементов галереи (объектов _CellStyle_), хранящихся в коллекции _CellStyles_ View Model.

Свойство [`RibbonGalleryItem.FocusedItem`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/FocusedItem.md) идентифицирует текущий [выбранный элемент галереи](#фокус-и-выбор-элементов-галереи). В примере свойство [`RibbonGalleryItem.FocusedItem`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/FocusedItem.md) привязано к свойству _SelectedCellStyle_ во View Model. Чтобы выполнять действия при выборе элемента галереи, обработчик события `PropertyChanged` View Model отслеживает изменения свойства _SelectedCellStyle_.

![ribbon-gallery-itemtemplate-example](../../images/ribbon-gallery-itemtemplate-example.png)

``` xml
<mxb:ToolbarManager IsWindowManager="True">
    <mxr:RibbonControl IsApplicationButtonVisible="False">
        <mxr:RibbonPage Header="Home">
            <mxr:RibbonPageGroup Header="Styles" IsHeaderButtonVisible="True">
                <mxr:RibbonGalleryItem MaxColumnCount="3"
                                        ItemWidth="108"
                                        ItemHeight="40"
                                        Header="Cell Styles"
                                        MaxDropDownColumnCount="4"
                                        ItemsSource="{Binding CellStyles}"
                                        FocusedItem="{Binding SelectedCellStyle, Mode=TwoWay}"
                                        >
                    <mxr:RibbonGalleryItem.ItemTemplate>
                        <DataTemplate>
                            <Border Background="{Binding BackColor}">
                                <TextBlock Text="{Binding Text}" 
                                  HorizontalAlignment="Center" 
                                  VerticalAlignment="Center"
                                  Foreground="{Binding TextColor}"/>
                            </Border>
                        </DataTemplate>
                    </mxr:RibbonGalleryItem.ItemTemplate>
                </mxr:RibbonGalleryItem>
            </mxr:RibbonPageGroup>
        </mxr:RibbonPage>
    </mxr:RibbonControl>
</mxb:ToolbarManager>
```

``` cs
public partial class MainWindowViewModel : ViewModelBase
{
    [ObservableProperty] private ObservableCollection<CellStyle> cellStyles;
    [ObservableProperty] private CellStyle selectedCellStyle;

    public MainWindowViewModel()
    {
        cellStyles = new ObservableCollection<CellStyle>
        {
            new CellStyle(){ Text="Normal", TextColor=Brushes.Black, BackColor=Brushes.White },
            new CellStyle(){ Text="Bad", TextColor=Brushes.Maroon, BackColor=Brushes.Pink },
            new CellStyle(){ Text="Good", TextColor=Brushes.Green, BackColor=Brushes.Honeydew },
            new CellStyle(){ Text="Neutral", TextColor=Brushes.Sienna, BackColor=Brushes.Khaki }
        };
        //Add accent colors
        Color[] accentColors = new Color[] { Colors.MediumOrchid, Colors.Chocolate, Colors.CadetBlue };
        for (int accentColorIndex=1; accentColorIndex<= accentColors.Length; accentColorIndex++)
        {
            Color accentColor = accentColors[accentColorIndex-1];
            string accentTitle = $"Accent {accentColorIndex}";
            cellStyles.Add(new CellStyle() { 
              Text = accentTitle, 
              TextColor=Brushes.White, 
              BackColor=new SolidColorBrush(accentColor) 
            });
            for (double opacity = 0.6; opacity > 0.1; opacity -= 0.2)
            {
                cellStyles.Add(new CellStyle() { 
                  Text = $"{opacity:p0} - " + accentTitle, 
                  TextColor=Brushes.Black, 
                  BackColor=new SolidColorBrush(accentColor, opacity)  
                });
            }
        };
        selectedCellStyle = cellStyles[0];
        PropertyChanged += PropertyChanged1;
    }

    // Perform actions when a gallery item is selected.
    private void PropertyChanged1(object? sender, System.ComponentModel.PropertyChangedEventArgs e)
    {
        if (e.PropertyName == nameof(SelectedCellStyle))
        {
            string selectedCellStyleName = SelectedCellStyle.Text;
            //...
        }
    }
}

public class CellStyle : ObservableObject
{
    public CellStyle() 
    {
        Text = "Default";
        TextColor = Brushes.Black;
        BackColor = Brushes.White;
    }
    public string Text { get; set; }
    public IBrush TextColor { get; set; }
    public IBrush BackColor { get; set; }
}
```

## Настройки отображения галереи

- [`RibbonGalleryItem.Header`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Header.md) — подпись галереи.  

  ``` xml
  <mxr:RibbonGalleryItem Header="Styles" ...>
  ```


  Подпись галереи отображается в следующих случаях:

  - В выпадающей галерее, когда включена опция [`IsDropDownHeaderVisible`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/IsDropDownHeaderVisible.md).

    ![ribbon-gallery-IsDropDownHeaderVisible](../../images/ribbon-gallery-IsDropDownHeaderVisible.png)
    

  - Когда объект [`RibbonGalleryItem`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem.md) отрисовывается как кнопка со связанной выпадающей галереей. Это происходит, когда объект [`RibbonGalleryItem`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem.md) встроен во всплывающее меню или когда используется [упрощённая компоновка команд](ribbon-command-layouts.md). Свойство [`RibbonGalleryItem.Header`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Header.md) задаёт подпись этой кнопки. 
  
    ![ribbon-gallery-in-popup-menu](../../images/ribbon-gallery-in-popup-menu.png)

    Подробнее смотрите в следующих разделах: [Галереи в упрощённой компоновке команд](#галереи-в-упрощённой-компоновке-команд) и [Галереи на панелях инструментов, во всплывающих и контекстных меню](#галереи-на-панелях-инструментов-во-всплывающих-и-контекстных-меню).

- [`RibbonGalleryItem.ItemHeight`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ItemHeight.md) — задаёт высоту элементов галереи. Это свойство имеет более высокий приоритет, чем настройка [`RibbonGalleryItem.StretchItemVertically`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/StretchItemVertically.md).

  Если свойство [`RibbonGalleryItem.ItemHeight`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ItemHeight.md) не задано, высота элемента галереи по умолчанию задаётся высотой первого элемента галереи. Эта высота берётся из соответствующего шаблона данных.

- [`RibbonGalleryItem.ItemWidth`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ItemWidth.md) — задаёт ширину элементов галереи.
- [`RibbonGalleryItem.MaxColumnCount`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/MaxColumnCount.md) — задаёт максимальное число столбцов во встроенной в Ribbon галерее.
- [`RibbonGalleryItem.MaxDropDownColumnCount`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/MaxDropDownColumnCount.md) — задаёт максимальное число столбцов в выпадающей галерее.
- [`RibbonGalleryItem.StretchItemVertically`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/StretchItemVertically.md) — задаёт, растягивать ли по вертикали первую строку элементов галереи, чтобы уместить её в высоту встроенной в Ribbon галереи. Эта автоматическая высота распространяется на другие строки, включая строки в выпадающей галерее.

  ![ribbon-gallery-StretchItemVertically](../../images/ribbon-gallery-StretchItemVertically.png)

  Свойство [`RibbonGalleryItem.StretchItemVertically`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/StretchItemVertically.md) не действует, если задано свойство [`RibbonGalleryItem.ItemHeight`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ItemHeight.md).

  Когда свойство [`RibbonGalleryItem.StretchItemVertically`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/StretchItemVertically.md) равно `false`, а свойство [`RibbonGalleryItem.ItemHeight`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ItemHeight.md) не используется, высота элемента галереи по умолчанию задаётся высотой первого элемента галереи. Эта высота берётся из соответствующего шаблона данных.

## Фокус и выбор элементов галереи

- [`RibbonGalleryItem.FocusedItem`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/FocusedItem.md) — позволяет получить бизнес-объект, соответствующий текущему сфокусированному элементу галереи. Сфокусированный элемент — это тот, который получает фокус. Вы можете определить сфокусированный элемент по рамке фокуса.

  ![ribbon-gallery-focuseditem](../../images/ribbon-gallery-focuseditem.png)
  

- [`RibbonGalleryItem.ItemSelectionMode`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ItemSelectionMode.md) — позволяет выбирать между режимами одиночного и множественного выбора элементов. Когда свойство [`ItemSelectionMode`](../../API/Eremex.AvaloniaUI.Controls.Editors/ItemSelectionMode.md) установлено в `Multiple`, пользователи могут выбирать несколько элементов галереи одновременно.
  
  В режиме одиночного выбора используйте свойство [`RibbonGalleryItem.FocusedItem`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/FocusedItem.md), чтобы получить/задать сфокусированный (выбранный) элемент.
  
  В режиме множественного выбора используйте свойство [`RibbonGalleryItem.SelectedItems`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/SelectedItems.md), чтобы получить/задать текущие выбранные элементы. 

  Когда вы щёлкаете по элементу в режиме множественного выбора, этот элемент автоматически фокусируется и выбирается. 
  Выбранные элементы имеют подсвеченный фон. Рамка вокруг элемента галереи указывает, что он сфокусирован.

  ![ribbon-gallery-multiple-selection](../../images/ribbon-gallery-multiple-selection.png)
  
  Чтобы выбрать несколько элементов, щёлкайте по элементам, удерживая клавишу CTRL и/или SHIFT. 
  
  Действие CTRL+щелчок переключает состояние выбора сфокусированного элемента. Это позволяет пользователю снять выбор со сфокусированного элемента.

  ![ribbon-gallery-multiple-selection-unselected](../../images/ribbon-gallery-multiple-selection-unselected.png)

- [`RibbonGalleryItem.SelectedItems`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/SelectedItems.md) — коллекция бизнес-объектов, соответствующих выбранным элементам галереи. Установите свойство [`RibbonGalleryItem.ItemSelectionMode`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ItemSelectionMode.md) в `Multiple`, чтобы разрешить множественный выбор элементов.

  
  В режиме одиночного выбора свойство [`RibbonGalleryItem.SelectedItems`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/SelectedItems.md) содержит один элемент. Он совпадает со свойством [`RibbonGalleryItem.FocusedItem`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/FocusedItem.md).

  




## Показ и закрытие выпадающей галереи

- [`RibbonGalleryItem.IsPopupOpen`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/IsPopupOpen.md) — возвращает или задаёт, открыта ли выпадающая галерея.
- [`RibbonGalleryItem.ClosePopup`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/ClosePopup.md) — закрывает выпадающую галерею.

## Дополнительные команды в выпадающей галерее

Выпадающая галерея может отображать дополнительные элементы Ribbon (команды) внизу. 

![ribbon-RibbonGalleryItem-dropdown](../../images/ribbon-RibbonGalleryItem-dropdown.png)

Используйте свойство [`RibbonGalleryItem.DropDownItems`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonGalleryItem/DropDownItems.md), чтобы задать эти дополнительные элементы.

``` xml
<mxr:RibbonPageGroup Header="Styles" IsHeaderButtonVisible="True">
    <mxr:RibbonGalleryItem MaxColumnCount="3" ItemWidth="108" StretchItemVertically="True"
                           ItemHeight="80"
                           Header="Styles"
                           MaxDropDownColumnCount="3"
                           ItemsSource="{Binding FontStyles}">
        <mxr:RibbonGalleryItem.DropDownItems>
            <mxb:ToolbarButtonItem Header="Create A Style..." Glyph="{x:Static icons:Basic.Add}" />
            <mxb:ToolbarButtonItem Header="Clear Formatting"
                                   Glyph="{x:Static icons:Filter.Does_not_contain}" />
            <mxb:ToolbarButtonItem Header="Apply Styles" Glyph="{x:Static icons:Filter.Starts_with}" />
        </mxr:RibbonGalleryItem.DropDownItems>
    </mxr:RibbonGalleryItem>
</mxr:RibbonPageGroup>
```

## Галереи в упрощённой компоновке команд

В [упрощённой компоновке команд](ribbon-command-layouts.md) галерея, добавленная в группу страниц, отрисовывается как кнопка. Щелчок по этой кнопке вызывает всю галерею.

![ribbon-gallery-simplified-layout](../../images/ribbon-gallery-simplified-layout.png)

Текст кнопки задаётся свойством [`RibbonGalleryItem.Header`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Header.md).

## Галереи на панелях инструментов, во всплывающих и контекстных меню

Когда вы добавляете галерею на традиционную панель инструментов или во всплывающее меню, галерея отображается как подменю.

![ribbon-gallery-in-popup-menu](../../images/ribbon-gallery-in-popup-menu.png)

Подпись подменю задаётся свойством [`RibbonGalleryItem.Header`](../../API/Eremex.AvaloniaUI.Controls.Bars/ToolbarItem/Header.md).


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
