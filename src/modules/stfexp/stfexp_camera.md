# stfexp.camera

A camera with perspective or orthographic projection.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Camera
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_camera.py)
*	- **Unity**
	- Camera
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Camera.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_Expanded/STFEXP_Camera_Processor.cs)
*	- **Godot**
	- Camera3D
	- [Module](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stfexp/STFEXP_Camera.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
projection | Yes | string | Possible values are "perspective" and "orthographic"
aspect_ratio | Yes | float | 
fov | Yes | float | Vertical field of view for "perspective" projection or the vertical size of the orthographic plane for "orthographic" projection.
:::

## Json Example
```json
"e7dd296d-024a-49cf-af5b-21c12c85eb31": {
	"type": "stfexp.camera",
	"name": "",
	"projection": "orthographic",
	"aspect_ratio": 1.7777777777777777,
	"fov": 4.114285737276077
},
```
