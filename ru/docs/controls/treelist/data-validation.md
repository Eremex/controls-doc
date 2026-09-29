---
title: Валидация данных
order: 3000
seealso: []
---

# Валидация данных

Механизм валидации данных позволяет проверять значения ячеек и отображать ошибки в ячейках, содержащих недопустимые данные.

Элементы управления TreeList и TreeView выполняют валидацию данных, когда пользователь изменяет значение ячейки и пытается сохранить (отправить) это значение. Контролы также вызывают механизм валидации для вновь отображаемых ячеек и ячеек, обновлённых в коде, даже если пользователь не изменял значения ячеек.

## Валидация значений при изменении данных ячейки пользователем

Элементы управления TreeList и TreeView активируют механизм валидации значения ячейки, когда пользователь изменяет значение ячейки и пытается сохранить его в источнике данных (например, пользователь нажимает клавишу ENTER или перемещает фокус на другую ячейку). На следующей диаграмме показаны этапы механизма валидации, выполняемые при изменении пользователем значения ячейки:

![TreeList - Validation Diagram](../../images/treelist-validation-diagram.png)

1. Встроенный редактор ячейки выполняет первичную валидацию значения во время ввода данных. Например, `SpinEditor`, принимающий только числовые значения, показывает ошибки, если пользователь пытается ввести букву.

    Пользователь не может покинуть ячейку, пока не будет введено допустимое значение или не будет нажата клавиша ESC, которая возвращает предыдущее значение.

1. Элемент управления TreeList/TreeView проверяет, применены ли к бизнес-объекту источника данных [атрибуты DataAnnotations](#атрибуты-dataannotations), и затем валидирует данные согласно этим правилам. Этот этап валидации включён, если свойство `DataControlBase.ShowItemsSourceErrors` установлено в `true` (значение по умолчанию).
    
    Пользователь не может покинуть ячейку, пока не будет введено допустимое значение или не будет нажата клавиша ESC, которая возвращает предыдущее значение.
    

1. Контрол вызывает [событие `DataControlBase.ValidateCellValue`](#событие-контрола-validatecellvalue), которое можно обработать для реализации собственной логики валидации значений.

    Пользователь не может покинуть ячейку, пока не будет введено допустимое значение или не будет нажата клавиша ESC, которая возвращает предыдущее значение.

1. Контрол отправляет (post) значение ячейки. На этом этапе источник данных может выбрасывать исключения, если отправленные данные недопустимы. Если перехвачено какое-либо исключение, контрол отображает ошибку в ячейке.

    Пользователь не может покинуть ячейку, пока не будет введено допустимое значение или не будет нажата клавиша ESC, которая возвращает предыдущее значение.

1. Элемент управления TreeList/TreeView проверяет, реализует ли бизнес-объект интерфейс [IDataErrorInfo](#интерфейс-idataerrorinfo) или [INotifyDataErrorInfo](#интерфейс-inotifydataerrorinfo), и использует эти интерфейсы для получения ошибок ячейки, если они есть. Этот этап валидации включён, если свойство `DataControlBase.ShowItemsSourceErrors` установлено в `true` (значение по умолчанию).
    
    Контрол позволяет пользователю покинуть ячейку, даже если значение ячейки недопустимо, поскольку значение уже было отправлено.


## Валидация значений вновь отображаемых ячеек и ячеек, обновлённых в коде

Контролы поддерживают механизм валидации для вновь отображаемых и обновлённых ячеек, даже если пользователь не изменял значения ячеек. Контрол валидирует значения ячеек в следующих случаях:

- Контрол отображается впервые, и поэтому ячейки отрисовываются в пределах видимой области.
- Ячейка становится видимой при прокрутке контрола.
- Значение ячейки изменяется в коде, из-за чего контролу необходимо перерисовать ячейку.

На следующей диаграмме показаны этапы механизма валидации в этих сценариях:

![TreeList - Validation Diagram](../../images/treelist-validation-diagram-When-ShowAndUpdate.png)

1. Элемент управления TreeList/TreeView проверяет, применены ли к бизнес-объекту источника данных [атрибуты DataAnnotations](#атрибуты-dataannotations), и затем валидирует данные согласно этим правилам. Этот этап валидации включён, если свойство `DataControlBase.ShowItemsSourceErrors` имеет значение `true` (значение по умолчанию).

1. Элемент управления TreeList/TreeView проверяет, реализует ли бизнес-объект интерфейс [IDataErrorInfo](#интерфейс-idataerrorinfo) или [INotifyDataErrorInfo](#интерфейс-inotifydataerrorinfo), и использует эти интерфейсы для получения ошибок ячейки, если они есть. Этот этап валидации включён, если свойство `DataControlBase.ShowItemsSourceErrors` установлено в `true` (значение по умолчанию).

1. Контрол вызывает [событие `DataControlBase.ValidateCellValue`](#событие-контрола-validatecellvalue), которое можно обработать для реализации собственной логики валидации значений. Этот этап валидации включён, если свойство `DataControlBase.ValidateCellValuesOnShowAndUpdate` имеет значение `true` (значение по умолчанию — `false`).



## Правила валидации источника данных

Если свойство `DataControlBase.ShowItemsSourceErrors` включено (поведение по умолчанию), элемент управления TreeList/TreeView валидирует данные с использованием атрибутов `DataAnnotations` и интерфейса `IDataErrorInfo`, применённых к бизнес-объекту источника данных.

### Атрибуты DataAnnotations

Вы можете применять атрибуты валидации `DataAnnotations` (потомки `System.ComponentModel.DataAnnotations.ValidationAttribute`) к бизнес-объекту, чтобы задать правила валидации для свойств этого объекта. В списке ниже перечислены наиболее распространённые атрибуты валидации:

- [`CompareAttribute`](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.compareattribute?view=net-7.0) — предоставляет атрибут, сравнивающий два свойства.
- [`CustomValidationAttribute`](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.customvalidationattribute?view=net-7.0) — задаёт пользовательский метод валидации, используемый для проверки свойства или экземпляра класса.
- [`MaxLengthAttribute`](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.maxlengthattribute?view=net-8.0) — задаёт максимальную длину массива или строковых данных, допустимую для свойства.
- [`MinLengthAttribute`](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.minlengthattribute?view=net-8.0) — задаёт минимальную длину массива или строковых данных, допустимую для свойства.
- [`RangeAttribute`](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.rangeattribute?view=net-8.0) — задаёт ограничения числового диапазона для значения поля данных.
- [`RegularExpressionAttribute`](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.regularexpressionattribute?view=net-8.0) — задаёт, что значение поля данных должно соответствовать указанному регулярному выражению.
- [`RequiredAttribute`](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.requiredattribute?view=net-8.0) — задаёт, что значение поля данных является обязательным.
- [`StringLengthAttribute`](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.stringlengthattribute?view=net-8.0) — задаёт минимальную и максимальную длину символов, допустимую для поля данных.

#### Пример

Следующий код применяет атрибут `StringLength` к свойству _Code_ бизнес-объекта. Атрибут требует, чтобы пользователь ввёл строку длиной не менее 4, но не более 8 символов.

``` csharp
public partial class Department : ObservableObject, IDataErrorInfo
{
    //...

    [ObservableProperty]
    [property: StringLength(8, MinimumLength = 4)]
    public string code = "0000";
}
```

### Интерфейс 'IDataErrorInfo'

Вы можете реализовать интерфейс [`System.ComponentModel.IDataErrorInfo`](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.idataerrorinfo?view=net-7.0) для бизнес-объекта, чтобы задать правила валидации для его свойств.

В настоящее время элементы управления TreeList и TreeView поддерживают ошибки только для отдельных ячеек, а не для строк целиком. Таким образом, действует только свойство `IDataErrorInfo.Item[String]`, а свойство `IDataErrorInfo.Error` игнорируется.

#### Пример — реализация интерфейса 'IDataErrorInfo'

В следующем примере реализуется интерфейс `IDataErrorInfo` для бизнес-объекта, возвращающий ошибку, если свойство _Phone_ пусто.

``` csharp
public partial class Department : ObservableObject, IDataErrorInfo
{
    //... 

    [ObservableProperty]
    public string phone = "0";

    string IDataErrorInfo.this[string columnName]
    {
        get
        {
            if (columnName != "Phone")
                return "";
            return string.IsNullOrEmpty(this.Phone) ? "Please specify the phone number" : "";
        }
    }
    string IDataErrorInfo.Error
    {
        get { return ""; }
    } 
}
```

### Интерфейс 'INotifyDataErrorInfo'

Интерфейс `System.ComponentModel.INotifyDataErrorInfo` позволяет реализовать пользовательские правила валидации на уровне бизнес-объекта. Интерфейс поддерживает синхронную и асинхронную валидацию, несколько ошибок на одно свойство и ошибки, зависящие от нескольких свойств.

#### Пример — реализация интерфейса 'INotifyDataErrorInfo'

Следующий пример показывает, как реализовать интерфейс `INotifyDataErrorInfo` для бизнес-объекта (_ProjectTask_). Интерфейс используется для определения правил валидации свойства _ProjectTask.EstimateTime_. Когда значение свойства нарушает правила валидации, элемент управления TreeList отображает ошибку в соответствующей ячейке.

Приведённая ниже реализация интерфейса `INotifyDataErrorInfo` поддерживает одновременно несколько ошибок для одного свойства.

![treelist-validation-inotifydataerrorinfo](../../images/treelist-validation-inotifydataerrorinfo.png)

``` xml
<mxtl:TreeListControl x:Name="treeList" ItemsSource="{Binding Tasks}"...>
    <mxtl:TreeListColumn FieldName="EstimateTime" Header="Estimate Time (h)" Width="*" />
</mxtl:TreeListControl>
```

``` csharp
public partial class TreeListDataEditorsPageViewModel : PageViewModelBase
{
    //...
    public List<ProjectTask> Tasks { get; }
}


public partial class ProjectTask : ObservableObject, INotifyDataErrorInfo
{
    public ProjectTask(ProjectTask parent, string description, TaskStatus status, 
      int estimateTime, int timeSpent, string assignee, DateTime dueDate)
    {
        Tasks = new();
        Parent = parent;
        this.estimateTime = estimateTime;
        //...
    }

    [ObservableProperty]
    private int estimateTime;


    private Dictionary<string, List<string>> propertyErrors = new Dictionary<string, List<string>>();

    partial void OnEstimateTimeChanged(int oldValue, int newValue) => ValidateEstimateTime();

    public bool HasErrors => propertyErrors.Any();

    public event EventHandler<DataErrorsChangedEventArgs> ErrorsChanged;

    public System.Collections.IEnumerable GetErrors(string propertyName)
    {
        if (propertyErrors.ContainsKey(propertyName))
            return propertyErrors[propertyName];
        else
            return null;
    }

    private void RaiseErrorsChanged(string propertyName)
    {
        ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(propertyName));
    }

    private void ValidateEstimateTime()
    {
        ClearErrors(nameof(EstimateTime));

        if (EstimateTime < 1)
            AddError(nameof(EstimateTime), "The Estimate Time cannot be less than 1.");
        if (EstimateTime > 800)
            AddError(nameof(EstimateTime), "The Estimate Time cannot be greater than 800");
            
    }

    private void AddError(string propertyName, string error)
    {
        if (!propertyErrors.ContainsKey(propertyName))
            propertyErrors[propertyName] = new List<string>();

        if (!propertyErrors[propertyName].Contains(error))
        {
            propertyErrors[propertyName].Add(error);
            RaiseErrorsChanged(propertyName);
        }
    }

    private void ClearErrors(string propertyName)
    {
        if (propertyErrors.ContainsKey(propertyName))
        {
            propertyErrors.Remove(propertyName);
            RaiseErrorsChanged(propertyName);
        }
    }

    public ProjectTask Parent { get; }
    public List<ProjectTask> Tasks { get; }
    //...
}
```

## Событие контрола 'ValidateCellValue'

Событие `DataControlBase.ValidateCellValue` позволяет реализовать пользовательскую логику валидации значений.

Возникновение события `DataControlBase.ValidateCellValue` — это обязательный этап механизма валидации, вызываемый после того, как пользователь изменил значение ячейки.

Механизм валидации также используется для проверки корректности вновь отображаемых ячеек и ячеек, обновлённых в коде. В этом случае событие `DataControlBase.ValidateCellValue` возникает только в том случае, если унаследованное свойство `DataControlBase.ValidateCellValuesOnShowAndUpdate` имеет значение `true` (значение по умолчанию — `false`).

### Пример 

В следующем примере обрабатывается событие `ValidateCellValue`, чтобы отображать ошибки, когда значение свойства _Date1_ больше значения свойства _Date2_.

``` csharp
public partial class Department : ObservableObject, IDataErrorInfo
{
    [ObservableProperty]
    public DateTime date1 = new DateTime();

    [ObservableProperty]
    public DateTime date2 = new DateTime();
}

treeList1.ValidateCellValue += TreeList1_ValidateCellValue;

// Uncomment the following code line to use the ValidateCellValue event handler
// to check cells when they are displayed or modified in code:

// treeList1.ValidateCellValuesOnShowAndUpdate = true;

private void TreeList1_ValidateCellValue(object? sender, TreeListValidateCellValueEventArgs e)
{
    Department dep = e.Node.Content as Department;
        
    if(e.Column.FieldName == "Date1")
    {
        DateTime value1 = Convert.ToDateTime(e.Value);
        DateTime value2 = dep.Date2;
        if(value1 > value2)
        {
            e.ErrorContent = "Date1 must be less than Date2";
            return;
        }
    }
}
```

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
