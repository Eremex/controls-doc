---
title: 系统要求
order: 100
seealso: []
---

# 系统要求

本主题描述了使用 Eremex Avalonia UI Controls 库的系统要求。

## 框架


| EMX Controls 版本 | .NET |  Avalonia UI 框架 |
| --- | --- | --- |
| **v1.4+** | 8.0+ | v12+ |
| **v1.2.95+** | 8.0+ | v11.3.8+ |
| **v1.2.63-1.2.92** | 8.0+ | v11.3.3 |
| **v1.1** | 6.0+ | v11.2.2+ |
| **v1.0** | 6.0+ | v11.0.10+ |
    

## 开发工具

支持 Avalonia UI 的 IDE：

- Visual Studio 2022 及更高版本
- JetBrains Rider 2021.3 及更高版本

## 支持的操作系统

- Windows
    - Windows 11
    - Windows 10
- Linux
    - Ubuntu
    - Debian
- 基于 Linux 的俄罗斯操作系统：
    - ALT Linux <br>
    - Astra Linux  <sup>&ast;</sup><br>
    <sup>&ast;</sup>包括针对 Elbrus 处理器优化的操作系统版本。
    - RED OS <br>
- macOS
- WebAssembly    


## 在 macOS 上使用 Graphics3DControl

[Graphics3DControl](../controls/graphics3dcontrol/index.md) 使用 Vulkan API 来渲染 3D 图形。目前，标准的 macOS 图形驱动程序不支持 Vulkan API。您可以安装 MoltenVK 运行时包，以在 macOS 上运行基于 Vulkan 的应用程序（包括使用 `Graphics3DControl` 的应用程序）。

您还可以安装包含 MoltenVK 包的 Vulkan SDK，以便在 macOS 上开发 Vulkan 应用程序。有关更多信息，请参阅以下链接：
[https://github.com/KhronosGroup/MoltenVK](https://github.com/KhronosGroup/MoltenVK)。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
