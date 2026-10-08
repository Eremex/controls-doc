---
title: System Requirements
order: 100
seealso: []
---

# System Requirements

This topic describes the system requirements to use the Eremex Avalonia UI Controls library.

## Framework


| EMX Controls Version | .NET |  Avalonia UI Framework |
| --- | --- | --- |
| **v1.4+** | 8.0+ | v12+ |
| **v1.2.95+** | 8.0+ | v11.3.8+ |
| **v1.2.63-1.2.92** | 8.0+ | v11.3.3 |
| **v1.1** | 6.0+ | v11.2.2+ |
| **v1.0** | 6.0+ | v11.0.10+ |
    

## Development Tools

IDE with Avalonia UI support:

- Visual Studio 2022 and higher
- JetBrains Rider 2021.3 and higher

## Supported Operating Systems

- Windows
    - Windows 11
    - Windows 10
- Linux
    - Ubuntu
    - Debian
- Russian Linux-based OSs:
    - ALT Linux <br>
    - Astra Linux  <sup>&ast;</sup><br>
    <sup>&ast;</sup>Including OS editions optimized for the Elbrus CPU.
    - RED OS <br>
- macOS
- WebAssembly    


## Using Graphics3DControl on MacOS

[Graphics3DControl](../controls/graphics3dcontrol/index.md) uses the Vulkan API to render 3D graphics. Currently, standard MacOS graphics drivers do not support the Vulkan API. You can install the MoltenVK runtime package to run Vulkan-based applications (including applications with [`Graphics3DControl`](../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl.md)) on MacOS. 

You can also install the Vulkan SDK, which includes the MoltenVK package, to develop Vulkan applications on MacOS. See the following link for more information:
[https://github.com/KhronosGroup/MoltenVK](https://github.com/KhronosGroup/MoltenVK).