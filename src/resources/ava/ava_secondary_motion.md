# ava.secondary_motion
Bare minimum representation of a bone-physics chain. The component must be placed at the root-node of the chain.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF_Component on Collection
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/ava/ava_secondary_motion.py)
*	- **Unity**
	- Only application specific representations
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/AVA/Runtime/Resources/AVA_SecondaryMotion.cs)\
		[VRChat Processor](https://codeberg.org/stf_format/stf_unity/src/branch/master/AVA/AVA_VRChat/Editor/Processors/VRC_AVA_SecondaryMotion_Processor.cs)\
		[UNIVRM0 Processor](https://codeberg.org/stf_format/stf_unity/src/branch/master/AVA/AVA_UNIVRM0/Editor/Processors/UNIVRM0_AVA_SecondaryMotion_Processor.cs)
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
intensity | No | float | placeholder value
:::

## Json Example
```json
"39472e4a-9a14-4b09-8711-0278cb09f8c4": {
	"type": "ava.secondary_motion",
	"name": "Hair Physics",
	"exclusion_group": "physics_hair",
	"intensity": 0.3
},
```
