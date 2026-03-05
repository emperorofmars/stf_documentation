# ava.face_tracking.blendshape
Defines wich face-tracking standard this avatar conforms to.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF_Component on bpy.types.Mesh
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/ava/ava_facial_tracking_blendshape/ava_face_tracking_blendshape.py)
*	- **Unity**
	- Only application specific representations
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/Runtime/Modules/AVA_FaceTracking_Blendshape.cs)\
		[VRChat Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_VRChat/Editor/Processors/VRC_AVA_FaceTracking_Blendshape_Processor.cs)
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
ft_type | Yes | string | Type of the face-tracking standard to use with this avatar
:::

## Json Example
```json
"6a3f10f1-e6b8-4cd9-bf15-1f93e5118133": {
	"type": "ava.face_tracking.blendshape",
	"ft_type": "unified_expressions"
},
```
