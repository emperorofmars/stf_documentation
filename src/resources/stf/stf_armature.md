# stf.armature
A armature represents a hierarchy of bones.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- Armature
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_armature/stf_armature.py)
*	- **Unity**
	- GameObject
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resource/Resources_STF/STF_Armature.cs)
*	- **Godot**
	- Skeleton3D
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Armature.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
root_bones | Yes | List<ID> | IDs of nodes
:::

The only allowed type for nodes in `root_bones` is [`stf.bone`](stf_bone.md).

Armatures can be instantiated by [`stf.instance.armature`](stf_instance_armature.md).


## Json Example
```json
"7ae076bd-d53f-478e-8b80-73bdaff97f2d": {
	"type": "stf.armature",
	"name": "Armature",
	"root_bones": [
		0
	],
	"referenced_resources": [
		"b6f82f9a-b78f-4778-a513-32f4e2342ed0"
	],
	"components": [
		"38ddf9ce-688c-41c2-b917-4bde02709913",
		"247d40d1-0a38-4453-9e1b-641bc21f5512",
		"4385a660-0778-447a-bacb-ff4852ea08fd"
	]
}
```
