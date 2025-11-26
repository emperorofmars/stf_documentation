# ava.visemes.blendshape
Define blendshapes for audio-based lip-sync.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF_Component on bpy.types.Mesh
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/ava/ava_visemes_blendshape.py)
*	- **Unity**
	- Only application specific representations
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/Runtime/Modules/AVA_Visemes_Blendshape.cs)\
		[VRChat Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_VRChat/Editor/Processors/VRC_AVA_Visemes_Blendshape_Processor.cs)\
		[UNIVRM0 Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_UNIVRM0/Editor/Processors/UNIVRM0_AVA_Visemes_Blendshape_Processor.cs)\
		[BasisVR Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_BASISVR/Editor/Processors/BASIS_AVA_Visemes_Blendshape_Processor.cs)
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
sil | Yes | string | Blendshape name
aa | Yes | string | Blendshape name
ch | Yes | string | Blendshape name
dd | Yes | string | Blendshape name
e | Yes | string | Blendshape name
ff | Yes | string | Blendshape name
ih | Yes | string | Blendshape name
kk | Yes | string | Blendshape name
nn | Yes | string | Blendshape name
oh | Yes | string | Blendshape name
ou | Yes | string | Blendshape name
pp | Yes | string | Blendshape name
rr | Yes | string | Blendshape name
ss | Yes | string | Blendshape name
th | Yes | string | Blendshape name
:::

## Json Example
```json
"cbded680-60c3-4676-aec1-67fcaaf6331a": {
	"type": "ava.visemes.blendshape",
	"sil": "Vis_SIL",
	"aa": "Vis_AA",
	"ch": "Vis_CH",
	"dd": "Vis_DD",
	"e": "Vis_E",
	"ff": "Vis_FF",
	"ih": "Vis_IH",
	"kk": "Vis_KK",
	"nn": "Vis_NN",
	"oh": "Vis_OH",
	"ou": "Vis_OU",
	"pp": "Vis_PP",
	"rr": "Vis_RR",
	"ss": "Vis_SS",
	"th": "Vis_TH"
},
```
