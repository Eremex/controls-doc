---
title: Export
order: 1500
seealso: []
---

# Export


The TreeList control can export data to the following formats:

- XLSX (Microsoft Excel)
- PDF
- CSV
- Image formats (PNG, JPEG, SVG, and WebP)

The TreeView control only supports data export to CSV format.

!!! note 

    The data export to XLSX, PDF and image formats is implemented in the **Eremex.DocumentProcessing** library. Ensure that this library in included in your project to use the export feature.


## Export to XLSX Format

The Excel export engine is data-aware, meaning it preserves the control's data shaping options in the output XLSX document, including:

- Node hierarchy
- Value formatting
- Data sorting

<!-- TODO
 - Data filtering settings 
-->


After data is exported, you can process and analyze it in Microsoft Excel or another worksheet processing application.

![treelist-export-result](../../images/treelist-export-result.png)

!!! note

    Cell formatting implemented using cell templates ([`TreeListColumn.CellTemplate`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md)) is not exported.

Use the following methods to export the control's data to XLSX format:

- <code>[TreeListControl.ExportToXlsx](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ExportToXlsx.md)(string fileName, XlsxExportOptions? options = null)</code> — Exports data to a file.

- <code>[TreeListControl.ExportToXlsx](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ExportToXlsx.md)(Stream stream, XlsxExportOptions? options = null)</code> — Exports data to a stream.

The optional `options` parameter (of type [`XlsxExportOptions`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions.md)) allows you to customize export settings. The [`XlsxExportOptions`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions.md) class exposes the following members:

- [`ExportProgress`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ExportOptions/ExportProgress.md) event — Fires repeatedly during data export. The event's [`ExportProgressEventArgs.ProgressPercentage`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ExportProgressEventArgs/ProgressPercentage.md) parameter indicates the progress as a percentage (0 to 100). You can use this event to display export progress to users in a customized way.
- [`AllowFixedColumnHeaderPanel`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/AllowFixedColumnHeaderPanel.md) property (default is `true`) — Specifies whether the column header panel remains fixed at the top in the exported document. 

- [`ApplyFormattingToEntireColumn`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/ApplyFormattingToEntireColumn.md) — Specifies whether cell formatting is applied to entire columns or individual cells in the output document.

- [`AllowGrouping`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/AllowGrouping.md) property (default is `true`) — Specifies whether the node hierarchy is exported. If [`AllowGrouping`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/AllowGrouping.md) is `false`, the node hierarchy is not stored in the output document.

- [`DocumentCulture`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/DocumentCulture.md) — A custom `CultureInfo` object that determines formatting rules for numeric and date-time values in the output document.

    If the [`DocumentCulture`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/DocumentCulture.md) property is not specified, the export engine uses the application's current culture.

- [`ShowBands`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/ShowBands.md) property (default is `null`) — Specifies whether the control's [bands](bands.md) are included in the export. 

    If [`ShowBands`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/ShowBands.md) is `null`, the setting is specified by the control's [`TreeListControl.ShowBands`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowBands.md) property. 

- [`ShowColumnHeaders`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ExportOptions/ShowColumnHeaders.md) property (default is `null`) — Specifies whether the column header panel is included in the export. 

    If `ShowColumnHeaders` is `null`, the setting is specified by the control's [`TreeListControl.ShowColumnHeaders`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowColumnHeaders.md) property. 

- [`ShowHorizontalLines`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/ShowHorizontalLines.md) — Specifies whether horizontal lines between cells are visible in the output document.

- [`ShowVerticalLines`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/ShowVerticalLines.md) — Specifies whether vertical lines between cells are visible in the output document.

- [`TextExportMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/TextExportMode.md) property — The **default** export mode of cell values. 

    Available options include: 

    - [`TextExportMode.Value`](../../API/Eremex.AvaloniaUI.Controls.DataControl/TextExportMode.md) — Exports cell values. If cell values are formatted in the TreeList control, the export engine attempts to apply matching formatting to the exported values in the output document.
    - [`TextExportMode.Text`](../../API/Eremex.AvaloniaUI.Controls.DataControl/TextExportMode.md) — Exports cell display text. If cell values are formatted in the TreeList control, the formatted string representation is exported.

    You can use the [`TreeListColumn.TextExportMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/TextExportMode.md) property to override the [`XlsxExportOptions.TextExportMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/XlsxExportOptions/TextExportMode.md) setting for individual columns.

    !!! note

        The export engine only takes into account cell formatting applied using the [`TreeListColumn.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md) property. For example:

        ```
        <mxtl:TreeListColumn Width="*" FieldName="Salary">
            <mxtl:TreeListColumn.EditorProperties>
                <mxe:TextEditorProperties DisplayFormatString="c"/>
            </mxtl:TreeListColumn.EditorProperties>
        </mxtl:TreeListColumn>
        ```

        Cell formatting applied using other approaches (for instance, with [`TreeListColumn.CellTemplate`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/CellTemplate.md)) is ignored during data export.


## Export to PDF Format

The PDF rendering engine follows the WYSIWYG concept, which retains the layout of TreeList elements in the output document. 


![treelist-export-to-pdf](../../images/treelist-export-to-pdf.png)


Use the following methods to export the control's data to PDF format:

- <code>[TreeListControl.ExportToPdf](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ExportToPdf.md)(string fileName, PageExportOptions? options = null)</code> — Exports data to a file.

- <code>[TreeListControl.ExportToPdf](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ExportToPdf.md)(Stream stream, PageExportOptions? options = null)</code> — Exports data to a stream.

The optional `options` parameter (of type [`PageExportOptions`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions.md)) allows you to customize export settings. The [`PageExportOptions`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions.md) class exposes the following members:

- [`PageExportOptions.ExportProgress`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ExportOptions/ExportProgress.md) event — Fires repeatedly during data export. The event's [`ExportProgressEventArgs.ProgressPercentage`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ExportProgressEventArgs/ProgressPercentage.md) parameter indicates the progress as a percentage (0 to 100). You can use this event to display export progress to users in a customized way.

- [`PageExportOptions.FitToPageWidth`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/FitToPageWidth.md) (default is `false`) — Specifies whether treelist columns are stretched to fit the paper width.

- [`PageExportOptions.Landscape`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/Landscape.md) (default is `false`) — Specifies whether the page orientation is horizontal ([`Landscape`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/Landscape.md)) or vertical (`Portrait`).

- [`PageExportOptions.Margins`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/Margins.md) (default is `72,72,72,72`) — The page margins, in points. 1 point = 1/72 inch.

- [`PageExportOptions.PageRange`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/PageRange.md) — A string that specifies the range of pages to be exported. You can use the following notations to specify the output page range:

    - "1" — Exports page 1.
    - "1, 4, 8-10" — Exports pages 1, 4, and 8 through 10.
    <!-- - "7-" — Exports from page 7 to the end. -->

    The default value of the [`PageRange`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/PageRange.md) property is an empty string, which exports all pages.

- [`PageExportOptions.PaperKind`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/PaperKind.md) (default is `A4`) — The paper size.

- [`PageExportOptions.ShowBands`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/ShowBands.md) property (default is `null`) — Specifies whether the control's [bands](bands.md) are included in the export. 

    If [`ShowBands`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/ShowBands.md) is `null`, the setting is specified by the control's [`TreeListControl.ShowBands`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowBands.md) property. 

- [`PageExportOptions.ShowColumnHeaders`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ExportOptions/ShowColumnHeaders.md) property (default is `null`) — Specifies whether the column header panel is included in the export. 

    If `ShowColumnHeaders` is `null`, the setting is specified by the control's [`TreeListControl.ShowColumnHeaders`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowColumnHeaders.md) property.  
    

## Export to CSV Format

The TreeList and TreeView controls provide the [`ExportToCsv`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ExportToCsv.md) method to export data to CSV format. CSV (comma-separated values) is a plain text data format to store tabular data. Each record is exported as a text line, in which values are delimited by a separator (typically, a comma).

The following [`ExportToCsv`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ExportToCsv.md) method overloads are available:

- <code>[DataControlBase.ExportToCsv](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ExportToCsv.md)(string filePath, TextExportMode textExportNode = TextExportMode.Text, string separator = ",", bool quoteStringsWithSeparators = true)</code> — Exports data to a file.

- <code>[DataControlBase.ExportToCsv](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ExportToCsv.md)(Stream stream, TextExportMode textExportMode = TextExportMode.Text, string separator = ",", bool quoteStringsWithSeparators = true)</code> — Exports data to a stream.

The following method parameters allow you to customize export options:

- `textExportMode` — The **default** export mode of cell values. 

    Available options include: 

    - [`TextExportMode.Value`](../../API/Eremex.AvaloniaUI.Controls.DataControl/TextExportMode.md) — Exports cell values. Data formats applied to cell values are not exported.
    - [`TextExportMode.Text`](../../API/Eremex.AvaloniaUI.Controls.DataControl/TextExportMode.md) — Exports cell display text. If cell values are formatted in the control, the formatted string representation is exported.

        !!! note

            The export engine only takes into account cell formatting applied using the [`EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md) properties ([`TreeListColumn.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/EditorProperties.md) and [`TreeViewControl.EditorProperties`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/EditorProperties.md)).

    For the TreeList control, you can use the [`TreeListColumn.TextExportMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/TextExportMode.md) property to override the method's `textExportMode` parameter for individual columns. 


- `separator` — A string that specified the separator used to delimit cell values in the output document. The default separator is a comma (",").

- `quoteStringsWithSeparators` — Specifies whether to wrap values in quotes (") if they contain the specified `separator`.



## Export to Image Formats

The TreeList control's [`ExportToImages`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ExportToImages.md) method performs a paginated export to an image format (PNG, JPEG, SVG, or WebP). If the control's content is too large to fit a single page, the method paginates the data (splits it into pages) and exports each page as a separate image. 

![treelist-export-to-images](../../images/treelist-export-to-images.png)

The target page's format and size are defined by a parameter passed to the method. The [`ExportToImages`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ExportToImages.md) method uses the same pagination mechanism as the [`ExportToPdf`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ExportToPdf.md) method.

- <code>[TreeListControl.ExportToImages](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ExportToImages.md)(string directory, string fileNameFormat, ImageExportOptions? options = null)</code>

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


Use the [`ExportToImages`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ExportToImages.md) method's parameters to customize the page settings, output image format, and file name pattern.

- `directory` — Specifies the directory in which to save image files. An exception is raised if the specified directory does not exist.

- `fileNameFormat` — Specifies file naming pattern for the output image files. 

    The `fileNameFormat` value should include the `{0}` placeholder at the position where you need to insert a page number in the generated file names. You can format the page number using the [standard](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings) and [custom numeric format specifiers](https://learn.microsoft.com/en-us/dotnet/standard/base-types/custom-numeric-format-strings). Below are examples of `fileNameFormat` values:

    - "image{0}.png" — Produces files like "image1.png", "image2.png", and so on.
    - "image{0:D3}.svg"  — Produces files like "image001.svg", "image002.svg", and so on.
    
The optional `options` parameter (of type [`ImageExportOptions`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ImageExportOptions.md)) allows you to customize export settings. The [`ImageExportOptions`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ImageExportOptions.md) class exposes the following members:

- [`ImageExportOptions.Format`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ImageExportOptions/Format.md) — The output image format (PNG, JPEG, SVG, or WebP).

- [`ImageExportOptions.PageBorderColor`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ImageExportOptions/PageBorderColor.md) — The color of the border drawn around each page.
- [`ImageExportOptions.PageBorderWidth`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ImageExportOptions/PageBorderWidth.md)  — The width of the border drawn around each page.


- [`PageExportOptions.ExportProgress`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ExportOptions/ExportProgress.md) event — Fires repeatedly during data export. The event's [`ExportProgressEventArgs.ProgressPercentage`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ExportProgressEventArgs/ProgressPercentage.md) parameter indicates the progress as a percentage (0 to 100). You can use this event to display export progress to users in a customized way.


- [`PageExportOptions.ShowBands`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/ShowBands.md) property (default is `null`) — Specifies whether the control's [bands](bands.md) are included in the export. 

    If [`ShowBands`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/ShowBands.md) is `null`, the setting is specified by the control's [`TreeListControl.ShowBands`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowBands.md) property. 

- [`PageExportOptions.ShowColumnHeaders`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ExportOptions/ShowColumnHeaders.md) property (default is `null`) — Specifies whether the column header panel is included in the export. 

    If `ShowColumnHeaders` is `null`, the setting is specified by the control's [`TreeListControl.ShowColumnHeaders`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/ShowColumnHeaders.md) property.  

- [`PageExportOptions.FitToPageWidth`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/FitToPageWidth.md) (default is `false`) — Specifies whether treelist columns are stretched to fit the paper width.

- [`PageExportOptions.Landscape`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/Landscape.md) (default is `false`) — Specifies whether the page orientation is horizontal ([`Landscape`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/Landscape.md)) or vertical (`Portrait`).

- [`PageExportOptions.Margins`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/Margins.md) (default is `72,72,72,72`) — The page margins, in points. 1 point = 1/72 inch.


- [`PageExportOptions.PageRange`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/PageRange.md) — A string that specifies the range of pages to be exported. You can use the following notations to specify the output page range:

    - "1" — Exports page 1.
    - "1, 4, 8-10" — Exports pages 1, 4, and 8 through 10.
    - "7-" — Exports from page 7 to the end.

    The default value of the [`PageRange`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/PageRange.md) property is an empty string, which exports all pages.

- [`PageExportOptions.PaperKind`](../../API/Eremex.AvaloniaUI.Controls.DataControl/PageExportOptions/PaperKind.md) (default is `A4`) — The paper size.