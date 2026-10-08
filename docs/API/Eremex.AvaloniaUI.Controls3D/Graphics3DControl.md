# Graphics3DControl class

Renders interactive 3D models with the Vulkan API and lets the user navigate the scene with the mouse and the keyboard.

**Namespace:** [`Eremex.AvaloniaUI.Controls3D`](./index.md)  
**Assembly:** `Eremex.Avalonia.Controls3D.dll`  
**NuGet Package:** [Eremex.Avalonia.Controls3D](https://www.nuget.org/packages/Eremex.Avalonia.Controls3D)

## Declaration

```csharp
public class Graphics3DControl : Graphics3DControlBase, ISceneHolder
```

## Public Members

| name | description |
| --- | --- |
| [Graphics3DControl](Graphics3DControl/Graphics3DControl.md)() | Initializes a new instance of the Graphics3DControl class. |
| [AllowDefaultLight](Graphics3DControl/AllowDefaultLight.md) { get; set; } | Gets or sets whether a default light attached to the camera is used when the scene has no lights of its own. |
| [AvailableMultisamplingModes](Graphics3DControl/AvailableMultisamplingModes.md) { get; } | Gets the multisampling modes supported by the graphics device the control runs on. |
| [AxesCenter](Graphics3DControl/AxesCenter.md) { get; set; } | Gets or sets the point that the coordinate axes and the grid pass through. |
| [AxisLength](Graphics3DControl/AxisLength.md) { get; set; } | Gets or sets the length of the coordinate axes. When no value is set, the axes match the size of the scene. |
| [AxisThickness](Graphics3DControl/AxisThickness.md) { get; set; } | Gets or sets the width, in pixels, of the coordinate axes. |
| [Camera](Graphics3DControl/Camera.md) { get; set; } | Gets or sets the camera that defines the view of the scene. When no camera is assigned, the control renders the scene with its own perspective camera. |
| [CompositionMode](Graphics3DControl/CompositionMode.md) { get; set; } | Gets or sets how the rendered image is combined with the Avalonia compositor. |
| [CoordinateSystem](Graphics3DControl/CoordinateSystem.md) { get; set; } | Gets or sets the handedness of the coordinate system in which the scene geometry is defined. The value determines the direction of the camera's Z axis, and therefore the sense of rotation, panning, and zooming. |
| [CullMode](Graphics3DControl/CullMode.md) { get; set; } | Gets or sets which triangle faces are discarded before rasterization. |
| [Exposure](Graphics3DControl/Exposure.md) { get; set; } | Gets or sets the exposure multiplier applied to the image during tone mapping. Larger values make the image brighter. |
| [Gamma](Graphics3DControl/Gamma.md) { get; set; } | Gets or sets the gamma value applied to the image during tone mapping. Larger values make the image brighter. |
| [Gizmo](Graphics3DControl/Gizmo.md) { get; set; } | Gets or sets the orientation indicator rendered on top of the control. |
| [GridSpacing](Graphics3DControl/GridSpacing.md) { get; set; } | Gets or sets the distance between the grid lines. When no value is set, the grid is split into ten equal parts. |
| [GridThickness](Graphics3DControl/GridThickness.md) { get; set; } | Gets or sets the width, in pixels, of the grid lines. |
| [HighlightColor](Graphics3DControl/HighlightColor.md) { get; set; } | Gets or sets the color of the box drawn around the highlighted element. |
| [HighlightedElement](Graphics3DControl/HighlightedElement.md) { get; set; } | Gets or sets the model or mesh under the mouse pointer. It is drawn with the highlight outline. |
| [HighlightMode](Graphics3DControl/HighlightMode.md) { get; set; } | Gets or sets the level of the scene at which elements are highlighted when the mouse pointer hovers over them. |
| [KeyboardMoveStep](Graphics3DControl/KeyboardMoveStep.md) { get; set; } | Gets or sets the step used to pan the scene with the keyboard. The step is relative to the width of the control and defaults to one tenth of that width. |
| [Lights](Graphics3DControl/Lights.md) { get; } | Gets the lights that illuminate the models of the scene. |
| [LightsSource](Graphics3DControl/LightsSource.md) { get; set; } | Gets or sets the collection used to populate the lights of the control. |
| [LightTemplate](Graphics3DControl/LightTemplate.md) { get; set; } | Gets or sets the template used to create a light for each item of LightsSource. |
| [Logger](Graphics3DControl/Logger.md) { get; set; } | Gets or sets the logger that receives the messages produced by the Vulkan renderer. |
| [LogLevel](Graphics3DControl/LogLevel.md) { get; set; } | Gets or sets the minimum severity of the messages written to the logger. |
| [LookCameraAtSceneCommand](Graphics3DControl/LookCameraAtSceneCommand.md) { get; } | Gets the command that moves the camera to a predefined view of the scene. Its parameter is a CameraPosition value. |
| [MultisamplingMode](Graphics3DControl/MultisamplingMode.md) { get; set; } | Gets or sets the number of samples per pixel used for multisample antialiasing. If the graphics device does not support the value, the closest supported mode is used. |
| [NavigationBindings](Graphics3DControl/NavigationBindings.md) { get; set; } | Gets or sets the keyboard shortcuts that navigate the scene. When null, the control uses its default shortcuts. |
| [RotateStep](Graphics3DControl/RotateStep.md) { get; set; } | Gets or sets the sensitivity of mouse-driven rotation. Larger values rotate the scene more slowly. |
| [SelectedElement](Graphics3DControl/SelectedElement.md) { get; set; } | Gets or sets the selected model or mesh. It is drawn with the selection outline. |
| [SelectionColor](Graphics3DControl/SelectionColor.md) { get; set; } | Gets or sets the color of the box drawn around the selected element. |
| [SelectionMode](Graphics3DControl/SelectionMode.md) { get; set; } | Gets or sets the level of the scene at which elements are selected when the user clicks them. |
| [ShowAxes](Graphics3DControl/ShowAxes.md) { get; set; } | Gets or sets whether the coordinate axes are drawn in the scene. |
| [ShowGrid](Graphics3DControl/ShowGrid.md) { get; set; } | Gets or sets whether a grid is drawn on the coordinate planes of the scene. |
| [ShowHints](Graphics3DControl/ShowHints.md) { get; set; } | Gets or sets whether a tooltip with the hint of the highlighted element is shown. |
| [ShowInfoPanel](Graphics3DControl/ShowInfoPanel.md) { get; set; } | Gets or sets whether the panel that reports rendering statistics is displayed in the corner of the control. |
| [Skybox](Graphics3DControl/Skybox.md) { get; set; } | Gets or sets the environment map that illuminates the scene and, when visible, forms its background. |
| [ZoomRate](Graphics3DControl/ZoomRate.md) { get; set; } | Gets or sets the part of the scene size by which the camera moves on a single mouse wheel notch. |
| [Export](Graphics3DControl/Export.md)() | Creates a bitmap of the currently rendered image. |
| [HitTest](Graphics3DControl/HitTest.md)(…) | Searches the scene for the model and mesh located under the given point. |
| [LookCameraAtScene](Graphics3DControl/LookCameraAtScene.md)(…) | Moves the camera to a predefined view of the scene and places it at a distance that fits the scene into the control. (2 methods) |

## Remarks

The user rotates the scene with the left mouse button, pans it with the right mouse button, and zooms it with the mouse wheel. The keyboard shortcuts are defined by the NavigationBindings property.

## See Also

* class [Graphics3DControlBase](./Graphics3DControlBase.md)
* namespace [Eremex.AvaloniaUI.Controls3D](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls3D.dll -->
