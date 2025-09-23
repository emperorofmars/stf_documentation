# stf.texture
Information on how an image is to be converted into a GPU texture.

## Properties
:::{table}
:align: left
:widths: auto
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|width |Yes |int |Width of the resulting GPU texture
|height |Yes |int |Height of the resulting GPU texture
|downscale_priority |Yes |int |In case of an enforced memory limit, how quickly should the resolution of the resulting GPU texture reduced.
|quality |Yes |float |Indicate how much the GPU texture can be compressed. Value range is from 0 to 1. 1 means not compression should be used.
|mipmaps |Yes |bool |Whether to generate mipmaps
:::

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_texture/stf_texture.py)
	- [GitHub](https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_texture/stf_texture.py)
*	- **Unity**
	- [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Texture.cs)
	- [GitHub](https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Texture.cs)
*	- **Godot**
	- TBD
	-
:::

## Json Example
```json
"f0aa405c-8548-453d-8758-516e5c43d45e": {
	"type": "stf.texture",
	"width": 1024,
	"height": 1024,
	"downscale_priority": 0,
	"quality": 0.800000011920929,
	"mipmaps": true
}
```
