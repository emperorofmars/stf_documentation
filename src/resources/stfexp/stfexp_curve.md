# stfexp.curve
2D and 3D Bézier Curves in 3D space

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Curve
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/stfexp/stfexp_curve.py)
*	- **Godot**
	- STFEXP_Curve_Resource
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stfexp/STFEXP_Curve.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
dimensions | Yes | int | 2 or 3
splines | Yes | Spline-Object | List of splines
:::

### Spline-Object properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
type | Yes | string | "bezier" is the only supported type
points | Yes | Point-Object | List of bezier points
cyclic | yes | bool | Whether the spline forms a circle
:::
:::

### Point-Object properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
translation | Yes | list[float] | Vector 3
handle_in | Yes | list[float] | Vector 3
handle_in_type | Yes | string | "free" \| "aligned" \| "auto"
handle_out | Yes | list[float] | Vector 3
handle_out_type | Yes | string | "free" \| "aligned" \| "auto"
tilt | Yes | float |
:::

## Json Example
```json
"1ed58998-148b-496e-89c4-40e09f1547ab": {
	"type": "stfexp.curve",
	"name": "B\u00e9zierCurve",
	"dimensions": 3,
	"splines": [
		{
			"type": "bezier",
			"points": [
				{
					"translation": [
						-1.0,
						0,
						0
					],
					"handle_in": [
						-1.5,
						0,
						0.5
					],
					"handle_in_type": "aligned",
					"handle_out": [
						-0.5,
						0,
						-0.5
					],
					"handle_out_type": "aligned",
					"tilt": 0.0
				},
				{
					"translation": [
						1.0,
						0,
						0
					],
					"handle_in": [
						0,
						0,
						0
					],
					"handle_in_type": "aligned",
					"handle_out": [
						2.0,
						0,
						0
					],
					"handle_out_type": "aligned",
					"tilt": 0.0
				}
			],
			"cyclic": false
		}
	]
},
```
