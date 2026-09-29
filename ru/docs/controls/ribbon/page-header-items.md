---
title: Элементы заголовка страницы
order: 550
seealso: []
---

# Элементы заголовка страницы

Элементы заголовка страницы — это [элементы Ribbon](ribbon-items.md), отображаемые в одну линию с заголовками страниц. Эти элементы привязаны к правому краю контрола Ribbon.

![ribbon-pageheaderitems](../../images/ribbon-pageheaderitems.png)

Используйте коллекцию `RibbonControl.PageHeaderItems`, чтобы добавлять, получать доступ и изменять элементы заголовка страницы.

``` xml
<mxr:RibbonControl.PageHeaderItems>
    <mxb:ToolbarEditorItem EditorWidth="100">
        <mxb:ToolbarEditorItem.EditorProperties>
            <mxe:ButtonEditorProperties>
                <mxe:ButtonEditorProperties.Buttons>
                    <mxe:ButtonSettings Glyph="{x:Static icons:Basic.Search}" GlyphSize="12, 12"/>
                </mxe:ButtonEditorProperties.Buttons>
            </mxe:ButtonEditorProperties>
        </mxb:ToolbarEditorItem.EditorProperties>
    </mxb:ToolbarEditorItem>
    <mxb:ToolbarButtonItem Name="btnAbout" Header="About" Click="BtnAbout_Click" />
</mxr:RibbonControl.PageHeaderItems>
```

Вы также можете использовать свойство `RibbonControl.PageHeaderItemsSource`, чтобы создавать элементы заголовка страницы из коллекции бизнес-объектов, хранящихся во View Model. Соответствующие шаблоны данных должны определять [элементы Ribbon](ribbon-items.md).


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
