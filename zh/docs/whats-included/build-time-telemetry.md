---
title: 构建期遥测
order: 50
seealso: []
---

# 构建期遥测


为了指导 Eremex Controls 库的开发，构建过程被配置为采集非个人的构建期数据。这些遥测数据让我们了解 Eremex Controls 库在开发过程中的实际使用情况，帮助我们提供更优质、更稳定的产品。

## 数据采集时机

- 当您生成使用 Eremex Controls 库的项目时，会采集遥测数据。
- 当运行使用 Eremex Controls 库的应用程序时，不会采集遥测数据。


## 采集的信息

遥测数据包括：

- TimeStamp — 生成事件发生的日期和时间。
- Machine — 由遥测引擎创建的唯一机器标识符。该 ID 不基于您的 IP 地址或 MAC 地址。
- HasEmxLicense — 指定是否存在 EMX Controls 库的许可证。
- EmxLicenseExpirationDate — 当前 EMX Controls 库许可证的到期日期。
- EMXControlsVersion — EMX Controls 库的版本。
- ProjectRootHash — 根据项目名称计算得出的哈希码。无法从这些哈希码中还原出项目名称。
- Ide — IDE 名称。
- CiProvider — CI 系统的名称。
- OutputType — 应用程序类型。
- TFM — 目标框架名称（Target framework moniker）。TFM 示例："net9.0" 和 "net8.0"。
- RID — 运行时标识符（Runtime identifier）。RID 值用于标识应用程序运行的目标平台。RID 示例：linux-x64、win-x64 或 osx-x64。
- AvaloniaMainPackageVersion — Avalonia 包版本。
- OSDescription — 操作系统名称和版本。
- ProcessorArchitecture — CPU 架构名称。

遥测数据不包含个人信息，例如用户名、电子邮件地址、IP 地址、MAC 地址、项目名称、文件/目录名称，或您代码库的任何部分。

## 如何选择退出

保持遥测功能启用状态，即表示您提供的匿名数据将帮助我们对真实构建环境做出明智的决策。允许收集此数据是为产品开发做出贡献的最简单方式。

但是，如果您选择禁用遥测功能，请将 EMX_TELEMETRY_OPTOUT 环境变量设置为 1 或 true。

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
