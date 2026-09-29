---
title: 数据编辑
order: 6000
seealso: []
---

# 数据编辑

## 默认就地 Eremex 编辑器

TreeList 和 TreeView 控件的默认行为是使用就地 Eremex 编辑器来显示和编辑常见数据类型的单元格值：
如果未显式指定单元格编辑器，则 TreeList 和 TreeView 控件使用就地 Eremex 编辑器来显示和编辑这些数据类型的单元格值：

- 布尔值 — `CheckEditor`
- 双值 — `SpinEditor`
- 枚举值 — `ComboBoxEditor`
- 具有 `TypeConverter` 属性且 `TypeConverter.GetStandardValuesSupported` 方法返回 `true` — `ComboBoxEditor` 的属性
- 其他值 — `TextEditor`

您可以显式指定列的单元格编辑器以覆盖默认编辑器分配，并自定义就地编辑器的设置。当前主题提供了有关编辑器分配的更多详细信息。

当单元格编辑操作开始时，您可以访问和修改活动的就地编辑器。有关详细信息，请参阅[访问活动就地 Eremex 编辑器](#access-the-active-in-place-eremex-editor)部分。

## 分配就地 Eremex 编辑器

TreeList 和 TreeView 控件允许您将就地 Eremex 编辑器显式分配给单元格（列）以覆盖默认编辑器分配，或者在 XAML 或后台代码中自定义单元格编辑器。为此目的，请使用以下属性：

- TreeView 控件：`TreeViewControl.EditorProperties`

TreeView 控件显示单个列的数据。因此，`TreeViewControl.EditorProperties` 属性指定用于编辑此列单元格的就地编辑器。

- TreeList 控件：`TreeListColumn.EditorProperties`
  
TreeList 控件中的每一列都可以有自己的就地编辑器。在 `TreeListControl.Columns` 集合中创建 TreeList 列（`TreeListColumn` 对象），并使用 `TreeListColumn.EditorProperties` 属性设置该列的编辑器。

您可以将 `EditorProperties` 属性设置为指定 in-place 编辑器类型的以下对象（所有这些对象都是 `BaseEditorProperties` 后代）：

- `ButtonEditorProperties` — 包含特定于 `ButtonEditor` 控件的设置。
- `CheckEditorProperties` — 包含特定于 `CheckEditor` 控件的设置。
- `ComboBoxEditorProperties` — 包含特定于 `ComboBoxEditor` 控件的设置。
- `DateEditorProperties` — 包含特定于 `DateEditor` 控件的设置。
- `HyperlinkEditorProperties` — 包含特定于 `HyperlinkEditor` 控件的设置。
- `MemoEditorProperties` — 包含特定于 `MemoEditor` 控件的设置。
- `PopupColorEditorProperties` — 包含特定于 `PopupColorEditor` 控件的设置。
- `SegmentedEditorProperties` — 包含特定于 `SegmentedEditor` 控件的设置。
- `SpinEditorProperties` — 包含特定于 `SpinEditor` 控件的设置。
- `TextEditorProperties` — 包含特定于 `TextEditor` 控件的设置。
    
假设您将 `EditorProperties` 属性设置为 `SpinEditorProperties` 对象。在显示模式下（单元格编辑未激活），TreeList/TreeView 控件使用 `SpinEditorProperties` 对象的设置在目标列的单元格中模拟 `SpinEditor`。在单元格编辑操作开始之前，不会创建真正的 `SpinEditor`。当用户开始单元格编辑时，TreeList/TreeView 控件会在焦点单元格中创建真正的 `SpinEditor` 就地编辑器。编辑操作完成后，控件会销毁真实的 `SpinEditor` 并重新开始在此单元格中模拟 `SpinEditor`。请参阅[访问活动就地 Eremex 编辑器](#access-the-active-in-place-eremex-editor)了解如何访问真实的单元格编辑器。

### 示例 - 如何在树列表列中使用 ButtonEditor 作为就地编辑器

以下代码将 `ButtonEditor` 就地编辑器分配给 TreeList 列。

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist" 
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxtl:TreeListControl.Columns>
    <mxtl:TreeListColumn Header="Name" FieldName="Name">
        <mxtl:TreeListColumn.EditorProperties>
            <mxe:ButtonEditorProperties>
                <mxe:ButtonEditorProperties.Buttons>
                    <mxe:ButtonSettings Content="Clear" 
                     Command="{Binding $parent[mxtl:CellControl].DataControl.
                               DataContext.ClearValueCommand}"/>
                </mxe:ButtonEditorProperties.Buttons>
            </mxe:ButtonEditorProperties>
        </mxtl:TreeListColumn.EditorProperties>
    </mxtl:TreeListColumn>
</mxtl:TreeListControl.Columns>
```

### 示例 - 如何在树视图中使用 ComboBoxEditor 作为就地编辑器

以下代码将 `ComboBoxEditor` 就地编辑器分配给 TreeView。

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist" 
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxtl:TreeViewControl.EditorProperties>
    <mxe:ComboBoxEditorProperties ItemsSource="{Binding Families}"/>
</mxtl:TreeViewControl.EditorProperties>
```

## 使用模板分配就地 Eremex 编辑器

您可以使用模板将 Eremex 编辑器分配给 TreeList 和 TreeView 列。单元格模板允许您为同一列中的不同行使用不同的编辑器。

!!!笔记

使用模板有以下限制：

- 通过单元格模板提供的显示文本不用于排序、分组和过滤数据。
    - 单元格模板不是 [exported](../export.md)。


要为单元格模板中的列编辑提供就地编辑器，请使用以下属性：

- `TreeListColumn.CellTemplate`
- `TreeViewControl.CellTemplate`

对于模板中定义的 Eremex 编辑器，将 `x:Name` 属性设置为 **“PART_Editor”**。这可确保编辑器的值 (`BaseEditor.EditorValue`) 自动绑定到列的字段。另外， 
编辑器的外观设置（活动和非活动状态下的边框可见性和前景色）将由 TreeList/TreeView 控件管理。

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
...
<mxtl:TreeListColumn Header="Phone" FieldName="Phone">
    <mxtl:TreeListColumn.CellTemplate>
        <DataTemplate>
            <mxe:ButtonEditor x:Name="PART_Editor">
                <mxe:ButtonEditor.Buttons>
                    <mxe:ButtonSettings Content="..."/>
                </mxe:ButtonEditor.Buttons>
            </mxe:ButtonEditor>
        </DataTemplate>
    </mxtl:TreeListColumn.CellTemplate>
</mxtl:TreeListColumn>
```


## 自定义编辑器

您可以使用单元格模板将自定义编辑器嵌入到 TreeList 和 TreeView 列中。可采用以下方法：

- 直接将编辑分配给特定列。
- 根据列的底层对象的数据类型动态地将编辑器分配给列。该技术适用于 TreeList 控件。

有关详细信息，请参阅 [Custom Editors](custom-editors.md) 主题。



## 获取和设置单元格值

TreeList 和 TreeView 控件公开以下 API 来获取和设置单元格值：

- `TreeListControl.GetCellDisplayText`
- `TreeListControl.GetCellValue`
- `TreeListControl.SetCellValue`
- `TreeViewControl.GetCellDisplayText`
- `TreeViewControl.GetCellValue`
- `TreeViewControl.SetCellValue`



## 访问活动就地 Eremex 编辑器

- `ActiveEditor` 属性 — 返回活动的 in-place 编辑器。
  
当将就地 Eremex 编辑器分配给 TreeList/TreeView 列（隐式分配，或使用 `EditorSettings` 属性和模板显式分配）时，控件会在显示模式下（即单元格编辑未激活时）在该列的单元格中模拟指定的就地编辑器。此时并不存在真正的就地编辑器。显示模式下的单元格编辑器模拟可提高应用程序性能。

当用户开始编辑单元格时，控件会创建一个真正的就地编辑器。此时，您可以使用控件的 `ActiveEditor` 属性来访问真实的 Eremex 编辑器实例。当单元格失去焦点时，真正的编辑器会被销毁，并且 `ActiveEditor` 属性返回 `null`。

- `ShownEditor` 事件 — 在为单元格创建就地编辑器并开始编辑操作后引发。您可以使用事件的 `Editor` 参数或控件的 `ActiveEditor` 属性访问活动编辑器。

## 显示单元格编辑器

- `ShowEditor` 方法 — 激活焦点单元格中的单元格编辑器。
- `ShowingEditor` 事件 — 允许您防止用户在特定情况下激活单元格编辑器。处理 `ShowingEditor` 事件时，将 `Cancel` 事件参数设置为 `true` 以禁用编辑器激活。


### 按用户显示单元格编辑器

启用单元格编辑后，单击节点单元格将激活单元格编辑器。使用 `DataControlBase.EditorShowMode` 属性指定哪个鼠标操作触发编辑器。您可以将此属性设置为以下值：

- `EditorShowMode.PointerPressed`（默认）— 按下鼠标按钮时会激活单元格编辑器。

当启用 [node drag-and-drop](../node-drag-and-drop.md) 且 `RowDragMode` 设置为 `RowDragMode.Row` 时，不支持 `EditorShowMode.PointerPressed` 模式。在此配置中，默认模式为 `EditorShowMode.PointerPressedInFocusedCell`。

- `EditorShowMode.PointerPressedInFocusedCell` — 当在焦点单元格中按下鼠标按钮时，单元格编辑器被激活。

如果节点拖放处于活动状态并且控件的 `RowDragMode` 属性设置为 `RowDragMode.Row`，则此模式为默认模式。

- `EditorShowMode.PointerReleased` — 释放鼠标按钮时会激活单元格编辑器。
- `EditorShowMode.PointerReleasedInFocusedCell` — 当鼠标按钮在聚焦单元格中释放时，单元格编辑器被激活。

## 关闭活动就地编辑器

- `CloseEditor` 方法 — 保存在单元格编辑器中所做的更改并关闭编辑器。
- `HideEditor` 方法 — 关闭单元格编辑器而不保存任何更改。

- `HiddenEditor` 事件 — 在活动单元格编辑器关闭后触发。


## 保存在就地编辑器中所做的更改

- `CloseEditor` 方法 — 保存在单元格编辑器中所做的更改并关闭编辑器。
- `PostEditor` 方法 — 保存在活动单元格编辑器中所做的更改，而不关闭编辑器。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
