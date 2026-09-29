---
title: Использование паттерна MVVM для заполнения элементами закрепления
order: 55000
seealso: []
---

# Использование паттерна MVVM для заполнения элементами закрепления

Контрол `DockManager` позволяет использовать паттерн проектирования MVVM, чтобы заполнять контрол элементами докинга (например, объектами `DocumentPane` и `DockPane`). При таком подходе вы назначаете коллекцию элементов докинга компоненту `DockManager` и задаёте шаблон, используемый для их отрисовки.

## Заполнение DockManager элементами из источника элементов

Используйте свойство `DockManager.ItemsSource`, чтобы привязать `DockManager` к коллекции объектов, которые нужно отрисовать как элементы докинга. Способ преобразования этих объектов в элементы докинга задаётся свойством `DockManager.ItemTemplate`.

Чтобы задать шаблон для отрисовки содержимого элементов докинга, созданных из коллекции `DockManager.ItemsSource`, используйте свойство `DockManager.ItemContentTemplate`.

Следующий пример из демонстрационного примера _IDE Layout_ использует свойство `DockManager.ItemsSource`, чтобы привязать контрол к коллекции _Documents_, определённой в главной модели представления. Элементы этой коллекции (объекты _IdeLayoutDocumentViewModel_) отрисовываются как объекты `DocumentPane`.

``` xml
<mxd:DockManager Grid.Column="0" Grid.Row="1"
                 BorderThickness="0" 
                 ItemsSource="{Binding Documents}"
                 ItemContentTemplate="{views:IdeLayoutDocumentContentTemplate}">
    <mxd:DockManager.ItemTemplate>
        <DataTemplate DataType="vm:IdeLayoutDocumentViewModel">
            <mxd:DocumentPane Header="{Binding Header}"
                IsActive="{Binding IsActive}"
                CloseCommand="{Binding CloseCommand}"/>
        </DataTemplate>
    </mxd:DockManager.ItemTemplate>
    <mxd:DockGroup>
        <!-- ... -->
        <!-- Созданные объекты DocumentPane размещаются в первом контейнере DocumentGroup. -->
        <mxd:DocumentGroup DockWidth="5*">
        </mxd:DocumentGroup>
    </mxd:DockGroup>
</mxd:DockManager>
```

``` cs
public partial class IdeLayoutPageViewModel : PageViewModelBase
{
    public ObservableCollection<IdeLayoutDocumentViewModel> Documents { get; };
    //...
}

public partial class IdeLayoutDocumentViewModel : ObservableObject
{
    [ObservableProperty] private string header;
    [ObservableProperty] private string uri;
    [ObservableProperty] private bool isActive;
    [ObservableProperty] private ICommand closeCommand;
}

public class IdeLayoutDocumentContentTemplate : MarkupExtension, IDataTemplate
{
    //...
}
```

Полный код этого примера смотрите в модуле _IDE Layout_ демонстрационного приложения.

!!! note
 
    Когда объекты `DocumentPane` создаются из коллекции `DockManager.ItemsSource`, они автоматически отображаются как вкладки в первом контейнере `DocumentGroup`. Убедитесь, что `DockManager` содержит как минимум один контейнер `DocumentGroup`. Вы можете реализовать **адаптер элементов** (`DockManager.ItemAdapter`), чтобы размещать созданные элементы докинга (например, объекты `DocumentPane`) в конкретном контейнере докинга. Подробнее смотрите в следующем разделе.


## Создание элементов докинга разных типов из источника элементов

Вам может понадобиться привязать свойство `DockManager.ItemsSource` к коллекции объектов, которые должны отрисовываться как dock-панели, document-панели, автоскрытые панели и/или плавающие панели. Чтобы решить эту задачу, используйте следующий подход:

1. Реализуйте **селектор шаблонов**, который создаёт конкретные элементы докинга из объектов коллекции `DockManager.ItemsSource`.
2. Добавьте в компонент `DockManager` контейнеры докинга, которые должны размещать созданные элементы докинга.
3. Создайте **адаптер элементов**, который размещает созданные элементы докинга в конкретных контейнерах докинга. 

### Пример

1. Определите коллекцию _Panes_ в главной модели представления. Эта коллекция будет содержать следующие элементы:

- Объекты _DockPaneViewModel_ — эти объекты нужно отрисовать как [dock-панели](dock-panes-and-containers.md) (`DockPane`).
- Объекты _DocumentPaneViewModel_ — эти объекты нужно отрисовать как [document-панели](document-panes.md) (`DocumentPane`).

``` cs
namespace EremexAvaloniaApplication1;

public class MainViewModel : ObservableObject
{
    public ObservableCollection<PaneViewModelBase> Panes { get; } = new();
}

public partial class PaneViewModelBase : ObservableObject
{
    [ObservableProperty] private string? header;
}

public class DockPaneViewModel : PaneViewModelBase { }
public class DocumentPaneViewModel : PaneViewModelBase { }
```

2. Инициализирует коллекцию _Panes_ образцовыми объектами.

``` cs
namespace EremexAvaloniaApplication1;

public partial class MainWindow : MxWindow
{
    public MainWindow()
    {
        var viewModel = new MainViewModel();
        viewModel.Panes.AddRange(new PaneViewModelBase[]
        {
            new DockPaneViewModel() { Header = "Pane1" },
            new DockPaneViewModel() { Header = "Pane2" },
            new DockPaneViewModel() { Header = "Pane3" },
            new DocumentPaneViewModel() { Header = "Doc1" },
            new DocumentPaneViewModel() { Header = "Doc2" }
        });
        DataContext = viewModel;
        
        InitializeComponent();
    }
}
```

3. Определите компонент `DockManager` в главном окне. Привяжите его к коллекции _MainViewModel.Panes_ и создайте два контейнера докинга:

- _paneHost_ — контейнер `DockGroup`, который должен отображать dock-панели, созданные из объектов _DockPaneViewModel_.
- _documentHost_ — контейнер `DocumentGroup`, который должен отображать document-панели, созданные из объектов _DocumentPaneViewModel_.

``` xml
<mx:MxWindow xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
             xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
             xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
             xmlns:mxd="https://schemas.eremexcontrols.net/avalonia/docking"
             xmlns:local="clr-namespace:EremexAvaloniaApplication1"
             mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
             x:Class="EremexAvaloniaApplication1.MainWindow"
             Icon="/Assets/EMXControls.ico"
             Title="EremexAvaloniaApplication1"
             x:DataType="local:MainViewModel">
    <mxd:DockManager ItemsSource="{Binding Panes}">
        <mxd:DockGroup>
            <mxd:DockGroup x:Name="paneHost" Orientation="Vertical"></mxd:DockGroup>
            <mxd:DocumentGroup x:Name="documentHost"></mxd:DocumentGroup>
        </mxd:DockGroup>
    </mxd:DockManager>
</mx:MxWindow>
```

4. Реализуйте **селектор шаблонов**, который создаёт объекты `DockPane` из элементов _DockPaneViewModel_ и объекты `DocumentPane` из элементов _DocumentPaneViewModel_. Назначьте этот селектор шаблонов свойству `DockManager.ItemTemplate`.

``` cs
namespace EremexAvaloniaApplication1;

public class PaneTemplateSelector : MarkupExtension, IDataTemplate
{
    public IDataTemplate? DocumentTemplate { get; set; }
    public IDataTemplate? DockPaneTemplate { get; set; }
    public Control? Build(object? param)
    {
        if (param is DocumentPaneViewModel) return DocumentTemplate?.Build(param);
        return DockPaneTemplate?.Build(param);
    }

    public bool Match(object? data)
    {
        return data is PaneViewModelBase;
    }

    public override object ProvideValue(IServiceProvider serviceProvider) => this;
}
```

``` xml
<mxd:DockManager ItemsSource="{Binding Panes}">
    <mxd:DockManager.ItemTemplate>
        <local:PaneTemplateSelector>
            <local:PaneTemplateSelector.DocumentTemplate>
                <DataTemplate DataType="local:DocumentPaneViewModel">
                    <mxd:DocumentPane Header="{Binding Header}" />
                </DataTemplate>
            </local:PaneTemplateSelector.DocumentTemplate>
            <local:PaneTemplateSelector.DockPaneTemplate>
                <DataTemplate DataType="local:DockPaneViewModel">
                    <mxd:DockPane Header="{Binding Header}" />
                </DataTemplate>
            </local:PaneTemplateSelector.DockPaneTemplate>
        </local:PaneTemplateSelector>
    </mxd:DockManager.ItemTemplate>
    <mxd:DockGroup>
        <mxd:DockGroup x:Name="paneHost" Orientation="Vertical"></mxd:DockGroup>
        <mxd:DocumentGroup x:Name="documentHost"></mxd:DocumentGroup>
    </mxd:DockGroup>
</mxd:DockManager>
```

5. Создайте **адаптер элементов**, который размещает созданные объекты `DockPane` и `DocumentPane` в соответствующих контейнерах докинга. 

Адаптер элементов — это класс, реализующий интерфейс `IDockManagerItemAdapter`. Метод `IDockManagerItemAdapter.Adapt` вызывается для каждого элемента докинга, созданного из коллекции `DockManager.ItemsSource`. Этот метод должен размещать элемент докинга в конкретном контейнере докинга.

Используйте свойство `DockManager.ItemAdapter`, чтобы задать адаптер элементов.

``` cs
namespace EremexAvaloniaApplication1;

public class PaneAdapter : MarkupExtension, IDockManagerItemAdapter
{
    public void Adapt(DockManager dockManager, DockItemBase dockItem, object item)
    {
        var target = dockManager.FindItem<DockGroup>(dockItem is DocumentPane ? "documentHost" : "paneHost"); 
        target?.Add(dockItem);
    }

    public override object ProvideValue(IServiceProvider serviceProvider)
    {
        return this;
    }
}
```

``` xml
<mxd:DockManager ItemsSource="{Binding Panes}" ItemAdapter="{local:PaneAdapter}">
<!-- ... -->
```

6. Запустите приложение, чтобы увидеть компонент `DockManager`, заполненный элементами докинга из коллекции _Panes_.

![dockmanager-mvvm-itemadapter-example](../../images/dockmanager-mvvm-itemadapter-example.png)


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
