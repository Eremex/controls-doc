---
title: Page Header Items
order: 550
seealso: []
---

# Page Header Items

Page Header Items are [ribbon items](ribbon-items.md) displayed in line with page headers. These items are anchored to the Ribbon control's right edge.

![ribbon-pageheaderitems](../../images/ribbon-pageheaderitems.png)

Use the [`RibbonControl.PageHeaderItems`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonControl/PageHeaderItems.md) collection to add, access and modify Page Header Items.

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

You can also use the [`RibbonControl.PageHeaderItemsSource`](../../API/Eremex.AvaloniaUI.Controls.Ribbon/RibbonControl/PageHeaderItemsSource.md) property to create Page Header Items from a collection of business objects stored in a View Model. Corresponding data templates should define [ribbon items](ribbon-items.md).