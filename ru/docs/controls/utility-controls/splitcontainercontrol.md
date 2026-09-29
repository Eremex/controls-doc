---
title: SplitContainerControl
order: 1400
seealso: []
---

# SplitContainerControl

`SplitContainerControl` — это составной контрол, отображающий две панели, разделённые подвижным разделителем. Пользователи могут перетаскивать разделитель, чтобы изменять размер панелей. Они также могут щёлкнуть по разделителю, чтобы свернуть выбранную панель, а затем щёлкнуть по разделителю ещё раз, чтобы восстановить панель.

![SplitContainerControl](../../images/SplitContainerControl.png)

Основные возможности контрола включают:

- Пользователи могут перетаскивать разделитель, чтобы изменять размер панелей.
- Задание размера панелей в коде.
- Вертикальное или горизонтальное расположение панелей.
- Возможность сворачивать/разворачивать одну из панелей.
- Опция скрытия разделителя.

## Содержимое для панелей

Используйте свойства `SplitContainerControl.Panel1` и `SplitContainerControl.Panel2`, чтобы разместить содержимое на панелях контрола. Поддерживаются два сценария использования:

- Инициализируйте эти свойства контролами, которые будут отображаться на панелях. 
- Инициализируйте эти свойства пользовательскими объектами. В этом случае используйте свойства `SplitContainerControl.Panel1Template` и `SplitContainerControl.Panel2Template`, чтобы задать DataTemplate, которые будут отрисовывать пользовательские объекты.

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

## Настройка размера и направления панели

Используйте свойство `SplitContainerControl.Orientation`, чтобы выбрать между горизонтальным (по умолчанию) и вертикальным расположением панелей.

![splitcontainercontrol-orientation](../../images/splitcontainercontrol-orientation.png)

Чтобы задать размер панелей контейнера, используйте свойства `SplitContainerControl.Panel1Length` или `SplitContainerControl.Panel2Length`.

- В горизонтальной ориентации эти свойства задают ширину панелей.
- В вертикальной ориентации они задают высоту панелей.

Свойства `Panel1MinLength`, `Panel1MaxLength`, `Panel2MinLength` и `Panel2MaxLength` позволяют задавать ограничения на изменение размера панелей. Пользователи не могут изменять размер панелей за пределами этих лимитов. 

## Сворачивание и восстановление панели

Значок стрелки, отображаемый на разделителе, указывает, что панель будет свёрнута, когда пользователь щёлкнет по разделителю. В свёрнутом состоянии значок стрелки на разделителе меняет своё направление на противоположное. Пользователь может щёлкнуть по разделителю ещё раз, чтобы восстановить панель.

![SplitContainerControl](../../images/splitcontainercontrol-collapse.gif)

Свойство `SplitContainerControl.CollapsePanel` позволяет задать сворачиваемую панель. Значение свойства по умолчанию — _Panel2_.

Чтобы свернуть и восстановить панель в коде, используйте свойство `IsCollapsed`.

## Отключение сворачивания панели

Установите свойство `SplitContainerControl.CollapsePanel` в `None`, чтобы отключить функцию сворачивания панели. В этом режиме разделитель не отображает значки стрелок.

## Скрытие разделителя

Установите свойство `SplitContainerControl.IsSplitterVisible` в `false`, чтобы скрыть разделитель в определённых случаях. Это не позволяет пользователю выполнять операции изменения размера и сворачивания/восстановления панелей.


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
