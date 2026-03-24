# stf.instance.armature
Instantiates an armature onto a node.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Object with bpy.types.Armature
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_instance_armature/stf_instance_armature.py)
*	- **Unity**
	- GameObject
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Instance_Armature.cs)\
		[Default Processor](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Processors/Processors_STF/STF_Instance_Armature_Processor.cs)
*	- **Godot**
	- Skeleton3D
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Instance_Armature.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
armature | Yes | Resource-ID | ID of the instantiated armature resource, usually [`stf.armature`](stf_armature.md)
pose | No | Map<Resource-ID, TRS> | Map of the corresponding bone and TRS.
added_components | No | Map<Resource-ID, List<Resource-ID>> | A list of component-IDs that are added to bones within this armature instance.
modified_components | No | Map<Resource-ID, Map<Resource-ID, JSON>> | A reference to bones within the armature instance -> a component on that bone instance -> a JSON object with changes to that component.
:::

## Json Example
```json
"14b62a8a-2b3d-408f-aef0-72b3e797318b": {
	"type": "stf.instance.armature",
	"name": "",
	"referenced_resources": [
		"7ae076bd-d53f-478e-8b80-73bdaff97f2d"
	],
	"armature": 0,
	"pose": {
		"b6f82f9a-b78f-4778-a513-32f4e2342ed0": [
			[
				0,
				0.6796078085899353,
				-0.01611711084842682
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
		"1e803b23-4d6e-4f3e-8194-976fe699a46c": [
			[
				0,
				0.11233383417129517,
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
		]
	}
}
```
