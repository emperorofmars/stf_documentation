# stf.bone
Can only exist within `stf.armature`.

## Properties
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|translation |Yes |Translation |The position of the bone relative to its armature position.
|rotation |Yes |Rotation |The rotation of the bones head relative to its armature position.
|length |Yes |Float |The bones length
|connected |No |Boolean |Default `false`

Only other `stf.bone` type resources are allowed as its children.

## Implementations
* Blender: [GitHub](https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_bone/stf_bone.py) | [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_bone/stf_bone.py)
* Unity: [GitHub](https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Bone.cs) | [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/commit/5320b3e0f2bd631ac0d901ebc2d5765b0eff2a8a/Runtime/Modules/Modules_Core/STF_Bone.cs)
* Godot: [GitHub](https://github.com/emperorofmars/stf_godot/blob/master/addons/stf_godot/modules/stf/STF_Bone.gd) | [Codeberg](https://codeberg.org/emperorofmars/stf_godot/src/commit/d518b25aeb5b74cc57eb0f82f31a5f7fdbca2aa0/addons/stf_godot/modules/stf/STF_Bone.gd)

## Json Example
```json
"0936400e-013c-475f-bd43-8d3f643e46a3": {
	"type": "stf.bone",
	"name": "LowerArm.R",
	"children": [
		"534a659c-5d6e-4692-9228-2974debbb46e",
		"3ea99969-ff70-48b6-9f47-168367e54296",
		"31832adf-f1eb-4902-9458-9946bbbdb463"
	],
	"connected": true,
	"translation": [
		-0.32599180936813354,
		1.0100003480911255,
		-0.04301619902253151
	],
	"rotation": [
		-0.5354142189025879,
		0.5126163959503174,
		0.5126165747642517,
		0.4333362877368927
	],
	"length": 0.21657702326774597
}
```
