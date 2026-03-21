# stfexp.instance.text

Instance of a text resource.

To be expanded with more attributes and functionality.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Object with bpy.types.TextCurve
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/expanded/stfexp_instance_text.py)
*	- **Unity**
	- TextMeshPro, Text
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STFEXP/STFEXP_Instance_Text.cs)
*	- **Godot**
	- Label3D
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stfexp/STFEXP_Instance_Text.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
text | Yes | Resource-ID | text
:::

## Json Example
```json
"66e4c731-4b20-408b-bbc5-9d68b0ee71e8": {
	"type": "stfexp.instance.text",
	"name": "My fancy text instance",
	"referenced_resources": [
		"6850e4f0-2f2f-40b0-8236-50b0c7740bd2"
	],
	"text": 0
},
```
