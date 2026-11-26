---
title: Итоги
order: 49900
seealso: []
---

# Итоги

[`DataGridControl`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl.md) позволяет вычислять итоги (агрегатные функции) по значениям ячеек. Поддерживаются два типа итогов:

- Общие итоги, вычисляемые по всем строкам.
- Групповые итоги, вычисляемые по группам строк, когда данные сгруппированы.

![grid-summaries](../../images/grid-summaries.png)

Основные возможности вычисления итогов:

- Встроенные функции итогов: Sum, Min, Max, Count и Average.
- Управление во время работы приложения — пользователи могут щёлкнуть кнопку Σ в ячейке нижней панели, чтобы добавить итоги или открыть диалог Summary Editor для расширенных операций с итогами.
- Несколько итогов на колонку — каждая колонка может отображать несколько саммари, вычисленных по значениям этой колонки.
- Итоги между колонками — можно вычислить итог по одной колонке и отобразить его в другой.
- Пользовательские итоги — можно обработать событие [`CustomSummary`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomSummary.md), чтобы вычислить собственную агрегатную функцию по своей логике.
- Итоги включаются в экспорт в XLSX и PDF.

## Общие итоги

Общие итоги вычисляются по всем строкам и отображаются в нижней панели контрола.

![grid-total-summaries](../../images/grid-total-summaries.png)

### Включение общих итогов

Установите свойство [`ShowTotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ShowTotalSummaries.md) в `true`, чтобы отобразить панель итогов и тем самым включить вычисление общих итогов. Панель итогов отображается в нижней части [`DataGridControl`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl.md), под всеми строками. Изначально эта панель скрыта.

```xml
<mxdg:DataGridControl x:Name="dataGrid" ShowTotalSummaries="True">...</mxdg:DataGridControl>
```

Панель итогов содержит ячейки итогов для всех колонок. Если включена [настройка итогов пользователем](#настройка-итогов-пользователем) (по умолчанию), эти ячейки содержат кнопку `Σ`, которая открывает меню итогов и редактор итогов.

![grid-summaries-sigma-button](../../images/grid-summaries-sigma-button.png)

**Связанный API**

- [`ShowTotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ShowTotalSummaries.md) — возвращает или задаёт, отображается ли панель общих итогов и включено ли вычисление общих итогов.
- [`TotalSummaryPanelMinHeight`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/TotalSummaryPanelMinHeight.md) — возвращает или задаёт минимальную высоту панели общих итогов.

### Определение общих итогов

Используйте коллекцию [`TotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/TotalSummaries.md) для определения общих итогов. Элементы этой коллекции инкапсулированы классом [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md). Каждый объект [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) задаёт поле для вычисления итога, тип итога, колонку, в которой отображается результат, и другие параметры.

```xml
xmlns:mxdc="clr-namespace:Eremex.AvaloniaUI.Controls.DataControl;assembly=Eremex.Avalonia.Controls"

<mxdg:DataGridControl x:Name="dataGrid" ShowTotalSummaries="True">
    <mxdg:DataGridControl.TotalSummaries>
        <mxdc:SummaryItem FieldName="Name" SummaryType="Count" />
        <mxdc:SummaryItem FieldName="SaleDate" SummaryType="Min" ShowInColumn="Total" />
        <mxdc:SummaryItem FieldName="SaleDate" SummaryType="Max" ShowInColumn="Total" />
        <mxdc:SummaryItem FieldName="Price" SummaryType="Min" />
        <mxdc:SummaryItem FieldName="Price" SummaryType="Max" />
        <mxdc:SummaryItem FieldName="Quantity" SummaryType="Average" />
        <mxdc:SummaryItem FieldName="Total" SummaryType="Sum" />
    </mxdg:DataGridControl.TotalSummaries>
</mxdg:DataGridControl>
```

**Связанный API**

- [`TotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/TotalSummaries.md) — предоставляет доступ к коллекции элементов итогов (объектов [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md)), определяющих общие итоги.
- [`SummaryItem.FieldName`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/FieldName.md) — возвращает или задаёт имя поля данных, значения которого используются для вычисления итога.
- [`SummaryItem.Name`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Name.md) — возвращает или задаёт имя элемента итога, по которому его можно идентифицировать. По имени можно получить элементы итогов из коллекции `TotalSummaries`.
- [`SummaryItem.Tag`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Tag.md) — возвращает или задаёт пользовательские данные, связанные с этим элементом `SummaryItem`.
- [`SummaryItem.ShowInColumn`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/ShowInColumn.md) — возвращает или задаёт имя поля колонки, которая отображает значение итога. Если свойство не задано, итог отображается в колонке, привязанной к `FieldName`.
- [`SummaryItem.SummaryType`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/SummaryType.md) — возвращает или задаёт тип агрегатной функции (`Sum`, `Min`, `Max`, `Count` или `Average`).
- [`SummaryItem.Label`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Label.md) — возвращает или задаёт пользовательскую подпись, отображаемую вместо подписи итога по умолчанию. Подпись по умолчанию показывает название функции итога. Если итог связан с другой колонкой (см. [`ShowInColumn`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/ShowInColumn.md)), подпись также показывает заголовок колонки, привязанной к [`SummaryItem.FieldName`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/FieldName.md).

    ![grid-summaries-labels](../../images/grid-summaries-labels.png)

## Групповые итоги

Групповые итоги позволяют вычислять агрегатные функции по группам строк, когда данные сгруппированы по колонкам. Групповые итоги отображаются в нижних панелях групп.

![grid-group-summaries](../../images/grid-group-summaries.png)

### Включение групповых итогов

Установите свойство [`ShowGroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ShowGroupSummaries.md) в `true`, чтобы отобразить нижние панели групповых итогов (изначально они скрыты) и тем самым включить вычисление групповых итогов. Нижние панели групповых итогов отображаются под всеми группами строк. У каждого уровня группировки своя панель.

```xml
<mxdg:DataGridControl x:Name="dataGrid" ShowGroupSummaries="True">...</mxdg:DataGridControl>
```

**Связанный API**

- [`ShowGroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ShowGroupSummaries.md) — возвращает или задаёт, отображаются ли нижние панели групп с групповыми итогами.
- [`GroupSummaryRowMinHeight`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GroupSummaryRowMinHeight.md) — возвращает или задаёт минимальную высоту нижних панелей групп.

### Определение групповых итогов

Используйте коллекцию [`GroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GroupSummaries.md) для определения групповых итогов. Как и в коллекции [`TotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/TotalSummaries.md), элементы коллекции [`GroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GroupSummaries.md) представлены классом [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md). Каждый объект [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) задаёт поле для вычисления итога, тип итога, колонку, в которой отображается результат, и другие параметры.

```xml
<mxdg:DataGridControl x:Name="dataGrid" ShowGroupSummaries="True">
    <mxdg:DataGridControl.GroupSummaries>
        <mxdc:SummaryItem FieldName="OrderId" SummaryType="Count" />
        <mxdc:SummaryItem FieldName="Quantity" SummaryType="Sum" />
        <mxdc:SummaryItem FieldName="TotalPrice" SummaryType="Sum" />
        <mxdc:SummaryItem FieldName="TotalPrice" SummaryType="Average" />
    </mxdg:DataGridControl.GroupSummaries>
</mxdg:DataGridControl>
```

**Связанный API**

- [`GroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GroupSummaries.md) — предоставляет доступ к коллекции элементов итогов (объектов [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md)), определяющих групповые итоги.
- [`SummaryItem.FieldName`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/FieldName.md) — возвращает или задаёт имя поля данных, значения которого используются для вычисления итога.
- [`SummaryItem.Name`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Name.md) — возвращает или задаёт имя элемента итога, по которому его можно идентифицировать. По имени можно получить элементы итогов из коллекции `GroupSummaries`.
- [`SummaryItem.Tag`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Tag.md) — возвращает или задаёт пользовательские данные, связанные с этим элементом `SummaryItem`.
- [`SummaryItem.ShowInColumn`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/ShowInColumn.md) — возвращает или задаёт имя поля колонки, которая отображает значение итога. Если свойство не задано, итог отображается в колонке, привязанной к `FieldName`.
- [`SummaryItem.SummaryType`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/SummaryType.md) — возвращает или задаёт тип агрегатной функции (`Sum`, `Min`, `Max`, `Count` или `Average`).
- [`SummaryItem.Label`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/Label.md) — возвращает или задаёт пользовательскую подпись, отображаемую вместо подписи итога по умолчанию. Подпись по умолчанию показывает название функции итога. Если итог связан с другой колонкой (см. [`ShowInColumn`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/ShowInColumn.md)), подпись также показывает заголовок колонки, привязанной к [`SummaryItem.FieldName`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/FieldName.md).


## Настройка итогов пользователем

По умолчанию итоги могут редактироваться пользователями. В этом режиме ячейки итогов отображают кнопку `Σ`, открывающую меню итогов:

![grid-summaries-summary-menu](../../images/grid-summaries-summary-menu.png)

Пользователи могут использовать это меню, чтобы:

- Добавлять или удалять итоги, устанавливая или снимая флажки рядом с функциями итогов.

    ![grid-summaries-summary-menu-multiple-items](../../images/grid-summaries-summary-menu-multiple-items.png)

- Выбрать `Customize`, чтобы открыть диалог `Summary Editor`.

    ![grid-summaries-summary-editor](../../images/grid-summaries-summary-editor.png)

    На вкладке `Summaries` этого диалога пользователи могут создавать итоги между колонками (итоги, вычисляемые по одной колонке, но отображаемые в другой).
    
    На вкладке `Order` пользователи могут изменять порядок отображения существующих итогов.

    ![grid-summaries-summary-editor-order-tab](../../images/grid-summaries-summary-editor-order-tab.png)


**Связанный API**

- [`AllowEditingTotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/AllowEditingTotalSummaries.md) — возвращает или задаёт, могут ли пользователи редактировать общие итоги.
- [`AllowEditingGroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/AllowEditingGroupSummaries.md) — возвращает или задаёт, могут ли пользователи редактировать групповые итоги.

Эти свойства влияют только на возможности пользователей изменять итоги и не влияют на вычисление итогов в коде.



## Пользовательские итоги

Пользовательские итоги позволяют вычислять агрегатные значения по вашей собственной логике. Можно определять пользовательские общие и пользовательские групповые итоги.

Чтобы добавить пользовательский итог, выполните следующие действия:

- Создайте объект [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) и установите его свойство [`SummaryItem.SummaryType`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem/SummaryType.md) в `Custom`.

    - Чтобы вычислить пользовательский общий итог, добавьте этот [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) в коллекцию [`TotalSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/TotalSummaries.md).
    - Чтобы вычислить пользовательский групповой итог, добавьте этот [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md) в коллекцию [`GroupSummaries`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GroupSummaries.md).

- Обработайте событие [`CustomSummary`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomSummary.md), чтобы вручную вычислить значение для этого [`SummaryItem`](../../API/Eremex.AvaloniaUI.Controls.DataControl/SummaryItem.md).

    Установите параметр события `e.SummaryValue`, чтобы передать свой результат.

    При обработке события [`CustomSummary`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomSummary.md) используйте коллекцию `e.RowIndexes` для перебора целевых строк. Элементы этой коллекции задают [индексы](rows.md#идентификация-и-получение-строк) строк, по которым вычисляется пользовательский итог. При вычислении пользовательского общего итога индексы относятся ко всем строкам DataGrid. При вычислении пользовательского группового итога событие CustomSummary возникает для каждой группы строк, а индексы в коллекции `e.RowIndexes` относятся к строкам внутри этой группы.

    Когда событие `CustomSummary` возникает для группового итога, параметр события [`IsGroupSummary`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridCustomSummaryEventArgs/IsGroupSummary.md) возвращает `true`, а параметр [`GroupRowIndex`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridCustomSummaryEventArgs/GroupRowIndex.md) задаёт [индекс](rows.md#идентификация-и-получение-строк) обрабатываемой строки группы.
    
    !!! Tip "Совет"
        
        Индексы строк позволяют обращаться к строкам при использовании построчного API DataGrid (например, [`DataGridControl.GetCellValue`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GetCellValue.md))

### Пример - вычисление пользовательского общего итога

Этот пример создаёт пользовательский общий итог, который вычисляет число заказов на сумму более $1000.

![grid-summaries-custom-summary-example](../../images/grid-summaries-custom-summary-example.png)


```xml
<!-- XAML -->
<mxdg:DataGridControl x:Name="dataGrid" CustomSummary="OnCustomSummary">
    <mxdg:DataGridControl.TotalSummaries>
        <mxdc:SummaryItem FieldName="Total" SummaryType="Custom" Label="Count (Total > $1000)" />
    </mxdg:DataGridControl.TotalSummaries>
</mxdg:DataGridControl>
```

```csharp
// Code-behind
void OnCustomSummary(object sender, DataGridCustomSummaryEventArgs e)
{
    int largeOrdersCount = 0;
    foreach (int rowIndex in e.RowIndexes)
    {
        if ((decimal)dataGrid.GetCellValue(rowIndex, e.SummaryItem.FieldName) > 1000m)
            largeOrdersCount++;
    }
    e.SummaryValue = largeOrdersCount.ToString();
}
```

**Связанный API**

- [`CustomSummary`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/CustomSummary.md) — возникает при вычислении значения итога. Используйте параметр события [`SummaryValue`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridCustomSummaryEventArgs/SummaryValue.md), чтобы передать пользовательское значение итога.


## Получение значений итогов

Вычисленные значения итогов можно получить в коде с помощью следующих методов:

- [`DataGridControl.GetTotalSummaryValue`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GetTotalSummaryValue.md) — возвращает вычисленное значение общего итога.
- [`DataGridControl.GetGroupSummaryValue`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GetGroupSummaryValue.md) — возвращает вычисленное значение группового итога для конкретной строки группы. Параметр `rowIndex` определяет индекс целевой строки группы, дочерние строки которой используются для вычисления итога.

```csharp
object? totalValue = dataGrid.GetTotalSummaryValue(summaryItem);

// Получить значение итога для первой группы строк
int rowIndex = -1; // Обратиться к первой строке группы.
object? groupValue = dataGrid.GetGroupSummaryValue(rowIndex, summaryItem);
```

## Стилизация элементов итогов

Контрол DataGrid позволяет настроить внешний вид элементов итогов. Для этого задайте стиль специального визуального контрола, который отрисовывает элементы итогов DataGrid.

### Класс целевого визуального контрола

`Eremex.AvaloniaUI.Controls.DataControl.Visuals.FooterCellItemControl`

DataContext каждого `FooterCellItemControl` — объект `FooterCellItem`.

### DataContext

`Eremex.AvaloniaUI.Controls.DataControl.Visuals.FooterCellItem`

Ниже для справки приведено определение класса `FooterCellItem`. В собственных сеттерах стилей и конвертерах можно выполнять привязку к свойствам итога (`FooterCellItem.FieldName`, `FooterCellItem.SummaryType`, `FooterCellItem.Value`, `FooterCellItem.Label` и `FooterCellItem.DisplayValue`). См. [пример](#пример---стилизация-элементов-итогов).

```csharp
/// <summary>Represents a summary value displayed in a footer cell.</summary>
public partial class FooterCellItem : ViewModelBase
{
	/// <summary>Gets or sets the summary item's label.</summary>
	[ObservableProperty] string label = string.Empty;

	/// <summary>Gets or sets the formatted summary value displayed in the footer cell.</summary>
	[ObservableProperty] string displayValue = string.Empty;

	/// <summary>Gets or sets the type of the aggregate function the summary calculates.</summary>
	public SummaryItemType SummaryType { get; set; } = SummaryItemType.None;

	/// <summary>Gets or sets the summary value.</summary>
	public object Value { get; set; }

	/// <summary>Gets or sets the name of the data field whose values the summary calculates.</summary>
	public string FieldName { get; set; }
}
```

### Шаблон отрисовки элементов итогов по умолчанию

Этот код показывает шаблон, которым элементы итогов отрисовываются по умолчанию. Этот шаблон можно найти в [исходном коде визуальной темы `DeltaDesign`](../themes/modify-control-themes.md#тема-по-умолчанию). Используйте его, чтобы составить селектор стиля для нужных элементов итога. Например, `TextBlock` с именем _Label_ отображает метку элемента итогов, а `TextBlock` с именем _DisplayValue_ — значение итога:

``` xml
<!-- DeltaDesign paint theme -->
xmlns:mxdcv="clr-namespace:Eremex.AvaloniaUI.Controls.DataControl.Visuals;assembly=Eremex.Avalonia.Controls"

<ControlTheme x:Key="{x:Type mxdcv:FooterCellItemControl}" TargetType="mxdcv:FooterCellItemControl">
    <Setter Property="Background" Value="Transparent" />
    <Setter Property="Padding" Value="{DynamicResource DataControlFooterPadding}" />
    
    <Setter Property="Template">
        <ControlTemplate TargetType="mxdcv:FooterCellItemControl">
            <DockPanel Margin="{TemplateBinding Padding}" Background="{TemplateBinding Background}">
                <TextBlock x:Name="Label"
                           Text="{Binding Label}"
                           DockPanel.Dock="Left"
                           TextTrimming="CharacterEllipsis"
                           HorizontalAlignment="Left"
                           mxc:TextBlockHelper.ShowTooltipWhenTrimming="True" />
                <TextBlock Text=" "/>
                <TextBlock x:Name="DisplayValue"
                           Text="{Binding DisplayValue}"
                           DockPanel.Dock="Right"
                           FontWeight="SemiBold"
                           TextTrimming="CharacterEllipsis"
                           HorizontalAlignment="Right"
                           mxc:TextBlockHelper.ShowTooltipWhenTrimming="True" />
            </DockPanel>
        </ControlTemplate>
    </Setter>
</ControlTheme>
```

### Пример - стилизация элементов итогов

Этот код меняет цвет двух значений итогов для колонки _Price_ в контроле DataGrid. Значение итога `Min` отображается зелёным, а значение `Max` — красным.

![datagrid-summaries-style-summaryitems](../../images/datagrid-summaries-style-summaryitems.png)

Созданный стиль применяется к текстовому блоку _DisplayValue_ в шаблоне `FooterCellItemControl` и с помощью собственного конвертера нескольких значений выбирает цвет текста по свойствам итога (`FooterCellItem.FieldName` и `FooterCellItem.SummaryType`).

```xml
xmlns:mxdg="https://schemas.eremexcontrols.net/avalonia/datagrid"

xmlns:mxdcv="clr-namespace:Eremex.AvaloniaUI.Controls.DataControl.Visuals;assembly=Eremex.Avalonia.Controls"

<mxdg:DataGridControl.Styles>
    <Style Selector="mxdcv|FooterCellItemControl /template/ TextBlock#DisplayValue" x:DataType="mxdcv:FooterCellItem">
        <Setter Property="Foreground">
          <Setter.Value>
            <MultiBinding Converter="{views:DataGridSummaryTypeToForegroundConverter}">
              <Binding Path="FieldName" />
              <Binding Path="SummaryType" />
              <DynamicResourceExtension ResourceKey="Icons/Outline/Green"/>
              <DynamicResourceExtension ResourceKey="Icons/Outline/Red"/>
            </MultiBinding>
          </Setter.Value>
        </Setter>
      </Style>                
</mxdg:DataGridControl.Styles>
```

```csharp
public class DataGridSummaryTypeToForegroundConverter : MarkupExtension, IMultiValueConverter
{
    public object Convert(IList<object> values, Type targetType, object parameter, CultureInfo culture)
    {
        if (values.Count != 4)
            return null;

        if (values[0] is string fieldName && fieldName == "Price" && values[1] is SummaryItemType sumType)
        {
            if (sumType == SummaryItemType.Min)
                return values[2];
            else if (sumType == SummaryItemType.Max)
                return values[3];
        }

        return null;
    }

    public override object ProvideValue(IServiceProvider serviceProvider)
    {
        return this;
    }
}
```

Полный код см. в [демонстрационном приложении](../../index.md#демонстрационное-приложение).

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
