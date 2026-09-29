---
title: Несвязанный режим
order: 80000
seealso: []
---

# Несвязанный режим

Элементы управления TreeList и TreeView поддерживают несвязанный режим, в котором вы можете вручную создавать иерархию узлов.

Не инициализируйте свойство `ItemSource` элемента управления. В противном случае элемент управления переключится в связанный режим и, соответственно, запретит вам вручную добавлять узлы.

Используйте свойство `TreeListControlBase.Nodes`, чтобы добавлять корневые узлы в элемент управления. Для каждого узла вы можете использовать свойство `TreeListNode.Nodes`, чтобы добавлять дочерние узлы.

Узел в элементах управления TreeList и TreeView инкапсулируется объектом `TreeListNode`. Его свойство `TreeListNode.Content` позволяет указать содержимое узла. Вы можете установить свойство `TreeListNode.Content` в бизнес-объект, публичные свойства которого предоставляют данные для колонок элемента управления. Для элемента управления TreeView вы можете установить свойство `TreeListNode.Content` в объект String.

Если вы используете элемент управления TreeList, убедитесь, что коллекция `TreeListControl.Columns` элемента управления содержит колонки, связанные с конкретными именами полей.

Следующий код XAML создаёт иерархическую структуру узлов в коллекции `TreeListControl.Nodes`. Свойство `Content` каждого узла инициализируется объектом _Person_, определённым в code-behind.

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

Следующий пример создаёт структуру узлов в code-behind. Он добавляет объект _node1_ на корневой уровень TreeList. Другие узлы добавляются на вложенных уровнях.

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

### Особенности TreeView

Вы можете установить свойство `Content` узла TreeView в бизнес-объект или простую строку.

Следующий код показывает, как заполнить узлы TreeView простыми строками.

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

Если вы присваиваете бизнес-объект свойству `Content`, установите член `TreeViewControl.DataFieldName` в имя свойства бизнес-объекта, которое предоставляет отображаемые значения для элемента управления, как показано в примере ниже.

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

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
