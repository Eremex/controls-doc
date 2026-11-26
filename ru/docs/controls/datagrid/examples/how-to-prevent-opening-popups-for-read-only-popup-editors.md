---
title: Как предотвратить открытие всплывающих окон для редакторов только для чтения
order: 1000
seealso: []
---

# Как предотвратить открытие всплывающих окон для редакторов только для чтения

Начиная с версии 1.2, вы можете использовать свойство [`ShowPopupIfReadOnly`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditorProperties/ShowPopupIfReadOnly.md) всплывающего редактора, чтобы предотвратить открытие всплывающих окон для редакторов только для чтения.

В более ранних версиях вы можете управлять этим поведением с помощью события [`PopupEditor.PopupOpening`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpening.md). Текущий раздел содержит более подробную информацию об использовании этого события.


При привязке к колонкам только для чтения встроенные всплывающие редакторы ([`DateEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md), [`ComboBoxEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/ComboBoxEditor.md), [`MemoEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/MemoEditor.md) и другие) по-прежнему позволяют отображать свои всплывающие окна.
Событие [`PopupEditor.PopupOpening`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpening.md) вызывается непосредственно перед появлением всплывающего окна, что позволяет условно отключать его — например, когда редактор привязан к колонке только для чтения. Вы можете обработать это событие для конкретного встроенного редактора или глобально (чтобы применить эту логику ко всем всплывающим редакторам в приложении).


## Отключение всплывающих окон для конкретной колонки только для чтения

1. Свяжите встроенный редактор с колонкой грида с помощью свойства [`GridColumn.CellTemplate`](../../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md).
2. Обработайте событие редактора [`PopupEditor.PopupOpening`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpening.md), чтобы выполнять действия при отображении всплывающего окна для этого редактора.

В этом примере колонка грида связана со встроенным редактором [`DateEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/DateEditor.md). Обработчик события [`DateEditor.PopupOpening`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpening.md) отключает всплывающее окно редактора, когда колонка грида доступна только для чтения.

``` xml
<mxdg:GridColumn FieldName="BirthDate" Width="*" MinWidth="80">
    <mxdg:GridColumn.CellTemplate>
        <DataTemplate>
            <mxe:DateEditor x:Name="PART_Editor" PopupOpening="DateEditor_PopupOpening"/>
        </DataTemplate>
    </mxdg:GridColumn.CellTemplate>
</mxdg:GridColumn>
```

``` cs
private void DateEditor_PopupOpening(object sender, OpeningPopupEventArgs e)
{
    e.Cancel = (sender as PopupEditor).ReadOnly;
}
```

## Отключение всплывающих окон для всех всплывающих редакторов, привязанных к колонкам только для чтения

Вы можете использовать обработчики классов (Class Handlers) или механизм поведений (Behavior), чтобы обрабатывать события редакторов глобально.

### Использование обработчика класса для глобального отключения всплывающих окон в редакторах только для чтения

Обработчики классов в Avalonia позволяют обрабатывать события на уровне класса, а не на уровне экземпляра. Они позволяют подключать обработчики событий ко всем экземплярам определённого типа контрола без ручной подписки на каждый из них.

Этот пример добавляет обработчик класса для события [`PopupEditor.PopupOpening`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpening.md). Этот код влияет на все потомки [`PopupEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor.md).


``` cs
public partial class MainWindow : MxWindow
{
    public MainWindow()
    {
        InitializeComponent();
        PopupEditor.PopupOpeningEvent.AddClassHandler<PopupEditor>(PopupEditor_PopupOpening);
    }

    private void PopupEditor_PopupOpening(object sender, OpeningPopupEventArgs e)
    {
        e.Cancel = (sender as PopupEditor).ReadOnly;
    }
}
```


### Использование механизма поведений для глобального отключения всплывающих окон в редакторах только для чтения

Этот подход требует использования пакета `Avalonia.Xaml.Interactivity`, который предоставляет реализацию паттерна Behavior для Avalonia UI. Объекты `Behavior` позволяют настраивать свойства и подписываться на события для всех экземпляров заданного типа контрола.

Следующий код создаёт глобальный объект `Behavior` для всех экземпляров класса [`PopupEditor`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor.md). Объект `Behavior` обрабатывает событие [`PopupEditor.PopupOpening`](../../../API/Eremex.AvaloniaUI.Controls.Editors/PopupEditor/PopupOpening.md), чтобы отключить всплывающие окна в колонках только для чтения.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:behaviors="using:DemoCenter.Behaviors"

<UserControl.Styles>
    <Style Selector=":is(mxe|PopupEditor)">
        <Setter Property="Interaction.Behaviors">
            <Setter.Value>
                <BehaviorCollectionTemplate>
                    <BehaviorCollection>
                        <behaviors:PopupEditorReadOnlyPopupBehavior/>
                    </BehaviorCollection>
                </BehaviorCollectionTemplate>
            </Setter.Value>
        </Setter>
    </Style>
</UserControl.Styles>
```

``` cs
using Avalonia.Xaml.Interactivity;
using Eremex.AvaloniaUI.Controls.Editors;

namespace DemoCenter.Behaviors
{
    public class PopupEditorReadOnlyPopupBehavior : Behavior<PopupEditor>
    {
        protected override void OnAttached()
        {
            base.OnAttached();
            AssociatedObject.PopupOpening += AssociatedObject_PopupOpening;
        }

        protected override void OnDetachedFromVisualTree()
        {
            base.OnDetachedFromVisualTree();
            AssociatedObject.PopupOpening -= AssociatedObject_PopupOpening;
        }

        void AssociatedObject_PopupOpening(object sender, OpeningPopupEventArgs e)
        {
            e.Cancel = AssociatedObject.ReadOnly;
        }
    }
}
```

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
