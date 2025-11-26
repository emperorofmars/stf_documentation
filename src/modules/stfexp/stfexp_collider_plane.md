# stfexp.collider.plane

An infinitely large plane collider.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF_Component on bpy.types.Object or bpy.types.Bone
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_collider_plane.py)
*	- **Unity**
	- Only Application specific components
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Collider_Plane.cs)
		[VRChat Physbone Collider Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_VRChat/Editor/Processors/VRC_STFEXP_Collider_Plane_Processor.cs)
*	- **Godot**
	- TBD
	-
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
offset_position | No | list[float][3] | The position offset from the node this component is placed on.
offset_rotation | No | list[float][3] | The rotation offset from the node this component is placed on.
:::

## Json Example
```json
"892232b9-101a-4a8b-9c6e-5943851114a6": {
	"type": "stfexp.collider.plane",
	"name": "ColliderFloor",
	"offset_position": [
		0,
		0.029999999329447746,
		0.0020000000949949026
	],
	"offset_rotation": [
		0.0523359514772892,
		0,
		0,
		0.9986295104026794
	]
},
```
