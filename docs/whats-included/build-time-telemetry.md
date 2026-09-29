---
title: Build-time Telemetry
order: 50
seealso: []
---

# Build-time Telemetry


To guide the development of the Eremex Controls Library, the build process is configured to capture non-personal build-time data. This telemetry provides insight into how the Eremex Controls library is used during development, helping us deliver a superior and stable product.

## When Data is Captured

- Telemetry is captured when you build a project that uses the Eremex Controls library.
- Telemetry IS NOT captured when an application that uses the Eremex Controls library is run.


## Collected Information

The telemetry data includes:

- TimeStamp – Date and time when the build event took place.
- Machine – A unique machine identifier created by the telemetry engine. This ID is not based on your IP or MAC address.
- HasEmxLicense – Specifies whether or not an EMX Controls Library license exists.
- EmxLicenseExpirationDate – The expiration date of the present EMX Controls Library license.
- EMXControlsVersion – The EMX Controls library version.
- ProjectRootHash – A hash code calculated from the project's name. It is not possible to identify project names from these hash codes.
- Ide – The IDE name.
- CiProvider – The name of the CI system.
- OutputType – The application type.
- TFM – Target framework moniker. Examples of TFMs: "net9.0" and "net8.0".
- RID – Runtime identifier. RID values are used to identify target platforms where the application runs. Examples of RIDs: linux-x64, win-x64, or osx-x64. 
- AvaloniaMainPackageVersion – Avalonia package version.
- OSDescription – OS name and version.
- ProcessorArchitecture – CPU architecture name.

The telemetry data does not include personal information, such as username, email, IP address, MAC-address, project names, file/directory names, or any part of your codebase. 

## How to Opt Out

By leaving telemetry enabled, you provide anonymous data that helps us make informed decisions about real-world build environments. Allowing this data collection is the simplest way to contribute to product development.

However, if you choose to disable telemetry, set the EMX_TELEMETRY_OPTOUT environment variable to 1 or true.