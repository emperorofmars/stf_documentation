# ava.expressions
Define the facial expressions and emotions an avatar can express.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF_Component on bpy.types.Collection
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/ava/ava_expressions.py)
*	- **Unity**
	- Only application specific representations
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/Runtime/Modules/AVA_Expressions.cs)\
		[VRChat Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_VRChat/Editor/Processors/VRC_AVA_Expressions_Processor.cs)\
		[UNIVRM0 Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/AVA/AVA_UNIVRM0/Editor/Processors/UNIVRM0_AVA_Expressions_Processor.cs)
*	- **Godot**
	- TBD
	-
:::

## Properties

:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
expressions | Yes | Dict<string, Expressions-Object> | Maps an emotion & face-expressions meaning to an animation
:::

### Expressions-Object Properties

:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
animation | No | Resource-ID |
fallback | No | Resource-ID |
:::

## Json Example
```json
"a85240dd-c9d3-42c0-87bc-f615c74c43e8": {
	"type": "ava.expressions",
	"name": "Expressions",
	"expressions": {
		"smile": {
			"animation": 0,
			"fallback": 1
		},
		"blep": {
			"animation": 2,
			"fallback": 3
		},
		"angry": {
			"animation": 4,
			"fallback": 5
		}
	},
	"referenced_resources": [
		"c82ebd9a-4efd-4688-9090-b54b345122b3",
		"e604492d-866e-4aba-9d57-459d0e0a75bd",
		"35304f52-bd12-41fe-b4a0-88d96071115f",
		"71059d15-8926-4927-b85d-5e81bf1ec05c",
		"8e657448-a4b0-4020-9254-437b0611a765",
		"e49fe8d5-7b16-40c8-a61c-235b8fd5c628"
	]
},
```
