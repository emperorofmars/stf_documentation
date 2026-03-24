# stf.prefab
A prefab represents a hierarchy of nodes. It's always the root resource of an STF asset.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Collection
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_prefab/stf_prefab.py)
*	- **Unity**
	- GameObject/Prefab
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Prefab.cs)\
		[Default Processor](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Processors/Processors_STF/STF_Prefab_Processor.cs)
*	- **Godot**
	- The root-node of a scene
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Prefab.gd)
:::

## Properties

:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
root_nodes | Yes | List<Resource-ID> | IDs of the root nodes within this prefab
animations | No | List<Resource-ID> | Animations which originate from this prefab's root
:::

The only allowed type for nodes in `root_nodes` is [`stf.node`](stf_node.md).

## Json Example
```json
"a6452f90-3edb-4fcd-bfe5-f7860a1ea665": {
	"type": "stf.prefab",
	"name": "Collection",
	"root_nodes": [
		0,
		1,
		2
	],
	"animations": [
		3
	],
	"referenced_resources": [
		"00058dcb-4e27-4067-9163-3f9ef959faf1",
		"b12620eb-5c3a-433c-a93c-4c5d6d158f2b",
		"1fe7444e-7090-495b-90e7-ca3cbc167930",
		"44ce3d6f-ccaf-48c1-ba59-155bb58d6a40"
	]
}
```
