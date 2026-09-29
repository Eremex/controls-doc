---
title: 导出
order: 1500
seealso: []
---

# 导出


TreeList 可以将数据导出为以下格式:

- XLSX(Microsoft Excel)
- PDF
- CSV
- 图像格式(PNG、JPEG、SVG 和 WebP)

TreeView 仅支持将数据导出为 CSV 格式。

!!! note 

    数据导出为 XLSX、PDF 和图像格式的功能是在 **Eremex.DocumentProcessing** 库中实现的。请确保您的项目中包含此库,才能使用导出功能。


## 导出为 XLSX 格式

Excel 导出引擎具有数据感知能力,这意味着它会在输出的 XLSX 文档中保留控件的数据整形选项,包括:

- 节点层次结构
- 值格式
- 数据排序

<!-- TODO
 - Data filtering settings 
-->


导出数据后,您可以在 Microsoft Excel 或其他电子表格处理应用程序中对其进行处理和分析。

![treelist-export-result](../../images/treelist-export-result.png)

!!! note

    使用单元格模板(`TreeListColumn.CellTemplate`)实现的单元格格式不会被导出。

使用以下方法将控件的数据导出为 XLSX 格式:

- <code>TreeListControl.ExportToXlsx(string fileName, XlsxExportOptions? options = null)</code> — 将数据导出到文件。

- <code>TreeListControl.ExportToXlsx(Stream stream, XlsxExportOptions? options = null)</code> — 将数据导出到流。

可选的 `options` 参数(类型为 `XlsxExportOptions`)允许您自定义导出设置。`XlsxExportOptions` 类公开以下成员:

- `ExportProgress` 事件 — 在数据导出期间反复触发。该事件的 `ExportProgressEventArgs.ProgressPercentage` 参数以百分比形式(0 到 100)指示进度。您可以使用此事件以自定义方式向用户显示导出进度。
- `AllowFixedColumnHeaderPanel` 属性(默认为 `true`)— 指定在导出的文档中,列标题面板是否保持固定在顶部。

- `ApplyFormattingToEntireColumn` — 指定单元格格式是应用于输出文档中的整列,还是仅应用于单个单元格。

- `AllowGrouping` 属性(默认为 `true`)— 指定是否导出节点层次结构。如果 `AllowGrouping` 为 `false`,则输出文档中不会保存节点层次结构。

- `DocumentCulture` — 一个自定义的 `CultureInfo` 对象,用于确定输出文档中数值和日期时间值的格式化规则。

    如果未指定 `DocumentCulture` 属性,导出引擎将使用应用程序当前的区域性设置。

- `ShowBands` 属性(默认为 `null`)— 指定控件的[波段(bands)](bands.md)是否包含在导出结果中。

    如果 `ShowBands` 为 `null`,则该设置由控件的 `TreeListControl.ShowBands` 属性指定。

- `ShowColumnHeaders` 属性(默认为 `null`)— 指定列标题面板是否包含在导出结果中。

    如果 `ShowColumnHeaders` 为 `null`,则该设置由控件的 `TreeListControl.ShowColumnHeaders` 属性指定。

- `ShowHorizontalLines` — 指定输出文档中单元格之间的水平线是否可见。

- `ShowVerticalLines` — 指定输出文档中单元格之间的垂直线是否可见。

- `TextExportMode` 属性 — 单元格值的**默认**导出模式。

    可用选项包括:

    - `TextExportMode.Value` — 导出单元格值。如果单元格值在 TreeList 中经过格式化,导出引擎会尝试将匹配的格式应用于输出文档中导出的值。
    - `TextExportMode.Text` — 导出单元格的显示文本。如果单元格值在 TreeList 中经过格式化,则导出其格式化后的字符串表示形式。

    您可以使用 `TreeListColumn.TextExportMode` 属性为各个列覆盖 `XlsxExportOptions.TextExportMode` 设置。

    !!! note

        导出引擎仅考虑通过 `TreeListColumn.EditorProperties` 属性应用的单元格格式。例如:

        ```
        <mxtl:TreeListColumn Width="*" FieldName="Salary">
            <mxtl:TreeListColumn.EditorProperties>
                <mxe:TextEditorProperties DisplayFormatString="c"/>
            </mxtl:TreeListColumn.EditorProperties>
        </mxtl:TreeListColumn>
        ```

        通过其他方式(例如使用 `TreeListColumn.CellTemplate`)应用的单元格格式在数据导出期间会被忽略。


## 导出为 PDF 格式

PDF 渲染引擎遵循所见即所得(WYSIWYG)理念,在输出文档中保留 TreeList 元素的布局。


![treelist-export-to-pdf](../../images/treelist-export-to-pdf.png)


使用以下方法将控件的数据导出为 PDF 格式:

- <code>TreeListControl.ExportToPdf(string fileName, PageExportOptions? options = null)</code> — 将数据导出到文件。

- <code>TreeListControl.ExportToPdf(Stream stream, PageExportOptions? options = null)</code> — 将数据导出到流。

可选的 `options` 参数(类型为 `PageExportOptions`)允许您自定义导出设置。`PageExportOptions` 类公开以下成员:

- `PageExportOptions.ExportProgress` 事件 — 在数据导出期间反复触发。该事件的 `ExportProgressEventArgs.ProgressPercentage` 参数以百分比形式(0 到 100)指示进度。您可以使用此事件以自定义方式向用户显示导出进度。

- `PageExportOptions.FitToPageWidth`(默认为 `false`)— 指定 TreeList 的列是否被拉伸以适应纸张宽度。

- `PageExportOptions.Landscape`(默认为 `false`)— 指定页面方向是水平(`Landscape`)还是垂直(`Portrait`)。

- `PageExportOptions.Margins`(默认为 `72,72,72,72`)— 页边距,以磅为单位。1 磅 = 1/72 英寸。

- `PageExportOptions.PageRange` — 一个字符串,用于指定要导出的页面范围。您可以使用以下表示法来指定输出页面范围:

    - "1" — 导出第 1 页。
    - "1, 4, 8-10" — 导出第 1、4 页以及第 8 到 10 页。
    <!-- - "7-" — Exports from page 7 to the end. -->

    `PageRange` 属性的默认值为空字符串,表示导出所有页面。

- `PageExportOptions.PaperKind`(默认为 `A4`)— 纸张大小。

- `PageExportOptions.ShowBands` 属性(默认为 `null`)— 指定控件的[波段(bands)](bands.md)是否包含在导出结果中。

    如果 `ShowBands` 为 `null`,则该设置由控件的 `TreeListControl.ShowBands` 属性指定。

- `PageExportOptions.ShowColumnHeaders` 属性(默认为 `null`)— 指定列标题面板是否包含在导出结果中。

    如果 `ShowColumnHeaders` 为 `null`,则该设置由控件的 `TreeListControl.ShowColumnHeaders` 属性指定。
    

## 导出为 CSV 格式

TreeList 和 TreeView 提供 `ExportToCsv` 方法,用于将数据导出为 CSV 格式。CSV(逗号分隔值)是一种用于存储表格数据的纯文本数据格式。每条记录都会导出为一行文本,其中的值由分隔符(通常是逗号)分隔。

提供以下 `ExportToCsv` 方法重载:

- <code>DataControlBase.ExportToCsv(string filePath, TextExportMode textExportNode = TextExportMode.Text, string separator = ",", bool quoteStringsWithSeparators = true)</code> — 将数据导出到文件。

- <code>DataControlBase.ExportToCsv(Stream stream, TextExportMode textExportMode = TextExportMode.Text, string separator = ",", bool quoteStringsWithSeparators = true)</code> — 将数据导出到流。

以下方法参数允许您自定义导出选项:

- `textExportMode` — 单元格值的**默认**导出模式。

    可用选项包括:

    - `TextExportMode.Value` — 导出单元格值。不会导出应用于单元格值的数据格式。
    - `TextExportMode.Text` — 导出单元格的显示文本。如果单元格值在控件中经过格式化,则导出其格式化后的字符串表示形式。

        !!! note

            导出引擎仅考虑通过 `EditorProperties` 属性(`TreeListColumn.EditorProperties` 和 `TreeViewControl.EditorProperties`)应用的单元格格式。

    对于 TreeList,您可以使用 `TreeListColumn.TextExportMode` 属性为各个列覆盖方法的 `textExportMode` 参数。


- `separator` — 一个字符串,用于指定输出文档中分隔单元格值所使用的分隔符。默认分隔符为逗号(",")。

- `quoteStringsWithSeparators` — 指定当值中包含指定的 `separator` 时,是否将该值用引号(")括起来。



## 导出为图像格式

TreeList 的 `ExportToImages` 方法执行分页导出,导出为图像格式(PNG、JPEG、SVG 或 WebP)。如果控件的内容过大,无法容纳在单个页面中,该方法会对数据进行分页(将其拆分为多个页面),并将每个页面导出为一张单独的图像。

![treelist-export-to-images](../../images/treelist-export-to-images.png)

目标页面的格式和大小由传递给该方法的参数定义。`ExportToImages` 方法使用与 `ExportToPdf` 方法相同的分页机制。

- <code>TreeListControl.ExportToImages(string directory, string fileNameFormat, ImageExportOptions? options = null)</code>

``` cs
using Eremex.AvaloniaUI.Controls.DataControl;
using Eremex.DocumentProcessing.Printing;

ImageExportOptions options = new ImageExportOptions();
options.Format = MxImageFormat.Svg;
options.FitToPageWidth = false;
options.PaperKind = PaperKind.A4;
options.Margins = new Margins(36, 36, 36, 36);
options.PageRange = "1-2";
treeList.ExportToImages(@"c:\images\", "img{0}.svg", options);
```


使用 `ExportToImages` 方法的参数来自定义页面设置、输出图像格式和文件名模式。

- `directory` — 指定用于保存图像文件的目录。如果指定的目录不存在,将引发异常。

- `fileNameFormat` — 指定输出图像文件的文件命名模式。

    `fileNameFormat` 的值应在需要插入生成文件名中页码的位置包含 `{0}` 占位符。您可以使用[标准](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings)和[自定义数字格式说明符](https://learn.microsoft.com/en-us/dotnet/standard/base-types/custom-numeric-format-strings)来设置页码的格式。以下是 `fileNameFormat` 值的示例:

    - "image{0}.png" — 生成诸如 "image1.png"、"image2.png" 等文件。
    - "image{0:D3}.svg"  — 生成诸如 "image001.svg"、"image002.svg" 等文件。
    
可选的 `options` 参数(类型为 `ImageExportOptions`)允许您自定义导出设置。`ImageExportOptions` 类公开以下成员:

- `ImageExportOptions.Format` — 输出图像格式(PNG、JPEG、SVG 或 WebP)。

- `ImageExportOptions.PageBorderColor` — 在每个页面周围绘制的边框颜色。
- `ImageExportOptions.PageBorderWidth`  — 在每个页面周围绘制的边框宽度。


- `PageExportOptions.ExportProgress` 事件 — 在数据导出期间反复触发。该事件的 `ExportProgressEventArgs.ProgressPercentage` 参数以百分比形式(0 到 100)指示进度。您可以使用此事件以自定义方式向用户显示导出进度。


- `PageExportOptions.ShowBands` 属性(默认为 `null`)— 指定控件的[波段(bands)](bands.md)是否包含在导出结果中。

    如果 `ShowBands` 为 `null`,则该设置由控件的 `TreeListControl.ShowBands` 属性指定。

- `PageExportOptions.ShowColumnHeaders` 属性(默认为 `null`)— 指定列标题面板是否包含在导出结果中。

    如果 `ShowColumnHeaders` 为 `null`,则该设置由控件的 `TreeListControl.ShowColumnHeaders` 属性指定。

- `PageExportOptions.FitToPageWidth`(默认为 `false`)— 指定 TreeList 的列是否被拉伸以适应纸张宽度。

- `PageExportOptions.Landscape`(默认为 `false`)— 指定页面方向是水平(`Landscape`)还是垂直(`Portrait`)。

- `PageExportOptions.Margins`(默认为 `72,72,72,72`)— 页边距,以磅为单位。1 磅 = 1/72 英寸。


- `PageExportOptions.PageRange` — 一个字符串,用于指定要导出的页面范围。您可以使用以下表示法来指定输出页面范围:

    - "1" — 导出第 1 页。
    - "1, 4, 8-10" — 导出第 1、4 页以及第 8 到 10 页。
    - "7-" — 从第 7 页导出到末尾。

    `PageRange` 属性的默认值为空字符串,表示导出所有页面。

- `PageExportOptions.PaperKind`(默认为 `A4`)— 纸张大小。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
