---
title: 在 Astra Linux 操作系统中窗口和菜单的阴影显示不正确
order: 10000
seealso: []
---

# 在 Astra Linux 操作系统中窗口和菜单的阴影显示不正确

Eremex 的窗口和菜单默认使用透明阴影。如果操作系统中禁用了窗口透明度,窗口和菜单的阴影将无法正确显示。下面展示了菜单渲染不正确的示例:

![troubleshooting-astra-transparent-shadow-issue](../../images/troubleshooting-astra-transparent-shadow-issue.png)

要解决该问题,您可以执行以下操作之一:

1. 在操作系统中启用窗口透明度

    在 Astra Linux Fly 环境中,窗口透明度默认是禁用的。要启用它,请检查显示设置:

    ![troubleshooting-astra-transparent-shadow-enable-transp-setting](../../images/troubleshooting-astra-transparent-shadow-enable-transp-setting.png)


2. 在您的应用程序中禁用所有 Eremex 窗口和弹出窗口的透明度

    `MxSettings` 类存储了 Avalonia UI 应用程序中所有 Eremex 控件通用的全局设置。该类包含 `MxSettings.EnableWindowTransparency` 属性,用于管理 Eremex 窗口和弹出窗口的透明度以及阴影可见性。

    要自定义 `MxSettings.EnableWindowTransparency` 设置,请在 `AppBuilder.Configure` 调用链中添加 `UseEMXServices` 方法调用,如下所示:

    ``` cs
    public static AppBuilder BuildAvaloniaApp()
        => AppBuilder.Configure<App>()
            .UsePlatformDetect()
            .WithInterFont()
            .LogToTrace()
            .UseEMXServices(settings => { settings.EnableWindowTransparency = false; });
    ```

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
