# stfexp.mesh.creases
Represents mesh's vertex and edge creases.

## Representations
* Blender: STF Component on Mesh
* Unity: Not relevant
* Godot: Not relevant

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
indices_width | No | int | The width of vertex-indices in bytes.
vertex_creases | No | Buffer-ID | A float represents the vertex-crease value at the index of the vertex.
edges | No | Buffer-ID | A pair of indices specifies the edge which has a crease value.
edge_creases | No | Buffer-ID | A float represents the crease value of the edge at the same index.
:::

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_mesh_creases.py)
*	- **Unity**
	- Not relevant
*	- **Godot**
	- Not relevant
:::

## Json Example
```json
"b258892d-6175-4c8c-8a95-20eb2a22c98a": {
	"type": "stfexp.mesh.creases",
	"referenced_buffers": [
		"92e4dc92-d183-4710-9c0f-37c7b302ed4a",
		"fb7ccce6-a6a1-47b4-b39f-b35b54eae760",
		"492ef1e5-bd88-4d52-9123-6182115aabe8"
	],
	"vertex_creases": 0,
	"edge_creases": 1,
	"edges": 2,
	"indices_width": 4
},
```
