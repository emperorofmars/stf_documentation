# stfexp.constraint.parent

A rigging behaviour that parents itself to its sources.\

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF component on bpy.types.Object or bpy.types.Bone (Could use actual CopyRotation modifiers in the future)
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_constraint_parent.py)
*	- **Unity**
	- ParentConstraint or application specific components
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Constraint_Parent.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_Expanded/STFEXP_Constraint_Rotation_Processor.cs)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
weight | No | float | The total weight of this constraint. Default is 1.
rotation_axes | No | list[boolean] | Which axes are affect rotation, must have exactly 3 entries for X, Y, Z.
translation_axes | No | list[boolean] | Which axes are affect translation, must have exactly 3 entries for X, Y, Z.
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
"d49613ca-584e-4be3-baa2-17145c3b38db": {
	"type": "stfexp.constraint.parent",
	"name": "Parent to Hand",
	"weight": 1.0,
	"translation_axes": [
		true,
		true,
		true
	],
	"rotation_axes": [
		true,
		true,
		true
	],
	"sources": [
		{
			"source": [
				0,
				"instance",
				1
			],
			"weight": 1.0
		}
	],
	"referenced_resources": [
		"e6ae2ed1-fc53-43ee-ac53-05bf296d5fc1",
		"1e803b23-4d6e-4f3e-8194-976fe699a46c"
	]
},
```
