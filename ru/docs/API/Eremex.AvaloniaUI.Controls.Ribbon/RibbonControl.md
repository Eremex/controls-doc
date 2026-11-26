# Класс RibbonControl

Отображает команды, упорядоченные по страницам и группам, с Application Button и панелью быстрого доступа.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.Ribbon`](./index.md)  
**Сборка:** `Eremex.Avalonia.Controls.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Объявление

```csharp
public class RibbonControl : TemplatedControl, IMxMainMenu, INavigatable
```

## Конструкторы

| имя | описание |
| --- | --- |
| [RibbonControl](RibbonControl/RibbonControl.md)() | Инициализирует новый экземпляр класса RibbonControl. |

## Свойства

| имя | описание |
| --- | --- |
| [AllowQuickAccessToolbarCustomizationMenu](RibbonControl/AllowQuickAccessToolbarCustomizationMenu.md) { get; set; } | Возвращает или задаёт, могут ли пользователи открывать меню настройки панели быстрого доступа. |
| [ApplicationButtonCommand](RibbonControl/ApplicationButtonCommand.md) { get; set; } | Возвращает или задаёт команду, выполняемую при активации Application Button. |
| [ApplicationButtonCommandParameter](RibbonControl/ApplicationButtonCommandParameter.md) { get; set; } | Возвращает или задаёт параметр, передаваемый команде Application Button. |
| [ApplicationButtonContent](RibbonControl/ApplicationButtonContent.md) { get; set; } | Возвращает или задаёт содержимое, отображаемое на Application Button. |
| [ApplicationButtonContentTemplate](RibbonControl/ApplicationButtonContentTemplate.md) { get; set; } | Возвращает или задаёт шаблон, используемый для отображения содержимого Application Button. |
| [ApplicationButtonDropDownControl](RibbonControl/ApplicationButtonDropDownControl.md) { get; set; } | Возвращает или задаёт всплывающее окно, отображаемое Application Button. |
| [ApplicationButtonGlyph](RibbonControl/ApplicationButtonGlyph.md) { get; set; } | Возвращает или задаёт изображение, отображаемое на Application Button. |
| [ApplicationButtonKeyTip](RibbonControl/ApplicationButtonKeyTip.md) { get; set; } | Возвращает или задаёт Key Tip, используемую для активации Application Button. |
| [CommandLayout](RibbonControl/CommandLayout.md) { get; set; } | Возвращает или задаёт макет команд, используемый Ribbon. |
| [GlyphSizeInSimplifiedLayout](RibbonControl/GlyphSizeInSimplifiedLayout.md) { get; set; } | Возвращает или задаёт размер глифов, используемый в упрощённом макете Ribbon. |
| [IsApplicationButtonVisible](RibbonControl/IsApplicationButtonVisible.md) { get; set; } | Возвращает или задаёт, видна ли Application Button. |
| [IsCommandLayoutSelectionButtonVisible](RibbonControl/IsCommandLayoutSelectionButtonVisible.md) { get; set; } | Возвращает или задаёт, видна ли кнопка переключения макета команд Ribbon. |
| [IsQuickAccessToolbarCustomizationButtonVisible](RibbonControl/IsQuickAccessToolbarCustomizationButtonVisible.md) { get; set; } | Возвращает или задаёт, видна ли кнопка настройки панели быстрого доступа. |
| [IsQuickAccessToolbarVisible](RibbonControl/IsQuickAccessToolbarVisible.md) { get; set; } | Возвращает или задаёт, видна ли панель быстрого доступа. |
| [Manager](RibbonControl/Manager.md) { get; set; } | Возвращает или задаёт менеджер панелей инструментов, связанный с этим объектом. |
| [PageHeaderItems](RibbonControl/PageHeaderItems.md) { get; } | Возвращает коллекцию элементов, отображаемых рядом с заголовками страниц Ribbon. |
| [PageHeaderItemsSource](RibbonControl/PageHeaderItemsSource.md) { get; set; } | Возвращает или задаёт коллекцию, элементы которой используются для создания элементов рядом с заголовками страниц Ribbon. |
| [Pages](RibbonControl/Pages.md) { get; } | Возвращает коллекцию страниц Ribbon. |
| [PagesSource](RibbonControl/PagesSource.md) { get; set; } | Возвращает или задаёт коллекцию, элементы которой используются для создания страниц Ribbon. |
| [QuickAccessToolbarItems](RibbonControl/QuickAccessToolbarItems.md) { get; } | Возвращает коллекцию элементов, отображаемых на панели быстрого доступа. |
| [QuickAccessToolbarItemsSource](RibbonControl/QuickAccessToolbarItemsSource.md) { get; set; } | Возвращает или задаёт коллекцию, элементы которой используются для создания элементов панели быстрого доступа. |
| [QuickAccessToolbarLocation](RibbonControl/QuickAccessToolbarLocation.md) { get; set; } | Возвращает или задаёт расположение панели быстрого доступа относительно Ribbon. |
| [SelectedPage](RibbonControl/SelectedPage.md) { get; set; } | Возвращает или задаёт выбранную в данный момент страницу Ribbon. |
| [SerializationInfo](RibbonControl/SerializationInfo.md) { get; } | Возвращает сведения о размещении, используемые при сериализации или десериализации. |
| [SmallGlyphSize](RibbonControl/SmallGlyphSize.md) { get; set; } | Возвращает или задаёт размер, используемый для отображения малых глифов Ribbon. |

## Методы

| имя | описание |
| --- | --- |
| [ResetNavigation](RibbonControl/ResetNavigation.md)() | Сбрасывает навигацию с клавиатуры внутри Ribbon. |
| [RestoreLayout](RibbonControl/RestoreLayout.md)(…) | Восстанавливает размещение из указанного потока с параметрами сериализации по умолчанию. (перегрузок: 2) |
| [SaveLayout](RibbonControl/SaveLayout.md)(…) | Сохраняет размещение в указанный поток с параметрами сериализации по умолчанию. (перегрузок: 2) |
| static [GetDisplayMode](RibbonControl/GetDisplayMode.md)(…) | Возвращает допустимые режимы отображения Ribbon для указанного элемента. |
| static [SetDisplayMode](RibbonControl/SetDisplayMode.md)(…) | Задаёт допустимые режимы отображения Ribbon для указанного элемента. |

## События

| имя | описание |
| --- | --- |
| event [ApplicationButtonClick](RibbonControl/ApplicationButtonClick.md) | Происходит при щелчке по Application Button. |
| event [ApplicationButtonPress](RibbonControl/ApplicationButtonPress.md) | Происходит при нажатии кнопки указателя над Application Button. |

## См. также

* пространство имён [Eremex.AvaloniaUI.Controls.Ribbon](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
