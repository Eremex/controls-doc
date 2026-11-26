---
title: CheckEditor
order: 116000
seealso: []
---

# CheckEditor

Контрол [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md) отображает флажок, который пользователь может переключать мышью и клавиатурой. В режиме по умолчанию редактор поддерживает два состояния нажатия (установленное и сброшенное). При необходимости вы можете включить неопределённое состояние.

![checkeditor](../../images/checkeditor.png)

Основные возможности контрола включают:

- Вы можете выбирать между двумя или тремя состояниями нажатия.
- Отображение надписи рядом с флажком.
- Пользователь может переключать контрол мышью и клавиатурой.
- Механизм валидации изменяет внешний вид контрола для информирования пользователей об ошибках.

## Состояние нажатия

Пользователь может переключать CheckEditor мышью. Если редактор в фокусе, пользователь может нажать клавишу Space или Enter на клавиатуре, чтобы изменить состояние нажатия.

В коде вы можете задать состояние нажатия или прочитать текущее состояние с помощью свойства [`CheckEditor.IsChecked`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor/IsChecked.md) или [`CheckEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md). Эти свойства синхронизированы. Они различаются типом значения: свойство [`IsChecked`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor/IsChecked.md) имеет тип nullable `bool`, тогда как свойство [`EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) имеет тип `object`, как во всех редакторах Eremex.

## Отображаемый текст

Контрол [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md) может отображать текст справа от флажка. Используйте свойство [`Content`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor/Content.md), чтобы задать этот текст.

### Пример - как создать CheckEditor

Этот пример определяет объект [`CheckEditor`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor.md), который управляет состоянием Enabled контрола TreeList. Пользователь не может редактировать данные TreeList, если флажок не установлен.

![checkeditor-sample](../../images/checkeditor-sample.png)

``` xml
xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
xmlns:mxtl="https://schemas.eremexcontrols.net/avalonia/treelist"

<mxe:CheckEditor IsChecked="{Binding IsEnabled, ElementName=treeList1}" Content="Edit Data"/>

<mxtl:TreeListControl Name="treeList1">...</mxtl:TreeListControl>
```

## Включение трех состояний

Включите свойство [`IsThreeState`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor/IsThreeState.md), чтобы позволить редактору иметь три состояния. 
Последовательные переключения редактора чередуют установленное, неопределённое и сброшенное состояния.

В неопределённом состоянии свойства [`CheckEditor.IsChecked`](../../API/Eremex.AvaloniaUI.Controls.Editors/CheckEditor/IsChecked.md) и [`CheckEditor.EditorValue`](../../API/Eremex.AvaloniaUI.Controls.Editors/BaseEditor/EditorValue.md) возвращают `null`.


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
