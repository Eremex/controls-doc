## Eremex.AvaloniaUI.Controls.ApplicationServices 命名空间

| 公共类型 | 说明 |
| --- | --- |
| class [AppearanceService](./AppearanceService.md) | IAppearanceService 的默认实现，用于控制正在运行的 Application 的外观。 |
| class [ApplicationLifetimeService](./ApplicationLifetimeService.md) | IApplicationLifetimeService 的默认实现，基于 Avalonia 经典桌面应用程序生命周期。 |
| static class [ApplicationServicesContext](./ApplicationServicesContext.md) | 对应用程序服务的环境访问及其组成的描述。 |
| abstract class [AvaloniaStorageDialogBase](./AvaloniaStorageDialogBase.md) | 文件对话框服务所使用的存储选择器对话框的基类。它包含所有选择器共享的设置（标题和起始文件夹），并将其转换为 Avalonia 存储提供程序选项。 |
| class [BackgroundWorkDialogService](./BackgroundWorkDialogService.md) | IBackgroundWorkDialogService 的默认实现。其行为与 [`DialogService`](./DialogService.md) 完全相同；单独设置该类型只是为了能够独立于普通对话框来解析和替换进度对话框。 |
| class [ChoiceDialogService](./ChoiceDialogService.md) | 基于 IDialogService 构建的 IChoiceDialogService 实现。 |
| class [ConfirmActionDialog](./ConfirmActionDialog.md) | [`ConfirmActionDialogViewModel`](./ConfirmActionDialogViewModel.md) 的视图。 |
| class [ConfirmActionDialogViewModel](./ConfirmActionDialogViewModel.md) | 确认或通知对话框的视图模型：可选的标题、一行或多行消息、可选的图标以及“不再显示”复选框。使用 String) 显示它，之后读取 [`DisableConfirmDialog`](./ConfirmActionDialogViewModel/DisableConfirmDialog.md)；是否持久保存该选择由应用程序决定。 |
| class [ConfirmDialogService](./ConfirmDialogService.md) | 基于 IDialogService 和 [`ConfirmActionDialogViewModel`](./ConfirmActionDialogViewModel.md) 构建的 IConfirmDialogService 实现。 |
| class [DensityOption](./DensityOption.md) | [`AppearanceService`](./AppearanceService.md) 提供的布局密度。 |
| abstract class [DialogAwareViewModel](./DialogAwareViewModel.md) | 由 IDialogService 以模态对话框形式显示的 ViewModel 的基类。它在 [`WindowAwareViewModel`](./WindowAwareViewModel.md) 的基础上，在窗口打开时构建对话框按钮。 |
| enum [DialogButtonType](./DialogButtonType.md) | 对话框按钮的类型 |
| class [DialogButtonViewModel](./DialogButtonViewModel.md) | IDialogButtonViewModel 的标准实现。对于常见按钮，请使用 `Create*` 工厂方法（它们会应用正确的标题、样式类以及默认/取消行为），并从 CreateButtons 返回结果。 |
| class [DialogChoice&lt;T&gt;](./DialogChoice-T.md) | 对话框中的单个选项：按钮标题以及按下该按钮时返回的结果。 |
| enum [DialogResult](./DialogResult.md) | 标识关闭模态对话框或消息框时所用的按钮。 |
| class [DialogService](./DialogService.md) | IDialogService 的默认实现。它将 ViewModel 承载在 [`DialogWindow`](./DialogWindow.md) 中，在对话框打开期间附加该 ViewModel，并通过 IWindowsManager 选择所有者窗口。 |
| class [DialogWindow](./DialogWindow.md) | 承载通过 IDialogService 或 IWindowService 显示的 ViewModel 的窗口。它在主体中呈现 Content，在底部呈现 ButtonsSource 中的按钮，并根据内容调整自身大小。该窗口由服务为您创建；通常没有理由直接实例化它。 |
| static class [DialogWindowClasses](./DialogWindowClasses.md) | 对话框窗口可识别的样式类的名称。将它们传递给 [`ViewLocatorAttribute`](./ViewLocatorAttribute.md) 以选择承载 ViewModel 的窗口的外观，而无需在每个调用位置重复字面字符串。 |
| class [DialogWindowItemsControl](./DialogWindowItemsControl.md) | [`DialogWindow`](./DialogWindow.md) 的页脚，承载 ButtonsSource 中的按钮，并为每个 ButtonType 创建一个 Button 或 CheckBox。它是公开的，以便 UI 测试可以定位对话框的按钮；通常没有理由直接使用它。 |
| class [DispatcherService](./DispatcherService.md) | IDispatcherService 的默认实现，基于 Avalonia UI 线程调度程序。 |
| enum [DockType](./DockType.md) | 对话框按钮的停靠方向 |
| class [ExternalProcessService](./ExternalProcessService.md) | IExternalProcessService 的默认实现。它通过系统外壳打开目标：在 Windows 上使用 `ShellExecute`，在其他平台上使用 `xdg-open`。 |
| class [FileDialogFileType](./FileDialogFileType.md) | 文件对话框提供的一种文件类型：显示名称及其匹配的模式。 |
| enum [FileDialogFolder](./FileDialogFolder.md) | 无需知道路径即可让文件对话框定位到的文件夹。 |
| static class [FileDialogServiceExtensions](./FileDialogServiceExtensions.md) | 文件对话框服务的简化形式，仅接受选项，或以 Avalonia TopLevel 形式接受所有者，适用于不使用 IWindow 约定的代码。不是 Window 的顶级窗口不提供所有者，因此使用活动应用程序窗口。 |
| interface [IActionWindow](./IActionWindow.md) | 支持操作的窗口（对话框等）的标记接口 |
| interface [IAppearanceOption](./IAppearanceOption.md) | [`IAppearanceService`](./IAppearanceService.md) 提供的一个选项：浅色/深色变体、调色板或布局密度。 |
| interface [IAppearanceService](./IAppearanceService.md) | 列出应用程序提供的外观选项并应用所选选项。 |
| interface [IApplicationLifetimeService](./IApplicationLifetimeService.md) | 跟踪应用程序生命周期：在应用程序停止时发出信号，并按请求将其关闭，使视图模型代码无需直接引用 UI 框架的应用程序生命周期即可观察和触发关闭。 |
| interface [IApplicationSettingsService](./IApplicationSettingsService.md) | 以键为地址存储应用程序设置，例如确认对话框的“不再显示”选择或上次使用的文件夹。 |
| interface [IBackgroundWorkDialogService](./IBackgroundWorkDialogService.md) | 专用于报告后台操作进度的对话框的 [`IDialogService`](./IDialogService.md)。其行为与 [`IDialogService`](./IDialogService.md) 相同，但它是一个独立的约定，因此进度对话框可以独立于普通对话框进行解析和替换。 |
| interface [IChoiceDialogService](./IChoiceDialogService.md) | 显示带有任意按钮集的对话框，并返回所按按钮的结果。 |
| interface [IConfirmDialogService](./IConfirmDialogService.md) | 显示带有“不再显示”复选框的确认或通知对话框，并遵从用户的选择：一旦勾选该复选框并作答，具有相同键的对话框将不再显示，而是返回记住的答案。 |
| interface [IDialogAwareViewModel](./IDialogAwareViewModel.md) | 由通过 [`IDialogService`](./IDialogService.md) 以模态对话框形式显示的 ViewModel 实现。它在 [`IWindowAwareViewModel`](./IWindowAwareViewModel.md) 已描述的内容基础上添加了对话框按钮。 |
| interface [IDialogButtonViewModel](./IDialogButtonViewModel.md) | 描述对话框底部的单个按钮：外观、位置以及按下时执行的操作。对话框通过 [`ButtonsSource`](./IDialogAwareViewModel/ButtonsSource.md) 公开其按钮。 |
| interface [IDialogResultWindow](./IDialogResultWindow.md) | 记住其关闭结果的对话框窗口。视图模型通过 [`CloseWithResult`](./IDialogResultWindow/CloseWithResult.md) 关闭其窗口，使结果除了模态显示外，也可从 [`Result`](./IDialogResultWindow/Result.md) 获得；当对话框以非模态方式显示（例如在应用程序启动期间、所有者窗口尚不存在时）这一点很重要。 |
| interface [IDialogService](./IDialogService.md) | 从 ViewModel 代码中显示应用程序对话框，使 ViewModel 无需引用任何窗口类型即可向用户提问。承载 ViewModel 的 View 通过 [`ViewLocatorAttribute`](./ViewLocatorAttribute.md) 定位，所有者窗口由实现选择。 |
| interface [IDispatcherService](./IDispatcherService.md) | 将工作封送到 UI 线程，使视图模型代码无需直接引用 UI 框架的调度程序即可更新 UI。 |
| interface [IExternalProcessService](./IExternalProcessService.md) | 使用操作系统外壳打开文件、文件夹和链接，使视图模型代码无需处理平台进程 API。 |
| interface [IMessageBoxService](./IMessageBoxService.md) | 从不得引用任何窗口类型的 ViewModel 代码中显示标准消息框（一小段文本、一个图标和一组固定按钮）。 |
| interface [IMultiThreadedDispatcherService](./IMultiThreadedDispatcherService.md) | 将工作封送到 UI 线程并等待其完成，适用于必须知道 UI 线程工作何时完成的调用方。 |
| class [InMemoryApplicationSettingsService](./InMemoryApplicationSettingsService.md) | IApplicationSettingsService 的默认实现：仅在进程生命周期内保留这些值。 |
| interface [IOpenFileDialogService](./IOpenFileDialogService.md) | 从不得引用任何窗口类型的 ViewModel 代码中显示平台的打开文件对话框。 |
| interface [ISaveFileDialogService](./ISaveFileDialogService.md) | 从不得引用任何窗口类型的 ViewModel 代码中显示平台的保存文件对话框。 |
| interface [ISplashScreenService](./ISplashScreenService.md) | 在应用程序启动期间显示并更新应用程序启动画面。默认实现是通用的；应用程序通过派生它来提供自己的品牌。 |
| interface [IStartupDialogService](./IStartupDialogService.md) | 用于在应用程序启动期间、主窗口出现之前显示的对话框的 [`IDialogService`](./IDialogService.md)。当没有窗口可作为对话框的所有者时，该服务以非模态方式显示对话框，并运行本地事件循环直到其关闭，因此仍可返回结果。 |
| interface [IWindow](./IWindow.md) | 这些服务所看到的应用程序窗口。ViewModel 从 [`IWindowsManager`](./IWindowsManager.md) 获取窗口，并将其作为所请求对话框的所有者传回，而无需指明 UI 框架的任何窗口类型。 |
| interface [IWindowAwareViewModel](./IWindowAwareViewModel.md) | 由在自己的窗口中显示的 ViewModel 实现。窗口服务在显示窗口之前调用 [`Attach`](./IWindowAwareViewModel/Attach.md)，在窗口关闭之后调用 [`Detach`](./IWindowAwareViewModel/Detach.md)，这使 ViewModel 能够观察其窗口而不依赖任何窗口类型。 |
| interface [IWindowService](./IWindowService.md) | 从 ViewModel 代码中显示非模态应用程序窗口，使 ViewModel 无需引用任何窗口类型即可打开窗口。模态对话框对应的服务是 [`IDialogService`](./IDialogService.md)。 |
| interface [IWindowsManager](./IWindowsManager.md) | 跟踪应用程序的窗口，以便其他服务知道新对话框属于哪个窗口。实现会跟踪窗口的激活和关闭，因此在整个应用程序生命周期内应只存在一个实例。 |
| class [JsonFileApplicationSettingsService](./JsonFileApplicationSettingsService.md) | IApplicationSettingsService 的默认实现：将这些值保存在当前用户应用程序数据文件夹中的 JSON 文件里，因此它们在应用程序重启后仍然保留。 |
| class [MessageBoxService](./MessageBoxService.md) | IMessageBoxService 的默认实现。它通过 IWindowsManager 解析所有者窗口，并显示 Eremex 消息框。 |
| static class [MessageBoxServiceExtensions](./MessageBoxServiceExtensions.md) | 针对常见情形的 MessageBoxIcon) 的简短形式，以及供已持有 Avalonia TopLevel 的代码使用、以其作为所有者的形式。不是 Window 的顶级窗口不提供所有者，因此使用活动应用程序窗口。 |
| class [MultiThreadedDispatcherService](./MultiThreadedDispatcherService.md) | IMultiThreadedDispatcherService 的默认实现，基于 Avalonia UI 线程调度程序。 |
| abstract class [OkCancelDialogAwareViewModel](./OkCancelDialogAwareViewModel.md) | 已连接常用 OK 和 Cancel 按钮的对话框的基类：OK 以 Ok 结果关闭对话框，Cancel 以 Cancel 结果关闭对话框。 |
| class [OpenFileDialogOptions](./OpenFileDialogOptions.md) | 配置由 [`IOpenFileDialogService`](./IOpenFileDialogService.md) 显示的打开文件对话框。所有属性都是可选的；未设置的属性保持平台默认值。 |
| class [OpenFileDialogService](./OpenFileDialogService.md) | IOpenFileDialogService 的默认实现。它通过 IWindowsManager 解析所有者窗口，并显示平台的打开文件对话框。 |
| class [PaletteOption](./PaletteOption.md) | [`AppearanceService`](./AppearanceService.md) 提供的调色板。 |
| class [SaveFileDialogOptions](./SaveFileDialogOptions.md) | 配置由 [`ISaveFileDialogService`](./ISaveFileDialogService.md) 显示的保存文件对话框。所有属性都是可选的；未设置的属性保持平台默认值。 |
| class [SaveFileDialogService](./SaveFileDialogService.md) | ISaveFileDialogService 的默认实现。它通过 IWindowsManager 解析所有者窗口，并显示平台的保存文件对话框。 |
| class [SimpleServiceProvider](./SimpleServiceProvider.md) | 不依赖任何 DI 容器的最小 IServiceProvider 实现。适用于不需要完整容器的应用程序和测试。使用容器的应用程序以自己的方式注册服务，请参阅 [`RegisterApplicationServices`](./ApplicationServicesContext/RegisterApplicationServices.md)。 |
| class [SplashScreen](./SplashScreen.md) | 由 [`SplashScreenService`](./SplashScreenService.md) 显示的通用、不含品牌信息的启动画面窗口。它绑定到 [`SplashScreenViewModel`](./SplashScreenViewModel.md)，并绘制其背景图像和文本行；应用程序通过提供派生的视图模型对其进行自定义。 |
| class [SplashScreenService](./SplashScreenService.md) | ISplashScreenService 的默认实现。它显示由 [`SplashScreenViewModel`](./SplashScreenViewModel.md) 驱动的通用 [`SplashScreen`](./SplashScreen.md) 窗口。应用程序通过派生此服务并重写 CreateViewModel 以返回已配置（也可以是派生的）视图模型来添加自己的品牌。 |
| class [SplashScreenViewModel](./SplashScreenViewModel.md) | 通用启动画面的视图模型。它仅承载呈现数据，不含应用程序品牌；应用程序通过派生它并在其构造函数中为属性（背景图像、版本、版权）赋值来提供品牌。 |
| class [StartupDialogService](./StartupDialogService.md) | IStartupDialogService 的默认实现。它像 [`DialogService`](./DialogService.md) 一样将视图模型承载在 [`DialogWindow`](./DialogWindow.md) 中，但允许没有所有者窗口：在应用程序启动期间、尚无任何窗口时，它以非模态方式显示对话框，并运行本地事件循环直到其关闭，因此仍会返回结果。 |
| class [ThemeOption](./ThemeOption.md) | [`AppearanceService`](./AppearanceService.md) 提供的浅色/深色变体。 |
| class [ViewLocatorAttribute](./ViewLocatorAttribute.md) | 应用于 ViewModel，用于声明由哪个 View 呈现它以及承载窗口应具有何种外观。窗口服务在显示 ViewModel 时读取此特性，创建 View 并将其放入 [`Content`](./IWindowAwareViewModel/Content.md)，因此 ViewModel 永远无需自行构造 View。 |
| class [WindowAwareViewModel](./WindowAwareViewModel.md) | 由 IWindowService 或 IDialogService 在其自身窗口中显示的 ViewModel 的基类。它跟踪 ViewModel 所附加的窗口，根据请求关闭窗口，并创建由 ViewLocatorAttribute 声明的 View。 |
| static class [WindowInterop](./WindowInterop.md) | 在与框架无关的 IWindow 协定和 Avalonia 窗口之间进行转换。 |
| class [WindowManager](./WindowManager.md) | IWindowsManager 的默认实现。它跟踪窗口激活以了解哪个窗口处于活动状态，并禁用模态对话框后面的窗口，使用户只能与对话框交互；在 Windows 和 X11 上，如果有可用的平台机制，则使用该机制。 |
| class [WindowService](./WindowService.md) | IWindowService 的默认实现。它将 ViewModel 承载在以非模态方式显示的 [`DialogWindow`](./DialogWindow.md) 中，并在窗口关闭后自动分离 ViewModel，包括用户通过标题栏按钮关闭窗口的情况。 |

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls.ApplicationServices.dll -->
<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Common.Contracts.dll -->

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
