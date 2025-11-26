# stfexp.constraint.twist

A rigging behavior that copies a percentage of the Y-axis rotation from its source.\
This is a special application of rotation-constraints, used to compensate for twist movement.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF component on bpy.types.Object or bpy.types.Bone (Could use actual CopyRotation modifiers in the future)
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_constraint_twist.py)
*	- **Unity**
	- RotationConstraint or application specific components
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Constraint_Twist.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_Expanded/STFEXP_Constraint_Twist_Processor.cs)\
		[VRChat Constraint Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_VRChat/Editor/Processors/VRC_STFEXP_Constraint_Twist_Processor.cs)
*	- **Godot**
	- CopyTransformModifier3D
	- [Module](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stfexp/STFEXP_Constraint_Twist.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
weight | No | float | How much of the source rotation to blend. Default is 0.5
source | No | [Resource-Path](../../format/stf_format.md#resource-path) | Path to the node from which to copy the rotation. If not set, the parent of the parent will be assumed.
:::

## Json Example
```json
"2fec4aaa-4eb8-4e4a-a9ae-3d99cdd99bf0": {
	"type": "stfexp.constraint.twist",
	"weight": 0.5,
	"referenced_resources": [
		"360e5f0a-3f49-4e1f-9988-a66bd73bc959"
	],
	"source": [
		0
	]
},
```
