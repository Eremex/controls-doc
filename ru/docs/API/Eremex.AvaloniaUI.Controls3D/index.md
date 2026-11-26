## Пространство имён Eremex.AvaloniaUI.Controls3D

| открытый тип | описание |
| --- | --- |
| struct [BoundingBox](./BoundingBox.md) | Представляет ограничивающий параллелепипед, выровненный по осям, который охватывает вершины сетки или модели. |
| abstract class [Camera](./Camera.md) | Служит базовым классом для камер, определяющих вид сцены. |
| class [CameraDirectionalLight](./CameraDirectionalLight.md) | Представляет направленный источник света, направленный вдоль направления взгляда камеры, поэтому он всегда освещает видимую сторону поверхности. |
| class [CameraPointLight](./CameraPointLight.md) | Представляет точечный источник света, следующий за камерой, поэтому сцена остаётся равномерно освещённой при перемещении камеры. |
| enum [CameraPosition](./CameraPosition.md) | Перечисляет значения, задающие направление, с которого камера по умолчанию смотрит на сцену. |
| enum [CompositionMode](./CompositionMode.md) | Перечисляет значения, задающие способ объединения отрисованного изображения с компоновщиком Avalonia. |
| enum [CoordinateSystem](./CoordinateSystem.md) | Перечисляет значения, задающие направленность (правая или левая) системы координат, в которой определена геометрия сцены. |
| enum [CullMode](./CullMode.md) | Перечисляет значения, задающие, какие грани треугольников отбрасываются перед растеризацией. |
| class [DirectionalLight](./DirectionalLight.md) | Представляет источник света, освещающий сцену параллельными лучами, как солнечный или лунный свет. |
| abstract class [DirectionLightBase](./DirectionLightBase.md) | Служит базовым классом для источников света, испускающих параллельные лучи в одном направлении. |
| enum [ElementSelectionMode](./ElementSelectionMode.md) | Перечисляет значения, задающие, какой элемент сцены контрол выделяет и выбирает под указателем. |
| class [GeometryModel3D](./GeometryModel3D.md) | Представляет объект, отображаемый в сцене. Объект объединяет одну или несколько сеток и добавляется в коллекцию моделей, отображаемых контролом. |
| class [Gizmo](./Gizmo.md) | Представляет индикатор ориентации, который Graphics3DControl отображает в одном из своих углов, чтобы показать направление камеры родительского контрола. Если у контрола нет собственных моделей, гизмо отображает оси координат с подписями X, Y и Z. |
| class [Graphics3DCollection&lt;T&gt;](./Graphics3DCollection-T.md) | Представляет коллекцию элементов, в которой контрол 3D-графики хранит свои модели, материалы и источники света. Коллекция отражает источник, присвоенный свойству источника элементов её владельца, поэтому элементы, добавленные в этот источник или удалённые из него, сразу появляются в коллекции. |
| class [Graphics3DControl](./Graphics3DControl.md) | Отрисовывает интерактивные 3D-модели с помощью API Vulkan и позволяет пользователю перемещаться по сцене с помощью мыши и клавиатуры. |
| abstract class [Graphics3DControlBase](./Graphics3DControlBase.md) | Служит базовым классом для контролов, отрисовывающих 3D-модели с помощью API Vulkan. Предоставляет коллекции моделей и материалов, которые модуль отрисовки загружает на графическое устройство. |
| class [Graphics3DKeyBinding](./Graphics3DKeyBinding.md) | Связывает жест клавиатуры с командой навигации камеры или командой контрола. |
| class [Graphics3DKeyBindings](./Graphics3DKeyBindings.md) | Представляет набор привязок клавиш, управляющих камерой контрола и другими командами. |
| class [Graphics3DSelectionChangingEventArgs](./Graphics3DSelectionChangingEventArgs.md) | Provides data for the SelectionChanging event, which the Graphics3DControl raises before it applies a selection. |
| delegate [Graphics3DSelectionChangingEventHandler](./Graphics3DSelectionChangingEventHandler.md) | Represents the method that handles the SelectionChanging event of a Graphics3DControl. |
| [Flags] enum [GridPlane](./GridPlane.md) | Перечисляет значения, задающие координатные плоскости, на которых рисуется сетка. |
| class [IsometricCamera](./IsometricCamera.md) | Представляет камеру, проецирующую сцену ортографически, как если бы наблюдатель находился бесконечно далеко. Используйте её для изометрических видов и технических чертежей. |
| abstract class [Light](./Light.md) | Служит базовым классом для источников света, освещающих сцену. |
| abstract class [Material](./Material.md) | Служит базовым классом для материалов, определяющих затенение сетки. |
| enum [MeshFillType](./MeshFillType.md) | Перечисляет значения, задающие, как сетка интерпретирует свои индексы для образования примитивов отрисовки. |
| class [MeshGeometry3D](./MeshGeometry3D.md) | Представляет геометрию одной сетки, состоящую из буфера вершин и буфера индексов примитивов. |
| enum [MultisamplingMode](./MultisamplingMode.md) | Перечисляет значения, задающие количество выборок на пиксель, используемое для сглаживания методом мультисэмплинга. |
| class [PerspectiveCamera](./PerspectiveCamera.md) | Представляет камеру, проецирующую сцену в перспективе, так что объекты, расположенные дальше от камеры, выглядят меньше. |
| class [PointLight](./PointLight.md) | Представляет точечный источник света, находящийся в фиксированной позиции сцены. |
| abstract class [PointLightBase](./PointLightBase.md) | Служит базовым классом для источников света, излучающих во всех направлениях из одной точки. |
| struct [RaycastHitTestResult](./RaycastHitTestResult.md) | Представляет элемент сцены, найденный при трассировке луча, вместе с расстоянием от начала луча. |
| enum [RotationMode](./RotationMode.md) | Перечисляет значения, задающие точку, вокруг которой вращается камера, когда пользователь поворачивает сцену. |
| class [SelectableElement](./SelectableElement.md) | Служит базовым классом для элементов сцены, которые контрол может выделять и выбирать указателем. |
| class [SimplePbrMaterial](./SimplePbrMaterial.md) | Представляет материал, определяемый одним базовым цветом и скалярными параметрами затенения, а не текстурами. |
| class [Skybox](./Skybox.md) | Представляет кубическую карту окружения, используемую для освещения на основе изображений и в качестве фона сцены. Контрол преобразует шесть изображений граней в предварительно отфильтрованную карту окружения. |
| class [TexturedPbrMaterial](./TexturedPbrMaterial.md) | Представляет материал, определяемый текстурами, а не скалярными параметрами затенения. |

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls3D.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
