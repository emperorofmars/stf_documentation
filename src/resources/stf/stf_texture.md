# stf.texture
Information on how an image is to be converted into a GPU texture.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- `stf.texture` STF Component on Blender Image
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/core/stf_texture/stf_texture.py)
*	- **Unity**
	- Texture2D
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Texture.cs)
*	- **Godot**
	- PortableCompressedTexture2D
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Texture.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
width | Yes | int | Width of the resulting GPU texture
height | Yes | int | Height of the resulting GPU texture
downscale_priority | Yes | int |In case of an enforced memory limit, how quickly should the resolution of the resulting GPU texture reduced.
quality | Yes | float | Indicate how much the GPU texture can be compressed. Value range is from 0 to 1. 1 means not compression should be used.
mipmaps | Yes | bool | Whether to generate mipmaps
:::

## Json Example
```json
"6db664cf-a4ba-4dd5-8845-477ca01f24d0": {
	"type": "stf.texture",
	"width": 2048,
	"height": 2048,
	"downscale_priority": 0,
	"quality": 0.8999999761581421,
	"mipmaps": true
}
```
