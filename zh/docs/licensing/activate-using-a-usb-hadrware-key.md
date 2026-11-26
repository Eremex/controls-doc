---
title: 使用 USB 硬件密钥激活（USB 加密狗）
order: 70
seealso: []
---

### 使用 USB 硬件密钥激活（USB 加密狗） {#activate-using-a-usb-hardware-key-usb-dongle}

1. 在目标计算机上安装 [_Guardant Control Center_ (GCC)](activate-and-manage-local-licenses.md#license-management-utilities)（对于[本地许可证](activate-and-manage-local-licenses.md)为开发者的计算机，对于[网络许可证](activate-and-manage-network-licenses.md)为服务器）。

2. 将 Guardant USB 加密狗插入计算机的 USB 端口。


#### 在 Windows 系统上安装加密狗 {#install-a-dongle-on-a-windows-system}

新型号的 Guardant 加密狗可以在 Windows 操作系统上以 HID 模式工作，无需安装额外的驱动程序。

将 HID 模式的加密狗连接到计算机的 USB 端口时，系统会将其识别为标准 HID 兼容设备。_Guardant Dongle License Service_ 应处于运行状态。


#### 在 Linux 系统上安装加密狗 {#install-a-dongle-on-a-linux-system}

从 Guardant Sign 开始的所有新型号 Guardant 加密狗均支持 Linux，并可在 HID 模式下工作。在 WINE 下运行的受保护 Windows 应用程序也受支持。

要在 GNU/Linux 下使用加密狗，必须添加热插拔规则。在大多数使用 2.6.x 内核的现代发行版中，热插拔由 **udev** 处理。

注意：写入 `/etc/udev/rules.d/` 需要超级用户 (root) 权限。

##### 添加 **udev** 规则 {#add-the-udev-rule}

要安装的规则取决于加密狗的工作模式：

**驱动程序模式**（以及使用 USB 设备文件系统 (usbfs) 中的设备文件时）：

``` bash
# cp etc/grdnt.udev /etc/udev/rules.d/95-grdnt.rules
```

**HID 模式**：

``` bash
# cp etc/grdnt_hid.udev /etc/udev/rules.d/95-grdnt_hid.rules
```

重新插拔加密狗（或重新启动 **udev** 服务）以使规则生效。

已安装的规则指示 **udev** 为代表 Guardant 加密狗的设备文件设置读写权限。这样系统上的所有用户都可以访问该加密狗。

#### 许可证验证 {#license-verification}

安装加密狗后，打开 GCC Web 界面 [http://localhost:3189/](http://localhost:3189/)，检查加密狗的许可证是否出现在许可证列表中。Web 界面的默认密码为 `admin`。

<sup>*</sup> 本页面使用机器翻译技术翻译。
