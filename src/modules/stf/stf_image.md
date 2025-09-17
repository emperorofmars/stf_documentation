# stf.image
// Licensed under CC-BY-4.0 (<https://creativecommons.org/licenses/by/4.0/>)

= stf.image
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

|format |Yes |String |Format of the image. Officially supported formats are: `png`, `jpg`
|buffer |Yes |Buffer-ID |Buffer containing the image file
|data_type |No |String |Type of image data. As of not it can be `color` or `non_color`.
|===

== Json Example
[,json]
----
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
----

== Implementations
* Blender: https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_image/stf_image.py[GitHub] | https://codeberg.org/emperorofmars/stf_blender/src/commit/f45c3b56085fbd550901d6160a2d7cc96f69cda5/stfblender/stf_modules/core/stf_image/stf_image.py[Codeberg]
* Unity: https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Image.cs[GitHub] | https://codeberg.org/emperorofmars/stf_unity/src/commit/5320b3e0f2bd631ac0d901ebc2d5765b0eff2a8a/Runtime/Modules/Modules_Core/STF_Image.cs[Codeberg]
* Godot: https://github.com/emperorofmars/stf_godot/blob/master/addons/stf_godot/modules/stf/STF_Image.gd[GitHub] | https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Image.gd[Codeberg]
