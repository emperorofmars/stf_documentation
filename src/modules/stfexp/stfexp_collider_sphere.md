# stfexp.collider.sphere

A sphere collider

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF_Component on bpy.types.Object or bpy.types.Bone
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_collider_sphere.py)
*	- **Unity**
	- SphereCollider or application specific components
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Collider_Sphere.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_Expanded/STFEXP_Collider_Sphere_Processor.cs)\
		[VRChat Physbone Collider Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_VRChat/Editor/Processors/VRC_STFEXP_Collider_Sphere_Processor.cs)\
		[UNIVRM0 Springbone Collider Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_UNIVRM0/Editor/Processors/UNIVRM0_STFEXP_Collider_Sphere_Processor.cs)
*	- **Godot**
	- CollisionShape3D & SphereShape3D
	- [Module](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stfexp/STFEXP_Collider_Sphere.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
radius | Yes | float | 
offset_position | No | list[float][3] | The position offset from the node this component is placed on.
:::

## Json Example
```json
"43ebc38a-125e-4c6a-98d2-1afcdb6c2707": {
	"type": "stfexp.collider.sphere",
	"name": "ColliderHead",
	"radius": 0.10999999940395355,
	"offset_position": [
		0,
		0.09799999743700027,
		0.019999999552965164
	]
},
```
