# ava.eyelids.blendshape
Defines blendshapes which move the eyelids.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF_Component on bpy.types.Mesh
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/ava/ava_eyelids_blendshape.py)
*	- **Unity**
	- Only application specific representations
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/Runtime/Modules/AVA_Eyelids_Blendshape.cs)\
		[VRChat Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_VRChat/Editor/Processors/VRC_AVA_Eyelids_Blendshape_Processor.cs)\
		[UNIVRM0 Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_UNIVRM0/Editor/Processors/UNIVRM0_AVA_Eyelids_Blendshape_Processor.cs)\
		[BasisVR Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_BASISVR/Editor/Processors/BASIS_AVA_Eyelids_Blendshape_Processor.cs)
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
closed | No | string | Blendshape name
up | No | string | Blendshape name
down | No | string | Blendshape name
left | No | string | Blendshape name
right | No | string | Blendshape name
closed_left | No | string | Blendshape name
up_left | No | string | Blendshape name
down_left | No | string | Blendshape name
left_left | No | string | Blendshape name
right_left | No | string | Blendshape name
closed_right | No | string | Blendshape name
up_right | No | string | Blendshape name
down_right | No | string | Blendshape name
left_right | No | string | Blendshape name
right_right | No | string | Blendshape name
:::

## Json Example
```json
"7e498d96-39a0-48a6-9a58-661de164e579": {
	"type": "ava.eyelids.blendshape",
	"closed": "EyeClosed",
	"up": "EyeLookUp",
	"down": "EyeLookDown",
	"left": "",
	"right": "",
	"closed_left": "EyeClosedLeft",
	"up_left": "EyeLookUpLeft",
	"down_left": "EyeLookDownLeft",
	"left_left": "",
	"right_left": "",
	"closed_right": "EyeClosedRight",
	"up_right": "EyeLookUpRight",
	"down_right": "EyeLookDownRight",
	"left_right": "",
	"right_right": ""
},
```
