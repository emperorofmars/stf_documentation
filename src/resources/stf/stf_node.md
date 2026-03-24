# stf.node
A node that exists in 3d space. It defines its location, rotation and scale relative to its parent.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Object
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_node/stf_node.py)
*	- **Unity**
	- Object
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Node.cs)\
		[Default Processor](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Processors/Processors_STF/STF_Mesh_Processor.cs)
*	- **Godot**
	- Node3D
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Node.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
trs | Yes | TRS | The nodes 3D transform
instance | No |Resource-ID | Reference to an instance-resource.
parent_binding | No | Path | Path to the parent resource. Usually, when the parent node is an armature-instance, its the path to a bone within the instantiated armature.
:::

Only other `stf.node` type resources are allowed as its children. Children may never loop.

## Json Example
```json
"bbff51e8-b34d-4ec4-aca4-3fcecad73309": {
	"type": "stf.node",
	"name": "Body",
	"children": [],
	"trs": [
		[
			0,
			0,
			0
		],
		[
			0,
			0,
			0,
			1
		],
		[
			1,
			1,
			1
		]
	],
	"referenced_resources": [
		"799b9826-85d9-40a3-a58b-b6489ba60452"
	],
	"instance": 0,
	"components": [
		"3a10d82c-3649-4f90-8300-c90a21dbafaa",
		"6cf57561-7578-4cc8-a66d-8353ce783e69"
	]
}
```
