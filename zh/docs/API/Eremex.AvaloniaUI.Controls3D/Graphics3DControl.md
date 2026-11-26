# Graphics3DControl 类

使用 Vulkan API 渲染交互式 3D 模型，并允许用户使用鼠标和键盘导航场景。

**命名空间：** [`Eremex.AvaloniaUI.Controls3D`](./index.md)  
**程序集：** `Eremex.Avalonia.Controls3D.dll`  
**NuGet 包：** [Eremex.Avalonia.Controls3D](https://www.nuget.org/packages/Eremex.Avalonia.Controls3D)

## 声明

```csharp
public class Graphics3DControl : Graphics3DControlBase, ISceneHolder
```

## 构造函数

| 名称 | 说明 |
| --- | --- |
| [Graphics3DControl](Graphics3DControl/Graphics3DControl.md)() | 初始化 Graphics3DControl 类的新实例。 |

## 属性

| 名称 | 说明 |
| --- | --- |
| [AllowDefaultLight](Graphics3DControl/AllowDefaultLight.md) { get; set; } | 获取或设置当场景没有自己的光源时，是否使用附加到相机的默认光源。 |
| [AvailableMultisamplingModes](Graphics3DControl/AvailableMultisamplingModes.md) { get; } | 获取运行控件的图形设备所支持的多重采样模式。 |
| [AxesCenter](Graphics3DControl/AxesCenter.md) { get; set; } | 获取或设置坐标轴和网格经过的点。 |
| [AxisLength](Graphics3DControl/AxisLength.md) { get; set; } | 获取或设置坐标轴的长度。未设置值时，坐标轴与场景大小相匹配。 |
| [AxisThickness](Graphics3DControl/AxisThickness.md) { get; set; } | 获取或设置坐标轴的宽度（以像素为单位）。 |
| [Camera](Graphics3DControl/Camera.md) { get; set; } | 获取或设置定义场景视图的相机。未分配相机时，控件使用自己的透视相机渲染场景。 |
| [CompositionMode](Graphics3DControl/CompositionMode.md) { get; set; } | 获取或设置如何将渲染图像与 Avalonia 合成器组合。 |
| [CoordinateSystem](Graphics3DControl/CoordinateSystem.md) { get; set; } | 获取或设置定义场景几何体的坐标系的手性。该值决定相机 Z 轴的方向，从而决定旋转、平移和缩放的方向。 |
| [CullMode](Graphics3DControl/CullMode.md) { get; set; } | 获取或设置在光栅化之前丢弃哪些三角形面。 |
| [Exposure](Graphics3DControl/Exposure.md) { get; set; } | 获取或设置在色调映射期间应用于图像的曝光乘数。值越大，图像越亮。 |
| [Gamma](Graphics3DControl/Gamma.md) { get; set; } | 获取或设置在色调映射期间应用于图像的 gamma 值。值越大，图像越亮。 |
| [Gizmo](Graphics3DControl/Gizmo.md) { get; set; } | 获取或设置在控件顶部渲染的方向指示器。 |
| [GridPlane](Graphics3DControl/GridPlane.md) { get; set; } | 获取或设置启用 ShowGrid 时绘制网格的坐标平面。 |
| [GridSpacing](Graphics3DControl/GridSpacing.md) { get; set; } | 获取或设置网格线之间的距离。未设置值时，网格被分成十等份。 |
| [GridThickness](Graphics3DControl/GridThickness.md) { get; set; } | 获取或设置网格线的宽度（以像素为单位）。 |
| [HighlightColor](Graphics3DControl/HighlightColor.md) { get; set; } | 获取或设置在突出显示的元素周围绘制的框的颜色。 |
| [HighlightedElement](Graphics3DControl/HighlightedElement.md) { get; set; } | 获取或设置鼠标指针下方的模型或网格。它以突出显示轮廓绘制。 |
| [HighlightMode](Graphics3DControl/HighlightMode.md) { get; set; } | 获取或设置鼠标指针悬停时突出显示元素所在的场景级别。 |
| [KeyboardMoveStep](Graphics3DControl/KeyboardMoveStep.md) { get; set; } | 获取或设置使用键盘平移场景的步长。该步长相对于控件的宽度，默认为该宽度的十分之一。 |
| [Lights](Graphics3DControl/Lights.md) { get; } | 获取照亮场景模型的光源。 |
| [LightsSource](Graphics3DControl/LightsSource.md) { get; set; } | 获取或设置用于填充控件光源的集合。 |
| [LightTemplate](Graphics3DControl/LightTemplate.md) { get; set; } | 获取或设置用于为 LightsSource 中的每一项创建光源的模板。 |
| [Logger](Graphics3DControl/Logger.md) { get; set; } | 获取或设置接收 Vulkan 渲染器所生成消息的记录器。 |
| [LogLevel](Graphics3DControl/LogLevel.md) { get; set; } | 获取或设置写入记录器的消息的最低严重性。 |
| [LookCameraAtSceneCommand](Graphics3DControl/LookCameraAtSceneCommand.md) { get; } | 获取将相机移到场景预定义视图的命令。其参数为 CameraPosition 值。 |
| [MultisamplingMode](Graphics3DControl/MultisamplingMode.md) { get; set; } | 获取或设置用于多重采样抗锯齿的每像素采样数。如果图形设备不支持该值，则使用最接近的受支持模式。 |
| [NavigationBindings](Graphics3DControl/NavigationBindings.md) { get; set; } | 获取或设置用于导航场景的键盘快捷方式。为 null 时，控件使用其默认快捷方式。 |
| [RotateStep](Graphics3DControl/RotateStep.md) { get; set; } | 获取或设置鼠标驱动旋转的灵敏度。值越大，场景旋转越慢。 |
| [RotationMode](Graphics3DControl/RotationMode.md) { get; set; } | 获取或设置用户按住鼠标左键拖动旋转场景时相机围绕旋转的中心点。 |
| [SelectedElement](Graphics3DControl/SelectedElement.md) { get; set; } | 获取或设置所选的模型或网格。它以选择轮廓绘制。 |
| [SelectionColor](Graphics3DControl/SelectionColor.md) { get; set; } | 获取或设置在所选元素周围绘制的框的颜色。 |
| [SelectionMode](Graphics3DControl/SelectionMode.md) { get; set; } | 获取或设置用户单击元素时选择元素所在的场景级别。 |
| [ShowAxes](Graphics3DControl/ShowAxes.md) { get; set; } | 获取或设置是否在场景中绘制坐标轴。 |
| [ShowGrid](Graphics3DControl/ShowGrid.md) { get; set; } | 获取或设置是否在场景的坐标平面上绘制网格。 |
| [ShowHints](Graphics3DControl/ShowHints.md) { get; set; } | 获取或设置是否显示包含突出显示元素提示的工具提示。 |
| [ShowInfoPanel](Graphics3DControl/ShowInfoPanel.md) { get; set; } | 获取或设置是否在控件角落显示报告渲染统计信息的面板。 |
| [Skybox](Graphics3DControl/Skybox.md) { get; set; } | 获取或设置照亮场景、并在可见时构成场景背景的环境贴图。 |
| [ZoomRate](Graphics3DControl/ZoomRate.md) { get; set; } | 获取或设置鼠标滚轮每滚动一格时相机移动的场景大小比例。 |

## 方法

| 名称 | 说明 |
| --- | --- |
| [CalcHitInfo](Graphics3DControl/CalcHitInfo.md)(…) | Returns all models and meshes that are located under the given point. |
| [Export](Graphics3DControl/Export.md)() | 创建当前渲染图像的位图。 |
| [HitTest](Graphics3DControl/HitTest.md)(…) | 在场景中搜索位于给定点下方的模型和网格。 |
| [LookCameraAtScene](Graphics3DControl/LookCameraAtScene.md)(…) | 将相机移到场景的预定义视图，并放置在使场景适合控件的距离处。（2 个重载） |

## 事件

| 名称 | 说明 |
| --- | --- |
| event [SelectionChanging](Graphics3DControl/SelectionChanging.md) | Occurs before the control applies a new selection, after the user clicks the control while SelectionMode is not None. Handlers can inspect the hit test results, replace the pending selection through the NewValue property, or cancel the change by setting Handled to true. |

## 备注

用户使用鼠标左键旋转场景，使用鼠标右键平移场景，使用鼠标滚轮缩放场景。键盘快捷方式由 NavigationBindings 属性定义。

## 另请参阅

* 类 [Graphics3DControlBase](./Graphics3DControlBase.md)
* 命名空间 [Eremex.AvaloniaUI.Controls3D](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls3D.dll -->

<br>
<br>

<sup>*</sup> 本页面使用机器翻译技术翻译。
