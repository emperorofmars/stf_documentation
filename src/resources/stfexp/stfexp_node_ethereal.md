# stfexp.node.ethereal
The presence of this component marks a node to be removed once the file import process concludes (in 3d non-authoring tools such as game-engines).

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF Component on `bpy.types.Object`
	- [Resource](https://codeberg.org/stf_format/stf_blender/src/branch/master/stfblender/stf_resources/stfexp/stfexp_node_ethereal.py)
*	- **Unity**
	- STF Component on GameObject
	- [Resource](https://codeberg.org/stf_format/stf_unity/src/branch/master/Runtime/Resources/Resources_STF/STF_Texture.cs)
*	- **Godot**
	- Meta attribute on Node3D
	- [Resource](https://codeberg.org/stf_format/stf_godot/src/branch/master/addons/stf_godot/resources/stf/STF_Texture.gd)
:::

## Properties
This resource has no additional properties.

## Json Example
```json
"ad5930be-bcab-45f5-85ab-e415ea4e1f6f": {
	"type": "stfexp.node.ethereal"
},
```
