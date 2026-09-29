---
title: 版本 1.0
order: 10
seealso: []
---

# 版本 1.0

## 1.0.96

### 新增内容

#### DataGridControl 和 TreeListControl

- 修复问题：将弹出式 UserControl 用作单元格编辑器时，该 UserControl 会意外失去焦点。

- 功能：提供在内置编辑器中处理导航键（方向键、Tab、Enter、F2、Esc、Home、End、PgUp 和 PgDown）的能力。

    Grid/TreeList 控件会拦截特定的导航键（方向键、Tab、Enter、F2、Esc、Home、End、PgUp 和 PgDown）以在单元格之间执行导航。要在内置编辑器中处理这些按键，请执行以下操作：
    - 创建一个实现 `IInplaceEditorNavigationHandler` 接口的类。
    - 实现 `IInplaceEditorNavigationHandler.NeedsKey` 方法。该方法应针对需要在内置编辑器中处理的按键返回 `true`。
    - 使用静态方法 `EditorNavigationHandlers.RegisterHandler` 将您的 `IInplaceEditorNavigationHandler` 对象与特定的内置编辑器类型关联。例如：`EditorNavigationHandlers.RegisterHandler<TextBox, MyTextBoxNavigationHandler>();`。

- 修复问题：禁用单元格编辑时，放置在单元格模板中的控件在单击时会被激活。
- 修复问题：更新已排序网格列中的单元格值会导致其他单元格的值发生变化。
- 修复问题：使用 CellTemplate 时，Esc 键不会回滚单元格中的更改。

#### PropertyGrid

- 功能：添加 `HiddenEditor` 事件。
- 功能：在 `ShowingEditor` 事件中添加 `Row` 参数。

#### 编辑器

- 使用较大的 DPI 设置时，弹出编辑器的尺寸不正确。


#### 图表
- 修复问题：某些情况下十字光标崩溃。
- 修复问题：在 `SortedDateTimeDataAdapter` 使用空数据时出现异常。


## 1.0.93


### 新增内容

#### ListView

- 修复问题：单击某个项目时，当前项目的选中状态不会被清除。
- 修复问题：在多选模式下，CTRL+A 快捷键不会选中所有项目。
- ListViewControl.GroupWidth 属性不再受支持，已被移除。
- ListViewControl.GetGroupValueDisplayText 方法现在为 internal。

#### PropertyGrid

- 修复问题：发生验证错误且使用 CellTemplate 时，无法将焦点从内置编辑器移开。



## 1.0

### 新增内容

#### 图表

`PolarChart` 控件——一个新的图表控件，可在极坐标系统上绘制图表。

- 十字光标
- 条带和恒定线
- 扫描方向和起始角度（针对 X 轴）
- Point Series View
- Line Series View
- Scatter Line Series View
- Area Series View
- Range Area Series View

`SmithChart` 控件——一个可绘制史密斯圆图的新控件。

- 十字光标
- Point Series View
- Scatter Line Series View

##### `CartesianChart` 更新

- 条带和恒定线
- Point Series View（支持 SVG 标记）
- Area Series View
- Scatter Line Series View
- Step Line Series View
- Step Area Series View
- Range Area Series View
- Bar Series View
- Range Bar Series View 

##### 通用功能

- 使用 MVVM 设计模式提供数据并自定义图表选项。
- 支持深色主题变体。
- 新增 `DiagramPointToScreenPoint` 和 `ScreenPointToDiagramPoint` 方法，当您需要显示自定义图形或工具提示，并需要确定目标图表元素的坐标时非常有用。


#### Docking
* `DockPane.ShowGlyphMode` 属性——指定面板标题中图标的可见性和位置。
* `DockPane.ShowTabGlyphMode` 属性——指定当面板托管在选项卡组中时，其标题（选项卡）中图标的可见性和位置。
- `FloatGroup.ShowGlyphMode` 属性——指定浮动窗口标题中图标的可见性和位置。
- `DockItemBase.FloatGroup` 属性——允许您获取当前停靠项（面板）在浮动模式下所托管的浮动窗口（`FloatGroup`）。
- `DockItemBase.AutoHideGroup` 属性——允许您获取当前停靠项（面板）在自动隐藏模式下所托管的自动隐藏容器（`AutoHideGroup`）。
- `DockManager.ExpandAutoHidePanel`——展开已折叠的自动隐藏面板。
- `DockManager.CollapseAutoHidePanel`——折叠已展开的自动隐藏面板。 
- `DockManager.SaveLayout` 和 `DockManager.RestoreLayout` 方法——允许您将控件的布局保存到流中，或从流中恢复布局。

#### DataGridControl 和 TreeListControl

- `SaveLayout` 和 `RestoreLayout` 方法——允许您将控件的布局保存到流中，或从流中恢复布局。

#### TreeListControl 和 TreeViewControl

- `ShowBranchesWithMatches` 过滤模式——您可以将 `TreeListControlBase.FilterMode` 属性设置为 `ShowBranchesWithMatches`，以在分支中包含符合过滤条件的节点时显示整个分支。

#### 编辑器

* `BaseEditor.Validate` 事件——Eremex 编辑器现在支持 `Validate` 事件，使您可以实现自定义验证规则。
* `BaseEditor.DoValidate` 方法——允许您强制触发验证。

#### 通用类

- `ImageLoader`——新的 `Eremex.AvaloniaUI.Controls.Utils.ImageLoader` 类提供了通过 URI 从资源中加载图像（SVG、PNG 等）的方法。


### 重大变更


#### DataGridControl 和 TreeListControl
* `ColumnBase.HeaderContentTemplate` 属性重命名为 `HeaderTemplate`
* `ColumnBase.HeaderHorizontalContentAlignment` 属性重命名为 `HeaderHorizontalAlignment`
* `ColumnBase.HeaderVerticalContentAlignment` 属性重命名为 `HeaderVerticalAlignment`

#### DataGridControl
* `GetRowIndexBySourceIndex` 方法重命名为 `GetRowIndexBySourceItemIndex`
* `GetRowIndexByVisibleIndex` 方法重命名为 `GetRowIndexByVisibleRowIndex`
* `GetSourceIndexByRowIndex` 方法重命名为 `GetSourceItemIndexByRowIndex`
* `GetSourceIndexByVisibleIndex` 方法重命名为 `GetSourceItemIndexByVisibleRowIndex`
* `GetVisibleIndexByRowIndex` 方法重命名为 `GetVisibleRowIndexByRowIndex`
* `GetVisibleIndexBySourceIndex` 方法重命名为 `GetVisibleRowIndexBySourceItemIndex`
* `GetItemByVisibleIndex` 方法重命名为 `GetSourceItemByVisibleRowIndex`
* `GetItemByRowIndex` 方法重命名为 `GetSourceItemByRowIndex`
* `CustomColumnSort` 事件：事件参数 `SourceIndex1` 重命名为 `SourceItemIndex1`。事件参数 `SourceIndex2` 重命名为 `SourceItemIndex2`

#### Docking

* 附加属性 `TabbedGroup.TabHeader` 替换为 `DockPane.TabHeader` 属性
* 附加属性 `TabbedGroup.TabHeaderTemplate` 替换为 `DockPane.TabHeaderTemplate` 属性
* 附加属性 `TabbedGroup.TabGlyph` 替换为 `DockPane.TabGlyph` 属性
* 附加属性 `TabbedGroup.TabGlyphSize` 替换为 `DockPane.TabGlyphSize` 属性
* `TabbedGroup.ShowTabPanelForSinglePage` 重命名为 `ShowTabStripForSingleChild`
* `DockManager.Hide` 方法重命名为 `DockManager.AutoHide`

#### 通用类
* `SerializationHelper` 类重命名为 `SerializationManager`

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
