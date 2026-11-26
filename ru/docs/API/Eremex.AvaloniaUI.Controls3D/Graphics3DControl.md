# Класс Graphics3DControl

Отрисовывает интерактивные 3D-модели с помощью API Vulkan и позволяет пользователю перемещаться по сцене с помощью мыши и клавиатуры.

**Пространство имён:** [`Eremex.AvaloniaUI.Controls3D`](./index.md)  
**Сборка:** `Eremex.Avalonia.Controls3D.dll`  
**NuGet-пакет:** [Eremex.Avalonia.Controls3D](https://www.nuget.org/packages/Eremex.Avalonia.Controls3D)

## Объявление

```csharp
public class Graphics3DControl : Graphics3DControlBase, ISceneHolder
```

## Конструкторы

| имя | описание |
| --- | --- |
| [Graphics3DControl](Graphics3DControl/Graphics3DControl.md)() | Инициализирует новый экземпляр класса Graphics3DControl. |

## Свойства

| имя | описание |
| --- | --- |
| [AllowDefaultLight](Graphics3DControl/AllowDefaultLight.md) { get; set; } | Возвращает или задаёт, используется ли привязанный к камере источник света по умолчанию, если в сцене нет собственных источников света. |
| [AvailableMultisamplingModes](Graphics3DControl/AvailableMultisamplingModes.md) { get; } | Возвращает режимы мультисэмплинга, поддерживаемые графическим устройством, на котором работает контрол. |
| [AxesCenter](Graphics3DControl/AxesCenter.md) { get; set; } | Возвращает или задаёт точку, через которую проходят оси координат и сетка. |
| [AxisLength](Graphics3DControl/AxisLength.md) { get; set; } | Возвращает или задаёт длину осей координат. Если значение не задано, оси соответствуют размеру сцены. |
| [AxisThickness](Graphics3DControl/AxisThickness.md) { get; set; } | Возвращает или задаёт ширину осей координат в пикселях. |
| [Camera](Graphics3DControl/Camera.md) { get; set; } | Возвращает или задаёт камеру, определяющую вид сцены. Если камера не назначена, контрол отрисовывает сцену собственной перспективной камерой. |
| [CompositionMode](Graphics3DControl/CompositionMode.md) { get; set; } | Возвращает или задаёт способ объединения отрисованного изображения с компоновщиком Avalonia. |
| [CoordinateSystem](Graphics3DControl/CoordinateSystem.md) { get; set; } | Возвращает или задаёт направленность системы координат, в которой определена геометрия сцены. Значение определяет направление оси Z камеры и, следовательно, направление вращения, сдвига и масштабирования. |
| [CullMode](Graphics3DControl/CullMode.md) { get; set; } | Возвращает или задаёт, какие грани треугольников отбрасываются перед растеризацией. |
| [Exposure](Graphics3DControl/Exposure.md) { get; set; } | Возвращает или задаёт множитель экспозиции, применяемый к изображению при тональной компрессии. Большие значения делают изображение ярче. |
| [Gamma](Graphics3DControl/Gamma.md) { get; set; } | Возвращает или задаёт значение гаммы, применяемое к изображению при тональной компрессии. Большие значения делают изображение ярче. |
| [Gizmo](Graphics3DControl/Gizmo.md) { get; set; } | Возвращает или задаёт индикатор ориентации, отображаемый поверх контрола. |
| [GridPlane](Graphics3DControl/GridPlane.md) { get; set; } | Возвращает или задаёт координатные плоскости, на которых рисуется сетка, когда включено ShowGrid. |
| [GridSpacing](Graphics3DControl/GridSpacing.md) { get; set; } | Возвращает или задаёт расстояние между линиями сетки. Если значение не задано, сетка делится на десять равных частей. |
| [GridThickness](Graphics3DControl/GridThickness.md) { get; set; } | Возвращает или задаёт ширину линий сетки в пикселях. |
| [HighlightColor](Graphics3DControl/HighlightColor.md) { get; set; } | Возвращает или задаёт цвет рамки, отображаемой вокруг выделенного элемента. |
| [HighlightedElement](Graphics3DControl/HighlightedElement.md) { get; set; } | Возвращает или задаёт модель или сетку под указателем мыши. Она отображается с контуром выделения. |
| [HighlightMode](Graphics3DControl/HighlightMode.md) { get; set; } | Возвращает или задаёт уровень сцены, на котором выделяются элементы при наведении на них указателя мыши. |
| [KeyboardMoveStep](Graphics3DControl/KeyboardMoveStep.md) { get; set; } | Возвращает или задаёт шаг сдвига сцены с клавиатуры. Шаг задаётся относительно ширины контрола и по умолчанию составляет одну десятую этой ширины. |
| [Lights](Graphics3DControl/Lights.md) { get; } | Возвращает источники света, освещающие модели сцены. |
| [LightsSource](Graphics3DControl/LightsSource.md) { get; set; } | Возвращает или задаёт коллекцию, используемую для заполнения источников света контрола. |
| [LightTemplate](Graphics3DControl/LightTemplate.md) { get; set; } | Возвращает или задаёт шаблон, используемый для создания источника света для каждого элемента LightsSource. |
| [Logger](Graphics3DControl/Logger.md) { get; set; } | Возвращает или задаёт средство ведения журнала, получающее сообщения, создаваемые модулем отрисовки Vulkan. |
| [LogLevel](Graphics3DControl/LogLevel.md) { get; set; } | Возвращает или задаёт минимальный уровень серьёзности сообщений, записываемых в журнал. |
| [LookCameraAtSceneCommand](Graphics3DControl/LookCameraAtSceneCommand.md) { get; } | Возвращает команду, перемещающую камеру в предопределённый вид сцены. Её параметр — значение CameraPosition. |
| [MultisamplingMode](Graphics3DControl/MultisamplingMode.md) { get; set; } | Возвращает или задаёт количество выборок на пиксель, используемое для сглаживания методом мультисэмплинга. Если графическое устройство не поддерживает это значение, используется ближайший поддерживаемый режим. |
| [NavigationBindings](Graphics3DControl/NavigationBindings.md) { get; set; } | Возвращает или задаёт сочетания клавиш для навигации по сцене. Если равно null, контрол использует сочетания клавиш по умолчанию. |
| [RotateStep](Graphics3DControl/RotateStep.md) { get; set; } | Возвращает или задаёт чувствительность вращения мышью. Большие значения вращают сцену медленнее. |
| [RotationMode](Graphics3DControl/RotationMode.md) { get; set; } | Возвращает или задаёт точку, вокруг которой вращается камера, когда пользователь поворачивает сцену перетаскиванием с нажатой левой кнопкой мыши. |
| [SelectedElement](Graphics3DControl/SelectedElement.md) { get; set; } | Возвращает или задаёт выбранную модель или сетку. Она отображается с контуром выбора. |
| [SelectionColor](Graphics3DControl/SelectionColor.md) { get; set; } | Возвращает или задаёт цвет рамки, отображаемой вокруг выбранного элемента. |
| [SelectionMode](Graphics3DControl/SelectionMode.md) { get; set; } | Возвращает или задаёт уровень сцены, на котором выбираются элементы при щелчке по ним. |
| [ShowAxes](Graphics3DControl/ShowAxes.md) { get; set; } | Возвращает или задаёт, отображаются ли оси координат в сцене. |
| [ShowGrid](Graphics3DControl/ShowGrid.md) { get; set; } | Возвращает или задаёт, отображается ли сетка на координатных плоскостях сцены. |
| [ShowHints](Graphics3DControl/ShowHints.md) { get; set; } | Возвращает или задаёт, отображается ли всплывающая подсказка с описанием выделенного элемента. |
| [ShowInfoPanel](Graphics3DControl/ShowInfoPanel.md) { get; set; } | Возвращает или задаёт, отображается ли в углу контрола панель со статистикой отрисовки. |
| [Skybox](Graphics3DControl/Skybox.md) { get; set; } | Возвращает или задаёт карту окружения, которая освещает сцену и, если она видима, образует её фон. |
| [ZoomRate](Graphics3DControl/ZoomRate.md) { get; set; } | Возвращает или задаёт долю размера сцены, на которую перемещается камера при одном щелчке колёсика мыши. |

## Методы

| имя | описание |
| --- | --- |
| [CalcHitInfo](Graphics3DControl/CalcHitInfo.md)(…) | Returns all models and meshes that are located under the given point. |
| [Export](Graphics3DControl/Export.md)() | Создаёт растровое изображение текущего отрисованного изображения. |
| [HitTest](Graphics3DControl/HitTest.md)(…) | Ищет в сцене модель и сетку, расположенные под заданной точкой. |
| [LookCameraAtScene](Graphics3DControl/LookCameraAtScene.md)(…) | Перемещает камеру в предопределённый вид сцены и располагает её на расстоянии, при котором сцена умещается в контроле. (перегрузок: 2) |

## События

| имя | описание |
| --- | --- |
| event [SelectionChanging](Graphics3DControl/SelectionChanging.md) | Occurs before the control applies a new selection, after the user clicks the control while SelectionMode is not None. Handlers can inspect the hit test results, replace the pending selection through the NewValue property, or cancel the change by setting Handled to true. |

## Примечания

Пользователь вращает сцену левой кнопкой мыши, сдвигает её правой кнопкой и масштабирует колёсиком мыши. Сочетания клавиш задаются свойством NavigationBindings.

## См. также

* класс [Graphics3DControlBase](./Graphics3DControlBase.md)
* пространство имён [Eremex.AvaloniaUI.Controls3D](./index.md)

<!-- DO NOT EDIT: generated by xmldocmd for Eremex.Avalonia.Controls3D.dll -->

<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
