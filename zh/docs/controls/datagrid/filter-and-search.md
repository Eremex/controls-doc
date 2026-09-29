---
title: 筛选和搜索
order: 50000
seealso: []
---

# 筛选和搜索

Data Grid 支持数据筛选和搜索功能,可帮助您查找包含特定文本的行。

## 列筛选器

用户可以使用筛选菜单来筛选网格列。
要打开某一列的筛选菜单,将鼠标悬停在该列的标题上,直到出现筛选按钮,然后点击该按钮。打开的筛选菜单包含该列中所有唯一值。在筛选菜单中选择一个项目,即可按该值筛选该列。


![grid-filtering-animation](../../images/grid-filtering-animation2.gif)

用户可以同时对多个列进行筛选。应用于多个列的筛选条件通过 AND 运算符进行组合。


### “List” 和 “Checked List” 显示模式

筛选菜单可以使用以下两种显示模式之一来呈现项目(列值)：

- `List`(默认) — 常规列表,一次只能选择一个项目。

    ![column-filtermenu-list](../../images/column-filtermenu-list.png)


- `CheckedList` — 带复选框的列表,允许用户同时选择多个项目。

    ![column-filtermenu-checkedlist](../../images/column-filtermenu-checkedlist.png)



您可以使用以下属性全局为所有列设置筛选菜单显示模式,或为单个列单独设置：

- `DataGridControl.ColumnFilterPopupMode`(默认值为 `List`) — 指定所有列筛选菜单的默认显示模式。此设置应用于其 `GridColumn.FilterPopupMode` 属性设置为 `null` 的列。

- `GridColumn.FilterPopupMode`(默认值为 `null`) — 为单个列指定筛选菜单显示模式。设置后,该属性会覆盖全局设置(`DataGridControl.ColumnFilterPopupMode`)。

以下示例将 `CheckedList` 显示模式应用于所有列,并将 `List` 显示模式应用于 _City_ 列。

``` cs
dataGrid.ColumnFilterPopupMode = Eremex.AvaloniaUI.Controls.DataControl.FilterPopupMode.CheckedList;
dataGrid.Columns["City"].FilterPopupMode = Eremex.AvaloniaUI.Controls.DataControl.FilterPopupMode.List;
```


### 筛选面板

应用筛选后,底部会出现筛选面板。它显示当前应用的筛选条件,并允许您临时禁用和清除筛选。

![grid-filterpanel](../../images/grid-filterpanel.png)

要了解如何以编程方式进行筛选,请参阅以下章节：

- [在代码中筛选](#在代码中筛选)


### 相关 API

**DataGrid 控件成员**

- `AllowColumnFiltering` — 获取或设置是否为所有列启用筛选按钮。您可以使用某列的 `ColumnBase.AllowColumnFiltering` 属性来为单个列覆盖全局设置。

    例如,要禁用除某一列之外所有列的筛选按钮,请将 `DataGridControl.AllowColumnFiltering` 属性设置为 `false`,并将目标列的 `ColumnBase.AllowColumnFiltering` 属性设置为 `true`。

- `ColumnFilterButtonDisplayMode` — 获取或设置筛选按钮是始终可见,还是仅在用户将鼠标悬停在列标题上时才出现(默认)。

- `ColumnFilterPopupMode` — 获取或设置所有列筛选菜单的默认显示模式(`List` 或 `CheckedList`)。使用某列的 `FilterPopupMode` 属性可为单个列覆盖此设置。

- `CustomColumnDisplayText` 事件 — 允许您为列值(包括筛选菜单和筛选面板中的值)提供自定义显示文本。当 `CustomColumnDisplayText` 事件针对筛选面板中的值触发时,该事件的 `SourceItemIndex` 参数返回 `-1`。

- `FilterPanelText` — 获取筛选面板中显示的筛选条件的文本表示形式。

- `FilterPanelDisplayMode` — 获取或设置筛选面板的可见性模式。可用选项包括： 

    - `Auto`(默认) — 当任意列应用了筛选条件时,筛选面板会出现。
    - `Never` — 筛选面板始终隐藏。

- `FilterString` — 获取或设置应用于控件的筛选条件。您可以使用此属性在[代码中构建筛选条件](#在代码中筛选)。

- `IsFilterEnabled` — 获取或设置筛选是否处于激活状态。

- `IsFilterPanelVisible` — 获取筛选面板当前是否可见。



**列成员**

 - `ColumnBase.AllowColumnFiltering` — 获取或设置当前列是否允许使用筛选按钮。要为所有列启用或禁用筛选按钮,请参阅 `DataGridControl.AllowColumnFiltering` 设置。`ColumnBase.AllowColumnFiltering` 选项允许您为单个列覆盖 `DataGridControl.AllowColumnFiltering` 设置。
 - `ColumnBase.ColumnFilterMode` — 获取或设置列数据的筛选方式。可用选项包括：

    - `Value`(默认) — 按底层值筛选列数据。
    - `DisplayText` — 按单元格显示文本筛选列数据。

<!-- TODO 
Example for ColumnFilterMode.DisplayText.
-->

- `ColumnBase.FilterPopupMode` — 获取或设置单个列的筛选菜单显示模式(`List` 或 `CheckedList`)。设置后,该属性会覆盖控件的 `ColumnFilterPopupMode` 属性。

 - `ColumnBase.IsFiltered` — 获取当前列是否已应用筛选。
 - `ColumnBase.RoundDateTimeForColumnFilter` — 获取或设置在为显示 DateTime 值的列构建筛选条件时,是否忽略 DateTime 值中的时间部分。此属性对使用列筛选菜单和[自动筛选行](#自动筛选行)创建的筛选条件生效。

<!-- TODO
Add screenshots for RoundDateTimeForColumnFilter
 -->
 

## 搜索面板

搜索面板可帮助用户根据行中包含的数据快速定位行。当用户在搜索面板中输入文本时,Data Grid 控件会显示包含所输入文本的行。

![grid-searchpanel](../../images/grid-searchpanel.png)

- 搜索功能不区分大小写。
- 数据搜索使用**包含（Contains）**比较运算符。
- 数据搜索会在所有列中进行。

将控件的 `SearchPanelDisplayMode` 属性(继承自 `DataControlBase` 类)设置为以下值之一,以启用搜索面板：

- `SearchPanelDisplayMode.Always` — 控件始终显示搜索面板。
- `SearchPanelDisplayMode.HotKey` — 当用户按下 CTRL+F 快捷键时,控件会显示搜索面板。按 ESC 键可清除搜索面板内容。再次按 ESC 键会关闭该面板。用户也可以从列标题的上下文菜单中激活搜索面板。



### 相关 API

- `DataControlBase.IsSearchPanelVisible` — 获取搜索面板当前是否可见。
- `DataControlBase.SearchPanelHighlightResults` — 指定是否在找到的行中高亮显示搜索文本。该属性的默认值为 `true`。
- `DataControlBase.SearchText` — 获取或设置搜索文本。您可以为此属性赋值,以在代码中筛选控件。即使搜索面板处于隐藏或禁用状态(`SearchPanelDisplayMode` 属性设置为 `SearchPanelDisplayMode.Never`),此筛选功能仍受支持。
- `DataControlBase.ShowSearchPanelCloseButton` — 允许您隐藏搜索面板内置的关闭按钮。

### 示例
以下代码启用了搜索面板。使用 `SearchText` 属性来设置搜索文本。

``` csharp
dataGrid.SearchPanelDisplayMode = SearchPanelDisplayMode.Always;
dataGrid.SearchText = "search";
```

## 自动筛选行

自动筛选行是显示在所有网格行上方的特殊行。它允许用户在其单元格中输入文本,以按相应列筛选数据。

![grid-autofilterrow](../../images/grid-autofilterrow.png)

- 筛选功能不区分大小写。

### 启用自动筛选行

将 `DataGridControl.ShowAutoFilterRow` 属性设置为 `true`。


### 启用运行时筛选运算符选择器

您可以允许用户在运行时为自动筛选行单元格选择筛选逻辑。启用此功能后,每个自动筛选行单元格中都会出现一个筛选运算符图标。用户可以点击该图标以打开下拉菜单并选择所需的运算符。

![autofilterrow-changecondition-runtime.gif](../../images/grid-autofilterrow-changecondition-runtime.gif)

使用以下属性启用筛选运算符选择器：

- `DataGridControl.ShowConditionInAutoFilterRow`(默认为 `false`) — 指定所有自动筛选行单元格(列)的筛选运算符选择器的默认可见性。 
- `ColumnBase.ShowConditionInAutoFilterRow` — 为单个列启用或禁用筛选运算符选择器。此属性会覆盖 `DataGridControl.ShowConditionInAutoFilterRow` 设置。

### 在代码中指定筛选运算符

使用 `ColumnBase.AutoFilterCondition` 属性,以编程方式为单个自动筛选行单元格(列)指定筛选运算符。支持以下筛选运算符：

- `Contains`(适用于字符串值) — 行值必须包含所输入的文本。
- `Default` — 默认模式。 

    - 对于 String 和 Object 数据类型,`Default` 等同于 `Contains` 选项。
    - 对于其他数据类型,`Default` 等同于 `Equals` 选项。

- `DoesNotContain`(适用于字符串值) — 行值不得包含所输入的文本。
- `DoesNotEqual` — 目标列中的行值不得与输入值匹配。
- `EndsWith`(适用于字符串值) — 行值必须以所输入的文本结尾。
- `Equals` — 行值必须与输入值匹配。
- `Greater` — 行值必须大于输入值。
- `GreaterOrEqual` — 行值必须大于或等于输入值。
- `Less` — 行值必须小于输入值。
- `LessOrEqual` — 行值必须小于或等于输入值。
- `StartsWith`(适用于字符串值) — 行值必须以所输入的文本开头。

### 指定筛选值

`ColumnBase.AutoFilterValue` 属性允许您在代码中为特定的自动筛选行单元格设置值。即使自动筛选行处于隐藏状态,您也可以使用 `ColumnBase.AutoFilterValue` 属性来筛选 Data Grid。

### 示例

以下代码激活自动筛选行,并显示 “Name” 列中值以 "M" 开头的行。

``` csharp
using Eremex.AvaloniaUI.Controls.DataControl;
using Eremex.AvaloniaUI.Controls.DataGrid;

dataGrid1.ShowAutoFilterRow = true;
GridColumn colName = dataGrid1.Columns["Name"];
colName.AutoFilterCondition = AutoFilterCondition.StartsWith;
colName.AutoFilterValue = "M";
```

## 使用事件动态筛选行

您可以处理 `CustomRowFilter` 事件,根据自定义条件隐藏特定行。

`CustomRowFilter` 事件会在以下情况下针对绑定项源中的每个项触发：

- 控件的项源发生更改。
- 控件的行被筛选(例如,使用搜索面板和自动筛选行)。
- 调用了控件的 `RefreshData` 方法。

使用 `SourceItemIndex` 事件参数来标识当前处理的项。要隐藏相应的行,请将 `Visible` 事件参数设置为 `false`。

### 示例 — 使用事件筛选行

在以下示例中,Data Grid 控件显示一个 _EmployeeInfo_ 对象列表。通过处理 `CustomRowFilter` 事件来实现自定义行筛选。行会根据 _EmployeeInfo.EmploymentType_ 属性的值被隐藏。

假设示例中包含一个用于启用和禁用自定义筛选的 “Enable Filter” 切换按钮。点击该按钮时,`ToggleButton.IsCheckedChanged` 事件处理程序会调用 `RefreshData` 方法,以刷新网格行并重新触发 `CustomRowFilter` 事件。

``` xml
<ToggleButton Name="btnEnableFilter" Content="Enable Filter" IsCheckedChanged="BtnEnableFilter_IsCheckedChanged" />

<mxdg:DataGridControl x:Name="dataGrid" Grid.Row="1" ItemsSource="{Binding Employees}" 
    CustomRowFilter="DataGrid_CustomRowFilter">
<!-- ... -->
```

``` cs
using Eremex.AvaloniaUI.Controls.DataGrid;

private void BtnEnableFilter_IsCheckedChanged(object sender, Avalonia.Interactivity.RoutedEventArgs e)
{
    dataGrid.RefreshData();
}

private void DataGrid_CustomRowFilter(object sender, DataGridCustomRowFilterEventArgs e)
{
    bool filterEnabled = btnEnableFilter.IsChecked == true;
    if (!filterEnabled)
        return;
    DataGridControl grid = sender as DataGridControl;
    IList<EmployeeInfo> dataSource = grid.ItemsSource as IList<EmployeeInfo>;
    EmployeeInfo employee = dataSource[e.SourceItemIndex];
    e.Visible = employee.EmploymentType != EmploymentType.Contract;
}
```


## 在代码中筛选

从 1.2 版开始,您可以使用 `DataGridControl.FilterString` 属性在代码中筛选控件数据。

``` cs
dataGrid.FilterString = "[FirstName] = 'Julia' && [Position] = 'Sales Representative'";
```

![grid-filterincode-2-filters-combined-result](../../images/grid-filterincode-2-filters-combined-result.png)

筛选字符串由多个独立的筛选表达式组成,这些表达式通过[逻辑运算符（AND 或 OR）](#逻辑运算符)进行组合。



### 清除和禁用筛选

- 要清除筛选,请将 `FilterString` 属性设置为 `null` 或空字符串。
- 要临时禁用筛选,请使用 `DataControlBase.IsFilterEnabled` 属性。

### 指定列

在筛选字符串中,列应通过其字段名并用方括号括起来进行引用。示例：

- `[FirstName]`
- `[Position]`

### 指定常量

- 数值常量必须使用常见的数字格式指定。示例： 

    - `500`、`0`
    - `10.314`、`.5` 
    - `12.0m`/`12.0M`、`12d`/`12D`、`12f`/`12F`
    - `-32.5`

- 字符串常量必须用单引号字符(`'`)括起来。要插入字面量 `'`,请使用 `''` 表示法。示例： 

    - `'Research and Development'`
    - `'Clair de lune'`
    - `'O''Neil'`

- DateTime 和 DateTimeOffset 常量必须用 `#` 字符括起来,并使用固定区域性（invariant culture）格式指定。示例：

    - `#2018-03-22#`
    - `#2018-03-22 13:18:51#`
    - `#2018-03-22 13:18:51.94944#`

- DateOnly 和 TimeOnly 常量必须用 `#!` 和 `!#` 字符串括起来。示例：

    - `#!2026-01-01!#`
    - `#!12:23:45!#`

- 布尔常量：
    - `true`、`True` 或 `TRUE` 
    - `false`、`False` 或 `FALSE`


### 逻辑运算符

您可以使用以下逻辑运算符来组合筛选字符串中的各个表达式：

- `&&`、`and`、`And` 或 `AND`
- `||`、`or`、`Or` 或 `OR`

``` cs
dataGrid.FilterString = "[Price] < 5 OR [Price] > 15";
```

### 运算符和函数

下表列出了可用于构建筛选表达式的运算符和函数：

| 运算符和函数 | 描述 | 示例 |
| --- | --- | --- |
| `=` 或 `==` | 等于 | `[Price] = 500` |
| `!=` 或 `<>` | 不等于 | `[Price] != 500` |
| `<` | 小于 | `[Price] < 700` |
| `>` | 大于 | `[Price] > 600` |
| `<=` | 小于或等于 | `[Price] <= 600` |
| `>=` | 大于或等于 | `[Price] >= 800` |
| `is null` | 选择 null 值 | `[Region] is null` |
| `is not null` | 选择非 null 值 | `[Region] is not null` |
| `IsNull` | 选择 null 值 | `IsNull([Region])` |
| `IsNullOrEmpty` | 选择 null 值和空字符串 | `IsNullOrEmpty([Region])` |
| `In` | 选择具有任意指定值的项目。 | `[City] In ('Beijing', 'Shenzhen', 'Chengdu')` |
| `Contains` | 选择包含指定字符串的项目。Contains 运算符不区分大小写。 | `Contains([Name], 'lan')` |
| `StartsWith` | 选择以指定字符串开头的项目。StartsWith 运算符不区分大小写。 | `StartsWith([Product], 'CPU')` |
| `EndsWith` | 选择以指定字符串结尾的项目。EndsWith 运算符不区分大小写。 | `EndsWith([Product], '9950X')` |
| `!`、`not`、`Not` 或 `NOT` | 取反运算符 | `!Contains([Maker], 'amd')` |

### 高级筛选表达式

您可以使用 `Eremex.AvaloniaUI.Controls.Data.Filtering.ExprStringBuilder` 类来创建高级筛选条件。这些筛选条件可以包括对操作数的运算、对受支持函数的调用等。要构建筛选条件,请使用 `ExprStringBuilder` 类的成员。

要获取筛选字符串,请调用结果 `ExprStringBuilder` 对象的 `ToString` 方法。然后,您可以将此筛选字符串赋值给目标控件的 `DataControlBase.FilterString` 属性。


``` cs
// [Price] * [Stock] > 5000m
// Note: All operands ([Price], [Stock] and '5000') must be of the same data type (e.g., decimal). Otherwise, the control will fail to evaluate the expression.
var filter = ExprStringBuilder.Property("Price").Multiply(ExprStringBuilder.Property("Stock")).GreaterThanValue(5000m);
var filterString = filter.ToString();
control.FilterString = filterString;
```

!!! Important

    目前,表达式操作数(列数据类型和常量)必须属于同一数据类型。目前不支持在同一表达式中使用不同的数据类型(例如 decimal 和 integer)。



``` cs 
// [PropertyA] IN (([PropertyB] + 2m) % 3.0, 'ABC', null)
var filterString = ExprStringBuilder.Property("PropertyA").In(ExprStringBuilder.Property("PropertyB").AddValue(2m) .ModuloValue(3d), ExprStringBuilder.Constant("ABC"), ExprStringBuilder.Null()).ToString();
control.FilterString = filterString;
```

### 指定枚举值

要在筛选字符串中指定枚举值,您需要使用 `Eremex.AvaloniaUI.Controls.Data.Filtering.ExprStringBuilder` 类来构建筛选条件。
`ExprStringBuilder.ToString` 方法允许您获取筛选字符串,并将其赋值给目标控件的 `FilterString` 属性。

在将筛选字符串赋值给目标控件之前,您还需要使用 `EnumProcessingHelper.RegisterEnum` 方法注册该枚举类型。

#### 示例 — 在筛选表达式中使用枚举值

以下两个示例针对 _EmploymentType_ 列创建筛选表达式。该列显示 _EmploymentKind_ 枚举值。

``` cs
public enum EmploymentKind
{
    [Display(Name = "Full Time")]
    FullTime,
    [Display(Name = "Part Time")]
    PartTime,
    Contract
}
```
##### 示例 1

下面的表达式使用 `ExprStringBuilder.EqualValue` 函数来选择 _EmploymentType_ 列等于 _EmploymentKind.Contract_ 的行。
请注意用于注册 _EmploymentKind_ 枚举的 `EnumProcessingHelper.RegisterEnum` 方法。

``` cs
using Eremex.AvaloniaUI.Controls.Data.Filtering;

EnumProcessingHelper.RegisterEnum(typeof(EmploymentKind));

// [EmploymentType] = 'Contract'
var filterString1 = ExprStringBuilder.Property("EmploymentType").EqualValue(EmploymentKind.Contract).ToString();
control.FilterString = filterString1;
```

![grid-filter-enumeration-example-equal](../../images/grid-filter-enumeration-example-equal.png)

##### 示例 2

以下表达式使用 `ExprStringBuilder.InValues` 函数生成 _In_ 运算符。此表达式检查 _EmploymentType_ 列是否等于 _EmploymentKind.FullTime_ 或 _EmploymentKind.PartTime_。

``` cs
// [EmploymentType] IN ('FullTime', 'PartTime')
var filterString2 = ExprStringBuilder.Property("EmploymentType").InValues(EmploymentKind.FullTime, EmploymentKind.PartTime).ToString();
control.FilterString = filterString2;
```

![grid-filter-enumeration-example-in](../../images/grid-filter-enumeration-example-in.png)


<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
