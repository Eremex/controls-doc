---
title: Начало работы с Graphics3DControl
order: 1000
seealso: []
---

# Начало работы с Graphics3DControl


Это руководство демонстрирует, как создать 3D-модель и отобразить её в контроле `Graphics3DControl`. Пример использует API, предоставляемый контролом, для определения сеток, вершин и материалов.

Вы можете одновременно отображать несколько 3D-моделей в `Graphics3DControl`. Это руководство создаёт одну 3D-модель. Она состоит из квадрата и двух треугольников, расположенных под прямым углом друг к другу. Каждая фигура отрисовывается с использованием своего материала.

![g3d-get-started-result](../../images/g3d-get-started-result.png)

## Предварительные требования: регистрация визуальной темы для Graphics3DControl

Начиная с версии 1.3, общие настройки внешнего вида для `Graphics3DControl` задаются визуальной темой `Controls3D`. Эти настройки включают выравнивание контрола, состояние фокусируемости, цвет фона и рамки, настройки гизмо и т. д. Визуальная тема `Controls3D` определена в той же сборке, что и сам контрол `Graphics3DControl`. Чтобы обеспечить корректную отрисовку `Graphics3DControl`, вам нужно зарегистрировать эту тему в файле _App.xaml_, как показано ниже:

- Откройте файл _App.xaml_ и добавьте следующее пространство имён в объект `Application`:

    ``` xml
    <!-- App.xaml file -->
    xmlns:theme3D="clr-namespace:Eremex.AvaloniaUI.Themes.Controls3D;assembly=Eremex.Avalonia.Controls3D"
    ```

- Включите элемент <code>&lt;theme3D:Controls3DTheme/&gt;</code> в коллекцию `Application.Styles`.

    ``` xml
    <!-- App.xaml file -->
    <Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyEMXCameraApp.App"
             xmlns:theme="clr-namespace:Eremex.AvaloniaUI.Themes.DeltaDesign;assembly=Eremex.Avalonia.Themes.DeltaDesign"
             xmlns:theme3D="clr-namespace:Eremex.AvaloniaUI.Themes.Controls3D;assembly=Eremex.Avalonia.Controls3D"
             RequestedThemeVariant="Default">
        <Application.Styles>
            <theme:DeltaDesignTheme/>
            <theme3D:Controls3DTheme />
        </Application.Styles>
    </Application>
    ```

!!! note

    Если визуальная тема `Controls3D` не зарегистрирована, `Graphics3DControl` будет отображаться пустым.

## Создание Graphics3DControl

Создайте контрол `Graphics3DControl` в XAML, используя следующий код:

``` xml
xmlns:mx3d="https://schemas.eremexcontrols.net/avalonia/controls3d"

<mx3d:Graphics3DControl Name="g3DControl" ShowAxes="True">
    <mx3d:Graphics3DControl.Camera>
        <mx3d:IsometricCamera/>
    </mx3d:Graphics3DControl.Camera>
</mx3d:Graphics3DControl>
```

Этот код отображает оси и включает изометрическую камеру для контрола `Graphics3DControl`. Вы также можете включить перспективную камеру. Для этого установите свойство `Graphics3DControl.Camera` в объект `PerspectiveCamera`.



## Определение 3D-модели

Класс `GeometryModel3D` инкапсулирует 3D-модель для `Graphics3DControl`. Чтобы добавить 3D-модели в контрол, добавьте один или несколько объектов `GeometryModel3D` в коллекцию `Graphics3DControl.Models`.

``` cs
using Eremex.AvaloniaUI.Controls3D;

GeometryModel3D model = new GeometryModel3D();
g3DControl.Models.Add(model);
```

3D-модель состоит из одной или нескольких сеток. Сетка — это часть модели, отрисованная с использованием определённого материала. 

Фигуры квадрата и треугольника в 3D-модели отрисовываются со своими материалами. Таким образом, нужно создать три сетки.

### Добавление сеток

Используйте коллекцию `GeometryModel3D.Meshes`, чтобы добавлять сетки. Каждая сетка инкапсулируется объектом `MeshGeometry3D`.

``` cs
using DynamicData;

MeshGeometry3D meshTriangle1 = new MeshGeometry3D();
MeshGeometry3D meshTriangle2 = new MeshGeometry3D();
MeshGeometry3D meshSquare = new MeshGeometry3D();
//...
model.Meshes.AddRange(new[] { meshTriangle1, meshTriangle2, meshSquare });
```

`Graphics3DControl` поддерживает три типа сеток:

- Сетка, определяемая коллекцией треугольников (по умолчанию, или когда `MeshGeometry3D.FillType` установлено в `MeshFillType.Triangles`)
- Сетка, определяемая коллекцией линий (когда `MeshGeometry3D.FillType` установлено в `MeshFillType.Lines`)
- Сетка, определяемая коллекцией точек (когда `MeshGeometry3D.FillType` установлено в `MeshFillType.Points`)

В текущем примере сетки создаются из треугольников. Для этого типа сетки вам нужно задать следующие свойства:

- `MeshGeometry3D.Vertices` — массив всех вершин (объектов `Vertex3D`), составляющих сетку. Объект `Vertex3D` предоставляет следующие основные свойства:

    - `Vertex3D.Position` — объект `Vector3`, задающий координаты вершины.
    - `Vertex3D.Normal` — объект `Vector3`, задающий нормаль вершины. Нормали вершин — это направленные векторы, используемые для расчёта отражения света для вершин и треугольника.
    - `Vertex3D.TextureCoord` — объект `Vector2`, задающий координаты текстуры для текущей вершины.

- `MeshGeometry3D.Indices` — массив индексов вершин в массиве `Vertices`, определяющих отдельные треугольники сетки. Этот массив содержит группы по три индекса каждая. Первые три индекса в массиве ссылаются на вершины первого треугольника сетки. Следующие три индекса ссылаются на вершины второго треугольника сетки, и так далее.
Порядок индексов для каждого треугольника важен, поскольку он определяет нормаль поверхности. Нормаль поверхности, в свою очередь, определяет переднюю и заднюю стороны треугольника, что существенно для операций вроде отсечения задних и передних граней.


#### Определение сеток для фигур Triangle 1 и Triangle 2

Сетки для фигур **Triangle 1** и **Triangle 2** легко определить, так как эти фигуры уже представляют собой треугольники. 

Сначала определим все вершины в созданной 3D-модели и их координаты (x, y, z).

![g3d-get-started-vertices-coords](../../images/g3d-get-started-vertices-coords.png)



В коде определите координаты всех вершин с помощью объектов `Vector3`:

``` cs
Vector3 pt1 = new(1, 0, 0);
Vector3 pt2 = new(0, 0, 0);
Vector3 pt3 = new(0, 0, 1);
Vector3 pt4 = new(1, 0, 1);
Vector3 pt5 = new(0, 1, 0);
```

Инициализируйте вершины и индексы для фигуры **Triangle 1**:

``` cs
Vertex3D[] meshTriangle1Vertices = new Vertex3D[]
{
    new Vertex3D() { Position = pt2,  Normal = new Vector3(0, 0, 1) },
    new Vertex3D() { Position = pt5,  Normal = new Vector3(0, 0, 1) },
    new Vertex3D() { Position = pt1,  Normal = new Vector3(0, 0, 1) },
};

// Define a mesh triangle.
uint[] meshTriangle1Indices = new uint[] { 0, 1, 2 };

meshTriangle1.Vertices = meshTriangle1Vertices;
meshTriangle1.Indices = meshTriangle1Indices;
```

Здесь индексы 0, 1 и 2 ссылаются на первую, вторую и третью вершины в массиве `Vertices`.

Аналогично инициализируйте вершины и индексы для фигуры **Triangle 2**:

``` cs
Vertex3D[] meshTriangle2Vertices = new Vertex3D[]
{
    new Vertex3D() { Position = pt2,  Normal = new Vector3(1, 0, 0) },
    new Vertex3D() { Position = pt5,  Normal = new Vector3(1, 0, 0) },
    new Vertex3D() { Position = pt3,  Normal = new Vector3(1, 0, 0) }
};

// Define a mesh triangle.
uint[] meshTriangle2Indices = new uint[] { 0, 1, 2 };

meshTriangle2.Vertices = meshTriangle2Vertices;
meshTriangle2.Indices = meshTriangle2Indices;
```

#### Определение сеток для фигуры Square

Фигуру **Square** можно разделить на два треугольника сетки. Например:

![g3d-get-started-square-triangulation](../../images/g3d-get-started-square-triangulation.png)


Массив `Vertices` для сетки **Square** должен содержать четыре точки. Массив `Indices` должен содержать шесть индексов, определяющих два треугольника сетки. 

``` cs
Vertex3D[] meshSquareVertices = new Vertex3D[]
{
    new Vertex3D() { Position = pt1,  Normal = new Vector3(0, 1, 0) },
    new Vertex3D() { Position = pt2,  Normal = new Vector3(0, 1, 0) },
    new Vertex3D() { Position = pt3,  Normal = new Vector3(0, 1, 0) },
    new Vertex3D() { Position = pt4,  Normal = new Vector3(0, 1, 0) }
};

// Define two mesh triangles.
// The first mesh triangle is formed by points pt1, pt2 and pt4.
// The second mesh triangle is formed by points pt2, pt3 and pt4.
uint[] meshSquareIndices = new uint[] { 0, 1, 3, 1, 2, 3 };

meshSquare.Vertices = meshSquareVertices;
meshSquare.Indices = meshSquareIndices;

```




## Задание материалов

Контрол `Graphics3DControl` поддерживает следующие материалы, производные от абстрактного класса `Eremex.AvaloniaUI.Controls3D.Material`:

- `SimplePbrMaterial` — материал, описывающий визуальные свойства поверхности числовыми значениями:

    - `Albedo` — базовый цвет
    - `Alpha` — прозрачность
    - `Emission` — интенсивность света, излучаемого поверхностью
    - `AmbientOcclusion` — уровень затенения, вызванного объектами, блокирующими окружающий свет
    - `Roughness` — гладкость поверхности
    - `Metallic` — отражательная способность поверхности.

- `TexturedPbrMaterial` — текстурированный материал в формате PBR. Этот материал позволяет задавать визуальные свойства (`Albedo`, `Alpha`, `Emission`, `AmbientOcclusion`, `Roughness`, `Metallic` и `Normal`) поверхности в виде растровых изображений.

Вам нужно назначить материалам уникальные ключи (строковые значения) с помощью свойства `Material.Key`. 
Затем вы можете связать материал с сеткой через свойство `MeshGeometry3D.MaterialKey`.


Следующий код добавляет три материала (объекта `SimplePbrMaterial`) с определёнными базовыми цветами (`Albedo`). Созданные сетки связываются с материалами с помощью свойства `MaterialKey`.

``` cs
using DynamicData;

g3DControl.Materials.AddRange(
    new[] {
        new SimplePbrMaterial(Color.FromUInt32(0xFF822c2e), "BrownColor"),
        new SimplePbrMaterial(Color.FromUInt32(0xffeb523f), "TomatoColor"),
        new SimplePbrMaterial(Color.FromUInt32(0xFFea3699), "VioletColor")
    }
);

//...

meshTriangle1.MaterialKey = "VioletColor";
meshTriangle2.MaterialKey = "TomatoColor";
meshSquare.MaterialKey = "BrownColor";
```

## Запуск приложения

Теперь можно запустить приложение. Используйте мышь и клавиатуру, чтобы панорамировать, масштабировать и вращать созданную 3D-модель.

![g3d-get-started-final-result](../../images/g3d-get-started-final-result.png)

## Полный код

``` xml
<mx:MxWindow xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:G3DControl_Get_Started.ViewModels"
        xmlns:d="http://schemas.microsoft.com/expression/blend/2008"
        xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
        xmlns:mx="https://schemas.eremexcontrols.net/avalonia"
        xmlns:mx3d="https://schemas.eremexcontrols.net/avalonia/controls3d"
        xmlns:mxe="https://schemas.eremexcontrols.net/avalonia/editors"
             
        mc:Ignorable="d" d:DesignWidth="800" d:DesignHeight="450"
        x:Class="G3DControl_Get_Started.Views.MainWindow"
        x:DataType="vm:MainWindowViewModel"
        Icon="/Assets/EMXControls.ico"
        Title="G3DControl_Get_Started">

    <Design.DataContext>
        <!-- This only sets the DataContext for the previewer in an IDE -->
        <vm:MainWindowViewModel/>
    </Design.DataContext>

    <mx3d:Graphics3DControl Name="g3DControl" ShowAxes="True">
        <mx3d:Graphics3DControl.Camera>
            <mx3d:IsometricCamera/>
        </mx3d:Graphics3DControl.Camera>
    </mx3d:Graphics3DControl>
</mx:MxWindow>
```

``` cs
using Avalonia.Controls;
using Avalonia.Media;
using DynamicData;
using Eremex.AvaloniaUI.Controls.Common;
using Eremex.AvaloniaUI.Controls3D;
using System;
using System.Numerics;

namespace G3DControl_Get_Started.Views;

public partial class MainWindow : MxWindow
{
    public MainWindow()
    {
        InitializeComponent();

        InitG3DControlMaterials();
        InitG3DControlMeshes();
    }

    private void InitG3DControlMaterials()
    {
        g3DControl.Materials.AddRange(
            new[] {
                new SimplePbrMaterial(Color.FromUInt32(0xFF822c2e), "BrownColor"),
                new SimplePbrMaterial(Color.FromUInt32(0xffeb523f), "TomatoColor"),
                new SimplePbrMaterial(Color.FromUInt32(0xFFea3699), "VioletColor")
            }
        );
    }

    private void InitG3DControlMeshes()
    {

        GeometryModel3D model = new GeometryModel3D();
        g3DControl.Models.Add(model);

        Vector3 pt1 = new(1, 0, 0);
        Vector3 pt2 = new(0, 0, 0);
        Vector3 pt3 = new(0, 0, 1);
        Vector3 pt4 = new(1, 0, 1);
        Vector3 pt5 = new(0, 1, 0);

        // Triangle 1
        MeshGeometry3D meshTriangle1 = new MeshGeometry3D();
        // Setting the FillType property to 'Triangles' is not required
        // as 'Triangles' is the default value of the FillType property.
        //meshTriangle1.FillType = MeshFillType.Triangles;
        Vertex3D[] meshTriangle1Vertices = new Vertex3D[]
        {
            new Vertex3D() { Position = pt2,  Normal = new Vector3(0, 0, 1) },
            new Vertex3D() { Position = pt5,  Normal = new Vector3(0, 0, 1) },
            new Vertex3D() { Position = pt1,  Normal = new Vector3(0, 0, 1) },
        };
        // Define a mesh triangle.
        uint[] meshTriangle1Indices = new uint[] { 0, 2, 1 };
        meshTriangle1.Vertices = meshTriangle1Vertices;
        meshTriangle1.Indices = meshTriangle1Indices;
        meshTriangle1.MaterialKey = "VioletColor";

        // Triangle 2
        MeshGeometry3D meshTriangle2 = new MeshGeometry3D();
        Vertex3D[] meshTriangle2Vertices = new Vertex3D[]
        {
            new Vertex3D() { Position = pt2,  Normal = new Vector3(1, 0, 0) },
            new Vertex3D() { Position = pt5,  Normal = new Vector3(1, 0, 0) },
            new Vertex3D() { Position = pt3,  Normal = new Vector3(1, 0, 0) }
        };
        // Define a mesh triangle.
        uint[] meshTriangle2Indices = new uint[] { 0, 2, 1 };
        meshTriangle2.Vertices = meshTriangle2Vertices;
        meshTriangle2.Indices = meshTriangle2Indices;
        meshTriangle2.MaterialKey = "TomatoColor";

        // Square
        MeshGeometry3D meshSquare = new MeshGeometry3D();
        Vertex3D[] meshSquareVertices = new Vertex3D[]
        {
            new Vertex3D() { Position = pt1,  Normal = new Vector3(0, 1, 0) },
            new Vertex3D() { Position = pt2,  Normal = new Vector3(0, 1, 0) },
            new Vertex3D() { Position = pt3,  Normal = new Vector3(0, 1, 0) },
            new Vertex3D() { Position = pt4,  Normal = new Vector3(0, 1, 0) }
        };
        // Define two mesh triangles.
        // The first mesh triangle is formed by points pt1, pt2 and pt4.
        // The second mesh triangle is formed by points pt2, pt3 and pt4.
        uint[] meshSquareIndices = new uint[] { 0, 1, 3, 1, 2, 3 };
        meshSquare.Vertices = meshSquareVertices;
        meshSquare.Indices = meshSquareIndices;
        meshSquare.MaterialKey = "BrownColor";

        model.Meshes.AddRange(new[] { meshTriangle1, meshTriangle2, meshSquare });
    }
}
```


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
