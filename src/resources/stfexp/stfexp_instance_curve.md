# stfexp.instance.curve
Instance of 2D and 3D Bézier Curves in 3D space

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Object with bpy.types.Curve
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/stfexp/stfexp_instance_curve.py)
*	- **Godot**
	- Path3D
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stfexp/STFEXP_Instance_Curve.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
curve | Yes | Resource-ID | Curve resource
:::

## Json Example
```json
"3b41aad4-e046-424b-bcfa-3ef8d29052ca": {
	"type": "stfexp.instance.curve",
	"name": "Instance of B\u00e9zierCurve",
	"referenced_resources": [
		"1ed58998-148b-496e-89c4-40e09f1547ab"
	],
	"curve": 0
},
```
