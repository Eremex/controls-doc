---
title: 汇总
order: 49900
seealso: []
---

# 汇总 {#summaries}

[`DataGridControl`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl.md) 允许针对单元格值计算汇总（聚合函数）。支持两种类型的汇总：

- 总计汇总，针对所有行计算。
- 分组汇总，在数据分组时针对各行分组计算。

![grid-summaries](../../images/grid-summaries.png)

汇总计算的主要功能包括：

- 内置汇总函数：Sum、Min、Max、Count 和 Average。
- 运行时管理 — 用户可以单击页脚单元格中的 Σ 按钮添加汇总，或打开 Summary Editor 对话框执行高级汇总操作。
- 每列多个汇总 — 每一列可以显示针对该列值计算的多个汇总。
- 跨列汇总 — 可以针对一列计算汇总，并在另一列中显示。
- 自定义汇总 — 可以处理 [`CustomSummary`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomSummary.md) 事件，按您自己的逻辑计算自定义聚合函数。
- 在 XLSX 和 PDF 导出中包含汇总。

## 总计汇总 {#total-summaries}

总计汇总针对所有行计算，并显示在控件的页脚中。

![grid-total-summaries](../../images/grid-total-summaries.png)

### 启用总计汇总 {#enable-total-summaries}

将 [`ShowTotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ShowTotalSummaries.md) 属性设置为 `true` 可显示汇总页脚，从而启用总计汇总计算。汇总页脚显示在 [`DataGridControl`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl.md) 底部、所有行的下方。该页脚最初处于隐藏状态。

```xml
<mxdg:DataGridControl x:Name="dataGrid" ShowTotalSummaries="True">...</mxdg:DataGridControl>
```

汇总页脚包含所有列的汇总单元格。如果启用了[用户汇总自定义](#user-summary-customizations)（默认启用），汇总单元格会包含 `Σ` 按钮，用于显示汇总菜单和汇总编辑器。

![grid-summaries-sigma-button](../../images/grid-summaries-sigma-button.png)

**相关 API**

- [`ShowTotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ShowTotalSummaries.md) — 获取或设置是否显示总计汇总页脚并启用总计汇总计算。
- [`TotalSummaryPanelMinHeight`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/TotalSummaryPanelMinHeight.md) — 获取或设置总计汇总页脚的最小高度。

### 定义总计汇总 {#define-total-summaries}

使用 [`TotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/TotalSummaries.md) 集合定义总计汇总。该集合中的项由 [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) 类封装。每个 [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) 对象指定要汇总的字段、汇总类型、显示结果的列以及其他设置。

```xml
xmlns:mxdc="clr-namespace:Eremex.AvaloniaUI.Controls.DataControl;assembly=Eremex.Avalonia.Controls"

<mxdg:DataGridControl x:Name="dataGrid" ShowTotalSummaries="True">
    <mxdg:DataGridControl.TotalSummaries>
        <mxdc:SummaryItem FieldName="Name" SummaryType="Count" />
        <mxdc:SummaryItem FieldName="SaleDate" SummaryType="Min" ShowInColumn="Total" />
        <mxdc:SummaryItem FieldName="SaleDate" SummaryType="Max" ShowInColumn="Total" />
        <mxdc:SummaryItem FieldName="Price" SummaryType="Min" />
        <mxdc:SummaryItem FieldName="Price" SummaryType="Max" />
        <mxdc:SummaryItem FieldName="Quantity" SummaryType="Average" />
        <mxdc:SummaryItem FieldName="Total" SummaryType="Sum" />
    </mxdg:DataGridControl.TotalSummaries>
</mxdg:DataGridControl>
```

**相关 API**

- [`TotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/TotalSummaries.md) — 提供对定义总计汇总的汇总项（[`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) 对象）集合的访问。
- [`SummaryItem.FieldName`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/FieldName.md) — 获取或设置其值用于计算汇总的数据字段的名称。
- [`SummaryItem.Name`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Name.md) — 获取或设置汇总项的名称，用于标识该汇总项。可以按名称从 `TotalSummaries` 集合中检索汇总项。
- [`SummaryItem.Tag`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Tag.md) — 获取或设置与此 `SummaryItem` 关联的自定义数据。
- [`SummaryItem.ShowInColumn`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/ShowInColumn.md) — 获取或设置显示汇总值的列的字段名。如果未设置此属性，汇总将显示在绑定到 `FieldName` 的列中。
- [`SummaryItem.SummaryType`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/SummaryType.md) — 获取或设置聚合函数的类型（`Sum`、`Min`、`Max`、`Count` 或 `Average`）。
- [`SummaryItem.Label`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Label.md) — 获取或设置要显示的自定义标签，用于代替默认汇总标签。默认汇总标签显示汇总函数的名称。如果汇总与另一列相关联（请参阅 [`ShowInColumn`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/ShowInColumn.md)），汇总标签还会显示绑定到 [`SummaryItem.FieldName`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/FieldName.md) 的列的标题。

    ![grid-summaries-labels](../../images/grid-summaries-labels.png)

## 分组汇总 {#group-summaries}

当数据按列分组时，分组汇总允许您针对各行分组计算聚合函数。分组汇总显示在分组页脚中。

![grid-group-summaries](../../images/grid-group-summaries.png)

### 启用分组汇总 {#enable-group-summaries}

将 [`ShowGroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ShowGroupSummaries.md) 属性设置为 `true` 可显示分组汇总页脚（最初处于隐藏状态），从而启用分组汇总计算。分组汇总页脚显示在所有行分组的下方。每个分组级别都有各自的页脚。

```xml
<mxdg:DataGridControl x:Name="dataGrid" ShowGroupSummaries="True">...</mxdg:DataGridControl>
```

**相关 API**

- [`ShowGroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ShowGroupSummaries.md) — 获取或设置是否显示用于显示分组汇总的分组页脚。
- [`GroupSummaryRowMinHeight`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GroupSummaryRowMinHeight.md) — 获取或设置分组页脚的最小高度。

### 定义分组汇总 {#define-group-summaries}

使用 [`GroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GroupSummaries.md) 集合定义分组汇总。与 [`TotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/TotalSummaries.md) 集合一样，[`GroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GroupSummaries.md) 集合中的项由 [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) 类表示。每个 [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) 对象指定要汇总的字段、汇总类型、显示结果的列以及其他设置。

```xml
<mxdg:DataGridControl x:Name="dataGrid" ShowGroupSummaries="True">
    <mxdg:DataGridControl.GroupSummaries>
        <mxdc:SummaryItem FieldName="OrderId" SummaryType="Count" />
        <mxdc:SummaryItem FieldName="Quantity" SummaryType="Sum" />
        <mxdc:SummaryItem FieldName="TotalPrice" SummaryType="Sum" />
        <mxdc:SummaryItem FieldName="TotalPrice" SummaryType="Average" />
    </mxdg:DataGridControl.GroupSummaries>
</mxdg:DataGridControl>
```

**相关 API**

- [`GroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GroupSummaries.md) — 提供对定义分组汇总的汇总项（[`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) 对象）集合的访问。
- [`SummaryItem.FieldName`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/FieldName.md) — 获取或设置其值用于计算汇总的数据字段的名称。
- [`SummaryItem.Name`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Name.md) — 获取或设置汇总项的名称，用于标识该汇总项。可以按名称从 `GroupSummaries` 集合中检索汇总项。
- [`SummaryItem.Tag`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Tag.md) — 获取或设置与此 `SummaryItem` 关联的自定义数据。
- [`SummaryItem.ShowInColumn`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/ShowInColumn.md) — 获取或设置显示汇总值的列的字段名。如果未设置此属性，汇总将显示在绑定到 `FieldName` 的列中。
- [`SummaryItem.SummaryType`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/SummaryType.md) — 获取或设置聚合函数的类型（`Sum`、`Min`、`Max`、`Count` 或 `Average`）。
- [`SummaryItem.Label`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Label.md) — 获取或设置要显示的自定义标签，用于代替默认汇总标签。默认汇总标签显示汇总函数的名称。如果汇总与另一列相关联（请参阅 [`ShowInColumn`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/ShowInColumn.md)），汇总标签还会显示绑定到 [`SummaryItem.FieldName`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/FieldName.md) 的列的标题。


## 用户汇总自定义 {#user-summary-customizations}

默认情况下，用户可以编辑汇总。在此模式下，汇总单元格会显示 `Σ` 按钮，用于打开汇总菜单：

![grid-summaries-summary-menu](../../images/grid-summaries-summary-menu.png)

用户可以使用此菜单：

- 通过切换汇总函数旁边的复选框来添加或删除汇总。

    ![grid-summaries-summary-menu-multiple-items](../../images/grid-summaries-summary-menu-multiple-items.png)

- 选择 `Customize` 打开 `Summary Editor` 对话框。

    ![grid-summaries-summary-editor](../../images/grid-summaries-summary-editor.png)

    在此对话框的 `Summaries` 选项卡中，用户可以创建跨列汇总（针对一列计算但显示在另一列中的汇总）。
    
    在 `Order` 选项卡中，用户可以更改现有汇总的显示顺序。

    ![grid-summaries-summary-editor-order-tab](../../images/grid-summaries-summary-editor-order-tab.png)


**相关 API**

- [`AllowEditingTotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/AllowEditingTotalSummaries.md) — 获取或设置用户是否可以编辑总计汇总。
- [`AllowEditingGroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/AllowEditingGroupSummaries.md) — 获取或设置用户是否可以编辑分组汇总。

这些属性只影响用户修改汇总的能力，不影响在代码中执行的汇总计算。



## 自定义汇总 {#custom-summaries}

自定义汇总允许您使用自己的逻辑计算聚合值。可以定义自定义总计汇总和自定义分组汇总。

要添加自定义汇总，请执行以下操作：

- 创建一个 [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) 对象，并将其 [`SummaryItem.SummaryType`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/SummaryType.md) 属性设置为 `Custom`。

    - 要计算自定义总计汇总，请将此 [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) 添加到 [`TotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/TotalSummaries.md) 集合。
    - 要计算自定义分组汇总，请将此 [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) 添加到 [`GroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GroupSummaries.md) 集合。

- 处理 [`CustomSummary`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomSummary.md) 事件，为此 [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) 手动计算值。

    设置 `e.SummaryValue` 事件参数以提供您的自定义结果。

    处理 [`CustomSummary`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomSummary.md) 事件时，使用 `e.RowIndexes` 集合遍历目标行。该集合中的项指定用于计算自定义汇总的行的[索引](rows.md#identify-and-get-rows)。计算自定义总计汇总时，索引指向 DataGrid 的所有行。计算自定义分组汇总时，会针对每个行分组引发 CustomSummary 事件，`e.RowIndexes` 集合中的索引指向每个分组内的行。

    当针对分组汇总触发 `CustomSummary` 事件时，事件的 [`IsGroupSummary`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridCustomSummaryEventArgs/IsGroupSummary.md) 参数返回 `true`，[`GroupRowIndex`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridCustomSummaryEventArgs/GroupRowIndex.md) 参数指定正在处理的分组行的[索引](rows.md#identify-and-get-rows)。
    
    !!! Tip "提示"
        
        行索引允许您在使用 DataGrid 的按行 API 时定位行（例如 [`DataGridControl.GetCellValue`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GetCellValue.md)）

### 示例 - 计算自定义总计汇总 {#example-calculate-a-custom-total-summary}

以下示例创建一个自定义总计汇总，用于计算金额超过 $1000 的订单数量。

![grid-summaries-custom-summary-example](../../images/grid-summaries-custom-summary-example.png)


```xml
<!-- XAML -->
<mxdg:DataGridControl x:Name="dataGrid" CustomSummary="OnCustomSummary">
    <mxdg:DataGridControl.TotalSummaries>
        <mxdc:SummaryItem FieldName="Total" SummaryType="Custom" Label="Count (Total > $1000)" />
    </mxdg:DataGridControl.TotalSummaries>
</mxdg:DataGridControl>
```

```csharp
// Code-behind
void OnCustomSummary(object sender, DataGridCustomSummaryEventArgs e)
{
    int largeOrdersCount = 0;
    foreach (int rowIndex in e.RowIndexes)
    {
        if ((decimal)dataGrid.GetCellValue(rowIndex, e.SummaryItem.FieldName) > 1000m)
            largeOrdersCount++;
    }
    e.SummaryValue = largeOrdersCount.ToString();
}
```

**相关 API**

- [`CustomSummary`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomSummary.md) — 在计算汇总值时发生。使用 [`SummaryValue`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridCustomSummaryEventArgs/SummaryValue.md) 事件参数提供自定义汇总值。


## 获取汇总值 {#get-summary-values}

可以使用以下方法在代码中获取已计算的汇总值：

- [`DataGridControl.GetTotalSummaryValue`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GetTotalSummaryValue.md) — 返回总计汇总的已计算值。
- [`DataGridControl.GetGroupSummaryValue`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GetGroupSummaryValue.md) — 返回特定分组行的分组汇总的已计算值。`rowIndex` 参数标识目标分组行的索引，该分组行的子行用于计算汇总。

```csharp
object? totalValue = dataGrid.GetTotalSummaryValue(summaryItem);

// 获取第一个行分组的汇总值
int rowIndex = -1; // 指向第一个分组行。
object? groupValue = dataGrid.GetGroupSummaryValue(rowIndex, summaryItem);
```

## 设置汇总项样式 {#style-summary-items}

DataGrid 控件允许您自定义汇总项的外观。为此，请为用于绘制 DataGrid 汇总项的专用可视控件设置样式。

### 目标可视控件类 {#target-visual-control-class}

`Eremex.AvaloniaUI.Controls.DataControl.Visuals.FooterCellItemControl`

每个 `FooterCellItemControl` 都以一个 `FooterCellItem` 对象作为其 DataContext。

### DataContext {#datacontext}

`Eremex.AvaloniaUI.Controls.DataControl.Visuals.FooterCellItem`

下面列出了 `FooterCellItem` 类的定义供您参考。创建自定义样式设置器和转换器时，可以绑定到汇总的属性（`FooterCellItem.FieldName`、`FooterCellItem.SummaryType`、`FooterCellItem.Value`、`FooterCellItem.Label` 和 `FooterCellItem.DisplayValue`）。请参阅[示例](#example-style-summary-items)。

```csharp
/// <summary>Represents a summary value displayed in a footer cell.</summary>
public partial class FooterCellItem : ViewModelBase
{
	/// <summary>Gets or sets the summary item's label.</summary>
	[ObservableProperty] string label = string.Empty;

	/// <summary>Gets or sets the formatted summary value displayed in the footer cell.</summary>
	[ObservableProperty] string displayValue = string.Empty;

	/// <summary>Gets or sets the type of the aggregate function the summary calculates.</summary>
	public SummaryItemType SummaryType { get; set; } = SummaryItemType.None;

	/// <summary>Gets or sets the summary value.</summary>
	public object Value { get; set; }

	/// <summary>Gets or sets the name of the data field whose values the summary calculates.</summary>
	public string FieldName { get; set; }
}
```

### 用于呈现汇总项的默认模板 {#default-template-to-render-summary-items}

以下代码显示了用于呈现汇总项的默认模板。您可以在 [`DeltaDesign` 视觉主题源代码](../themes/modify-control-themes.md#default-theme)中找到此模板。根据该模板中的信息创建样式选择器，以定位汇总项的特定元素。例如，名为 _Label_ 的 `TextBlock` 显示汇总项的标签，而名为 _DisplayValue_ 的 `TextBlock` 显示汇总值：

``` xml
<!-- DeltaDesign paint theme -->
xmlns:mxdcv="clr-namespace:Eremex.AvaloniaUI.Controls.DataControl.Visuals;assembly=Eremex.Avalonia.Controls"

<ControlTheme x:Key="{x:Type mxdcv:FooterCellItemControl}" TargetType="mxdcv:FooterCellItemControl">
    <Setter Property="Background" Value="Transparent" />
    <Setter Property="Padding" Value="{DynamicResource DataControlFooterPadding}" />
    
    <Setter Property="Template">
        <ControlTemplate TargetType="mxdcv:FooterCellItemControl">
            <DockPanel Margin="{TemplateBinding Padding}" Background="{TemplateBinding Background}">
                <TextBlock x:Name="Label"
                           Text="{Binding Label}"
                           DockPanel.Dock="Left"
                           TextTrimming="CharacterEllipsis"
                           HorizontalAlignment="Left"
                           mxc:TextBlockHelper.ShowTooltipWhenTrimming="True" />
                <TextBlock Text=" "/>
                <TextBlock x:Name="DisplayValue"
                           Text="{Binding DisplayValue}"
                           DockPanel.Dock="Right"
                           FontWeight="SemiBold"
                           TextTrimming="CharacterEllipsis"
                           HorizontalAlignment="Right"
                           mxc:TextBlockHelper.ShowTooltipWhenTrimming="True" />
            </DockPanel>
        </ControlTemplate>
    </Setter>
</ControlTheme>
```

### 示例 - 设置汇总项样式 {#example-style-summary-items}

以下代码修改 DataGrid 控件中 _Price_ 列两个汇总值的颜色。`Min` 汇总值显示为绿色，`Max` 汇总值显示为红色。

![datagrid-summaries-style-summaryitems](../../images/datagrid-summaries-style-summaryitems.png)

所创建的样式以 `FooterCellItemControl` 模板中的 _DisplayValue_ 文本块为目标，并使用自定义多值转换器根据汇总的属性（`FooterCellItem.FieldName` 和 `FooterCellItem.SummaryType`）选择前景色。

```xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"

xmlns:mxdcv="clr-namespace:Eremex.AvaloniaUI.Controls.DataControl.Visuals;assembly=Eremex.Avalonia.Controls"

<mxdg:DataGridControl.Styles>
    <Style Selector="mxdcv|FooterCellItemControl /template/ TextBlock#DisplayValue" x:DataType="mxdcv:FooterCellItem">
        <Setter Property="Foreground">
          <Setter.Value>
            <MultiBinding Converter="{views:DataGridSummaryTypeToForegroundConverter}">
              <Binding Path="FieldName" />
              <Binding Path="SummaryType" />
              <DynamicResourceExtension ResourceKey="Icons/Outline/Green"/>
              <DynamicResourceExtension ResourceKey="Icons/Outline/Red"/>
            </MultiBinding>
          </Setter.Value>
        </Setter>
      </Style>                
</mxdg:DataGridControl.Styles>
```

```csharp
public class DataGridSummaryTypeToForegroundConverter : MarkupExtension, IMultiValueConverter
{
    public object Convert(IList<object> values, Type targetType, object parameter, CultureInfo culture)
    {
        if (values.Count != 4)
            return null;

        if (values[0] is string fieldName && fieldName == "Price" && values[1] is SummaryItemType sumType)
        {
            if (sumType == SummaryItemType.Min)
                return values[2];
            else if (sumType == SummaryItemType.Max)
                return values[3];
        }

        return null;
    }

    public override object ProvideValue(IServiceProvider serviceProvider)
    {
        return this;
    }
}
```

完整代码请参阅[演示应用程序](../../index.md#demo-application)。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
