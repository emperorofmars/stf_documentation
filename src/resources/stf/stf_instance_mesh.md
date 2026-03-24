# stf.instance.mesh
Instantiates a mesh onto a node.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Object with bpy.types.Mesh
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_instance_mesh/stf_instance_mesh.py)
*	- **Unity**
	- MeshRenderer and SkinnedMeshRenderer
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Instance_Mesh.cs)\
		[Default Processor](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Processors/Processors_STF/STF_Instance_Mesh_Processor.cs)
*	- **Godot**
	- MeshInstance3D
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Instance_Mesh.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
mesh | Yes | ID | Resource-ID of the instantiated mesh resource, usually [`stf.mesh`](stf_mesh.md)
armature_instance | No | Resource-ID | ID of a node with an instantiated armature. Usually the instance resource is [`stf.instance.armature`](stf_instance_armature.md)
blendshape_values | No | List<float> | A value of `null` means that the resources default value is to be used.
materials | No | List<Resource-ID> | A value of `null` means that the resources default value is to be used.
:::

## Json Example
```json
"799b9826-85d9-40a3-a58b-b6489ba60452": {
	"type": "stf.instance.mesh",
	"name": "",
	"referenced_resources": [
		"8dedc60f-91cd-4e5e-a032-07dc82358519",
		"e6ae2ed1-fc53-43ee-ac53-05bf296d5fc1"
	],
	"mesh": 0,
	"armature_instance": 1,
	"materials": [
		null,
		null
	],
	"blendshape_values": [
		null,
		0.7,
		null,
		0.345,
		null,
		1.0,
		null,
		null,
		null,
		null,
		null,
		null
	]
}
```
