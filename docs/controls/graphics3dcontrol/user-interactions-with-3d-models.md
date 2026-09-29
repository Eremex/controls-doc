---
title: User Interactions with 3D Models
order: 10
seealso: []
---

# User Interactions with 3D Models

`Graphics3DControl` enables users to interact with 3D models. Users can rotate, zoom, and pan (move) the models with the mouse and keyboard. Additionally, you can allow users to select elements of the model with a mouse click or highlight elements when hovering over them with the mouse. 
The `Graphics3DControl` also supports tooltips for the models and its elements (meshes).

## Rotate the Model

#### Keyboard Shortcuts

- Rotate Left — Shift+Left Arrow
- Rotate Right — Shift+Right Arrow
- Rotate Up — Shift+Up Arrow
- Rotate Down — Shift+Down Arrow


#### Mouse Operations

- Rotate — Drag the model with Left mouse button.

### Rotate Options

- `Graphics3DControl.RotateStep` — Allows you to control the rotation speed. The `RotateStep` property is specified in internal units. The default value is 20. A higher value results in a greater rotation speed. 

<!-- TODO
Check the property in the demo. 
 -->

## Zoom the Model

#### Keyboard Shortcuts

- Zoom In — CTRL+Plus Key
- Zoom Out — CTRL+Minus Key

#### Mouse Operations

- Zoom — Use Mouse Scroll Wheel to zoom in and out.

### Zoom Options

- `Graphics3DControl.ZoomRate` — Controls the speed of zoom operations performed using the keyboard and mouse wheel. The default value is 0.1. A higher value increases the zoom speed.

## Move the Model

#### Keyboard Shortcuts

- Move Left — CTRL+Left Arrow
- Move Right — CTRL+Right Arrow
- Move Up — CTRL+Up Arrow
- Move Down — CTRL+Down Arrow

#### Mouse Operations

- Move — Drag the model with Right mouse button.

### Move Options

- `Graphics3DControl.KeyboardMoveStep` property — Allows you to specify the distance by which a model is shifted during a single keyboard move operation.

<!-- TODO
which units ?
 -->

## Rotate, Zoom and Move Models in Code

To view a model from a specific position and angle in code, you need to adjust the camera's position and orientation. See the following topic for more information:

- [Camera](camera.md)



## Override Keyboard Shortcuts

The `Graphics3DControl.NavigationBindings` property of the `Graphics3DKeyBindings` class allows you to override the default keyboard shortcuts. The `Graphics3DKeyBindings` class contains properties that define the shortcuts for the zoom, rotate and pan operations. Initially, these properties are set to the default shortcuts, which are listed above. You can use these properties to assign custom shortcuts to the operations.

The following code assigns the CTRL+1 and CTRL+2 shortcuts to the Zoom In and Zoom Out operations.

``` cs
g3DControl.NavigationBindings = new Graphics3DKeyBindings();
Graphics3DKeyBinding zoomInShortcut = new Graphics3DKeyBinding(Avalonia.Input.KeyModifiers.Control, Avalonia.Input.Key.D1);
Graphics3DKeyBinding zoomOutShortcut = new Graphics3DKeyBinding(Avalonia.Input.KeyModifiers.Control, Avalonia.Input.Key.D2);
g3DControl.NavigationBindings.ZoomIn = zoomInShortcut;
g3DControl.NavigationBindings.ZoomOut = zoomOutShortcut;
```

## Show Hints

`Graphics3DControl` can display hints when a user hovers over models or individual meshes. 

![g3dControl-hint](../../images/g3dControl-hint.png)

Use the following properties to assign hints to models, meshes, or both models and meshes at the same time:

- `GeometryModel3D.Hint` — A hint for a model.
- `MeshGeometry3D.Hint` — A hint for a mesh.

The following example sets hints for a model and its meshes. Hints for meshes indicate their names.

``` xml
<mx3d:GeometryModel3D x:Name="Cube" MeshesSource="{Binding Meshes}" Hint="Cube">
    <mx3d:GeometryModel3D.MeshTemplate>
        <DataTemplate x:DataType="vm:MeshViewModel">
            <mx3d:MeshGeometry3D 
                Name="{Binding Name}" 
                Hint="{Binding Name}"
                ...
            />
        </DataTemplate>
    </mx3d:GeometryModel3D.MeshTemplate>
</mx3d:GeometryModel3D>
```
``` cs
public partial class MeshViewModel : ObservableObject
{
    [ObservableProperty] string name;
    [ObservableProperty] Vertex3D[] vertices;
    //...
}
```

When hints are set for both the model and a mesh, these hints are merged into a single hint, separated by the ',' delimiter.

![g3dcontrol hints animation](../../images/g3dcontrol-hints-animation.gif)

Set the `Graphics3DControl.ShowHints` property to `false` to disable hints. This property has a default value of `true`.

## Highlight Elements

`Graphics3DControl` supports model and mesh highlighting. With this feature, the control draws a highlight border around a model/mesh when a user hovers over it.

![g3dControl-highlight](../../images/g3dControl-highlight.png)

Use the `Graphics3DControl.HighlightMode` property to enable the highlight feature and specify highlight mode. The following options are available:

- `Mesh` — Enables highlighting of individual meshes.
- `Model` — Enables highlighting of individual models.
- `None` (default) — The highlight feature is disabled.

**Related API**

- `Graphics3DControl.HighlightedElement` — Gets or sets the currently highlighted element.
- `Graphics3DControl.HighlightColor` — Gets or sets the color used to draw a highlight border around highlighted elements.


## Select Elements

You can enable the selection feature to allow a user to select elements (models or meshes) with a mouse click. A selection border is painted around an element when a user clicks it.

![g3dcontrol selection animation](../../images/g3dcontrol-selection-animation.gif)

Use the `Graphics3DControl.SelectionMode` property to activate the selection feature and define selection mode. The available options include:

- `Mesh` — Enables selection of individual meshes on a mouse click.
- `Model` — Enables selection of individual models on a mouse click.
- `None` (default) — The selection feature is disabled.


**Related API**

- `Graphics3DControl.SelectedElement` — Gets or sets the currently selected element.
- `Graphics3DControl.SelectionColor` — Gets or sets the color used to draw a border around selected elements.


## See Also

- [Camera](camera.md)