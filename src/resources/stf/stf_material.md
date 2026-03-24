# stf.material

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Material
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_material/stf_material.py)
*	- **Unity**
	- Material
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Material/STF_Material.cs)\
		[Default Processor](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Processors/Processors_STF/STF_Material_Processor.cs)
*	- **Godot**
	- Material
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Material.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
style_hints | No | List<string> | Hints on the visual style of the material
shader_targets | No | Dict<List<string>> | Hints on the target shader per target application
properties | Yes | Dict<string, Property-Object> | Dict of Property-ID as a string to an Object
:::

Property-IDs can be freely chosen by users.\
If an implementations happens to support a Property-ID with its Property-Object's type, it will be used.

### Property-Object properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
type | No | String | Type of the value variables
values | No | List<Value-Variable> | List of values. The value object is determined by the `type`
:::

The following types for property-values are supported:

#### `float`
Json float value

#### `int`
Json int value

#### `color`
Json array of four floats, corresponding to the RGBA color channels.

#### `image`
An Image-Property-Value-Object:

:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
image | Yes | Resource-ID | ID of an `stf.image` or compatible resource.
:::

TODO: the image object should be expanded with UV-offsets and such

## Json Example
```json
"0060c2b8-d856-4459-a88a-16e659792e6f": {
	"type": "stf.material",
	"name": "Body",
	"properties": {
		"albedo.texture": {
			"type": "image",
			"values": [
				{
					"image": 0
				}
			]
		},
		"roughness.texture": {
			"type": "image",
			"values": [
				{
					"image": 1
				}
			]
		},
		"metallic.texture": {
			"type": "image",
			"values": [
				{
					"image": 2
				}
			]
		},
		"normal.texture": {
			"type": "image",
			"values": [
				{
					"image": 3
				}
			]
		}
	},
	"style_hints": [
		"realistic",
		"pbr"
	],
	"shader_targets": {
		"blender": [
			"ShaderNodeBsdfPrincipled"
		]
	},
	"referenced_resources": [
		"f518a35d-d788-4692-a2dd-84d036d259e8",
		"edc8188f-7d85-419c-967f-5f7b427d8288",
		"5761ccd4-55bd-4fa5-ac98-f3d32004ac9e",
		"746f1aa1-5287-4d57-8892-e26fe631b953"
	]
}
```
