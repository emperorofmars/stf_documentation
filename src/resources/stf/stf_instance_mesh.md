# stf.instance.mesh
Instantiates a mesh onto a node.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Object with bpy.types.Mesh
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_instance_mesh/stf_instance_mesh.py)
*	- **Unity**
	- MeshRenderer and SkinnedMeshRenderer
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Instance_Mesh.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_Core/STF_Instance_Mesh_Processor.cs)
*	- **Godot**
	- MeshInstance3D
	- [Module](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Instance_Mesh.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
mesh | Yes | ID | Resource-ID of the instantiated mesh resource, usually [`stf.mesh`](stf_mesh.md)
armature_instance | No | Resource-ID | ID of a node with an instantiated armature. Usually the instance resource is [`stf.instance.armature`](stf_instance_armature.md)
blendshape_values | No | List<float> |
materials | No | List<Resource-ID> |
:::

## Json Example
```json
"799b9826-85d9-40a3-a58b-b6489ba60452": {
	"type": "stf.instance.mesh",
	"mesh": "8dedc60f-91cd-4e5e-a032-07dc82358519",
	"armature_instance": "e6ae2ed1-fc53-43ee-ac53-05bf296d5fc1",
	"blendshape_values": [
		null,
		0.3,
		0.65,
		null,
		null,
		null,
		1.0,
		null
	]
},
```
