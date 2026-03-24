# stf.animation
An animation relative to a prefab.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- Actions set-up with [Slot Link](https://extensions.blender.org/add-ons/slot-link/)
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_animation/stf_animation.py)
*	- **Unity**
	- AnimationClip
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Animation.cs)
		[Default Processor](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Processors/Processors_STF/STF_Animation_Processor.cs)
*	- **Godot**
	- Animation
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Animation.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
loop | Yes | string | Whether to loop the animation and how
fps | Yes | float |
range | Yes | List<float> | Beginning and end frame of the animation
bake_on_export | No | bool | Whether the animation should be baked on
tracks | Yes | List<Track-Object> |
tracks_baked | No | List<Track-Object> | Tracks that are the result of a baking operation.
:::

### Track-Object properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
target | Yes | Path | STF path of the target property
timepoints | Yes | List<float> | Sorted list of points in time at which keyframes exist
interpolation | No | string | Interpolation type for the entire track.
subtracks | Yes | List<Subtrack-Object / null> |
track_baked | No | bool | Indicates whether the entire tracks is generated, i.e. by a baking operation.
reset_animation | No | Resource-ID | Reference to a reset animation.
is_reset_animation | No | bool | Whether this animation is a reset-animation. Default is `false`.
:::

### Subtrack-Object properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
keyframes | Yes | List<Keyframe-Array / null> |
baked | No | Buffer-ID | Baked values between range[0] and range[1]
:::

### Keyframe-Array
:::{table}
:align: left
:widths: auto
Index | Type | Description
:--- | :--- | :---
0 |bool |`true` if this keyframe is a source of truth, as in not baked or generated.
1 |float |The main value
2 |string |interpolation type
:::

In case the previous keyframe has an out-tangent, this keyframes in-tangent is added at the last position in the keyframe-array.

:::{table}
:align: left
:widths: auto
Index | Type | Description
:--- | :--- | :---
last | float | In-tangent x and y offset, present only if the previous keyframe has an out-tangent
:::

Depending on the `interpolation type`, the following properties are added.

#### bezier
:::{table}
:align: left
:widths: auto
Index | Type | Description
:--- | :--- | :---
3 | string | tangent type
4 | List<float> | Out-tangent x and y offset
:::


## Json Example
```json
"8e657448-a4b0-4020-9254-437b0611a765": {
	"type": "stf.animation",
	"name": "Test Animation",
	"loop": "none",
	"fps": 24,
	"range": [
		1.0,
		5.0
	],
	"reset_animation": 0,
	"tracks": [
		{
			"target": [
				"bbff51e8-b34d-4ec4-aca4-3fcecad73309",
				"instance",
				"blendshape",
				"MouthEdgesOpen",
				"value"
			],
			"timepoints": [
				1.0,
				5.0
			],
			"subtracks": [
				{
					"keyframes": [
						[
							true,
							0.0,
							"bezier",
							"auto",
							[
								1.3333334922790527,
								0.0
							]
						],
						[
							true,
							1.0,
							"bezier",
							"auto",
							[
								1.3333334922790527,
								0.0
							],
							[
								-1.3333334922790527,
								0.0
							]
						]
					],
					"baked": 0
				}
			],
			"interpolation": "bezier",
			"track_baked": false
		},
		{
			"target": [
				"e6ae2ed1-fc53-43ee-ac53-05bf296d5fc1",
				"instance",
				"29c1fb4e-37f7-46d5-b07e-526934455996",
				"r"
			],
			"timepoints": [
				1.0,
				5.0
			],
			"subtracks": [
				{
					"keyframes": [
						[
							true,
							0.8330915570259094,
							"bezier",
							"auto",
							[
								1.3333334922790527,
								0.0
							]
						],
						[
							true,
							0.8460156917572021,
							"bezier",
							"auto",
							[
								1.3333334922790527,
								0.0
							],
							[
								-1.3333334922790527,
								0.0
							]
						]
					],
					"baked": 6
				},
				{
					"keyframes": [
						[
							true,
							4.20605830192368e-16,
							"bezier",
							"auto",
							[
								1.3333334922790527,
								0.0
							]
						],
						[
							true,
							4.3544335926898076e-16,
							"bezier",
							"auto",
							[
								1.3333334922790527,
								0.0
							],
							[
								-1.3333334922790527,
								0.0
							]
						]
					],
					"baked": 7
				},
				{
					"keyframes": [
						[
							true,
							-1.713443229014921e-16,
							"bezier",
							"auto",
							[
								1.3333334922790527,
								0.0
							]
						],
						[
							true,
							-1.7949213134447822e-16,
							"bezier",
							"auto",
							[
								1.3333334922790527,
								0.0
							],
							[
								-1.3333334922790527,
								0.0
							]
						]
					],
					"baked": 8
				},
				{
					"keyframes": [
						[
							true,
							0.5531351566314697,
							"bezier",
							"auto",
							[
								1.3333334922790527,
								0.0
							]
						],
						[
							true,
							0.5331581234931946,
							"bezier",
							"auto",
							[
								1.3333334922790527,
								0.0
							],
							[
								-1.3333334922790527,
								0.0
							]
						]
					],
					"baked": 9
				}
			],
			"interpolation": "bezier",
			"track_baked": false
		}
	],
	"referenced_buffers": [
		"d8127b86-db5a-4914-b04b-8303058abbcf",
		"65d2a116-3534-418d-a60d-8fbf63e086d0",
		"62291a71-9c14-4fee-811b-406abf5dadec",
		"87638823-adb0-4822-ad66-9cabdf0e0de4",
		"e17a8389-5517-4c33-a5d7-17d93f0d00b4",
		"a893069d-0b84-44e4-846c-24d59ece8fac",
		"4c462ff6-8fd6-4c62-b668-ac87e700c9df",
		"265c2f68-85fb-4f73-8643-8f419f5b9c62",
		"2ccf7b4a-1a7f-4f9f-b729-751b9539eaf6",
		"c7859f35-1c2e-46af-a50e-e52df147b53f"
	],
	"referenced_resources": [
		"49ebe3d6-b733-4556-91ce-5adc6779f0b3"
	]
}
```
