# Класс ToolbarItem

Предоставляет базовую функциональность для элементов, отображаемых на панелях инструментов, в меню и в Ribbon.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls.Bars`](./index.md)  
**Сборка:** `Eremex.Avalonia.Controls.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls](https://www.nuget.org/packages/Eremex.Avalonia.Controls)

## Объявление

```csharp
public class ToolbarItem : TemplatedControl, IBorderStateProvider, ICommandSource, INavigationItem, 
    IToolbarActionItem
```

## Конструкторы

| имя | описание |
| --- | --- |
| [ToolbarItem](ToolbarItem/ToolbarItem.md)() | Инициализирует новый экземпляр класса ToolbarItem. |

## Свойства

| имя | описание |
| --- | --- |
| [Alignment](ToolbarItem/Alignment.md) { get; set; } | Возвращает или задаёт выравнивание элемента на его панели инструментов. |
| [Category](ToolbarItem/Category.md) { get; set; } | Возвращает или задаёт категорию, используемую для упорядочивания элемента при настройке. |
| [CloseMenuOnClick](ToolbarItem/CloseMenuOnClick.md) { get; set; } | Возвращает или задаёт, закрывает ли щелчок по элементу содержащее его меню. |
| [Command](ToolbarItem/Command.md) { get; set; } | Возвращает или задаёт команду, выполняемую при активации элемента. |
| [CommandParameter](ToolbarItem/CommandParameter.md) { get; set; } | Возвращает или задаёт параметр, передаваемый команде элемента. |
| [CustomizationName](ToolbarItem/CustomizationName.md) { get; set; } | Возвращает или задаёт имя, отображаемое для элемента при настройке. |
| [Description](ToolbarItem/Description.md) { get; set; } | Возвращает или задаёт дополнительный описательный текст, отображаемый для элемента. |
| [DisplayMode](ToolbarItem/DisplayMode.md) { get; set; } | Возвращает или задаёт, какие части элемента отображаются. |
| [Glyph](ToolbarItem/Glyph.md) { get; set; } | Возвращает или задаёт изображение, отображаемое для элемента. |
| [GlyphAlignment](ToolbarItem/GlyphAlignment.md) { get; set; } | Возвращает или задаёт положение глифа относительно заголовка элемента. |
| [GlyphSize](ToolbarItem/GlyphSize.md) { get; set; } | Возвращает или задаёт размер, используемый для отображения глифа элемента. |
| [GlyphSizeMode](ToolbarItem/GlyphSizeMode.md) { get; set; } | Возвращает или задаёт способ определения размера глифа элемента. |
| [GlyphTemplate](ToolbarItem/GlyphTemplate.md) { get; set; } | Возвращает или задаёт шаблон, используемый для отображения глифа элемента. |
| [Group](ToolbarItem/Group.md) { get; } | Возвращает группу элементов панели инструментов, содержащую элемент, или null, если его держатель не является группой. |
| [Header](ToolbarItem/Header.md) { get; set; } | Возвращает или задаёт содержимое заголовка элемента. |
| [HeaderContentHorizontalAlignment](ToolbarItem/HeaderContentHorizontalAlignment.md) { get; set; } | Возвращает или задаёт горизонтальное выравнивание содержимого заголовка элемента. |
| [HeaderTemplate](ToolbarItem/HeaderTemplate.md) { get; set; } | Возвращает или задаёт шаблон, используемый для отображения заголовка элемента. |
| [Hint](ToolbarItem/Hint.md) { get; set; } | Возвращает или задаёт текст всплывающей подсказки, отображаемой для элемента. |
| [Holder](ToolbarItem/Holder.md) { get; } | Возвращает контейнер, владеющий элементом. |
| [HotKey](ToolbarItem/HotKey.md) { get; set; } | Возвращает или задаёт сочетание клавиш, активирующее элемент. |
| [HotKeyDisplayString](ToolbarItem/HotKeyDisplayString.md) { get; set; } | Возвращает или задаёт текст, отображаемый для сочетания клавиш элемента. |
| [Id](ToolbarItem/Id.md) { get; set; } | Возвращает или задаёт идентификатор элемента панели инструментов. |
| [IsLocatedInRibbon](ToolbarItem/IsLocatedInRibbon.md) { get; } | Возвращает, принадлежит ли элемент Ribbon. |
| [IsSelected](ToolbarItem/IsSelected.md) { get; set; } | Возвращает или задаёт, выбран ли элемент. |
| [KeyTip](ToolbarItem/KeyTip.md) { get; set; } | Возвращает или задаёт последовательность клавиш, отображаемую для активации этого элемента при навигации по подсказкам клавиш. |
| [Manager](ToolbarItem/Manager.md) { get; set; } | Возвращает или задаёт менеджер панелей инструментов, связанный с этим объектом. |
| [Palette](ToolbarItem/Palette.md) { get; set; } | Возвращает или задаёт палитру, используемую для отрисовки глифа элемента. |
| [RecognizesAccessKey](ToolbarItem/RecognizesAccessKey.md) { get; set; } | Возвращает или задаёт, обозначает ли подчёркивание в заголовке клавишу доступа. |
| [RibbonCommandLayout](ToolbarItem/RibbonCommandLayout.md) { get; } | Возвращает макет команды Ribbon, используемый для отображения элемента. |
| [ScreenBounds](ToolbarItem/ScreenBounds.md) { get; } | Возвращает границы элемента в экранных координатах. |
| [SerializationInfo](ToolbarItem/SerializationInfo.md) { get; } | Возвращает сведения о размещении, используемые при сериализации или десериализации. |
| [SerializationName](ToolbarItem/SerializationName.md) { get; set; } | Возвращает или задаёт имя, идентифицирующее этот объект при сериализации размещения. |
| [ShowSeparator](ToolbarItem/ShowSeparator.md) { get; set; } | Возвращает или задаёт, отображается ли разделитель перед элементом. |
| [Toolbar](ToolbarItem/Toolbar.md) { get; } | Возвращает панель инструментов, содержащую элемент. |

## Методы

| имя | описание |
| --- | --- |
| [GetRootHolder](ToolbarItem/GetRootHolder.md)() | Возвращает самый внешний держатель элемента панели инструментов. |
| virtual [GetShortcutDisplayString](ToolbarItem/GetShortcutDisplayString.md)() | Возвращает текст, используемый для отображения сочетания клавиш элемента. |
| [OnDragLeave](ToolbarItem/OnDragLeave.md)() | Сбрасывает состояние перетаскивания над элементом. |
| [OnDropDownBorderEnter](ToolbarItem/OnDropDownBorderEnter.md)(…) | Обрабатывает вход указателя в область раскрытия элемента. |
| [OnDropDownBorderLeave](ToolbarItem/OnDropDownBorderLeave.md)(…) | Обрабатывает выход указателя из области раскрытия элемента. |
| [OnDropDownBorderReleased](ToolbarItem/OnDropDownBorderReleased.md)(…) | Обрабатывает отпускание кнопки указателя над областью раскрытия элемента. |
| override [ToString](ToolbarItem/ToString.md)() |  |

## События

| имя | описание |
| --- | --- |
| event [Click](ToolbarItem/Click.md) | Происходит при щелчке по элементу. |
| event [Press](ToolbarItem/Press.md) | Происходит при нажатии кнопки указателя над элементом. |

## См. также

* пространство имён [Eremex.AvaloniaUI.Controls.Bars](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
