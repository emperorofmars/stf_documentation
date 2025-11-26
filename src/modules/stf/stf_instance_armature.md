# stf.instance.armature
Instantiates an armature onto a node.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- bpy.types.Object with bpy.types.Armature
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_instance_armature/stf_instance_armature.py)
*	- **Unity**
	- GameObject
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Instance_Armature.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_Core/STF_Instance_Armature_Processor.cs)
*	- **Godot**
	- Skeleton3D
	- [Module](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Instance_Armature.gd)
:::

## Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
armature | Yes | Resource-ID | ID of the instantiated armature resource, usually [`stf.armature`](stf_armature.md)
pose | No | Map<Resource-ID, TRS> | Map of the corresponding bone and TRS.
:::

## Json Example
```json
"73d67945-2937-41c8-b683-7a992cbca5c5": {
	"type": "stf.instance.armature",
	"name": "",
	"armature": "5251057d-a989-417b-a007-0bbc2fad19d3",
	"pose": {
		"ead3e787-8014-48ac-9af9-37db03edaed6": [
			[ 3.166873430160422e-10, 0.009894609451293945, -0.0011758268810808659 ],
			[ 0.5493189096450806, 9.955886071111308e-08, 6.540119557030266e-08, 0.8356127738952637 ],
			[ 1.0, 1.0, 1.000001072883606 ]
		],
		"793cd8e7-81aa-4034-939b-33fda8582fd8": [
			[ 2.4785646868252798e-09, 0.02414402738213539, -0.010395778343081474 ],
			[ 0.09529310464859009, -2.0173215489194263e-06, -1.7039580768596352e-07, 0.9954492449760437 ],
			[ 1.0, 0.9999999403953552, 0.9999999403953552 ]
		],
		"9a663148-f9a4-4b24-8f4c-7f4d388330dc": [
			[ -3.951510230137956e-09, 0.04944222792983055, 0.016573714092373848 ],
			[ 0.19152779877185822, -3.042036723854835e-06, -5.479599849422812e-07, 0.9814872145652771 ],
			[ 1.0, 0.9999999403953552, 0.9999998807907104 ]
		]
	}
}
```
