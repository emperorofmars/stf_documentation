# stf.armature
A armature represents a hierarchy of bones.
It can never be instantiated recursively.

## Properties
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
| root_bones | Yes | List<ID> | IDs of nodes |

The only allowed type for nodes in `root_bones` is [`stf.bone`](stf_bone.md).

Armatures can be instantiated by [`stf.instance.armature`](stf_instance_armature.md).

## Implementations
* Blender: [GitHub](https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_armature/stf_armature.py) | [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_armature/stf_armature.py)
* Unity: [GitHub](https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Armature.cs) | [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Armature.cs)
* Godot: [GitHub](https://github.com/emperorofmars/stf_godot/blob/master/addons/stf_godot/modules/stf/STF_Armature.gd) | [Codeberg](https://codeberg.org/emperorofmars/stf_godot/src/commit/d518b25aeb5b74cc57eb0f82f31a5f7fdbca2aa0/addons/stf_godot/modules/stf/STF_Armature.gd)

## Json Example
```json
"90b9fbb6-3e2d-44e5-8821-454c97c8d15a": {
	"type": "stf.armature",
	"name": "Armature",
	"root_bones": [
		"ed9fac3c-1500-436e-9c4e-fd88822be434"
	],
	"components": [
		"1e7c6be0-e53c-4af5-8e2d-c1bdc7c687c5",
		"1b453833-a3c8-4ac8-9d26-7a9e84eb27f9",
		"8324983e-c79f-466b-b21d-b1cdbe5bf229"
	]
}
```
