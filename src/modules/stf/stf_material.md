# stf.material
// Licensed under CC-BY-4.0 (<https://creativecommons.org/licenses/by/4.0/>)

= stf.material
:homepage: https://stfform.at
:keywords: stf, 3d, fileformat, format, interchange, interoperability
:hardbreaks-option:
:idprefix:
:idseparator: -
:library: Asciidoctor
ifdef::env-github[]
:tip-caption: :bulb:
:note-caption: :information_source:
endif::[]

== Properties
[%autowidth, %header,cols=4*]
|===
|Key |Required |Type |Description

|style_hints |No |List<String> |Hints on the visual style of the material
|shader_targets |No |Dict<List<String>> |Hints on the target stader per target application
|properties |Yes |Dict<String, Property-Object> |Dict of Property-ID as a string to an Object
|===

=== Property-Object properties
[%autowidth, %header,cols=4*]
|===
|Key |Required |Type |Description

|type |No |String |Type of the value variables
|values |No |List<Value-Variable> |List of values. The value object is determined by the `type`
|===

The following types for property-values are supported:

==== `float`
Json float value

==== `int`
Json int value

==== `color`
Json array of four floats, corresponding to the RGBA color channels.

==== `image`
An Image-Property-Value-Object:
[%autowidth, %header,cols=4*]
|===
|Key |Required |Type |Description

|image |Yes |Resource-ID |ID of an `stf.image` or compatible resource.
|===
TODO the image object should be expanded with UV-offsets and such


== Json Example
[,json]
----
"bdf11d99-70d2-42df-8a58-19f1e5238662": {
	"type": "stf.material",
	"name": "Body",
	"style_hints": [
		"realistic",
		"pbr"
	],
	"shader_targets": {
		"stfblender": [
			"ShaderNodeBsdfPrincipled"
		],
		"unity": [
			"PoiyomiToon"
		]
	},
	"properties": {
		"albedo.texture": {
			"type": "image",
			"values": [
				{
					"image": "1bf800ea-1bda-491c-ba89-c7bfa364e239"
				}
			]
		},
		"roughness.texture": {
			"type": "image",
			"values": [
				{
					"image": "155888f8-041c-4fe7-bf57-a558bd7b2137"
				}
			]
		},
		"metallic.texture": {
			"type": "image",
			"values": [
				{
					"image": "937ef22d-5175-4c4b-aa89-51da4c445dd4"
				}
			]
		},
		"normal.texture": {
			"type": "image",
			"values": [
				{
					"image": "e0c8e0ce-f667-49cc-b39a-5fb2dcde48ee"
				}
			]
		}
	}
}
----

== Implementations
* Blender: https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_material/stf_material.py[GitHub] | https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_material/stf_material.py[Codeberg]
* Unity: https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Material/STF_Material.cs[GitHub] | https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Material/STF_Material.cs[Codeberg]
* Godot: https://github.com/emperorofmars/stf_godot/blob/master/addons/stf_godot/modules/stf/STF_Material.gd[GitHub] | https://codeberg.org/emperorofmars/stf_godot/src/commit/d518b25aeb5b74cc57eb0f82f31a5f7fdbca2aa0/addons/stf_godot/modules/stf/STF_Material.gd[Codeberg]
