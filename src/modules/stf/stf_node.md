# stf.node
A node that exists in 3d space. It defines its location, rotation and scale relative to its parent.

## Representations
* Blender: Object
* Unity: GameObject
* Godot: Node3D

## Properties
:::{table}
:align: left
:widths: auto
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|trs |Yes |TRS |The nodes 3D transform |
|instance |No |Resource-ID |Reference to an instance-resource. |
|parent_binding |No |Path |Path to the parent resource. Usually, when the parent node is an armature-instance, its the path to a bone within the instantiated armature. |
:::

Only other `stf.node` type resources are allowed as its children. Children may never loop.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_node/stf_node.py)
*	- **Unity**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Node.cs)
*	- **Godot**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Node.gd)
:::

## Json Example
```json
"880c2403-471d-46e4-99ac-0b218f201337": {
	"type": "stf.node",
	"name": "ArmatureHair",
	"enabled": true,
	"children": [
		"0912ff56-e534-4c8e-a99e-d3ef2a9ea8ba"
	],
	"trs": [
		[
			-6.138677122180525e-09,
			1.584037184715271,
			-0.029444340616464615
		],
		[
			-3.725290298461914e-09,
			-4.618527782440651e-14,
			1.7659484985443896e-15,
			1.0
		],
		[
			1.0,
			1.0,
			1.0
		]
	],
	"instance": "73d67945-2937-41c8-b683-7a992cbca5c5",
	"components": [
		"3051ea80-cc8a-4b6a-afce-dd75e1868fa5"
	],
	"parent_binding": [
		"9fac8ebe-54ee-4c97-a193-235fcc5ebe7f",
		"instance",
		"9a6e0ab7-29e4-48b1-ba25-5e0cd86988e7"
	]
}
```
