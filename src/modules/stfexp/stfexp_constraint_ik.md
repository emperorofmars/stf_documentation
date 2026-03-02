# stfexp.constraint.ik

Basic inverse-kinematik constraint. The component has to be placed on the last bone in the ik-chain.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF component on bpy.types.Bone and bpy.types.KinematicConstraint
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_constraint_ik.py)
*	- **Unity**
	- Application specific components
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Constraint_IK.cs)
*	- **Godot**
	- Various subclasses of IKModifier3D
	- [Module](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stfexp/STFEXP_Constraint_IK.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
chain_length | Yes | int | The length of the IK chain
target | Yes | [Resource-Path](../../format/stf_format.md#resource-path) | Path of the target node
pole | No | [Resource-Path](../../format/stf_format.md#resource-path) | Path of the poole node
:::

## Json Example
```json
"fa7771ef-4b58-47d5-9e02-99c58671c589": {
	"type": "stfexp.constraint.ik",
	"name": "Arm IK",
	"chain_length": 2,
	"referenced_resources": [
		"e9fc8507-5797-44a9-9513-9f7ae6abace0",
		"637ccf78-6369-49e6-bba9-137f91105987"
	],
	"target": [
		0
	],
	"pole": [
		1
	]
},
```
