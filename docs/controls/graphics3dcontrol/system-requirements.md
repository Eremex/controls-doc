---
title: System Requirements
order: 5
seealso: []
---

# System Requirements

[`Graphics3DControl`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl.md) is built on Vulkan SDK 1.1. Vulkan employs GPU-accelerated rendering when supported by hardware. This approach delivers significantly higher performance compared to software-based rendering.

## GPU Requirements

To use GPU-accelerated rendering, your system must meet the following requirements:

- A Vulkan-compatible GPU
- A graphics driver with Vulkan 1.1 support

See the following link to check whether your GPU and GPU driver are Vulkan-compatible:

- [Devices - Vulkan Hardware Database](https://vulkan.gpuinfo.org/)


If you experience rendering issues, you can check your system for Vulkan compatibility as follows:

1. Download the Vulkan SDK 
2. Run the `vulkaninfo` executable to check for Vulkan support. 

    Refer to the following article for more details: [Checking For Vulkan Support](https://docs.vulkan.org/guide/latest/checking_for_support.html)

## Software Rendering Implementation

If GPU rendering is not available (for instance, in a virtual machine), you can use [software implementations](https://docs.vulkan.org/guide/latest/checking_for_support.html#_software_implementation) of the Vulkan API. Software rendering delivers noticeably lower performance, as it relies on CPU processing rather than GPU acceleration.
