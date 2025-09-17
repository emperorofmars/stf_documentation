# stf.instance.mesh
// Licensed under CC-BY-4.0 (<https://creativecommons.org/licenses/by/4.0/>)

= stf.instance.mesh
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
|mesh |Yes |ID |Resource-ID of the instantiated mesh resource, usually xref:../data/stf_mesh.adoc[`stf.mesh`]
|armature_instance |No |Resource-ID |ID of a node with an instantiated armature. Usually the instance resource is xref:./stf_instance_armature.adoc[`stf.instance.armature`]
|blendshape_values |No |List<float> |
|materials |No |List<Resource-ID> |
|===

== Json Example
[,json]
----
----

== Implementations
* Blender: https://github.com/emperorofmars/stf_blender/blob/master/stfblender/stf_modules/core/stf_instance_mesh/stf_instance_mesh.py[GitHub] | https://codeberg.org/emperorofmars/stf_blender/src/branch/master/stfblender/stf_modules/core/stf_instance_mesh/stf_instance_mesh.py[Codeberg]
* Unity: https://github.com/emperorofmars/stf_unity/blob/master/Runtime/Modules/Modules_Core/STF_Instance_Mesh.cs[GitHub] | https://codeberg.org/emperorofmars/stf_unity/src/branch/master/Runtime/Modules/Modules_Core/STF_Instance_Mesh.cs[Codeberg]
* Godot: https://github.com/emperorofmars/stf_godot/blob/master/addons/stf_godot/modules/stf/STF_Instance_Mesh.gd[GitHub] | https://codeberg.org/emperorofmars/stf_godot/src/branch/master/addons/stf_godot/modules/stf/STF_Instance_Mesh.gd[Codeberg]
