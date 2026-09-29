---
title: Export
order: 1500
seealso: []
---

# Export

The DataGrid control supports data export to the following formats:

- XLSX (Microsoft Excel)
- PDF
- CSV
- Image formats (PNG, JPEG, SVG, and WebP)

!!! note 

    The data export to XLSX, PDF and image formats is implemented in the **Eremex.DocumentProcessing** library. Ensure that this library in included in your project to use the export feature.


## Export to XLSX Format

The Excel export engine is data-aware, meaning it preserves the grid's data shaping options in the output XLSX document, including:

- Row grouping
- Value formatting
- Data sorting

<!-- TODO
 - Data filtering settings 
-->


After data is exported, you can process and analyze it in Microsoft Excel or another worksheet processing application.

![datagrid-export-result](../../images/datagrid-export-result.png)

!!! note

    Cell formatting implemented using cell templates (`GridColumn.CellTemplate`) is not exported.

Use the following methods to export the control's data to XLSX format:

- <code>DataGridControl.ExportToXlsx(string fileName, XlsxExportOptions? options = null)</code> — Exports data to a file.

- <code>DataGridControl.ExportToXlsx(Stream stream, XlsxExportOptions? options = null)</code> — Exports data to a stream.

The optional `options` parameter (of type `XlsxExportOptions`) allows you to customize export settings. The `XlsxExportOptions` class exposes the following members:

- `ExportProgress` event — Fires repeatedly during data export. The event's `ExportProgressEventArgs.ProgressPercentage` parameter indicates the progress as a percentage (0 to 100). You can use this event to display export progress to users in a customized way.
- `AllowFixedColumnHeaderPanel` property (default is `true`) — Specifies whether the column header panel remains fixed at the top in the exported document. 

- `ApplyFormattingToEntireColumn` — Specifies whether cell formatting is applied to entire columns or individual cells in the output document.

- `AllowGrouping` property (default is `true`) — Specifies whether group rows and the group hierarchy are exported. If `AllowGrouping` is `false`, data rows are only exported.

- `DocumentCulture` — A custom `CultureInfo` object that determines formatting rules for numeric and date-time values in the output document.

    If the `DocumentCulture` property is not specified, the export engine uses the application's current culture.

- `ShowBands` property (default is `null`) — Specifies whether the control's [bands](bands.md) are included in the export. 

    If `ShowBands` is `null`, the setting is specified by the control's `DataGridControl.ShowBands` property. 

- `ShowColumnHeaders` property (default is `null`) — Specifies whether the column header panel is included in the export. 

    If `ShowColumnHeaders` is `null`, the setting is specified by the control's `DataGridControl.ShowColumnHeaders` property. 

- `ShowHorizontalLines` — Specifies whether horizontal lines between cells are visible in the output document.

- `ShowVerticalLines` — Specifies whether vertical lines between cells are visible in the output document.

- `TextExportMode` property — The **default** export mode of cell values. 

    Available options include: 

    - `TextExportMode.Value` — Exports cell values. If cell values are formatted in the DataGrid control, the export engine attempts to apply matching formatting to the exported values in the output document.
    - `TextExportMode.Text` — Exports cell display text. If cell values are formatted in the DataGrid control, the formatted string representation is exported.

    You can use the `GridColumn.TextExportMode` property to override the `XlsxExportOptions.TextExportMode` setting for individual columns.

    !!! note

        The export engine only takes into account cell formatting applied using the `GridColumn.EditorProperties` property. For example:

        ```
        <mxdg:GridColumn Width="*" FieldName="Salary">
            <mxdg:GridColumn.EditorProperties>
                <mxe:TextEditorProperties DisplayFormatString="c"/>
            </mxdg:GridColumn.EditorProperties>
        </mxdg:GridColumn>
        ```

        Cell formatting applied using other approaches (for instance, with `GridColumn.CellTemplate`) is ignored during data export.

        


<!-- TODO
image with data grouping export
 -->




## Export to PDF Format

The PDF rendering engine follows the WYSIWYG concept, which retains the layout of grid elements in the output document. 


![grid-export-to-pdf](../../images/grid-export-to-pdf.png)


Use the following methods to export the control's data to PDF format:

- <code>DataGridControl.ExportToPdf(string fileName, PageExportOptions? options = null)</code> — Exports data to a file.

- <code>DataGridControl.ExportToPdf(Stream stream, PageExportOptions? options = null)</code> — Exports data to a stream.

The optional `options` parameter (of type `PageExportOptions`) allows you to customize export settings. The `PageExportOptions` class exposes the following members:

- `PageExportOptions.ExportProgress` event — Fires repeatedly during data export. The event's `ExportProgressEventArgs.ProgressPercentage` parameter indicates the progress as a percentage (0 to 100). You can use this event to display export progress to users in a customized way.

- `PageExportOptions.FitToPageWidth` (default is `false`) — Specifies whether grid columns are stretched to fit the paper width.

- `PageExportOptions.Landscape` (default is `false`) — Specifies whether the page orientation is horizontal (`Landscape`) or vertical (`Portrait`).

- `PageExportOptions.Margins` (default is `72,72,72,72`) — The page margins, in points. 1 point = 1/72 inch.

- `PageExportOptions.PageRange` — A string that specifies the range of pages to be exported. You can use the following notations to specify the output page range:

    - "1" — Exports page 1.
    - "1, 4, 8-10" — Exports pages 1, 4, and 8 through 10.
    <!-- - "7-" — Exports from page 7 to the end. -->

    The default value of the `PageRange` property is an empty string, which exports all pages.

- `PageExportOptions.PaperKind` (default is `A4`) — The paper size.

- `PageExportOptions.ShowBands` property (default is `null`) — Specifies whether the control's [bands](bands.md) are included in the export. 

    If `ShowBands` is `null`, the setting is specified by the control's `DataGridControl.ShowBands` property. 

- `PageExportOptions.ShowColumnHeaders` property (default is `null`) — Specifies whether the column header panel is included in the export. 

    If `ShowColumnHeaders` is `null`, the setting is specified by the control's `DataGridControl.ShowColumnHeaders` property.  
    

## Export to CSV Format

The DataGrid control provides the `ExportToCsv` method to export data to CSV format. CSV (comma-separated values) is a plain text data format to store tabular data. Each record is exported as a text line, in which values are delimited by a separator (typically, a comma).

The following `ExportToCsv` method overloads are available:

- <code>DataGridControl.ExportToCsv(string filePath, TextExportMode textExportNode = TextExportMode.Text, string separator = ",", bool quoteStringsWithSeparators = true)</code> — Exports data to a file.

- <code>DataGridControl.ExportToCsv(Stream stream, TextExportMode textExportMode = TextExportMode.Text, string separator = ",", bool quoteStringsWithSeparators = true)</code> — Exports data to a stream.

The following method parameters allow you to customize export options:

- `textExportMode` — The **default** export mode of cell values. 

    Available options include: 

    - `TextExportMode.Value` — Exports cell values. Data formats applied to cell values are not exported.
    - `TextExportMode.Text` — Exports cell display text. If cell values are formatted in the DataGrid control, the formatted string representation is exported.

        !!! note

            The export engine only takes into account cell formatting applied using the `GridColumn.EditorProperties` property.

    You can use the `GridColumn.TextExportMode` property to override the method's `textExportMode` parameter for individual columns. 


- `separator` — A string that specified the separator used to delimit cell values in the output document. The default separator is a comma (",").

- `quoteStringsWithSeparators` — Specifies whether to wrap values in quotes (") if they contain the specified `separator`.



## Export to Image Formats

The DataGrid control's `ExportToImages` method performs a paginated export to an image format (PNG, JPEG, SVG, or WebP). If the control's content is too large to fit a single page, the method paginates the data (splits it into pages) and exports each page as a separate image. 

![treelist-export-to-images](../../images/treelist-export-to-images.png)

The target page's format and size are defined by a parameter passed to the method. The `ExportToImages` method uses the same pagination mechanism as the `ExportToPdf` method.

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

Use the `ExportToImages` method's parameters to customize the page settings, output image format, and file name pattern.

- `directory` — Specifies the directory in which to save image files. An exception is raised if the specified directory does not exist.

- `fileNameFormat` — Specifies file naming pattern for the output image files. 

    The `fileNameFormat` value should include the `{0}` placeholder at the position where you need to insert a page number in the generated file names. You can format the page number using the [standard](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings) and [custom numeric format specifiers](https://learn.microsoft.com/en-us/dotnet/standard/base-types/custom-numeric-format-strings). Below are examples of `fileNameFormat` values:

    - "image{0}.png" — Produces files like "image1.png", "image2.png", and so on.
    - "image{0:D3}.svg"  — Produces files like "image001.svg", "image002.svg", and so on.
    
The optional `options` parameter (of type `ImageExportOptions`) allows you to customize export settings. The `ImageExportOptions` class exposes the following members:

- `ImageExportOptions.Format` — The output image format (PNG, JPEG, SVG, or WebP).

- `ImageExportOptions.PageBorderColor` — The color of the border drawn around each page.
- `ImageExportOptions.PageBorderWidth`  — The width of the border drawn around each page.


- `PageExportOptions.ExportProgress` event — Fires repeatedly during data export. The event's `ExportProgressEventArgs.ProgressPercentage` parameter indicates the progress as a percentage (0 to 100). You can use this event to display export progress to users in a customized way.


- `PageExportOptions.ShowBands` property (default is `null`) — Specifies whether the control's [bands](bands.md) are included in the export. 

    If `ShowBands` is `null`, the setting is specified by the control's `DataGridControl.ShowBands` property. 

- `PageExportOptions.ShowColumnHeaders` property (default is `null`) — Specifies whether the column header panel is included in the export. 

    If `ShowColumnHeaders` is `null`, the setting is specified by the control's `DataGridControl.ShowColumnHeaders` property.  

- `PageExportOptions.FitToPageWidth` (default is `false`) — Specifies whether grid columns are stretched to fit the paper width.

- `PageExportOptions.Landscape` (default is `false`) — Specifies whether the page orientation is horizontal (`Landscape`) or vertical (`Portrait`).

- `PageExportOptions.Margins` (default is `72,72,72,72`) — The page margins, in points. 1 point = 1/72 inch.


- `PageExportOptions.PageRange` — A string that specifies the range of pages to be exported. You can use the following notations to specify the output page range:

    - "1" — Exports page 1.
    - "1, 4, 8-10" — Exports pages 1, 4, and 8 through 10.
    - "7-" — Exports from page 7 to the end.

    The default value of the `PageRange` property is an empty string, which exports all pages.

- `PageExportOptions.PaperKind` (default is `A4`) — The paper size.