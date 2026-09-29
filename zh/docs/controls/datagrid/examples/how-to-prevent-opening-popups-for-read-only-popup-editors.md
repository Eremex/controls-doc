---
title: 如何为只读弹出式编辑器阻止打开弹出窗口
order: 1000
seealso: []
---

# 如何为只读弹出式编辑器阻止打开弹出窗口


从 1.2 版本开始，您可以使用弹出式编辑器的 `ShowPopupIfReadOnly` 属性，来阻止只读弹出式编辑器打开弹出窗口。

在早期版本中，您可以通过 `PopupEditor.PopupOpening` 事件来控制此行为。本主题将提供关于使用该事件的更多信息。


当绑定到只读列时，内置弹出式编辑器（`DateEditor`、`ComboBoxEditor`、`MemoEditor` 等）仍然允许显示其弹出窗口。
`PopupEditor.PopupOpening` 事件会在弹出窗口出现之前触发，使您可以有条件地禁用它——例如，当编辑器绑定到只读列时。您可以针对特定的内置编辑器处理此事件，也可以全局处理（将该逻辑应用于应用程序中所有的弹出式编辑器）。


## 为特定的只读列禁用弹出窗口

1. 使用 `GridColumn.CellTemplate` 属性将内置编辑器与表格列关联。
2. 处理该编辑器的 `PopupEditor.PopupOpening` 事件，以在为此编辑器显示弹出窗口时执行相应操作。

在以下示例中，表格列与 `DateEditor` 内置编辑器相关联。`DateEditor.PopupOpening` 事件处理程序会在表格列为只读时禁用该编辑器的弹出窗口。

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

## 为所有绑定到只读列的弹出式编辑器禁用弹出窗口

您可以使用类处理程序（Class Handlers）或行为（Behavior）机制来全局处理编辑器的事件。

### 使用类处理程序全局禁用只读编辑器的弹出窗口

Avalonia 中的类处理程序允许在类级别而非实例级别处理事件。它们使您能够将事件处理程序附加到某种控件类型的所有实例上，而无需手动为每个实例订阅事件。

以下示例为 `PopupEditor.PopupOpening` 事件添加了一个类处理程序。此代码会影响 `PopupEditor` 的所有后代类。


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


### 使用行为机制全局禁用只读编辑器的弹出窗口

此方法需要使用 `Avalonia.Xaml.Interactivity` 包，该包为 Avalonia UI 提供了 Behavior 模式的实现。`Behavior` 对象允许您为给定控件类型的所有实例自定义属性并订阅事件。

以下代码为所有 `PopupEditor` 类实例创建了一个全局 `Behavior` 对象。该 `Behavior` 对象处理 `PopupEditor.PopupOpening` 事件，以禁用只读列中的弹出窗口。

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

<sup>*</sup> 本页面使用机器翻译技术翻译。
