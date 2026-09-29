---
title: Eremex Avalonia UI Controls Library
seealso: []
---

# Eremex Avalonia UI Controls Library

The Eremex Avalonia UI Controls Library includes powerful UI controls and utility libraries for the Avalonia framework to help you build highly customizable cross-platform applications with enhanced UX.

[![Controls - Light Theme](images/collage-v1.2.77-1600.png)](images/collage-v1.2.77-3200.png)

## Getting Started 

- [Get Started with Eremex Avalonia UI Controls](get-started/get-started-with-emx-controls.md)
- [Use Standard Avalonia UI Templates to Create a New Project with Eremex Controls](get-started/create-new-avalonia-project-using-avalonia-templates.md)

## Demo Application

Our Demo application allows you to explore and test a wide range of features of the Eremex Controls library.

### Download and Run Demo Offline

- [Eremex Avalonia Controls Demo](https://github.com/Eremex/controls-demo)

### Run Demo Online

You can run the WASM (WebAssembly) version of the Demo application and practice using the Eremex Controls directly in your browser. Access the Online Demo at:

- [Eremex Avalonia Controls Online Demo](https://eremex.github.io/controls-demo/)

Certain example modules are disabled in the Online Demo, including:

- Examples that demonstrate features not supported in WASM (for instance, the 3D engine).
- Examples not optimized for display and interaction in a web browser.

Known limitations: Hyperlinks are not supported.

## What's Included

- [Assemblies](whats-included/assemblies.md)
- [Project Templates](whats-included/project-templates.md)
- [System Requirements](whats-included/system-requirements.md)

<br>

<style>

th {
    visibility: collapse;
}
td, th, tr {
   border: none!important;
   vertical-align: top;
}
</style>

## Controls and Libraries

<br>    

### Data Management Controls


| <div style="width:400px"></div> | col 2 |
| --- | --- |
| **Data Grid** |  |
| ![thumb-datagrid](images/thumb-datagrid.png) | Displays data from an item source as a two-dimensional table, and provides rich data shaping and editing functionality.<br><br>- Large data sources support<br>- Unbound data<br>- Data sorting and grouping<br>- In-place editors<br>- Search and data filtration<br>- Multiple row selection<br>- Row drag-and-drop<br>- Data validation<br>- Built-in and custom context menus<br>- Column bands<br>[Learn more...](controls/datagrid/index.md) |  
| **Tree List and Tree View** |
| ![thumb-treelist](images/thumb-treelist.png) | Renders hierarchical data in the form of a tree. Tree List supports multiple data columns, while Tree View is a single-column control.<br><br>- Binding to self-referential (flat) and hierarchical data sources<br>- Unbound mode (allows you to manually supply data)<br>- Multiple row selection<br>- Row selection via built-in checkboxes<br>- Data sorting<br>- In-place editors<br>- Data search and filtering<br>- Row drag-and-drop<br>- Data validation<br>- Built-in and custom context menus<br>- Column bands<br>[Learn more...](controls/treelist/index.md) | 
| **Property Grid** |
| ![thumb-propertygrid](images/thumb-propertygrid.png) | An efficient solution for browsing and editing properties of one or more objects. <br><br>- Automatic generation of rows from public properties of a bound object(s)<br>- Manual row creation mode<br>- Combining rows into category rows<br>- Combining rows into embedded tabs<br>- Search panel (for quick row location)<br>- In-place editors<br>[Learn more...](controls/propertygrid/index.md) | 
| **List View** |
| ![thumb-propertygrid](images/thumb-listview.png) | An advanced list that renders items according to your template. Supports item sorting, grouping, filtering and multi-selection.<br><br>- Two item arrangement modes: `Stack` (a single column of items) and `Wrap` (multi-column arrangement with the item wrapping feature) <br>- Rendering ListView items in a custom manner according to your template<br>- Item sorting and grouping against an unlimited number of item properties<br>- Item filtration with an event<br>- Single and multiple selection modes<br>[Learn more...](controls/listview/index.md) | 



<br>    


### Navigation and Layout Controls

| <div style="width:400px"></div> | col 2 |
| --- | --- |
| **Ribbon** |
| ![thumb-ribbon](images/thumb-ribbon.png) | The menu inspired by the ribbon UI found in Microsoft Office products.<br><br>- Classic and Simplified views<br>- Support for all types of items (commands) available in the [traditional menus](controls/toolbars-and-menus/index.md): regular buttons, check buttons, editors, labels, sub-menus and button groups.<br>- In-place and dropdown galleries<br>- Quick Access Toolbar - A user can add frequently used commands to this toolbar at runtime from a context menu.<br>- Customizing the Quick Access Toolbar position (above or below the Ribbon command panel) and visibility<br>- Displaying items in the tab header area<br>- Tab header colorization (allows you to highlight contextual tabs)- Ribbon item navigation with the keyboard<br>- Adaptive layout of groups and items (adjusts the layout of commands when the Ribbon control's width changes)<br>[Learn more...](controls/ribbon/index.md) |
| **Toolbars and Menus** |  |
| ![thumb-bars](images/thumb-bars.png) | Traditional toolbars and menus for your applications.<br><br>- Supported toolbar item types: buttons, check buttons, sub-menus, item groups, and more<br>- Docking toolbars at the edges of a container<br>- Placing toolbars at any position within the window (for example, at the top of client controls)<br>- Horizontal and vertical toolbar orientations<br>- Adaptive layout of commands<br>- Toolbar layout customization at runtime using drag-and-drop operations<br>- Runtime customization mode for advanced toolbar personalization<br>- Quick customization (without the need to activate customization mode)<br>- Show values in toolbars, and allow users to edit them using in-place editors<br>- Hotkey support, including complex shortcuts, such as Ctrl+R, Ctrl+K<br>- Context menus for external controls<br>[Learn more...](controls/toolbars-and-menus/index.md) | 
| **Docking UI** |
| ![thumb-docking](images/thumb-docking.png) | Classic docking interface inspired by the Microsoft Visual Studio IDE.<br><br>- Dock panels help you create tool panes<br>- Documents (embedded dock windows) allow you to display the main content of your UI<br>- Floating panels<br>- Panel auto-hide functionality<br>- Tab containers<br>- Panel resizing and drag-and-drop<br>- Dock hints<br>- Built-in context menus to perform operations on panels and Documents<br>- MVVM support<br>- Docking on multiple monitors<br>- Save and restore layouts of dock panels between application runs<br>[Learn more...](controls/docking/index.md) |

<br>   

### Data Visualization Controls

| <div style="width:400px"></div> | col 2 |
| --- | --- |
| **Chart Controls** |  |
| ![thumb-chartcontrol](images/thumb-chartcontrol.png) | The `CartesianChart`, `PolarChart` and `SmithChart` controls allow you to integrate the most popular interactive graphs into your application's UI.<br><br>- An unlimited number of data series<br>- Supported Views: Line, Bar, Range Bar, Step Line, Candlestick, and more<br>- Multiple axis types: Numeric, Date-Time, Time Span, Qualitative, and Logarithmic<br>- Scrolling and zooming the entire view and individual axes<br>- High-performance when displaying large data.<br>- Real-time data visualization.<br>[Learn more...](controls/charts/index.md) | 
| **Heatmap Control** |  |
| ![thumb-heatmap](images/thumb-heatmap.png) | A two-dimensional heat map - a chart that visualizes data using colored points.<br><br>- 2D representation of numerical values as color<br>- Customization of the X and Y axes<br>- Crosshair<br>- Strips and constant lines<br>- Scroll and zoom with the mouse<br>- Export rendering to a bitmap<br>[Learn more...](controls/charts/heatmap.md) | 

<br>    

### 3D Graphics

| <div style="width:400px"></div> | col 2 |
| --- | --- |
| **Graphics3D Control** |  |
| ![thumb-graphics3dcontrol2](images/thumb-graphics3dcontrol2.png) | Allows you to visualize 3D models in your Avalonia applications.<br><br>- API to specify 3D models<br>- Simple materials<br>- Textured materials in PBR format<br>- Displaying multiple 3D models simultaneously<br>- Perspective and isometric camera modes<br>- Model rotation, panning and zooming with the mouse and keyboard at runtime<br>- Rendering on a video card with the Vulkan SDK<br>- MVVM pattern support for specifying 3D models<br>[Learn more...](controls/graphics3dcontrol/index.md) | 


<br> 

### Editors and Utility Controls
| <div style="width:400px"></div> | col 2 |
| --- | --- |
| **Data Editors** |  |
| ![thumb-editors](images/thumb-editors.png) | Simple and advanced editors that allow users to edit almost everything - from text and numbers to date/time values and colors. You can use them as standalone controls, or as in-place editors <br><br>- ButtonEditor<br>- CheckEditor<br>- ComboBoxEditor<br>- DateEditor<br>- HyperlinkEditor<br>- MemoEditor<br>- PopupColorEditor<br>- SegmentedEditor<br>- SpinEditor<br>- TextEditor<br>[Learn more...](controls/editors/index.md) |
| **Utility Controls** |  |
| ![thumb-utilitycontrols](images/thumb-utilitycontrols.png) | A collection of useful controls shipped with the Eremex Controls library allow you to create feature-rich applications.<br><br>- TabControl<br>-  SplitContainerControl<br>-  GroupBox<br>-  CalendarControl<br>-  MxMessageBox<br>-  CircleProgressIndicator<br>[Learn more...](controls/utility-controls/index.md) |

<br>    

### Eremex Paint Themes

The Eremex Controls Library ships with the 'DeltaDesign' paint theme that helps you deliver interfaces with the light and dark color palettes.


| <div style="width:400px"></div> | <div style="width:400px"></div> |
| --- | --- |
| **DeltaDesign Light Theme** | **DeltaDesign Dark Theme** |
| ![thumb-lighttheme](images/thumb-lighttheme.png) | ![thumb-darktheme](images/thumb-darktheme.png) |
| ![thumb-lighttheme2](images/thumb-lighttheme2.png) | ![thumb-darktheme2](images/thumb-darktheme2.png) |

See the following topic for more information: 

- [Themes](controls/themes/index.md)
