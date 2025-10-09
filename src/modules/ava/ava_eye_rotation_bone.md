# ava.eye_rotation.bone
Defines limits for eyebone rotations.

## Representations
* Blender: Component on Armature
* Unity: Component
* Godot: TBD

## Properties

:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
up | Yes | float | Angle in radians.
down | Yes | float | Angle in radians.
in | Yes | float | Angle in radians.
out | Yes | float | Angle in radians.
:::

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/ava/ava_eyerotation_bone.py)
*	- **Unity**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/Runtime/Modules/AVA_EyeRotation_Bone.cs)
*	- **Godot**
	- TBD
:::

## Json Example
```json
"247d40d1-0a38-4453-9e1b-641bc21f5512": {
	"type": "ava.eye_rotation.bone",
	"up": 0.3490658402442932,
	"down": 0.3141592741012573,
	"in": 0.2617993950843811,
	"out": 0.3141592741012573
},
```
