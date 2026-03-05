# stfexp.collider.capsule

A capsule collider

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF_Component on bpy.types.Object or bpy.types.Bone
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_collider_capsule.py)
*	- **Unity**
	- CapsuleCollider or application specific components
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Collider_Capsule.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_Expanded/STFEXP_Collider_Capsule_Processor.cs)\
		[VRChat Physbone Collider Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_VRChat/Editor/Processors/VRC_STFEXP_Collider_Capsule_Processor.cs)\
		[UNIVRM0 Springbone Collider Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_UNIVRM0/Editor/Processors/UNIVRM0_STFEXP_Collider_Capsule_Processor.cs)
*	- **Godot**
	- CollisionShape3D & CapsuleShape3D
	- [Module](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stfexp/STFEXP_Collider_Capsule.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
radius | Yes | float | 
height | Yes | float | 
offset_position | No | list[float][3] | The position offset from the node this component is placed on.
offset_rotation | No | list[float][3] | The rotation offset from the node this component is placed on.
:::

## Json Example
```json
"ebde9045-5b00-44e8-8bcc-01ce02929234": {
	"type": "stfexp.collider.capsule",
	"name": "ColliderChest",
	"radius": 0.10000000149011612,
	"height": 0.44999998807907104,
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
