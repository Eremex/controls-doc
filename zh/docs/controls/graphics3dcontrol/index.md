---
title: Graphics 3D Control
order: 51000
seealso: []
---

# Graphics 3D Control

`Graphics3DControl` 允许您在 Avalonia UI 应用程序的窗口中显示一个或多个可交互的 3D 模型。该控件的渲染引擎基于 Vulkan API v1.1。

![graphics3dcontrol](../../images/graphics3dcontrol.png)

该控件支持用户与模型进行交互，允许用户使用鼠标和键盘操作对模型进行旋转、平移和缩放。

要为 `Graphics3DControl` 指定 3D 模型，请使用该控件的 API。此 API 包含用于定义顶点、网格、材质（PBR 格式）、相机设置、模型变换等的类和成员。

该控件的主要功能包括：

- 基于 Vulkan SDK 1.1 构建。请参阅[系统要求](system-requirements.md)。
- 使用 Vulkan SDK 进行 GPU 加速渲染
- 拥有用于指定 3D 模型的专用 API
- 简单材质 
- PBR 格式的贴图材质
- 同时显示多个 3D 模型
- 透视和等距相机模式
- 运行时通过鼠标和键盘对模型进行旋转、平移和缩放
- 选择并高亮显示模型元素。
- 为模型元素显示提示信息。
- 模型变换
- 支持使用 MVVM 模式指定 3D 模型

## Graphics3DControl 的绘制主题

从 EMX Controls 库 v1.3 版本开始，您必须在 _App.xaml_ 文件中注册 `Controls3D` 绘制主题才能使用 `Graphics3DControl`。此主题包含正确渲染控件所需的通用外观设置。有关更多信息，请参阅以下主题：

- [为 Graphics3DControl 注册绘制主题](get-started-with-graphics3dcontrol.md#prerequisites-register-the-paint-theme-for-the-graphics3dcontrol)


!!! note

    如果未注册 `Controls3D` 绘制主题，`Graphics3DControl` 将显示为空白。


## 演示

以下演示应用程序包含演示 `Graphics3DControl` 组件功能的示例：

- [Eremex Avalonia Controls Demo](https://github.com/Eremex/controls-demo)

## 了解更多

- [Graphics3DControl 入门](get-started-with-graphics3dcontrol.md)

- [Graphics3DControl 概述](graphics3dcontrol-overview.md)

- [系统要求](system-requirements.md)

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
