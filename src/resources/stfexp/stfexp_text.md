# stfexp.text

Bare minimum text resource.

To be expanded with more attributes, i.e. alignment, fontsize, etc...

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.TextCurve
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/expanded/stfexp_text/stfexp_text.py)
*	- **Unity**
	- TextMeshPro, Text
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STFEXP/STFEXP_Text.cs)
*	- **Godot**
	- STFEXP_Text_Resource
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stfexp/STFEXP_Text.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
text | Yes | string | text
:::

## Json Example
```json
"6850e4f0-2f2f-40b0-8236-50b0c7740bd2": {
	"type": "stfexp.text",
	"name": "Text",
	"text": "foo\nbar"
},
```
