# stf.image

## Representations
* Blender: Image
* Unity: STF_Image
* Godot: Image

## Properties
:::{table}
:align: left
:widths: auto
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|format |Yes |String |Format of the image. Officially supported formats are: `png`, `jpg`
|buffer |Yes |Buffer-ID |Buffer containing the image file
|data_type |No |String |Type of image data. As of not it can be `color` or `non_color`.
:::

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_image/stf_image.py)
*	- **Unity**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Image.cs)
*	- **Godot**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Image.gd)
:::


## Json Example
```json
"1bf800ea-1bda-491c-ba89-c7bfa364e239": {
	"type": "stf.image",
	"name": "Body_BaseColor.png",
	"format": "png",
	"buffer": "ef192623-cc41-445e-acd7-e435be793e95",
	"data_type": "color",
	"components": [
		"f79c8521-845f-4a6c-a44f-bd2647877e0e"
	]
}
```
