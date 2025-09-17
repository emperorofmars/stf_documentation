# stf.image

## Properties
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|format |Yes |String |Format of the image. Officially supported formats are: `png`, `jpg`
|buffer |Yes |Buffer-ID |Buffer containing the image file
|data_type |No |String |Type of image data. As of not it can be `color` or `non_color`.

## Implementations
* Blender: [GitHub](https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_image/stf_image.py) | [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/commit/f45c3b56085fbd550901d6160a2d7cc96f69cda5/stfblender/stf_modules/core/stf_image/stf_image.py)
* Unity: [GitHub](https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Image.cs) | [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/commit/5320b3e0f2bd631ac0d901ebc2d5765b0eff2a8a/Runtime/Modules/Modules_Core/STF_Image.cs)
* Godot: [GitHub](https://github.com/emperorofmars/stf_godot/blob/master/addons/stf_godot/modules/stf/STF_Image.gd) | [Codeberg](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Image.gd)

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
