# stfexp.constraint.rotation

A rigging behavior that copies a percentage of the rotation from its source.\

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF component on bpy.types.Object or bpy.types.Bone (Could use actual CopyRotation modifiers in the future)
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_constraint_rotation.py)
*	- **Unity**
	- ParentConstraint or application specific components
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Constraint_Rotation.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_Expanded/STFEXP_Constraint_Rotation_Processor.cs)
*	- **Godot**
	- CopyTransformModifier3D
	- [Module](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stfexp/STFEXP_Constraint_Rotation.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
weight | No | float | The total weight of this constraint. Default is 1.
axes | No | list[boolean] | Which axes are affected, must have exactly 3 entries for X, Y, Z.
sources | No | list[Source-Object] | List of sources from which to copy the rotation.
:::

`Source-Object` Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
weight | No | float | How much of the source rotation to blend. Default is 0.5
source | Yes | [Resource-Path](../../format/stf_format.md#resource-path) | Path to the node from which to copy the rotation.
:::

## Json Example
```json
"aec4ca85-341b-4b16-952a-5418827a8558": {
	"type": "stfexp.constraint.rotation",
	"name": "asdf",
	"weight": 0.7685009241104126,
	"axes": [ true, false, true ],
	"sources": [
		{
			"source": [ 0, "instance", 1 ],
			"weight": 0.5
		},
		{
			"source": [ 0, "instance", 2 ],
			"weight": 0.7390891909599304
		},
		{
			"source": [ 3 ],
			"weight": 0.7087286710739136
		}
	],
	"referenced_resources": [
		"e6ae2ed1-fc53-43ee-ac53-05bf296d5fc1",
		"ca433094-3789-44c2-b7cb-890691a98b73",
		"3344754b-fafd-45de-82df-7b3f15fce86a",
		"1bef1076-0f2a-402e-8e9f-57d2c7095319"
	]
},
```
