# stfexp.lightprobe_anchor
Define a object/bone from which a game-engine will sample lightprobe values.

## Representations
* Blender: STF Component
* Unity: The `Probes` -> `Anchor Override` property on a `Renderer`.
* Godot: `LightmapProbe`

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
anchor | Yes | [Resource-Path](../../format/stf_format.md#resource-path) | Path to the node from which to use as the lightprobe anchor.
:::

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_constraint_twist.py)
*	- **Unity**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Constraint_Twist.cs)
*	- **Godot**
	- TBD
:::

## Json Example
```json
"6cf57561-7578-4cc8-a66d-8353ce783e69": {
	"type": "stfexp.lightprobe_anchor",
	"referenced_resources": [
		"e6ae2ed1-fc53-43ee-ac53-05bf296d5fc1",
		"c0eac8b8-4644-40b0-a63a-e6366c70c0e4"
	],
	"anchor": [
		0,
		"instance",
		1
	]
},
```
