# stf.instance.mesh
Instantiates a mesh onto a node.

## Properties
:::{table}
:align: left
:widths: auto
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|mesh |Yes |ID |Resource-ID of the instantiated mesh resource, usually xref:../data/stf_mesh.adoc[`stf.mesh`]
|armature_instance |No |Resource-ID |ID of a node with an instantiated armature. Usually the instance resource is xref:./stf_instance_armature.adoc[`stf.instance.armature`]
|blendshape_values |No |List<float> |
|materials |No |List<Resource-ID> |
:::

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_instance_mesh/stf_instance_mesh.py)
	- [GitHub](https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_instance_mesh/stf_instance_mesh.py)
*	- **Unity**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Instance_Mesh.cs)
	- [GitHub](https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Instance_Mesh.cs)
*	- **Godot**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Instance_Mesh.gd)
	- [GitHub](https://github.com/emperorofmars/stf_godot/blob/master/addons/stf_godot/modules/stf/STF_Instance_Mesh.gd)
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
