# stf.mesh

## Representations
* Blender: Mesh
* Unity: Mesh
* Godot: Mesh

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Mesh
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_mesh/stf_mesh.py)
*	- **Unity**
	- Mesh
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Mesh/STF_Mesh.cs)\
		[Default Processor](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Processors/Processors_STF/STF_Mesh_Processor.cs)
*	- **Godot**
	- Mesh
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Mesh.gd)
:::

## Datamodel
* **Face:** Made up of one or more triangles.\
The Material Index exists at this level.
* **Triangle:** 3 Face Corners, which can be shared by other triangles of the same face.
* **Face Corner:** Reference to a Split, which can be shared by other face corners.
* **Split:** References a vertex, which can be shared by other splits, as long as at least one of their other properties (Normal, UV, Color, ...) is unique.\
Normals, UVs and colors exist at this level.
* **Vertex:** Position\
Blendshapes, weights & vertex groups exist at this level.

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
float_width | No | uint | Byte-width of float-values. Default: 4
indices_width | No | uint | Byte-width of indices. Default: 4
material_slots | No | List<Resource-ID / null> |List of material IDs in the order of the meshes material-slots
vertices | Yes | Buffer-ID | 3 floats per vertex
face_corners | Yes | Buffer-ID | Index of the split for each face corner
splits | Yes | Buffer-ID | Vertex index for each unique combination of normals, uvs, colors, etc..
split_normals | No | Buffer-ID | 3 floats per normal
split_colors | No | Buffer-ID | 4 floats per color (RGBA)
tris | Yes | Buffer-ID | 3 indices per triangle
faces | Yes | Buffer-ID | number of tris for the face
material_indices | No | Buffer-ID | Material index per face
sharp_edges | No | Buffer-ID |
sharp_face_indices | No | Buffer-ID |
lines | No | Buffer-ID |
armature | No | Resource-ID | ID of the armature if the mesh is skinned
weight_lens_width | No | uint |
bone_indices_width | No | uint |
bones | No | List<Resource-ID> | Bone references in the order by which they will be referenced by `bone_indices`.
weight_lens | No | Buffer-ID |
bone_indices | No | Buffer-ID |
weights | No | Buffer-ID |
uvs | No | List<UV-Object> |
blendshapes | No | List<Blendshape-Object> |
vertex_groups | No | List<VertexGroup-Object> |
:::

### UV-Object properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
name | Yes | string |
uv | Yes | Buffer-ID | 2 floats per split
:::

### Blendshape-Object properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
name | Yes | string |
default_value | No | float | default: 0
limit_upper | No | float | default: 1
limit_lower | No | float | default: 0
indices | No | Buffer-ID | int
position_offsets | Yes | Buffer-ID | 3 floats per vertex
split_indices | No | Buffer-ID | int
split_normals | No | Buffer-ID | 3 floats per split
:::

### VertexGroup-Object properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
name | Yes | string |
indices | No | Buffer-ID | int
weights | Yes | Buffer-ID | float per vertex
:::


## Json Example
```json
"ededda7a-651c-44a9-b5a2-b6b6ff799881": {
	"type": "stf.mesh",
	"name": "Cube",
	"referenced_resources": [
		"ec16a927-1b26-4157-a3f2-71455d05e2bf"
	],
	"material_slots": [
		0
	],
	"float_width": 4,
	"indices_width": 1,
	"referenced_buffers": [
		"a2678730-f63c-4415-85a8-9426bfc7242e",
		"be7acc51-f47c-406c-82f6-c7ea7833ed4d",
		"c29e0d3a-9b4d-444b-93f1-e3163332fdcb",
		"d3329a1a-b79a-4d27-b16d-f7af2420951a",
		"97925952-70a7-4773-96fe-00e44d4cdfee",
		"05039913-1397-4f3c-9b54-d514ace748e7",
		"4d86408e-84f5-4f05-86b2-82f3a8803f9d",
		"6cdbf5c5-e770-4bbf-924f-4c10818826e9",
		"e7b0b03d-c004-4876-97a3-c4a26b7ac3c9",
		"ecb6ef8b-618c-4dcd-a0b0-0a0cf70cf143",
		"42a32c5f-edb6-43c3-a028-fa2a75b46671"
	],
	"vertices": 0,
	"face_corners": 1,
	"splits": 2,
	"split_normals": 3,
	"uvs": [
		{
			"name": "UVMap",
			"uv": 4
		}
	],
	"tris": 5,
	"material_indices_width": 1,
	"faces": 6,
	"material_indices": 7,
	"sharp_face_indices": 8,
	"lines": 9,
	"sharp_edges": 10,
	"components": [
		"5b09c146-b626-4fb4-a4fa-b33b0e5085e2"
	]
}
```
