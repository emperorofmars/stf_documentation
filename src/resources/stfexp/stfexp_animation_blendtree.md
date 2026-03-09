# stfexp.animation_blendtree
Associate animations with a 1d or 2d position.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STFEXP_Animation_Blendtree
	- [Resource](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_resources/expanded/stfexp_animation_blendtree.py)
*	- **Unity**
	- BlendTree
	- [Resource](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Resources/Resources_STFEXP/STFEXP_AnimationBlendtree.cs)\
		[Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_STFEXP/STFEXP_AnimationBlendtree_Processor.cs)
*	- **Godot**
	- TBD
	- -
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
blendtree_type | Yes | string | `1d` or `2d`
animations | Yes | Array[Animation-Mapping-Object] |
:::

### Animation-Mapping-Object properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
position | Yes | float / Array<float> | A single float for `1d` blendtrees or an array of two floats for `2d` blendtrees.
animation | Yes | Resource-ID |
:::

## Json Example
```json
"eefcb040-54f2-4025-98e2-b0fda174a572": {
	"type": "stfexp.animation_blendtree",
	"name": "Tail Puppet",
	"blendtree_type": "2d",
	"referenced_resources": [
		"7e1534a8-fef7-4f87-8c81-b356e5962bc3",
		"0530bc0d-603e-4a4a-b105-29645cac5ce1",
		"98be1861-4e41-4076-9655-4884b3bdf58b",
		"1d1bfee4-e8dd-48c0-903f-1832e595778a",
		"f101992e-9619-48e8-a1bd-9da39c1e9a34"
	],
	"animations": [
		{
			"position": [
				0.0,
				1.0
			],
			"animation": 0
		},
		{
			"position": [
				0.0,
				-1.0
			],
			"animation": 1
		},
		{
			"position": [
				-1.0,
				0.0
			],
			"animation": 2
		},
		{
			"position": [
				1.0,
				0.0
			],
			"animation": 3
		},
		{
			"position": [
				0.0,
				0.0
			],
			"animation": 4
		}
	]
},
```

