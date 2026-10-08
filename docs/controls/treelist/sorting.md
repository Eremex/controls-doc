---
title: Sorting
order: 5000
seealso: []
---

# Sorting

The data sorting feature allows you to sort sibling nodes in the TreeList and TreeView controls in ascending or descending order. 

TreeList supports data sorting against one or multiple columns. The control also allows your users to sort data with a mouse click on a column header and by using a column header's context menu.

## End User Actions (TreeList)

In the TreeList control, a user can left-click a column header to sort this column. A subsequent click on the same column header reverses the sort direction. To clear sorting, hold down the CTRL key and click the column header.

To sort data by multiple columns, a user needs to hold down the SHIFT key and then click column headers in the required order. The control will sort data against the first clicked column, then against the second column, and so on.

A user can also change a column's sort settings from a column header's context menu. Right-click the column header to invoke this menu.

Use the following properties to prevent a user from sorting data:

- Set [`TreeListControl.AllowSorting`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/AllowSorting.md) to `false` to prevent a user from sorting against any column.
- Set [`ColumnBase.AllowSorting`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/AllowSorting.md) to `false` to prevent a user from sorting against a specific column.

These properties do not prevent you from sorting data in code.

The TreeView control does not have features to sort data from the UI. You can sort data in code in this control.

## Alphanumeric Sorting

For columns that display text in a TreeListControl and TreeViewControl, you can use the inherited [`DataControlBase.TextSortMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/TextSortMode.md) property to choose between alphabetical and alphanumeric sorting.

- `Alphabetical` Sort (default): This mode compares strings character by character. If the text contains numbers, the sorting algorithm treats them as individual characters, but not as numbers. For example:

    ![sorting-alphabetical-example1](../../images/grid-sorting-alphabetical-example1.png)



- `Alphanumeric` Sort (natural ordering): This mode is suitable for strings that contain a mix of text and numbers. The sorting algorithm arranges strings in a human-friendly, logical order by treating numbers as numerical values instead of just characters. For example:

    ![sorting-alphanumeric-example1](../../images/grid-sorting-alphanumeric-example1.png)

    The following code applies the alphanumeric sort order:

    ``` xml
    <mxtl:TreeListControl Name="treeList1" ItemsSource="{Binding MyData}" ChildrenSelector="{StaticResource childrenSelector}" 
                        TextSortMode="Alphanumeric"
                        />
    ```

The [`DataControlBase.TextSortMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/TextSortMode.md) property affects sorting for all columns that display text values.

The following image demonstrates more examples that compare alphabetical and alphanumeric sort modes:

![ sorting-textsortmode-example2](../../images/grid-sorting-textsortmode-example2.png)



## Sort in Code (TreeList)

You can sort TreeList's data against one or multiple columns. When you sort data by multiple columns, the TreeList control reorders nodes according to values of the first sort column. Then it reorders sorted nodes by the second sort column, while keeping the value order in the first column, and so on.

Use the following properties to sort data by a column:

- Set the [`ColumnBase.SortDirection`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/SortDirection.md) property to `Ascending` or `Descending`. This property specifies the sort order of the column's data. 

- Set the [`ColumnBase.SortIndex`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/SortIndex.md) property to a non-negative value to sort data against the column in ascending order. The [`ColumnBase.SortIndex`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/SortIndex.md) property specifies the column's position among sorted columns. 

Do one of the following to clear sorting:

- Set a column's [`SortDirection`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/SortDirection.md) property to `null` to clear sorting for this column. 
- Call the control's inherited [`DataControlBase.ClearSorting`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ClearSorting.md) method to remove sorting applied to all columns.

The following code clears sorting and then sorts data against two columns:

``` csharp
using CommunityToolkit.Mvvm.ComponentModel;
using System.ComponentModel;

treeList.ClearSorting();
treeListColumn1.SortDirection = ListSortDirection.Ascending;
treeListColumn3.SortDirection = ListSortDirection.Descending;
```

You can wrap your code with the [`BeginDataUpdate`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/BeginDataUpdate.md) and [`EndDataUpdate`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/EndDataUpdate.md) methods to prevent superfluous updates when changing the control's multiple settings (including sort settings).

``` csharp
using CommunityToolkit.Mvvm.ComponentModel;
using System.ComponentModel;

treeList.BeginDataUpdate();
treeList.ClearSorting();
treeListColumn1.SortIndex = 0;
treeListColumn3.SortIndex = 1;
treeListColumn2.SortDirection = ListSortDirection.Descending;
treeList.EndDataUpdate();
```

## Sort in Code (TreeView)

To sort data in the TreeView, use the [`SortDirection`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/SortDirection.md) property of your [`TreeViewControl`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl.md) object. Set this property to `Ascending` or `Descending` to sort data in required order. 

``` csharp
treeViewControl1.SortDirection = ListSortDirection.Ascending;
```

Do one of the following to clear sorting:

- Set the [`SortDirection`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/SortDirection.md) property to `null`. 
- Call the control's inherited [`DataControlBase.ClearSorting`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/ClearSorting.md) method.


## Sortable Columns and Sort Mode (TreeList and TreeView)

The TreeList and TreeView controls can sort columns by edit values, display values, or according to a custom sorting algorithm. Default sort mode is dependent on the column's in-place editor and bound property's data type:

- Sorting by edit values — All columns, except columns with an embedded ComboBoxEditor.
- Sorting by display text — Columns with an embedded ComboBoxEditor.
- No sorting — Columns bound to objects that do not implement the `IComparable` interface. For instance, image data types do not implement this interface, thus no sorting is available for corresponding columns, by default. See the [Custom Sorting](#custom-sorting) section below for information, on how to forcibly sort these columns.

The [`ColumnBase.SortMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/SortMode.md) property (in the TreeList) and [`TreeViewControl.SortMode`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/SortMode.md) property (in the TreeView) allows you to change default sort mode. The following options are available:

- [`SortMode.Value`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SortMode.md) — Sort by cell edit values.
- [`SortMode.DisplayText`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SortMode.md) — Sort by cell display text.
- [`SortMode.Custom`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SortMode.md) — Custom sorting. Set the [`SortMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SortMode.md) property to `Custom`, and then handle the [`TreeListControl.CustomColumnSort`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/CustomColumnSort.md)/[`TreeViewControl.CustomSort`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/CustomSort.md) event to implement a custom sorting routine. See [Custom Sorting](#custom-sorting).

### Custom Sorting

The [`CustomColumnSort`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/CustomColumnSort.md)/[`CustomSort`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/CustomSort.md) event allows you to implement custom sorting logic. Set the [`ColumnBase.SortMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/SortMode.md) property (in the TreeList) and [`TreeViewControl.SortMode`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/SortMode.md) property (in the TreeView) to `Custom` to enable this event.

If a column's bound data type does not implement the `IComparable` interface (for instance, an image data type), the TreeList/TreeView control defaults to preventing sorting for this column. You can, however, enable sorting for this column, as follows:

- TreeList: Set the column's [`AllowSorting`](../../API/Eremex.AvaloniaUI.Controls.DataControl/ColumnBase/AllowSorting.md) property to `true` (this property's default value is `null`).
- TreeList and TreeView: Set the [`SortMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SortMode.md) property to `Custom`.
- TreeList and TreeView: Handle the [`CustomColumnSort`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/CustomColumnSort.md)/[`CustomSort`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/CustomSort.md) event to implement custom sorting.

When you handle the [`CustomColumnSort`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/CustomColumnSort.md)/[`CustomSort`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewControl/CustomSort.md) event, you should compare two nodes specified in the event arguments. Assign the result of the comparison to the [`Result`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewCustomSortEventArgs/Result.md) event parameter as follows:

- Set [`Result`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewCustomSortEventArgs/Result.md) to `-1` if the first node should be displayed above the second node when data is sorted in ascending order. 

- Set [`Result`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewCustomSortEventArgs/Result.md) to `1` if the first node should be displayed below the second node when data is sorted in ascending order. 

 - Set [`Result`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeViewCustomSortEventArgs/Result.md) to `0` if the two nodes are equal. 
 

The following example handles the [`TreeListControl.CustomColumnSort`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControl/CustomColumnSort.md) event to sort data in the "_FileName_" column in a custom manner. The "_FileName_" column stores file names in the standard "_filename.ext_" format. The custom sorting routine sorts file names by their extensions.

``` csharp
<mxtl:TreeListControl Name="treeList" CustomColumnSort="TreeList_CustomColumnSort">
    <mxtl:TreeListControl.Columns>
        <mxtl:TreeListColumn  Width="*" FieldName="FileName"  SortMode="Custom" />
    </mxtl:TreeListControl.Columns>
</mxtl:TreeListControl>

private void TreeList_CustomColumnSort(object? sender, TreeListCustomColumnSortEventArgs e)
{
    if (e.Column.FieldName == "FileName")
    {
        string fileName1 = Convert.ToString(e.Value1);
        string fileName2 = Convert.ToString(e.Value2);

        string newfileName1 = extractFileExtension(fileName1) + "." + fileName1;
        string newfileName2 = extractFileExtension(fileName2) + "." + fileName2;
        e.Result = String.Compare(newfileName1, newfileName2);
    }
}

string extractFileExtension(string fileName)
{
    string res = "";
    int dotIndex = fileName.LastIndexOf('.');
    if (dotIndex > 0)
        res = fileName.Substring(dotIndex + 1);
    return res;
}
```

## Respond to Data Sorting

Handle the following events to perform custom actions when data is sorted:

- [`DataControlBase.StartSorting`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/StartSorting.md) — Fires when data is about to be sorted.
- [`DataControlBase.EndSorting`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/EndSorting.md) — Fires when data sorting is complete.

## Additional API

- [`TreeListControlBase.AutoScrollOnSorting`](../../API/Eremex.AvaloniaUI.Controls.TreeList/TreeListControlBase/AutoScrollOnSorting.md) — Specifies whether the control automatically scrolls the view port to make the focused node visible when data is sorted.

