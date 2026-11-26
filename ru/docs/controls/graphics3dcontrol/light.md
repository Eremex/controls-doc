---
title: Light
order: 85
seealso: []
---

# Light

В Graphics3DControl источники света используются для освещения 3D-моделей. Вы можете использовать свет по умолчанию или создавать пользовательские источники света для вашей 3D-сцены.


## Свет по умолчанию

[`Graphics3DControl`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl.md) предоставляет свет по умолчанию «из коробки». Свет по умолчанию представляет собой белый точечный свет, связанный с камерой. Его направление всегда синхронизировано с направлением камеры.

Следующее изображение демонстрирует свет по умолчанию, отражённый от металлической плоскости. 

![g3dControl-default-light](../../images/g3dControl-default-light.png)

Фактический визуальный эффект любого света определяется [материалами](graphics3dcontrol-overview.md#материалы), применёнными к 3D-моделям.


#### Связанные опции

- [`Graphics3DControl.AllowDefaultLight`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl/AllowDefaultLight.md) (значение по умолчанию — `true`) — установите это свойство в `false`, чтобы принудительно отключить свет по умолчанию.

    Когда вы создаёте пользовательские источники света, свет по умолчанию автоматически отключается. 


## Пользовательские источники света


Чтобы добавить пользовательские источники света в 3D-сцену, создайте источники света и добавьте их в коллекцию [`Graphics3DControl.Lights`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl/Lights.md). Вы также можете использовать свойства [`Graphics3DControl.LightsSource`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl/LightsSource.md) и [`Graphics3DControl.LightTemplate`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl/LightTemplate.md), чтобы добавлять пользовательские источники света в соответствии с паттерном MVVM.


[`Graphics3DControl`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl.md) поддерживает следующие типы источников света:

- Точечный свет ([`PointLight`](../../API/Eremex.AvaloniaUI.Controls3D/PointLight.md))
- Направленный свет ([`DirectionalLight`](../../API/Eremex.AvaloniaUI.Controls3D/DirectionalLight.md))
- Точечный свет, связанный с камерой ([`CameraPointLight`](../../API/Eremex.AvaloniaUI.Controls3D/CameraPointLight.md))
- Направленный свет, связанный с камерой ([`CameraDirectionalLight`](../../API/Eremex.AvaloniaUI.Controls3D/CameraDirectionalLight.md))

Все эти источники света имеют одного предка — абстрактный класс [`Light`](../../API/Eremex.AvaloniaUI.Controls3D/Light.md).

### Точечный свет

Излучает во всех направлениях (как лампочка). 

#### Класс

[`PointLight`](../../API/Eremex.AvaloniaUI.Controls3D/PointLight.md)

#### Настройки
    
- [`Color`](../../API/Eremex.AvaloniaUI.Controls3D/Light/Color.md) — цвет света.
- [`Position`](../../API/Eremex.AvaloniaUI.Controls3D/PointLight/Position.md) — положение излучателя света.
- [`Radius`](../../API/Eremex.AvaloniaUI.Controls3D/PointLightBase/Radius.md) — радиус излучателя света.

#### Пример

Этот пример создаёт точечный свет цвета Coral. Изображение ниже демонстрирует этот свет, отражённый от металлической плоскости и сферы.

![g3dControl-point-light-coral-example](../../images/g3dControl-point-light-coral-example.png)

``` xml
<mx3d:Graphics3DControl.Lights>
    <mx3d:PointLight Color="{Binding MyLightColor}" Position="{Binding MyLightPosition}" Radius="10"/>
</mx3d:Graphics3DControl.Lights>
```
``` cs
PointLight myLight = new PointLight();
myLight.Color = Avalonia.Media.Colors.Coral;
myLight.Position = new Vector3(0, 50, 0);
myLight.Radius = 10;
g3DControl.Lights.Add(myLight);
```

### Направленный свет

Излучает параллельные лучи в заданном направлении, имитируя удалённое освещение (как солнечный свет).


#### Класс

[`DirectionalLight`](../../API/Eremex.AvaloniaUI.Controls3D/DirectionalLight.md)

#### Настройки

- [`Color`](../../API/Eremex.AvaloniaUI.Controls3D/Light/Color.md) — цвет света.
- [`Direction`](../../API/Eremex.AvaloniaUI.Controls3D/DirectionalLight/Direction.md) — вектор, задающий направление лучей света.

#### Пример


Этот пример добавляет источник направленного света, направленный в сторону отрицательной оси Y. Изображение ниже демонстрирует этот свет, отражённый от металлической плоскости и сферы.

![g3dControl-directional-light-coral-example](../../images/g3dControl-directional-light-coral-example.png)



``` xml
<mx3d:Graphics3DControl.Lights>
    <mx3d:DirectionalLight Color="{Binding MyLightColor}" Direction="{Binding MyLightDirection}"/>
</mx3d:Graphics3DControl.Lights>
```
``` cs
using Eremex.AvaloniaUI.Controls3D;

DirectionalLight myLight = new DirectionalLight();
myLight.Direction = new System.Numerics.Vector3(0, -1, 0);
myLight.Color = Avalonia.Media.Colors.Coral;
g3DControl.Lights.Add(myLight);
```



### Точечный свет, связанный с камерой

Точечный свет, излучаемый из камеры. Положение и направление этого света синхронизированы с положением и направлением камеры.

#### Класс

[`CameraPointLight`](../../API/Eremex.AvaloniaUI.Controls3D/CameraPointLight.md)

#### Настройки

- [`Color`](../../API/Eremex.AvaloniaUI.Controls3D/Light/Color.md) — цвет света.
- [`Radius`](../../API/Eremex.AvaloniaUI.Controls3D/PointLightBase/Radius.md) — радиус излучателя света.

#### Пример 

Этот пример создаёт точечный свет, связанный с камерой. Изображение ниже демонстрирует этот свет, отражённый от металлической плоскости и сферы.

![g3dControl-camera-point-light-coral-example](../../images/g3dControl-camera-point-light-coral-example.png)

``` xml
<mx3d:Graphics3DControl.Lights>
    <mx3d:CameraPointLight Color="{Binding MyLightColor}" Radius="10"/>
</mx3d:Graphics3DControl.Lights>
```
``` cs
using Eremex.AvaloniaUI.Controls3D;

CameraPointLight myLight = new CameraPointLight();
myLight.Radius = 10;
myLight.Color = Avalonia.Media.Colors.Coral;
g3DControl.Lights.Add(myLight);
```


### Направленный свет, связанный с камерой

Излучает параллельные лучи в направлении камеры, имитируя удалённое освещение (как солнечный свет).

#### Класс

[`CameraDirectionalLight`](../../API/Eremex.AvaloniaUI.Controls3D/CameraDirectionalLight.md)

#### Настройки

- [`Color`](../../API/Eremex.AvaloniaUI.Controls3D/Light/Color.md) — цвет света.


#### Пример 

Этот пример создаёт направленный свет, связанный с камерой. Изображение ниже демонстрирует этот свет, отражённый от металлической плоскости и сферы.

![g3dControl-camera-directional-light-coral-example](../../images/g3dControl-camera-directional-light-coral-example.png)

``` xml
<mx3d:Graphics3DControl.Lights>
    <mx3d:CameraDirectionalLight Color="{Binding MyLightColor}"/>
</mx3d:Graphics3DControl.Lights>
```
``` cs
using Eremex.AvaloniaUI.Controls3D;

CameraDirectionalLight myLight = new CameraDirectionalLight();
myLight.Color = Avalonia.Media.Colors.Coral;
g3DControl.Lights.Add(myLight);
```


<!-- TODO

### Add Lights Using the MVVM Approach

- [`Graphics3DControl.LightsSource`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl/LightsSource.md) — Supports the MVVM design patters. The [`LightsSource`](../../API/Eremex.AvaloniaUI.Controls3D/Graphics3DControl/LightsSource.md) property is a collection of business objects  -->


<br>
<br>

<sup>*</sup> Эта страница переведена с использованием технологий машинного перевода.
