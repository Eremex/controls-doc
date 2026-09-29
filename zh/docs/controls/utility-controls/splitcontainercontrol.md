---
title: SplitContainerControl
order: 1400
seealso: []
---

# SplitContainerControl

`SplitContainerControl` 是复合 control，显示由可移动分流器分隔的两个面板。用户可以拖动拆分器来更改面板的大小。他们还可以单击拆分器来折叠选定的面板，然后再次单击拆分器来恢复面板。

![SplitContainerControl](../../images/SplitContainerControl.png)

control的主要特点包括：

- 用户可以拖放拆分器来调整面板大小。
- 在代码中设置面板的大小。
- 面板的垂直或水平布置。
- 能够折叠/展开其中一个面板。
- 用于隐藏分离器的 option。

## 指定面板内容

使用 `SplitContainerControl.Panel1` 和 `SplitContainerControl.Panel2` 属性将内容放置到 control 的面板上。支持两种使用场景：

- 使用 controls 初始化这些属性以显示在面板中。 
- 使用自定义对象初始化这些属性。在这种情况下，使用 `SplitContainerControl.Panel1Template` 和 `SplitContainerControl.Panel2Template` 属性来指定将呈现自定义对象的 DataTemplates。

``` xml
<mxe:SplitContainerControl Name="splitContainer"
                            Grid.Row="1"
                            BorderThickness="1" BorderBrush="Gray">
    <mxe:SplitContainerControl.Panel1>
        <Label Content="Panel1" HorizontalAlignment="Center" VerticalAlignment="Center"/>
    </mxe:SplitContainerControl.Panel1>
    <mxe:SplitContainerControl.Panel2>
        <Label Content="Panel2" HorizontalAlignment="Center" VerticalAlignment="Center"/>
    </mxe:SplitContainerControl.Panel2>
</mxe:SplitContainerControl>
```

## 设置面板大小和方向

使用 `SplitContainerControl.Orientation` 属性来设置 choose between 的水平（默认）和垂直面板排列。

![splitcontainercontrol-orientation](../../images/splitcontainercontrol-orientation.png)

要设置容器面板的大小，请使用 `SplitContainerControl.Panel1Length` 或 `SplitContainerControl.Panel2Length` 属性。

- 在水平方向上，这些属性设置面板的宽度。
- 在垂直方向上，它们设置面板的高度。

`Panel1MinLength`、`Panel1MaxLength`、`Panel2MinLength` 和 `Panel2MaxLength` 属性允许您设置面板大小调整约束。  用户无法将面板大小调整到超出这些限制。

## 折叠和恢复面板

拆分器中显示的箭头图标表示当用户单击拆分器时面板将折叠。在折叠状态下，分离器的箭头图标会反转其方向。用户可以再次单击拆分器来恢复面板。

![SplitContainerControl](../../images/splitcontainercontrol-collapse.gif)

`SplitContainerControl.CollapsePanel` 属性允许您指定可折叠面板。该属性的默认值为_Panel2_。

要在代码中折叠和恢复面板，请使用 `IsCollapsed` 属性。

## 禁用面板折叠

将 `SplitContainerControl.CollapsePanel` 属性设置为 `None` 以禁用面板折叠功能。在此模式下，拆分器不显示箭头图标。

## 隐藏分离器

使用 `SplitContainerControl.IsSplitterVisible` 属性至 `false` 可在特定情况下隐藏拆分器。这防止用户在面板上执行调整大小和折叠/恢复操作。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
