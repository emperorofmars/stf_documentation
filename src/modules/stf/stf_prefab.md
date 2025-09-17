# stf.prefab
A prefab represents a hierarchy of nodes.
It can never be instantiated recursively.

## Properties
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
|root_nodes |Yes |List<Resource-ID> |IDs of the root nodes within this prefab |
|animations |No |List<Resource-ID> |Animations which originate from this prefab's root |

The only allowed type for nodes in `root_nodes` is [`stf.node`](stf_node.md).

## Implementations
* Blender: [GitHub](https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_prefab/stf_prefab.py) | [Codeberg](https://codeberg.org/emperorofmars/stf_blender/src/commit/f45c3b56085fbd550901d6160a2d7cc96f69cda5/stfblender/stf_modules/core/stf_prefab/stf_prefab.py)
* Unity: [GitHub](https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Prefab.cs) | [Codeberg](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Prefab.cs)
* Godot: [GitHub](https://github.com/emperorofmars/stf_godot/blob/master/addons/stf_godot/modules/stf/STF_Prefab.gd) | [Codeberg](https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Prefab.gd)

## Json Example
```json
"f23cdae6-3b52-4212-b180-dfdb0fcfcaba": {
	"type": "stf.prefab",
	"name": "Warrior of the Squeak",
	"root_nodes": [
		"bf97e4a7-2aa8-4d90-9a4b-b7fa6223d8e7",
		"899799a1-17a6-439f-a6fb-1017d07f5a04"
	],
	"animations": [
		"b3879585-9587-4362-b6c5-58130e4c03ef",
		"d7d5365a-9d0a-4fab-bbe6-193fb1f23b9e",
		"3e8fb358-4501-41a6-a9f7-57ee47e1ffdb",
		"aeecdee5-eb5c-4923-8b28-f89e3f6769a4",
		"a63aa1f8-b819-4af3-99b4-c62aa5faae71",
		"4c2cc28b-937f-4e27-bc19-7f8dfe2c56d8",
		"4b63a246-e0eb-41c7-a999-ceb237f5f159",
		"798af1e9-7bee-4c46-99b8-4d1510ab46de",
		"c472603c-9bc7-4420-8766-7638df8621a3",
		"4b393856-2189-4e9d-a282-a8810342d8fe",
		"11826e52-f1f8-478d-b4dd-94e91d4a225f",
		"947d80c1-7f75-453f-a32d-00e6f0fb075c"
	],
	"components": [
		"19615892-fdcf-4f23-b47e-b59504b38561",
		"346ebced-a516-426c-879f-dd6a6607fc55",
		"8cd515fa-c589-49e1-a211-dbfd368d6a97"
	]
}
```
