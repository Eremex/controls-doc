---
title: TextEditor
order: 120000
seealso: []
---

# TextEditor

Контрол [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) предоставляет базовые возможности редактирования текста. Он поддерживает маски, которые позволяют ограничивать ввод пользователя и форматировать значения.

![texteditor](../../images/texteditor.png)

Основные возможности контрола включают:

- Поддержку однострочного и многострочного текста.
- Перенос текста.
- Использование масок для задания шаблона ввода данных.
- Использование масок для форматирования значений, когда редактор не в фокусе.
- Выделение текста.
- Водяные знаки

## Задание текста и настройка параметров текста

Свойство [`TextEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) задаёт текст редактора. Если текст содержит символы _NewLine_, редактор отображает текст на нескольких строках. 

### Перенос текста

Свойство [`TextEditor.TextWrapping`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/TextWrapping.md) позволяет активировать автоматический перенос текста у правого края редактора. Установите это свойство в значение `Avalonia.Media.TextWrapping.Wrap`, чтобы включить обычный режим переноса текста.

### Приём клавиш _Tab_ и _Enter_ при вводе

Пользователи могут нажимать клавиши _Tab_ и _Enter_, чтобы вставлять символы _Tab_ и _Return_ в текст. Вы можете использовать следующие опции, чтобы изменить это поведение:

- [`TextEditor.AcceptsReturn`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/AcceptsReturn.md) — задаёт, вставляется ли символ _NewLine_ при нажатии клавиши _Enter_. Если это свойство отключено, редактор игнорирует клавишу _Enter_.
- `TextEditor.AcceptsTab` — задаёт, вставляется ли символ табуляции при нажатии клавиши _Tab_. Если это свойство отключено, фокус перемещается на следующий контрол в порядке табуляции при нажатии клавиши _Tab_.

## Маски

[Маска](masks/index.md), применённая к текстовому редактору, направляет пользователя вводить значения в соответствии с заданным шаблоном. Ввод с маской по умолчанию включён для контролов [DateEditor](dateeditor.md) и [SpinEditor](spineditor.md) и отключён для других текстовых редакторов. 

Чтобы включить ввод с маской, сделайте следующее:

- Установите свойство [`TextEditor.MaskType`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskType.md) в тип маски.
- Установите свойство [`TextEditor.Mask`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Mask.md) в маску.

### Тип маски 

Свойство [`TextEditor.MaskType`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskType.md) позволяет выбрать режим маски из следующих опций:

- [`MaskType.Numeric`](../../API/Eremex.AvaloniaUI.Controls.Editors/MaskType.md) — режим маски, предназначенный для приёма числовых значений.
- [`MaskType.DateTime`](../../API/Eremex.AvaloniaUI.Controls.Editors/MaskType.md) — режим маски, предназначенный для приёма значений даты-времени.
- [`MaskType.None`](../../API/Eremex.AvaloniaUI.Controls.Editors/MaskType.md) — ввод с маской отключён.

### Строки маски

Используйте свойство [`TextEditor.Mask`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Mask.md), чтобы задать строку, определяющую маску. Маска составляется из спецификаторов маски, специфичных для выбранного типа маски.

Дополнительную информацию смотрите в следующих разделах:

- [Маски](masks/index.md)
- [Числовые маски](masks/numeric-masks.md)
- [Маски даты и времени](masks/date-time-masks.md)

#### Пример - разрешение ввода целочисленных значений в текстовом редакторе

Следующий код применяет числовую маску "_d_", чтобы ограничить ввод данных целочисленными значениями в TextEditor.

![texteditor-numericmask-d](../../images/texteditor-numericmask-d.png)

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:TextEditor Name="textEditor1" MaskType="Numeric" Mask="d" 
 HorizontalContentAlignment="Right"/>
```

### Использование маски как формата отображения

Маску, заданную свойством [`TextEditor.Mask`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Mask.md), можно использовать для форматирования значения редактора в режиме отображения (когда редактирование текста не активно). Эту настройку задаёт свойство [`TextEditor.MaskUseAsDisplayFormat`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskUseAsDisplayFormat.md). Значение свойства по умолчанию — `true`.

### Настройки культуры маски

Многие маски зависят от текущей культуры. Например, десятичный разделитель для числовых масок различается в разных культурах. Значения даты-времени форматируются с использованием специфичных для культуры шаблонов и локализованных названий дней недели и месяцев.

Свойство [`TextEditor.MaskCulture`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/MaskCulture.md) позволяет задать культуру, используемую маской. Если это свойство не задано, используется культура приложения по умолчанию.

#### Пример 

Следующий код задаёт числовую маску "c" для ввода денежных значений в текстовом редакторе и применяет к маске культуру _китайскую (упрощённую)_.

![texteditor-mask-currency-chinese](../../images/texteditor-mask-currency-chinese.png)

``` csharp
textEditor1.EditorValue = 12.34567;
textEditor1.MaskType = Eremex.AvaloniaUI.Controls.Editors.MaskType.Numeric;
textEditor1.MaskCulture = new CultureInfo("zh-CN");
textEditor1.Mask = "c";
```

## Выделение текста

Пользователь может выделять текст с помощью мыши и клавиатуры. 

Чтобы выделить часть текста и очистить выделение в коде, используйте следующий API:

- [`TextEditor.SelectionStart`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/SelectionStart.md) — индекс (начиная с нуля) начального символа выделения текста.
- [`TextEditor.SelectionEnd`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/SelectionEnd.md) — индекс (начиная с нуля) конечного символа выделения текста.
- [`TextEditor.SelectAll`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/SelectAll.md) — выделяет весь текст.
- [`TextEditor.ClearSelection`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/ClearSelection.md) — снимает выделение с выделенного текста.

## Водяные знаки

Контрол [`TextEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor.md) и его потомки поддерживают водяные знаки. Водяной знак — это серая подсказка, отображаемая, когда значение редактора пусто или равно null.

![texteditor-watermark](../../images/texteditor-watermark.png)

Используйте свойство [`TextEditor.Watermark`](../../API/Eremex.AvaloniaUI.Controls.Editors/TextEditor/Watermark.md), чтобы задать водяной знак.

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"

<mxe:TextEditor Name="textEditor1" Watermark="Type to search"/>
```


## Смотрите также

- [Как создать текстовое поле для ввода пароля](examples/How-to-create-a-password-text-box.md)


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
