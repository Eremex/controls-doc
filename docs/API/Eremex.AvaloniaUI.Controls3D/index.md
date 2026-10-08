## Eremex.AvaloniaUI.Controls3D namespace

| public type | description |
| --- | --- |
| struct [BoundingBox](./BoundingBox.md) | Represents an axis-aligned bounding box that encloses the vertices of a mesh or of a model. |
| abstract class [Camera](./Camera.md) | Serves as the base class for cameras that define the view of a scene. |
| class [CameraDirectionalLight](./CameraDirectionalLight.md) | Represents a directional light that points along the camera's viewing direction, so that it always illuminates the visible side of a surface. |
| class [CameraPointLight](./CameraPointLight.md) | Represents a point light that follows the camera, so that the scene stays evenly lit as the camera moves. |
| enum [CameraPosition](./CameraPosition.md) | Lists values that specify the direction from which the camera views the scene by default. |
| enum [CompositionMode](./CompositionMode.md) | Lists values that specify how the rendered image is combined with the Avalonia compositor. |
| enum [CoordinateSystem](./CoordinateSystem.md) | Lists values that specify the handedness of the coordinate system in which scene geometry is defined. |
| enum [CullMode](./CullMode.md) | Lists values that specify which triangle faces are discarded before rasterization. |
| class [DirectionalLight](./DirectionalLight.md) | Represents a light that illuminates the scene with parallel rays, as sunlight or moonlight does. |
| abstract class [DirectionLightBase](./DirectionLightBase.md) | Serves as the base class for lights that emit parallel rays in a single direction. |
| enum [ElementSelectionMode](./ElementSelectionMode.md) | Lists values that specify which scene element the control highlights and selects under the pointer. |
| class [GeometryModel3D](./GeometryModel3D.md) | Represents an object displayed in a scene. The object combines one or more meshes and is added to the collection of models shown by the control. |
| class [Gizmo](./Gizmo.md) | Represents the orientation indicator that a Graphics3DControl renders in one of its corners to show the direction of the parent control's camera. When the control has no models of its own, the gizmo draws coordinate axes labeled X, Y, and Z. |
| class [Graphics3DCollection&lt;T&gt;](./Graphics3DCollection-T.md) | Represents a collection of elements that a 3D graphics control uses to hold its models, materials, and lights. The collection mirrors the source assigned to the items source property of its owner, so items added to, or removed from, that source appear in the collection immediately. |
| class [Graphics3DControl](./Graphics3DControl.md) | Renders interactive 3D models with the Vulkan API and lets the user navigate the scene with the mouse and the keyboard. |
| abstract class [Graphics3DControlBase](./Graphics3DControlBase.md) | Serves as the base class for controls that render 3D models with the Vulkan API. It exposes the collections of models and materials that the renderer uploads to the graphics device. |
| class [Graphics3DKeyBinding](./Graphics3DKeyBinding.md) | Binds a keyboard gesture to a camera navigation command or to a control command. |
| class [Graphics3DKeyBindings](./Graphics3DKeyBindings.md) | Represents the set of keyboard bindings that drive the control's camera and other commands. |
| class [IsometricCamera](./IsometricCamera.md) | Represents a camera that projects the scene orthographically, as if the viewer were infinitely far away. Use it for isometric views and technical drawings. |
| abstract class [Light](./Light.md) | Serves as the base class for lights that illuminate a scene. |
| abstract class [Material](./Material.md) | Serves as the base class for materials that define how a mesh is shaded. |
| enum [MeshFillType](./MeshFillType.md) | Lists values that specify how a mesh interprets its indices to form drawing primitives. |
| class [MeshGeometry3D](./MeshGeometry3D.md) | Represents the geometry of a single mesh, which consists of a vertex buffer and a buffer of primitive indices. |
| enum [MultisamplingMode](./MultisamplingMode.md) | Lists values that specify the number of samples per pixel used for multisample antialiasing. |
| class [PerspectiveCamera](./PerspectiveCamera.md) | Represents a camera that projects the scene in perspective, so that objects farther from the camera appear smaller. |
| class [PointLight](./PointLight.md) | Represents a point light that stays at a fixed position in the scene. |
| abstract class [PointLightBase](./PointLightBase.md) | Serves as the base class for lights that emit in every direction from a single point. |
| struct [RaycastHitTestResult](./RaycastHitTestResult.md) | Represents the scene element found by a ray cast, together with the distance from the ray's origin. |
| class [SelectableElement](./SelectableElement.md) | Serves as the base class for scene elements that the control can highlight and select with the pointer. |
| class [SimplePbrMaterial](./SimplePbrMaterial.md) | Represents a material that is defined by a single base color and by scalar shading parameters, instead of by textures. |
| class [Skybox](./Skybox.md) | Represents the cube map environment used for image-based lighting and as the background of a scene. The control converts the six face images into a prefiltered environment map. |
| class [TexturedPbrMaterial](./TexturedPbrMaterial.md) | Represents a material that is defined by textures, instead of by scalar shading parameters. |

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls3D.dll -->
