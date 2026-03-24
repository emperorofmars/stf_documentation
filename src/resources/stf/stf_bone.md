# stf.bone
Can only exist within `stf.armature`.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Bone
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_bone/stf_bone.py)
*	- **Unity**
	- GameObject
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Bone.cs)
*	- **Godot**
	- Skeleton3D's bones
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Bone.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
translation | Yes | Translation | The position of the bone relative to its armature position.
rotation | Yes | Rotation | The rotation of the bones head relative to its armature position.
length | Yes | Float | The bones length
connected | No | Boolean | Default `false`
deform | No | Boolean | Whether the bone can deform meshes. Implicit default is `true`
non_deform_use | No | String | Indicates the purpose of the bone if `deform` is `false`. Possible values include: `ik_target`, `ik_pole`, ...
:::

Only other `stf.bone` type resources are allowed as its children.


## Json Example
```json
"360e5f0a-3f49-4e1f-9988-a66bd73bc959": {
	"type": "stf.bone",
	"name": "Wrist.L",
	"children": [
		0,
		1,
		2,
		3,
		4
	],
	"connected": true,
	"referenced_resources": [
		"c55897a3-89b3-41ad-b72b-b2af215668c1",
		"2399cb0c-45fa-427f-b060-180ac74423c3",
		"70739cc3-c4da-44b0-a295-09c64c64e19d",
		"6cf96773-1a92-40f9-a718-03cff6b5a96e",
		"abd6565e-b64a-4f70-a1a5-af7223131db4"
	],
	"translation": [
		0.5410950183868408,
		0.9885833859443665,
		-0.02969183586537838
	],
	"rotation": [
		-0.48921021819114685,
		-0.5100647211074829,
		-0.5100647807121277,
		0.4902461767196655
	],
	"length": 0.06538591533899307
}
```
