# ava.avatar
Represents a VR & V-tubing avatar model.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF_Component on Collection
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/ava/ava_avatar.py)
*	- **Unity**
	- Only application specific representations
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/Runtime/Modules/AVA_Avatar.cs)\
		[VRChat Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_VRChat/Editor/Processors/VRC_AVA_Avatar_Processor.cs)\
		[UNIVRM0 Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_UNIVRM0/Editor/Processors/UNIVRM0_AVA_Avatar_Processor.cs)\
		[BasisVR Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_BASISVR/Editor/Processors/BASIS_AVA_Avatar_Processor.cs)
*	- **Godot**
	- TBD
	-
:::

## Properties

:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
viewport | No | Resource-ID | `stf.node` representing the viewport position.
primary_armature_instance | No | Resource-ID | Armature instance for humanoid IK, eye-rotations, ...
primary_mesh_instance | No | Resource-ID | Mesh instance for facial visemes
:::

## Json Example
```json
"f4957bbb-007e-4191-8429-8e871412e2f5": {
	"type": "ava.avatar",
	"referenced_resources": [
		"1bef1076-0f2a-402e-8e9f-57d2c7095319",
		"e6ae2ed1-fc53-43ee-ac53-05bf296d5fc1",
		"bbff51e8-b34d-4ec4-aca4-3fcecad73309"
	],
	"viewport": 0,
	"primary_armature_instance": 1,
	"primary_mesh_instance": 2
}
```
