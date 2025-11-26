# stfexp.armature.humanoid
Declares that this Armature is humanoid. Defines which bone corresponds to which body part.

## Implementations
:::{list-table}
:align: left
:widths: auto
*	- **Blender**
	- STF Component on bpy.types.Armature
	- [Module](https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/expanded/stfexp_armature_humanoid.py)
*	- **Unity**
	- Avatar
	- [Module](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Expanded/STFEXP_Humanoid_Armature.cs)\
		[Default Processor](https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Processors/Processors_Expanded/STFEXP_Humanoid_Armature_Processor.cs)
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
locomotion_type | No | string | Locomotion Type
no_jaw | No | boolean | Ignore Jaw Mapping
settings | No | Settings-Object | Humanoid Settings
mappings | No | Map<string, Mappings-Object> | Bone to human bodypart mappings. The key of the map is the human bodypart name.
:::

### Settings-Object Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
arm_stretch | No | float |
upper_arm_twist | No | float |
lower_arm_twist | No | float |
leg_stretch | No | float |
upper_leg_twist | No | float |
lower_leg_twist | No | float |
feet_spacing | No | float |
use_translation | No | boolean |
:::

### Mappings-Object Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
target | Yes | Resource-ID | Id of the bone which corresponds to this bodypart.
rotation_limits | No | RotationLimits-Object |
:::

### RotationLimits-Object Properties
:::{table}
:align: left
:widths: auto
Key | Required | Type | Description
:--- | :--- | :--- | :---
primary | No | List<float> | 3 values define the minimum, center and maximum rotation values for the primary axis.
secondary | No | List<float> | 3 values define the minimum, center and maximum rotation values for the secondary axis.
twist | No | List<float> | 3 values define the minimum, center and maximum rotation values for the twist axis.
:::

## Json Example
```json
"38ddf9ce-688c-41c2-b917-4bde02709913": {
	"type": "stfexp.armature.humanoid",
	"locomotion_type": "digi",
	"no_jaw": true,
	"settings": {
		"arm_stretch": 0.05299999937415123,
		"upper_arm_twist": 0.5,
		"lower_arm_twist": 0.5,
		"leg_stretch": 0.05000000074505806,
		"upper_leg_twist": 0.5,
		"lower_leg_twist": 0.5,
		"feet_spacing": 0.0,
		"use_translation": false
	},
	"mappings": {
		"hip": {
			"target": "b6f82f9a-b78f-4778-a513-32f4e2342ed0"
		},
		"spine": {
			"target": "1e803b23-4d6e-4f3e-8194-976fe699a46c",
			"rotation_limits": {
				"primary": [
					-1.0471975803375244,
					0.0,
					1.0471975803375244
				],
				"secondary": [
					-1.0471975803375244,
					0.0,
					1.0471975803375244
				],
				"twist": [
					-1.5707963705062866,
					0.0,
					1.5707963705062866
				]
			}
		},
		"chest": {
			"target": "c0eac8b8-4644-40b0-a63a-e6366c70c0e4"
		},
		"neck": {
			"target": "a30cf351-28e4-4a24-a35c-c82b4c8cc6cb"
		},
		"head": {
			"target": "d95ac541-c0eb-4e6e-aa4e-69dbae7ca8f5"
		},
		"jaw": {
			"target": "29c1fb4e-37f7-46d5-b07e-526934455996"
		},
		"eye.l": {
			"target": "ca433094-3789-44c2-b7cb-890691a98b73"
		},
		"eye.r": {
			"target": "5525d8a9-00f4-4626-ba89-fef17623a94f"
		},
		"shoulder.l": {
			"target": "58f7acae-6bcc-40b7-8432-06e665f4a118"
		},
		"upper_arm.l": {
			"target": "3344754b-fafd-45de-82df-7b3f15fce86a"
		},
		"lower_arm.l": {
			"target": "53157ff3-10c4-415f-a2c9-617f0f89f29d"
		},
		"wrist.l": {
			"target": "360e5f0a-3f49-4e1f-9988-a66bd73bc959"
		},
		"thumb_1.l": {
			"target": "abd6565e-b64a-4f70-a1a5-af7223131db4"
		},
		"thumb_2.l": {
			"target": "455142f9-711c-442a-a316-f9572193e6df"
		},
		"thumb_3.l": {
			"target": "b8fc25f0-8ebc-4258-aa5f-a15932c32a26"
		},
		"index_1.l": {
			"target": "6cf96773-1a92-40f9-a718-03cff6b5a96e"
		},
		"index_2.l": {
			"target": "363c6c8b-a793-4a8e-866f-8c7a018994ae"
		},
		"index_3.l": {
			"target": "c3cd37d2-8cd6-4df7-933d-52b75e4f18fe"
		},
		"middle_1.l": {
			"target": "c55897a3-89b3-41ad-b72b-b2af215668c1"
		},
		"middle_2.l": {
			"target": "3206b12e-d5b5-4275-865a-3e2afc48265a"
		},
		"middle_3.l": {
			"target": "4b6e9f60-586f-4972-b99e-6b3a0c5336e7"
		},
		"ring_1.l": {
			"target": "2399cb0c-45fa-427f-b060-180ac74423c3"
		},
		"ring_2.l": {
			"target": "c18f5fc2-6552-4d88-9ba9-8722c4d8f608"
		},
		"ring_3.l": {
			"target": "b6f0ec91-8225-4443-ba9c-0cd14de13123"
		},
		"little_1.l": {
			"target": "70739cc3-c4da-44b0-a295-09c64c64e19d"
		},
		"little_2.l": {
			"target": "a70de5c4-8c99-4b4f-aa0d-bab3d69c2f6f"
		},
		"little_3.l": {
			"target": "1497929d-a7a9-43a4-bf4e-52f963e9d924"
		},
		"shoulder.r": {
			"target": "c794cb04-83a5-4373-93b6-430522ae20a9"
		},
		"upper_arm.r": {
			"target": "0e6dcfa9-dbae-4360-8543-6ad62a78b739"
		},
		"lower_arm.r": {
			"target": "e687a20e-f9f6-4d9a-9433-b91b1ae3896d"
		},
		"wrist.r": {
			"target": "d8cf4850-7a85-42b1-973d-40d4c5c97600"
		},
		"thumb_1.r": {
			"target": "7f1414e5-5a04-499d-95f3-f8617c67d970"
		},
		"thumb_2.r": {
			"target": "d17bbf33-6c66-4b1a-bc8a-2378e87413a3"
		},
		"thumb_3.r": {
			"target": "abfb5baa-b875-407b-b141-ba73a484d1cf"
		},
		"index_1.r": {
			"target": "761a0a82-1a31-42ca-972b-8236e54d32a0"
		},
		"index_2.r": {
			"target": "52ac8fd4-467a-473f-9d73-dbc51ad7f221"
		},
		"index_3.r": {
			"target": "6545e07a-05bc-4b8e-987a-f968b40987a1"
		},
		"middle_1.r": {
			"target": "14288b09-93fd-4736-b953-a3e68af940f2"
		},
		"middle_2.r": {
			"target": "eb6f5932-0949-4c2c-bd35-d560ebf53205"
		},
		"middle_3.r": {
			"target": "8217549e-ed05-4eda-882e-382614ea0bd6"
		},
		"ring_1.r": {
			"target": "ecf9d697-ab7c-4de1-9046-6d037a3b7db6"
		},
		"ring_2.r": {
			"target": "95280b00-e0db-4e02-bec8-1c0f98951045"
		},
		"ring_3.r": {
			"target": "c8fec4da-cba6-4156-9ec0-1900e5437da1"
		},
		"little_1.r": {
			"target": "eaabd609-2189-4634-a85c-3a94306e45ce"
		},
		"little_2.r": {
			"target": "82e3cdf3-1fb1-4853-90f4-98fa6220039c"
		},
		"little_3.r": {
			"target": "6e00fbe7-586a-4dbc-a74c-984d2899c6dd"
		},
		"upper_leg.l": {
			"target": "f78f75ce-9a8c-4618-ac9c-b9a169aca0b8"
		},
		"lower_leg.l": {
			"target": "f46c1337-a8ac-4193-b067-e2c585e168b0"
		},
		"foot.l": {
			"target": "4c43c30c-3894-4f7e-b39e-fc89f1a3a534"
		},
		"toes.l": {
			"target": "b3136261-3d96-4d73-8d3a-ed04d72e39a5"
		},
		"upper_leg.r": {
			"target": "8da3ea1c-bbd0-4187-b375-497c40d0dcf2"
		},
		"lower_leg.r": {
			"target": "5c77372f-350d-4187-91d0-3644f33cb1cd"
		},
		"foot.r": {
			"target": "0bc18f5b-0361-42e5-8a0d-70df81db1f55"
		},
		"toes.r": {
			"target": "99ba5702-5953-4138-aafa-b9591d964391"
		}
	}
},
```
