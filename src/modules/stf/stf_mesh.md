# stf.mesh

## Representations
* Blender: Mesh
* Unity: Mesh
* Godot: Mesh

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
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|float_width |No |uint |Byte-width of float-values. Default: 4
|indices_width |No |uint |Byte-width of indices. Default: 4
|material_slots |No |List<Resource-ID / null> |List of material IDs in the order of the meshes material-slots
|vertices |Yes |Buffer-ID |3 floats per vertex
|face_corners |Yes |Buffer-ID |Index of the split for each face corner
|splits |Yes |Buffer-ID |Vertex index for each unique combination of normals, uvs, colors, etc..
|split_normals |No |Buffer-ID |3 floats per normal
|split_colors |No |Buffer-ID |4 floats per color (RGBA)
|tris |Yes |Buffer-ID |3 indices per triangle
|faces |Yes |Buffer-ID |number of tris for the face
|material_indices |No |Buffer-ID |Material index per face
|sharp_edges |No |Buffer-ID |
|sharp_face_indices |No |Buffer-ID |
|lines |No |Buffer-ID |
|armature |No |Resource-ID |ID of the armature if the mesh is skinned
|weight_lens_width |No |uint |
|bone_indices_width |No |uint |
|bones |No |List<Resource-ID> |Bone references in the order by which they will be referenced by `bone_indices`.
|weight_lens |No |Buffer-ID |
|bone_indices |No |Buffer-ID |
|weights |No |Buffer-ID |
|uvs |No |List<UV-Object> |
|blendshapes |No |List<Blendshape-Object> |
|vertex_groups |No |List<VertexGroup-Object> |
:::

### UV-Object properties
:::{table}
:align: left
:widths: auto
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|name |Yes |string |
|uv |Yes |Buffer-ID |2 floats per split
:::

### Blendshape-Object properties
:::{table}
:align: left
:widths: auto
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|name |Yes |string |
|default_value |No |float |default: 0
|limit_upper |No |float |default: 1
|limit_lower |No |float |default: 0
|indices |No |Buffer-ID |int
|position_offsets |Yes |Buffer-ID |3 floats per vertex
|split_indices |No |Buffer-ID |int
|split_normals |No |Buffer-ID |3 floats per split
:::

### VertexGroup-Object properties
:::{table}
:align: left
:widths: auto
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|name |Yes |string |
|indices |No |Buffer-ID |int
|weights |Yes |Buffer-ID |float per vertex
:::


## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_mesh/stf_mesh.py)
	- [GitHub](https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_mesh/stf_mesh.py)
*	- **Unity**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Mesh/STF_Mesh.cs)
	- [GitHub](https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Mesh/STF_Mesh.cs)
*	- **Godot**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Mesh.gd)
	- [GitHub](https://github.com/emperorofmars/stf_godot/blob/master/addons/stf_godot/modules/stf/STF_Mesh.gd)
:::

## Json Example
```json
"783134da-9e2a-4d69-a1f0-59952bc36895": {
	"type": "stf.mesh",
	"name": "Superawesome Mesh",
	"material_slots": [
		"dc07246c-47e9-41bb-b009-5a4eb60303e4"
	],
	"float_width": 4,
	"indices_width": 2,
	"vertices": "23ec5dc3-2e0e-460b-b07d-413e64f9326e",
	"face_corners": "3e6c056e-6dd9-4011-bb14-97cf8e6eaaa0",
	"splits": "c4c432c7-2b1e-4282-92a3-af1a001b08bf",
	"split_normals": "528e70e1-65a1-4155-bff5-cc60fa140d14",
	"uvs": [
		{
			"name": "UVMap",
			"uv": "a0001434-7844-4038-ba8a-2e0540fe65c8"
		}
	],
	"tris": "98ef746d-1023-424b-ac04-2b27540637b6",
	"material_indices_width": 1,
	"faces": "f15060e3-49f1-43d6-a6e9-117984cbe8fe",
	"material_indices": "04a31482-e1cd-437b-be16-be26f164bfdb",
	"sharp_face_indices": "5ef64c4d-0cc8-4ad1-aadc-898b8cc7b436",
	"lines": "13084993-3492-48ca-956b-0ee0766527bf",
	"sharp_edges": "a9d12c37-94d3-43f0-ae48-4a4619416f6e",
	"vertex_groups": [
		{
			"name": "Select Some Things",
			"weights": "14f9133b-fcd4-4c00-95ee-7d8c7dab8bff",
			"indices": "af4f4676-5e26-49fc-a639-4e467076828e"
		},
		{
			"name": "Normal Project Blend Weights",
			"weights": "2a69a2fe-1a2e-4472-a3cf-064762d6b974"
		}
	],
	"blendshapes": [
		{
			"name": "ToggleOff",
			"default_value": 0.0,
			"limit_upper": 1.0,
			"limit_lower": 0.0,
			"indices": "313f0ad4-4933-49bf-8c0c-6957c2750d16",
			"position_offsets": "b4d196a5-1776-460f-8e04-721d7cff5281",
			"split_indices": "c854ed9b-93df-41f5-ab43-e0e9b8ae2625",
			"split_normals": "5fa5f424-6f4e-49c4-82b5-fb8dcaff82ef"
		},
		{
			"name": "Vis_AA",
			"default_value": 0.0,
			"limit_upper": 1.0,
			"limit_lower": 0.0,
			"position_offsets": "9db99d09-0ff7-4f92-896e-0318a31bfd46",
			"split_normals": "949c0d7a-edb7-4d8e-9b9f-c24a56646f65"
		},
		{
			"name": "Vis_IH",
			"default_value": 0.0,
			"limit_upper": 1.0,
			"limit_lower": 0.0,
			"position_offsets": "37118f5c-3dee-4e75-8067-adec146769d0",
			"split_normals": "7c88cbd6-38c2-4755-90aa-54fcd9a880d3"
		}
	],
	"components": [
		"60850594-9bab-4cb2-ac64-657ec5589f5f",
		"5e6c4973-d3cf-423f-aabe-a6a6d0959e40"
	]
}
```
