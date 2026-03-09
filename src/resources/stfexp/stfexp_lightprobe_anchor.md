# stfexp.lightprobe_anchor
Define a object/bone from which a game-engine will sample lightprobe values.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF Component on bpy.types.Object with bpy.types.Mesh
	- [Resource](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_resources/expanded/stfexp_lightprobe_anchor.py)
*	- **Unity**
	- The `Probes` -> `Anchor Override` property on a `Renderer`.
	- [Resource](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Resources/Resources_STFEXP/STFEXP_LightprobeAnchor.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_STFEXP/STFEXP_LightprobeAnchor_Processor.cs)
*	- **Godot**
	- LightmapProbe
	- [Resource](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/resources/stfexp/STFEXP_Lightprobe_Anchor.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
anchor | Yes | [Resource-Path](../../format/stf_format.md#resource-path) | Path to the node whose position to use as the lightprobe anchor.
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
