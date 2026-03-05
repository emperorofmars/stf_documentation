# ava.voice_position
Position of the voice audio-source on a VR & V-tubing avatar.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF_Component on Collection
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/ava/ava_voice_position.py)
*	- **Unity**
	- Only application specific representations
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/Runtime/Modules/AVA_VoicePosition.cs)\
		[BasisVR Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_BASISVR/Editor/Processors/BASIS_AVA_VoicePosition_Processor.cs)
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
voice_position | No | Resource-ID | `stf.node` representing the voice position.
:::

## Json Example
```json
"95c7b129-1b5a-423a-a87c-cd12e1e62cbf": {
	"type": "ava.voice_position",
	"name": "Voice Position",
	"referenced_resources": [
		"2a6749bb-989f-4cbc-a58e-9f62ab621b85"
	],
	"voice_position": 0
},
```
