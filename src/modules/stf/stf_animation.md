# stf.animation

## Properties
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|loop |Yes |string |Whether to loop the animation and how
|fps |Yes |float |
|range |Yes |List<float> |Beginning and end frame of the animation
|bake_on_export |No |bool |Whether the animation should be baked on
|tracks |Yes |List<Track-Object> |

### Track-Object properties
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|target |Yes |Path |STF path of the target property
|subtracks |Yes |List<Subtrack-Object / null> |

### Subtrack-Object properties
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|keyframes |Yes |List<Keyframe-Array / null> |
|baked |No |Buffer-ID |Baked values between range[0] and range[1]

### Keyframe-Array
| Index | Type | Description |
| :--- | :--- | :--- |
|0 |bool |`true` if this keyframe is a source of truth, as in not baked or generated.
|1 |float |Timepoint in frames
|2 |float |The main value
|3 |string |interpolation type

In case the previous keyframe has an out-tangent, this keyframes in-tangent is added at the last position in the keyframe-array.

| Index | Type | Description |
| :--- | :--- | :--- |
| last | float | In-tangent x and y offset, present only if the previous keyframe has an out-tangent

Depending on the `interpolation type`, the following properties are added.

#### bezier
| Index | Type | Description |
| :--- | :--- | :--- |
|4 |string |tangent type
|5 |List<float> |Out-tangent x and y offset

## Implementations
* Blender: [GitHub](https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_animation/stf_animation.py) | [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_animation/stf_animation.py)
* Unity: [GitHub](https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Animation.cs) | [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Animation.cs)
* Godot: [GitHub](https://github.com/emperorofmars/stf_godot/blob/master/addons/stf_godot/modules/stf/STF_Animation.gd) | [Codeberg](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Animation.gd)


## Json Example
```json
"6a60e775-4374-4439-bbbe-49ea5edc9438": {
	"type": "stf.animation",
	"name": "Anim Test",
	"loop": "none",
	"fps": 24,
	"bake_on_export": true,
	"range": [
		1.0,
		16.0
	],
	"tracks": [
		{
			"target": [
				"737c6e44-4269-409b-95a8-cfc8e680a13b",
				"t"
			],
			"subtracks": [
				{
					"keyframes": [
						[
							true,
							1.0,
							-0.7435536980628967,
							"bezier",
							"aligned",
							[
								2.0,
								0.0
							]
						],
						[
							true,
							16.0,
							-0.2216922640800476,
							"bezier",
							"aligned",
							[
								3.0,
								0.0
							],
							[
								-3.0,
								0.0
							]
						]
					],
					"baked": "ba4b975f-3df3-42cf-8508-d527b1468b18"
				},
				{
					"keyframes": [
						[
							true,
							1.0,
							2.200054168701172,
							"bezier",
							"aligned",
							[
								2.0,
								0.0
							]
						],
						[
							true,
							16.0,
							0.4340066909790039,
							"bezier",
							"aligned",
							[
								3.0,
								0.0
							],
							[
								-3.0,
								0.0
							]
						]
					],
					"baked": "591f8e72-d4bc-456f-8420-95a46a687329"
				},
				{
					"keyframes": [
						[
							true,
							1.0,
							1.996330738067627,
							"bezier",
							"aligned",
							[
								2.0,
								0.0
							]
						],
						[
							true,
							16.0,
							0.2330167293548584,
							"bezier",
							"aligned",
							[
								3.0,
								0.0
							],
							[
								-3.0,
								0.0
							]
						]
					],
					"baked": "b1951f62-a79e-4cfb-bb3b-75e431d52ca0"
				}
			]
		},
		{
			"target": [
				"737c6e44-4269-409b-95a8-cfc8e680a13b",
				"instance",
				"blendshape",
				"Key 1",
				"value"
			],
			"subtracks": [
				{
					"keyframes": [
						[
							true,
							1.0,
							0.0,
							"bezier",
							"aligned",
							[
								2.0,
								0.0
							]
						],
						[
							true,
							7.0,
							0.7300613522529602,
							"bezier",
							"aligned",
							[
								3.0,
								0.0
							],
							[
								-2.0,
								0.0
							]
						],
						[
							true,
							16.0,
							0.0,
							"bezier",
							"aligned",
							[
								3.0,
								0.0
							],
							[
								-3.0,
								0.0
							]
						]
					],
					"baked": "fba2e828-e6c9-476f-b47c-d1851bcacc7d"
				}
			]
		}
	]
},
```
