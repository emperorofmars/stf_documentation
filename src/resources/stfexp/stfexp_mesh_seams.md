# stfexp.mesh.seams
Represents a mesh's UV-seams.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF Component on bpy.types.Mesh
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_mesh_seams.py)
*	- **Unity**
	- Not relevant
	-
*	- **Godot**
	- Not relevant
	-
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
indices_width | No | int | The width of vertex-indices in bytes.
seams | No | Buffer-ID | A pair of indices specifies the edge which has a UV-seam.
:::

## Json Example
```json
"2160c271-80a5-4cbe-a12f-a81d883d4e49": {
	"type": "stfexp.mesh.seams",
	"indices_width": 4,
	"referenced_buffers": [
		"4211de00-5f56-497b-8f67-1edd4e2d1c9b"
	],
	"seams": 0
},
```
