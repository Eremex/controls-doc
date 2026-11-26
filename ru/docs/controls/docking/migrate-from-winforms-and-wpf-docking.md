---
title: Переход с докинга WinForms и WPF на Docking UI для Avalonia
order: 64000
seealso: []
---

# Переход с докинга WinForms и WPF на Docking UI для Avalonia

Если вы создавали интерфейсы в стиле IDE с менеджером докинга в Windows Forms или WPF и переходите на Avalonia UI, то Docking UI библиотеки Eremex Avalonia UI Controls покажется вам знакомым. Библиотека предназначена только для Avalonia UI: она не содержит контролов для Windows Forms или WPF. Компонент **Dock Manager** создаёт панели инструментов, которые можно закреплять, автоматически скрывать и делать плавающими, а также области документов с вкладками — всё это в кроссплатформенном приложении Avalonia UI (Windows, Linux, macOS).

В этой статье знакомые вам понятия сопоставляются со строительными блоками библиотеки и указывается, где найти подробности.

## Карта понятий

| Что вам нужно | Строительный блок в библиотеке Eremex |
| --- | --- |
| Компонент, управляющий всем размещением докинга | [`DockManager`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager.md) - см. [Dock Manager и элементы докинга](dock-manager.md) |
| Окно инструментов (Solution Explorer, Properties, Output и т. д.) | [`DockPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockPane.md) - см. [Dock-панели и контейнеры](dock-panes-and-containers.md) |
| Вкладка документа в основной области (MDI с вкладками) | [`DocumentPane`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentPane.md) - см. [Document-панели](document-panes.md) |
| Группа вкладок | [`TabbedGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/TabbedGroup.md) (контейнер вкладок для Dock-панелей) и [`DocumentGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DocumentGroup.md) (контейнер вкладок для Document-панелей) |
| Панели рядом или друг над другом, разделённые сплиттерами | [`DockGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockGroup.md) (контейнер с разделением) - см. [Разделённые панели](dock-panes-and-containers.md#разделённые-панели) |
| Панель, выдвигающаяся от края окна | Автоскрытие - см. [Автоскрытые панели](dock-panes-and-containers.md#автоскрытые-панели) |
| Панель в отдельном окне | [`FloatGroup`](../../API/Eremex.AvaloniaUI.Controls.Docking/FloatGroup.md) - см. [Плавающие панели](dock-panes-and-containers.md#плавающие-панели) |
| Направляющие перетаскивания, показывающие, куда будет закреплена панель | Направляющие докинга - см. [Dock Manager и элементы докинга](dock-manager.md#направляющие-докинга), а также событие [`DockManager.CustomizeDockGuide`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/CustomizeDockGuide.md) (версия 1.5), позволяющее скрыть определённые направляющие |
| Переключение окон по Ctrl+Tab | [Переключатель документов](document-switcher.md) |
| Сохранение и восстановление размещения между сеансами | [Сохранение и восстановление размещения панелей](save-and-restore-layout.md) |
| Построение размещения в коде (упорядочивание, разделение, перевод в плавающий режим, активация, закрытие) | [Выполнение операций закрепления в коде](perform-dock-operations-in-code.md) |
| Размещение, управляемое ViewModel | [Использование паттерна MVVM для заполнения элементами закрепления](use-mvvm-pattern-to-populate-dock-items.md) |

## Отличия, которые стоит знать

- **Сначала XAML.** Размещение объявляется в XAML (Dock Manager содержит Dock-панели, Document-панели и группы), а операции докинга можно также выполнять в коде.
- **Поддержка MVVM.** Панели можно создавать из коллекции ViewModel, поэтому размещение докинга вписывается в MVVM-приложение без code-behind.
- **Сериализация размещения.** Размещение Dock-панелей и документов можно сохранять и восстанавливать с помощью методов [`DockManager.SaveLayout`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/SaveLayout.md) и [`DockManager.RestoreLayout`](../../API/Eremex.AvaloniaUI.Controls.Docking/DockManager/RestoreLayout.md).
- **Кроссплатформенность.** Один и тот же Docking UI работает на всех платформах, которые поддерживает Avalonia UI.

## Минимальное размещение

В этом примере показана структура типичного размещения: область документов с панелью *Error List* под ней и контейнер вкладок с двумя панелями инструментов рядом с ними. Пошаговое описание приведено в статье [Начало работы с Docking](get-started-with-docking.md).

``` xml
xmlns:mxd="https://schemas.eremexcontrols.net/avalonia/docking"

<mxd:DockManager>
    <mxd:DockGroup>
        <mxd:DockGroup Orientation="Vertical">
            <mxd:DocumentGroup></mxd:DocumentGroup>
            <mxd:DockPane Header="Error List"/>
        </mxd:DockGroup>
        <mxd:TabbedGroup>
            <mxd:DockPane Header="Properties"/>
            <mxd:DockPane Header="Debug"/>
        </mxd:TabbedGroup>
    </mxd:DockGroup>
</mxd:DockManager>
```

## Что дальше

- [Начало работы с Docking](get-started-with-docking.md)
- [Обзор интерфейса докинга](index.md)
- [Примеры](examples/index.md)

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
