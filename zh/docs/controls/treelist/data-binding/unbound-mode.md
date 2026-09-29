---
title: 未绑定模式
order: 80000
seealso: []
---

# 未绑定模式

TreeList 和 TreeView 控件支持非绑定模式，您可以手动创建节点层次结构。

不要初始化该控件的 `ItemSource` 属性。否则，该控件会切换到绑定模式，从而禁止您手动添加节点。

使用 `TreeListControlBase.Nodes` 属性将根节点添加到控件。对于每个节点，您可以使用 `TreeListNode.Nodes` 属性来添加子节点。

TreeList 和 TreeView 控件中的节点由 `TreeListNode` 对象封装。它的 `TreeListNode.Content` 属性允许您指定节点的内容。您可以将 `TreeListNode.Content` 属性设置为一个业务对象，该对象的公共属性为控件的列提供数据。对于 TreeView 控件，您可以将 `TreeListNode.Content` 属性设置为 String 对象。

如果您使用 TreeList 控件，请确保该控件的 `TreeListControl.Columns` 集合具有绑定到特定字段名称的列。

以下 XAML 代码在 `TreeListControl.Nodes` 集合中创建分层节点结构。每个节点的 `Content` 属性均使用代码隐藏中定义的 _Person_ 对象进行初始化。

``` xml
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"
xmlns:local="clr-namespace:AvaloniaApplication1"
...
<mxtl:TreeListControl Grid.Column="3" Width="800" Name="treeListUnbound" 
 HorizontalAlignment="Stretch">
    <mxtl:TreeListControl.Columns>
        <mxtl:TreeListColumn Name="colFirstName" FieldName="FirstName" 
         Header="First Name" Width="*"  AllowSorting="False"  />
        <mxtl:TreeListColumn Name="colLastName" FieldName="LastName" 
         Header="Last Name" Width="*"/>
        <mxtl:TreeListColumn Name="colCity" FieldName="City" 
         Header="City" Width="*" ReadOnly="True" />
        <mxtl:TreeListColumn Name="colPhone" FieldName="Phone" 
         Header="Phone" Width="*"/>
    </mxtl:TreeListControl.Columns>

    <mxtl:TreeListControl.Nodes>
        <mxtl:TreeListNode>
            <mxtl:TreeListNode.Content>
                <local:Person FirstName="Roman" LastName="Suponin" 
                 City="Saint Petersburg" Phone="(7)724-347-47"/>
            </mxtl:TreeListNode.Content>
            <mxtl:TreeListNode.Nodes>
                <mxtl:TreeListNode >
                    <mxtl:TreeListNode.Content>
                        <local:Person FirstName="Ivan" LastName="Kovalev" 
                         City="Moscow" Phone="(7)111-90-73"/>
                    </mxtl:TreeListNode.Content>
                    <mxtl:TreeListNode.Nodes>
                        <mxtl:TreeListNode>
                            <mxtl:TreeListNode.Content>
                                <local:Person FirstName="Artin" LastName="Tusk" 
                                 City="Aksaray" Phone="(4)123-14-56"/>
                            </mxtl:TreeListNode.Content>
                        </mxtl:TreeListNode>
                        <mxtl:TreeListNode>
                            <mxtl:TreeListNode.Content>
                                <local:Person FirstName="George" LastName="Botkin" 
                                 City="Hua Hin" Phone="(61)457-198-34"/>
                            </mxtl:TreeListNode.Content>
                            <mxtl:TreeListNode.Nodes>
                                <mxtl:TreeListNode>
                                    <mxtl:TreeListNode.Content>
                                        <local:Person FirstName="Lee" LastName="Wan" 
                                         City="Shanghai" Phone="(56)335-57-89"/>
                                    </mxtl:TreeListNode.Content>
                                </mxtl:TreeListNode>
                            </mxtl:TreeListNode.Nodes>
                        </mxtl:TreeListNode>
                    </mxtl:TreeListNode.Nodes>
                </mxtl:TreeListNode>
            </mxtl:TreeListNode.Nodes>
        </mxtl:TreeListNode>
    </mxtl:TreeListControl.Nodes>
</mxtl:TreeListControl>
```

``` cs
public partial class Person : ObservableObject
{
    public Person() { }
    public Person(string firstName, string lastName, string city, string phone)
    {
        this.firstName = firstName;
        this.lastName = lastName;
        this.city = city;
        this.phone = phone;
    }

    [ObservableProperty]
    string firstName;
    [ObservableProperty]
    string lastName;
    [ObservableProperty]
    string city;
    [ObservableProperty]
    string phone;
}
```

以下示例在代码隐藏中创建节点结构。它将 _node1_ 对象添加到 TreeList 的根级别。其他节点以嵌套级别添加。

``` cs
TreeListNode node1 = new TreeListNode() 
{ 
    Content = new Person("Kim", "Magnus", "Doha", "(5)433-07-12") 
};
TreeListNode node11 = new TreeListNode() 
{ 
    Content = new Person("Patricia", "Rooney", "Cairo", "(5)450-39-49") 
};
TreeListNode node111 = new TreeListNode() 
{ 
    Content = new Person("Victor", "Boev", "Sarajevo", "(98)328-23-54") 
};
TreeListNode node12 = new TreeListNode() 
{ 
    Content = new Person("Vincent", "Novak", "Belgrad", "(476)487-598-465") 
};
treeListUnbound.Nodes.Add(node1);
node1.Nodes.Add(node11);
node11.Nodes.Add(node111);
node1.Nodes.Add(node12);
```

### TreeView 详细信息

您可以将 TreeView 节点的 `Content` 属性设置为业务对象或简单字符串。

以下代码显示如何使用简单字符串填充 TreeView 节点。

``` xml
<mxtl:TreeViewControl Grid.Column="5" Width="400" Name="treeViewUnbound2">
    <mxtl:TreeViewControl.Nodes>
        <mxtl:TreeListNode Content="Russia">
            <mxtl:TreeListNode.Nodes>
                <mxtl:TreeListNode Content="Tula oblast">
                    <mxtl:TreeListNode.Nodes>
                        <mxtl:TreeListNode Content="Tula"/>
                        <mxtl:TreeListNode Content="Aleksin">
                            <mxtl:TreeListNode.Nodes>
                                <mxtl:TreeListNode Content="Pavlovo"/>
                                <mxtl:TreeListNode Content="Kolosovo"/>
                                <mxtl:TreeListNode Content="Shutilovo"/>
                            </mxtl:TreeListNode.Nodes>
                        </mxtl:TreeListNode>
                        <mxtl:TreeListNode Content="Belyov"/>
                        <mxtl:TreeListNode Content="Suvorov"/>
                    </mxtl:TreeListNode.Nodes>
                </mxtl:TreeListNode>
            </mxtl:TreeListNode.Nodes>
                    
        </mxtl:TreeListNode>
    </mxtl:TreeViewControl.Nodes>
</mxtl:TreeViewControl>
```

如果将业务对象分配给 `Content` 属性，请将 `TreeViewControl.DataFieldName` 成员设置为为该控件提供显示值的业务对象属性的名称，如下例所示。

``` cs
TreeListNode node1 = new TreeListNode() 
{ 
    Content = new Person("Kim", "Magnus", "Doha", "(5)433-07-12") 
};
TreeListNode node11 = new TreeListNode() 
{ 
    Content = new Person("Patricia", "Rooney", "Cairo", "(5)450-39-49") 
};
TreeListNode node111 = new TreeListNode() 
{ 
    Content = new Person("Victor", "Boev", "Sarajevo", "(98)328-23-54") 
};
TreeListNode node12 = new TreeListNode() 
{ 
    Content = new Person("Vincent", "Novak", "Belgrad", "(476)487-598-465") 
};

treeViewUnbound1.DataFieldName = "LastName";
treeViewUnbound1.Nodes.Add(node1);
node1.Nodes.Add(node11);
node11.Nodes.Add(node111);
node1.Nodes.Add(node12);
```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
