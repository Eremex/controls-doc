---
title: Activation Using a USB Hardware Key (USB Dongle)
order: 70
seealso: []
---

### Activate Using a USB Hardware Key (USB Dongle)

1. Install [_Guardant Control Center_ (GCC)](activate-and-manage-local-licenses.md#license-management-utilities) on the target machine (a developer's machine for a [local license](activate-and-manage-local-licenses.md), or a server for a [network license](activate-and-manage-network-licenses.md)).

2. Plug your Guardant USB dongle into a USB port on the machine.


#### Install a Dongle on a Windows System

New Guardant dongle models can work on Windows operating systems in HID mode without installing additional drivers.

When connecting a dongle in HID mode to the USB port of a computer, the system recognizes the dongle as a standard HID-compatible device. The _Guardant Dongle License Service_ should be running.


#### Install a Dongle on a Linux System

All new Guardant dongle models, starting with Guardant Sign, support Linux and can operate in HID mode. Protected Windows applications running under WINE are also supported.

To use a dongle under GNU/Linux, you must add a hotplugging rule. On most modern distributions using the 2.6.x kernel, hotplugging is handled by **udev**.

Note: Writing to `/etc/udev/rules.d/` requires superuser (root) privileges.

##### Add the **udev** Rule

The rule you install depends on the dongle's operating mode:

**Driver mode** (and when using device files from the USB device filesystem (usbfs)):

``` bash
# cp etc/grdnt.udev /etc/udev/rules.d/95-grdnt.rules
```

**HID mode**:

``` bash
# cp etc/grdnt_hid.udev /etc/udev/rules.d/95-grdnt_hid.rules
```

Re-plug the dongle (or restart the **udev** service) for the rules to take effect. 

The installed rules instruct **udev** to set read and write permissions on the device file that represents the Guardant dongle. This grants all users on the system access to the dongle.

#### License Verification

After installing the dongle, open the GCC web interface at [http://localhost:3189/](http://localhost:3189/) and check whether the dongle's license appears in the license list. The default password for the web UI is `admin`.
