---
title: 导出
order: 1500
seealso: []
---

# 导出

DataGrid 控件支持将数据导出为以下格式：

- XLSX（Microsoft Excel）
- PDF
- CSV
- 图像格式（PNG、JPEG、SVG 和 WebP）

!!! note 

    向 XLSX、PDF 及图像格式导出数据的功能是在 **Eremex.DocumentProcessing** 库中实现的。请确保您的项目中已包含该库,以便使用导出功能。


## 导出为 XLSX 格式

Excel 导出引擎具有数据感知能力,可在输出的 XLSX 文档中保留网格的数据整理设置,包括：

- 行分组
- 值格式化
- 数据排序

<!-- TODO
 - Data filtering settings 
-->


导出数据后,您可以在 Microsoft Excel 或其他电子表格处理应用程序中处理和分析数据。

![datagrid-export-result](../../images/datagrid-export-result.png)

!!! note

    使用单元格模板（`GridColumn.CellTemplate`）实现的单元格格式化不会被导出。

使用以下方法将控件数据导出为 XLSX 格式：

- <code>DataGridControl.ExportToXlsx(string fileName, XlsxExportOptions? options = null)</code> — 将数据导出到文件。

- <code>DataGridControl.ExportToXlsx(Stream stream, XlsxExportOptions? options = null)</code> — 将数据导出到流。

可选参数 `options`（类型为 `XlsxExportOptions`）用于自定义导出设置。`XlsxExportOptions` 类公开以下成员：

- `ExportProgress` 事件 — 在数据导出过程中反复触发。该事件的 `ExportProgressEventArgs.ProgressPercentage` 参数以百分比（0 到 100）表示进度。您可以使用此事件以自定义方式向用户展示导出进度。
- `AllowFixedColumnHeaderPanel` 属性(默认值为 `true`) — 指定导出文档中列标题面板是否保持固定在顶部。

- `ApplyFormattingToEntireColumn` — 指定单元格格式化是应用于整列还是应用于输出文档中的单个单元格。

- `AllowGrouping` 属性(默认值为 `true`) — 指定是否导出分组行及分组层次结构。如果 `AllowGrouping` 为 `false`,则仅导出数据行。

- `DocumentCulture` — 一个自定义的 `CultureInfo` 对象,用于确定输出文档中数值和日期时间值的格式化规则。

    如果未指定 `DocumentCulture` 属性,导出引擎将使用应用程序的当前区域性设置。

- `ShowBands` 属性(默认值为 `null`) — 指定是否在导出内容中包含控件的[分区（bands）](bands.md)。

    如果 `ShowBands` 为 `null`,则使用控件的 `DataGridControl.ShowBands` 属性所指定的设置。

- `ShowColumnHeaders` 属性(默认值为 `null`) — 指定是否在导出内容中包含列标题面板。

    如果 `ShowColumnHeaders` 为 `null`,则使用控件的 `DataGridControl.ShowColumnHeaders` 属性所指定的设置。

- `ShowHorizontalLines` — 指定输出文档中单元格之间的水平线是否可见。

- `ShowVerticalLines` — 指定输出文档中单元格之间的垂直线是否可见。

- `TextExportMode` 属性 — 单元格值的**默认**导出模式。

    可用选项包括： 

    - `TextExportMode.Value` — 导出单元格值。如果 DataGrid 控件中的单元格值已被格式化,导出引擎将尝试在输出文档中对导出的值应用相匹配的格式。
    - `TextExportMode.Text` — 导出单元格的显示文本。如果 DataGrid 控件中的单元格值已被格式化,则导出其格式化后的字符串表示形式。

    您可以使用 `GridColumn.TextExportMode` 属性为单个列覆盖 `XlsxExportOptions.TextExportMode` 设置。

    !!! note

        导出引擎仅考虑通过 `GridColumn.EditorProperties` 属性应用的单元格格式化。例如：

        ```
        <mxdg:GridColumn Width="*" FieldName="Salary">
            <mxdg:GridColumn.EditorProperties>
                <mxe:TextEditorProperties DisplayFormatString="c"/>
            </mxdg:GridColumn.EditorProperties>
        </mxdg:GridColumn>
        ```

        通过其他方式(例如使用 `GridColumn.CellTemplate`)应用的单元格格式化在数据导出时会被忽略。

        


<!-- TODO
image with data grouping export
 -->




## 导出为 PDF 格式

PDF 渲染引擎遵循所见即所得（WYSIWYG）理念,在输出文档中保留网格元素的布局。


![grid-export-to-pdf](../../images/grid-export-to-pdf.png)


使用以下方法将控件数据导出为 PDF 格式：

- <code>DataGridControl.ExportToPdf(string fileName, PageExportOptions? options = null)</code> — 将数据导出到文件。

- <code>DataGridControl.ExportToPdf(Stream stream, PageExportOptions? options = null)</code> — 将数据导出到流。

可选参数 `options`(类型为 `PageExportOptions`)用于自定义导出设置。`PageExportOptions` 类公开以下成员：

- `PageExportOptions.ExportProgress` 事件 — 在数据导出过程中反复触发。该事件的 `ExportProgressEventArgs.ProgressPercentage` 参数以百分比(0 到 100)表示进度。您可以使用此事件以自定义方式向用户展示导出进度。

- `PageExportOptions.FitToPageWidth`(默认值为 `false`) — 指定网格列是否拉伸以适应纸张宽度。

- `PageExportOptions.Landscape`(默认值为 `false`) — 指定页面方向是水平(`Landscape`)还是垂直(`Portrait`)。

- `PageExportOptions.Margins`(默认值为 `72,72,72,72`) — 页面边距,单位为点。1 点 = 1/72 英寸。

- `PageExportOptions.PageRange` — 一个字符串,指定要导出的页面范围。您可以使用以下表示法来指定输出页面范围：

    - "1" — 导出第 1 页。
    - "1, 4, 8-10" — 导出第 1、4 页以及第 8 到 10 页。
    <!-- - "7-" — Exports from page 7 to the end. -->

    `PageRange` 属性的默认值为空字符串,表示导出所有页面。

- `PageExportOptions.PaperKind`(默认值为 `A4`) — 纸张大小。

- `PageExportOptions.ShowBands` 属性(默认值为 `null`) — 指定是否在导出内容中包含控件的[分区（bands）](bands.md)。

    如果 `ShowBands` 为 `null`,则使用控件的 `DataGridControl.ShowBands` 属性所指定的设置。

- `PageExportOptions.ShowColumnHeaders` 属性(默认值为 `null`) — 指定是否在导出内容中包含列标题面板。

    如果 `ShowColumnHeaders` 为 `null`,则使用控件的 `DataGridControl.ShowColumnHeaders` 属性所指定的设置。 
    

## 导出为 CSV 格式

DataGrid 控件提供 `ExportToCsv` 方法,用于将数据导出为 CSV 格式。CSV(comma-separated values,逗号分隔值)是一种用于存储表格数据的纯文本数据格式。每条记录都作为一行文本导出,其中的值由分隔符(通常是逗号)分隔。

`ExportToCsv` 方法提供以下重载：

- <code>DataGridControl.ExportToCsv(string filePath, TextExportMode textExportNode = TextExportMode.Text, string separator = ",", bool quoteStringsWithSeparators = true)</code> — 将数据导出到文件。

- <code>DataGridControl.ExportToCsv(Stream stream, TextExportMode textExportMode = TextExportMode.Text, string separator = ",", bool quoteStringsWithSeparators = true)</code> — 将数据导出到流。

以下方法参数可用于自定义导出选项：

- `textExportMode` — 单元格值的**默认**导出模式。

    可用选项包括： 

    - `TextExportMode.Value` — 导出单元格值。应用于单元格值的数据格式不会被导出。
    - `TextExportMode.Text` — 导出单元格的显示文本。如果 DataGrid 控件中的单元格值已被格式化,则导出其格式化后的字符串表示形式。

        !!! note

            导出引擎仅考虑通过 `GridColumn.EditorProperties` 属性应用的单元格格式化。

    您可以使用 `GridColumn.TextExportMode` 属性为单个列覆盖方法的 `textExportMode` 参数。 


- `separator` — 一个字符串,指定用于在输出文档中分隔单元格值的分隔符。默认分隔符是逗号(",")。

- `quoteStringsWithSeparators` — 指定当值包含指定的 `separator` 时,是否用引号(")将其括起来。



## 导出为图像格式

DataGrid 控件的 `ExportToImages` 方法会执行分页导出,导出为图像格式(PNG、JPEG、SVG 或 WebP)。如果控件的内容过大而无法容纳在单页中,该方法会将数据分页(拆分为多页),并将每一页导出为单独的图像。

![treelist-export-to-images](../../images/treelist-export-to-images.png)

目标页面的格式和大小由传递给该方法的参数定义。`ExportToImages` 方法使用与 `ExportToPdf` 方法相同的分页机制。

- <code>DataGridControl.ExportToImages(string directory, string fileNameFormat, ImageExportOptions? options = null)</code>

``` cs
using Eremex.AvaloniaUI.Controls.DataControl;
using Eremex.DocumentProcessing.Printing;

ImageExportOptions options = new ImageExportOptions();
options.Format = MxImageFormat.Svg;
options.FitToPageWidth = false;
options.PaperKind = PaperKind.A4;
options.Margins = new Margins(36, 36, 36, 36);
options.PageRange = "1-2";
dataGrid.ExportToImages(@"c:\images\", "img{0}.svg", options);
```

使用 `ExportToImages` 方法的参数可自定义页面设置、输出图像格式和文件名模式。

- `directory` — 指定用于保存图像文件的目录。如果指定的目录不存在,将引发异常。

- `fileNameFormat` — 指定输出图像文件的命名模式。

    `fileNameFormat` 的值应在需要插入生成文件名中页码的位置包含 `{0}` 占位符。您可以使用[标准](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings)和[自定义数字格式说明符](https://learn.microsoft.com/en-us/dotnet/standard/base-types/custom-numeric-format-strings)来格式化页码。以下是 `fileNameFormat` 值的示例：

    - "image{0}.png" — 生成类似 "image1.png"、"image2.png" 等文件。
    - "image{0:D3}.svg"  — 生成类似 "image001.svg"、"image002.svg" 等文件。
    
可选参数 `options`(类型为 `ImageExportOptions`)用于自定义导出设置。`ImageExportOptions` 类公开以下成员：

- `ImageExportOptions.Format` — 输出图像格式(PNG、JPEG、SVG 或 WebP)。

- `ImageExportOptions.PageBorderColor` — 绘制在每个页面周围的边框颜色。
- `ImageExportOptions.PageBorderWidth`  — 绘制在每个页面周围的边框宽度。


- `PageExportOptions.ExportProgress` 事件 — 在数据导出过程中反复触发。该事件的 `ExportProgressEventArgs.ProgressPercentage` 参数以百分比(0 到 100)表示进度。您可以使用此事件以自定义方式向用户展示导出进度。


- `PageExportOptions.ShowBands` 属性(默认值为 `null`) — 指定是否在导出内容中包含控件的[分区（bands）](bands.md)。

    如果 `ShowBands` 为 `null`,则使用控件的 `DataGridControl.ShowBands` 属性所指定的设置。

- `PageExportOptions.ShowColumnHeaders` 属性(默认值为 `null`) — 指定是否在导出内容中包含列标题面板。

    如果 `ShowColumnHeaders` 为 `null`,则使用控件的 `DataGridControl.ShowColumnHeaders` 属性所指定的设置。 

- `PageExportOptions.FitToPageWidth`(默认值为 `false`) — 指定网格列是否拉伸以适应纸张宽度。

- `PageExportOptions.Landscape`(默认值为 `false`) — 指定页面方向是水平(`Landscape`)还是垂直(`Portrait`)。

- `PageExportOptions.Margins`(默认值为 `72,72,72,72`) — 页面边距,单位为点。1 点 = 1/72 英寸。


- `PageExportOptions.PageRange` — 一个字符串,指定要导出的页面范围。您可以使用以下表示法来指定输出页面范围：

    - "1" — 导出第 1 页。
    - "1, 4, 8-10" — 导出第 1、4 页以及第 8 到 10 页。
    - "7-" — 从第 7 页导出至末尾。

    `PageRange` 属性的默认值为空字符串,表示导出所有页面。

- `PageExportOptions.PaperKind`(默认值为 `A4`) — 纸张大小。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
