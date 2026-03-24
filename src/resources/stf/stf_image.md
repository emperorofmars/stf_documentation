# stf.image

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Image
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_image/stf_image.py)
*	- **Unity**
	- [STF_Image Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Image.cs#L9)
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Image.cs)
		[Default Processor](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Processors/Processors_STF/STF_Image_Processor.cs)
*	- **Godot**
	- Image
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Image.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
format | Yes | String | Format of the image. Officially supported formats are: `png`, `jpg`
buffer | Yes | Buffer-ID | Buffer containing the image file
data_type | No | String | Type of image data. As of not it can be `color` or `non_color`.
:::


## Json Example
```json
"f518a35d-d788-4692-a2dd-84d036d259e8": {
	"type": "stf.image",
	"name": "squeak_warrior_paint_Body_BaseColor.png",
	"format": "png",
	"data_type": "color",
	"referenced_buffers": [
		"2f1f1b32-6960-44d6-9b9a-a441be06f38c"
	],
	"buffer": 0,
	"components": [
		"6db664cf-a4ba-4dd5-8845-477ca01f24d0"
	]
}
```
