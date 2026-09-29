---
title: Unbound Mode
order: 80000
seealso: []
---

# Unbound Mode

The TreeList and TreeView controls support unbound mode, in which you can manually create a node hierarchy. 

Do not initialize a control's `ItemSource` property. Otherwise, the control switches to bound mode, and thus it forbids you to manually add nodes.

Use the `TreeListControlBase.Nodes` property to add root nodes to the control. For each node, you can use the `TreeListNode.Nodes` property to add child nodes. 

A node in the TreeList and TreeView controls is encapsulated by a `TreeListNode` object. Its `TreeListNode.Content` property allows you to specify a node's content. You can set the `TreeListNode.Content` property to a business object whose public properties provide data for the control's columns. For the TreeView control, you can set the `TreeListNode.Content` property to a String object.

If you use a TreeList control, ensure that the control's `TreeListControl.Columns` collection has columns bound to specific field names.

The following XAML code creates a hierarchical node structure in the `TreeListControl.Nodes` collection. Each node's `Content` property is initialized with a _Person_ object defined in code-behind.

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

The following example creates a node structure in code-behind. It adds a _node1_ object to the TreeList's root level. Other nodes are added at nested levels.

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

### TreeView Specifics

You can set the TreeView node's `Content` property to a business object or simple string.

The following code shows how to populate TreeView nodes with simple strings.

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

If you assign a business object to the `Content` property, set the `TreeViewControl.DataFieldName` member to the name of the business object's property that supplies display values for the control, as demonstrated in the example below.

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

