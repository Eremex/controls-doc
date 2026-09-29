---
title: 系统要求
order: 5
seealso: []
---

# 系统要求

`Graphics3DControl` 基于 Vulkan SDK 1.1 构建。当硬件支持时，Vulkan 采用 GPU 加速渲染。与基于软件的渲染相比，这种方法可提供显着更高的性能。

## GPU 要求

要使用 GPU 加速渲染，您的系统必须满足以下要求：

- 兼容 Vulkan 的 GPU
- 支持 Vulkan 1.1 的图形驱动程序

请参阅以下链接检查您的 GPU 和 GPU 驱动程序是否与 Vulkan 兼容：

- [Devices - Vulkan Hardware Database](https://vulkan.gpuinfo.org/)


如果您遇到渲染问题，您可以检查系统的 Vulkan 兼容性，如下所示：

1.下载Vulkan SDK 
2. 运行 `vulkaninfo` 可执行文件以检查 Vulkan 支持。

更多详情请参阅以下文章：[Checking For Vulkan Support](https://docs.vulkan.org/guide/latest/checking_for_support.html)

## 软件渲染实现

如果 GPU 渲染不可用（例如在虚拟机中），您可以使用 Vulkan API 的[软件实现](https://docs.vulkan.org/guide/latest/checking_for_support.html#_software_implementation)。软件渲染的性能明显较低，因为它依赖于 CPU 处理而不是 GPU 加速。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
