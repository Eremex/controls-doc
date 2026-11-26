---
title: Clipboard
order: 1200
seealso: []
---

# Clipboard

DataGrid теперь поддерживает сочетание клавиш CTRL+C для копирования выделенных строк в буфер обмена.

В коде вы можете использовать метод [`CopyToClipboardAsync`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/CopyToClipboardAsync.md), чтобы скопировать выделенные строки. Этот метод является асинхронным — он немедленно возвращает объект `Task`, не дожидаясь завершения операции копирования. 
Асинхронные методы не блокируют поток пользовательского интерфейса.

- Метод [`CopyToClipboardAsync`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/CopyToClipboardAsync.md) копирует отображаемый текст ячеек выделенных строк. В режиме одиночного выделения в буфер обмена копируется сфокусированная строка. В режиме множественного выделения копируются все выделенные строки. 
- Если выделена строка группировки, она также копируется в буфер обмена. Строки, вложенные в выделенную строку группировки, не копируются, если они не выделены отдельно.
- Заголовки колонок по умолчанию копируются в буфер обмена. Установите параметр [`DataGridControl.ClipboardCopyHeaders`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ClipboardCopyHeaders.md) в значение false, чтобы предотвратить копирование заголовков колонок.
- Заголовки колонок и значения ячеек в буфере обмена разделяются символами табуляции (TAB).


## Связанный API

- [`DataControlBase.SelectionMode`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/SelectionMode.md) — позволяет включить множественное выделение строк.
- [`DataControlBase.SelectedItems`](../../API/Eremex.AvaloniaUI.Controls.DataControl/DataControlBase/SelectedItems.md) — определяет коллекцию объектов данных (бизнес-объектов), соответствующих выделенным строкам.
- [`DataGridControl.GetCellDisplayText`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/GetCellDisplayText.md) — возвращает отображаемый текст конкретной ячейки, адресуемой по строке и колонке (или имени поля).
- [`DataGridControl.ClipboardCopyHeaders`](../../API/Eremex.AvaloniaUI.Controls.DataGrid/DataGridControl/ClipboardCopyHeaders.md) — определяет, копируются ли заголовки колонок в буфер обмена.


<!-- TODO
CTRL+C ??
example for CTRL+C ?
 -->

 <!-- TODO
 create Clipboard topic for TreeList
  -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
