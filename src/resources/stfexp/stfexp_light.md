# stfexp.light

A real-time rendering friendly light-source. It can represent pointlights, directional lights & spotlights.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Light
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_light.py)
*	- **Unity**
	- Light
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Light.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_Expanded/STFEXP_Light_Processor.cs)
*	- **Godot**
	- Light3D
	- [Module](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stfexp/STFEXP_Light.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
light_type | Yes | string | Possible values are: "point", "directional", "spot"
brightness | Yes | float | 
color | Yes | list[float] | Light color
temperature | No | float | If set, the color will be used as the tint
shadow | No | boolean | Whether this light casts shadows
range | If light_type is "point" or "spot" | float | 
spot_angle | If light_type is "spot" | float | 
:::

## Json Example
```json
"e21e75ef-fc71-4970-b127-47873b09ce90": {
	"type": "stfexp.light",
	"name": "",
	"light_type": "spot",
	"range": 8.0,
	"spot_angle": 1.3089969158172607,
	"brightness": 1000.0,
	"color": [
		1.0,
		0.046901725232601166,
		0.6305924654006958
	],
	"temperature": 6500.0,
	"shadow": true
},
```
