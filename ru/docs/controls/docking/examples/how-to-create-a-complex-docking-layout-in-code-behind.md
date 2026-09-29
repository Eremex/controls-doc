---
title: Как создать сложный макет для докинга в коде
seealso: []
---

# Как создать сложный макет для докинга в коде

Этот пример показывает, как создать закреплённые, плавающие и автоскрытые панели в code-behind и расположить их, как показано на изображении ниже:

![dock-operations-in-code-complex-layout-example](../../../images/dock-operations-in-code-complex-layout-example.png)


Предполагается, что для изображений, используемых в этом примере, свойство `Build Action` установлено в `AvaloniaResource`.

``` cs
using Eremex.AvaloniaUI.Controls.Common;
using Eremex.AvaloniaUI.Controls.Docking;
using Eremex.AvaloniaUI.Controls.Utils;

public partial class MainWindow : MxWindow
{
    public MainWindow()
    {
        InitializeComponent();

        DockManager dockManager1 = new DockManager();
        this.Content = dockManager1;

        // Инициализировать корневую группу DockManager.
        dockManager1.Root = new DockGroup();

        // Создать dock-панели
        DockPane paneProperties = new DockPane() 
        { 
            Header = "Properties", 
            Glyph=ImageLoader.LoadSvgImage(Assembly.GetExecutingAssembly(), "Images/settings.svg"), 
            GlyphSize=new Avalonia.Size(16,16) 
        };
        DockPane paneDebug = new DockPane() 
        { 
            Header = "Debug",
            Glyph = ImageLoader.LoadSvgImage(Assembly.GetExecutingAssembly(), "Images/debug2.svg"),
            GlyphSize = new Avalonia.Size(16, 16)
        };
        DockPane paneOutput = new DockPane() { Header = "Output"};
        DockPane paneTerminal = new DockPane() 
        { 
            Header = "Terminal", 
            DockHeight = new GridLength(100, GridUnitType.Pixel) 
        };
        // Создать группу вкладок для документов
        DocumentGroup documentGroup = new DocumentGroup();

        // Добавить панели в dock manager
        dockManager1.Root.Add(paneProperties);
        // Закрепить группу вкладок документов слева от панели 'Properties'.
        dockManager1.Dock(documentGroup, paneProperties, DockType.Left);
        // Закрепить панель 'Debug' снизу от панели 'Properties'.
        dockManager1.Dock(paneDebug, paneProperties, DockType.Bottom);
        // Создать группу вкладок из панелей 'Debug' и 'Output'
        dockManager1.Dock(paneOutput, paneDebug, DockType.Fill);

        // Добавить документы в группу вкладок
        DocumentPane document1 = new DocumentPane() { Header = "MainWindow.xaml" };
        DocumentPane document2 = new DocumentPane() { Header = "App.xaml", Content = new TextBlock() { Text = "Lorem ipsum" } };
        dockManager1.Dock(document1, documentGroup, DockType.Fill);
        dockManager1.Dock(document2, documentGroup, DockType.Fill);
        // Отобразить панель 'Terminal' снизу от корневой группы.
        dockManager1.Dock(paneTerminal, dockManager1.Root, DockType.Bottom);

        // Задать относительный размер для панели 'Properties' и группы вкладок (paneDebug.DockParent)
        paneProperties.DockHeight = new GridLength(4, GridUnitType.Star);
        paneDebug.DockParent.DockHeight = new GridLength(3, GridUnitType.Star);

        // Задать абсолютный размер для панели
        paneProperties.DockParent.DockWidth = new GridLength(250, GridUnitType.Pixel);

        // Создать автоскрытую панель
        DockPane paneToolbox = new DockPane() { Header = "Toolbox" };
        AutoHideGroup autoHideGroup = new AutoHideGroup() { Dock = Dock.Left };
        dockManager1.AutoHideGroups.Add(autoHideGroup);
        autoHideGroup.Add(paneToolbox);
        AutoHideGroup.SetAutoHideWidth(paneToolbox, 150);

        // Создать плавающую панель
        DockPane paneErrors = new DockPane() { Header = "Errors" };
        dockManager1.Float(paneErrors);
        paneErrors.FloatGroup.FloatLocation = new PixelPoint(200, 200);
        paneErrors.FloatGroup.FloatWidth = 200;
        paneErrors.FloatGroup.FloatHeight = 100;
    }
}
```


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
