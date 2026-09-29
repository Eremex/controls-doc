---
title: Use MVVM Pattern to Populate Dock Items
order: 55000
seealso: []
---

# Use MVVM Pattern to Populate Dock Items

The `DockManager` control allows you to use the MVVM design pattern to populate the control with dock items (for instance, with `DocumentPane` and `DockPane` objects). With this technique, you assign a collection of dock items to the `DockManager` component, and specify a template used to render dock items.

## Populate the DockManager with Items from an Item Source

Use the `DockManager.ItemsSource` property to bind a `DockManager` to a collection of objects that need to be rendered as dock items. The way these objects are converted to dock items is specified by the `DockManager.ItemTemplate` property.

To specify a template to render the content of dock items created from the `DockManager.ItemsSource` collection, use the `DockManager.ItemContentTemplate` property.

The following example from the _IDE Layout_ demo uses the `DockManager.ItemsSource` property to bind the control to the _Documents_ collection defined in the main View Model. Elements of this collection (_IdeLayoutDocumentViewModel_ objects) are rendered as `DocumentPane` objects.

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
        <!-- Created DocumentPane objects are placed in the first DocumentGroup container. -->
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

See the complete code of this example in the _IDE Layout_ module of the Demo application.

!!! note
 
    When `DocumentPane` objects are created from the `DockManager.ItemsSource` collection, they are automatically rendered as tabs in the first `DocumentGroup` container. Ensure that a `DockManager` has at least one `DocumentGroup` container. You can implement an **item adapter** (`DockManager.ItemAdapter`)  to position created dock items (for example, `DocumentPane` objects) to a specific dock container. See the following section for more details.


## Create Various Dock Item Types from an Item Source

You may want to bind the `DockManager.ItemsSource` property to a collection of objects that should be rendered as dock panes, document panes, auto-hide panels, and/or float panes. To accomplish this task, use the following approach:

1. Implement a **template selector** that creates specific dock items from objects in the `DockManager.ItemsSource` collection.
2. Add dock containers to the `DockManager` component that should host created dock items.
3. Create an **item adapter** that places created dock items in specific dock containers. 

### Example

1. Define the _Panes_ collection in the main View Model. This collection will contain the following elements:

- _DockPaneViewModel_ objects - These objects need to be rendered as [dock panes](dock-panes-and-containers.md) (`DockPane`).
- _DocumentPaneViewModel_ objects - These objects need to be rendered as [document panes](document-panes.md) (`DocumentPane`).

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

2. Initializes the _Panes_ collection with sample objects.

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

3. Define a `DockManager` component in the main window. Bind it to the _MainViewModel.Panes_ collection and create two dock containers:

- _paneHost_ — The `DockGroup` container that should display dock panes created from _DockPaneViewModel_ objects.
- _documentHost_ – The `DocumentGroup` container that should display document panes created from _DocumentPaneViewModel_ objects.

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

4. Implement a **template selector** that creates `DockPane` objects from _DockPaneViewModel_ elements, and `DocumentPane` objects from _DocumentPaneViewModel_ elements. Assign this template selector to the `DockManager.ItemTemplate` property.

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

5. Create an **item adapter** that places created `DockPane` and `DocumentPane` objects to corresponding dock containers. 

An item adapter is a class that implements the `IDockManagerItemAdapter` interface. The `IDockManagerItemAdapter.Adapt` method is called for each dock item created from the `DockManager.ItemsSource` collection. This method should position a dock item within a specific dock container.

Use the `DockManager.ItemAdapter` property to specify the item adapter.

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

6. Run the application to see the `DockManager` component populated with dock items from the _Panes_ collection.

![dockmanager-mvvm-itemadapter-example](../../images/dockmanager-mvvm-itemadapter-example.png)
