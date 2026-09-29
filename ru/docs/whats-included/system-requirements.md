---
title: Системные требования
order: 100
seealso: []
---

# Системные требования

В этом разделе описаны системные требования для использования библиотеки Eremex Avalonia UI Controls.

## Фреймворк


| Версия EMX Controls | .NET |  Фреймворк Avalonia UI |
| --- | --- | --- |
| **v1.4+** | 8.0+ | v12+ |
| **v1.2.95+** | 8.0+ | v11.3.8+ |
| **v1.2.63-1.2.92** | 8.0+ | v11.3.3 |
| **v1.1** | 6.0+ | v11.2.2+ |
| **v1.0** | 6.0+ | v11.0.10+ |
    

## Инструменты разработки

IDE с поддержкой Avalonia UI:

- Visual Studio 2022 и выше
- JetBrains Rider 2021.3 и выше

## Поддерживаемые операционные системы

- Windows
    - Windows 11
    - Windows 10
- Linux
    - Ubuntu
    - Debian
- Российские ОС на базе Linux:
    - ALT Linux <br>
    - Astra Linux  <sup>&ast;</sup><br>
    <sup>&ast;</sup>Включая редакции ОС, оптимизированные для процессора Эльбрус.
    - RED OS <br>
- macOS
- WebAssembly    


## Использование Graphics3DControl на macOS

[Graphics3DControl](../controls/graphics3dcontrol/index.md) использует API Vulkan для отрисовки 3D-графики. В настоящее время стандартные графические драйверы macOS не поддерживают API Vulkan. Вы можете установить пакет среды выполнения MoltenVK, чтобы запускать приложения на основе Vulkan (в том числе приложения с `Graphics3DControl`) на macOS. 

Вы также можете установить Vulkan SDK, который включает пакет MoltenVK, чтобы разрабатывать приложения Vulkan на macOS. Дополнительную информацию смотрите по ссылке:
[https://github.com/KhronosGroup/MoltenVK](https://github.com/KhronosGroup/MoltenVK).


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
