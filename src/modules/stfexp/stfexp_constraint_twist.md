# stfexp.constraint.twist

A rigging behavior that copies a percentage of the Y-axis rotation from its target.\
This is a special application of rotation-constraints, used to compensate for twist movement.

## Representations
* Blender: STF component (Could use actual CopyRotation modifiers in the future)
* Unity: RotationConstraint
* Godot: CopyTransformModifier3D (TBD)

## Properties
:::{table}
:align: left
:widths: auto
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|weight |No |float |How much of the target rotation to blend. Default is 0.5 |
|target |No |[Resource-Path](../../format/stf_format.md#resource-path) |Path to the target node. Default is the parent of the parent. |
:::

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_constraint_twist.py)
*	- **Unity**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Constraint_Twist.cs)
*	- **Godot**
	- TBD
:::

## Json Example
```json
"2fec4aaa-4eb8-4e4a-a9ae-3d99cdd99bf0": {
	"type": "stfexp.constraint.twist",
	"weight": 0.5,
	"referenced_resources": [
		"360e5f0a-3f49-4e1f-9988-a66bd73bc959"
	],
	"target": [
		0
	]
},
```
