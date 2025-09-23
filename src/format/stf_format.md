
<!-- Licensed under CC-BY-4.0 (<https://creativecommons.org/licenses/by/4.0/>) -->

# STF Format

## Introduction
STF is a binary file format, containing a binary header, a Json definition and a set of binary buffers.

The Json definition contains meta information, arbitrary resources and buffer references.
Resources have a `type` property, and are identified by a unique ID as a string.
Based on a resources type, a module gets selected which provides support to import & export it.

The minimum required set of supported modules is specified in [Core Modules](../modules/stf/index.md).

STF implementations must provide an easy to use plugin system for modules. If in any way possible, modules should be hot-loadable at runtime.

## Key Facts
* The file extension for stf binary files is `.stf`.
* The media-type for stf binary files is `model/stf+binary`.
* The STF binary header is stored in `little endian` byte order.
* The Json definition is encoded as `utf8`.
* STF uses the same coordinate system as glTF 2.0. (See [glTF-2.0. coordinate-system-and-units](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#coordinate-system-and-units))

## Binary Format
An STF binary file consists of a binary header, a [json-definition](#json-definition), and zero or more binary buffers.

:::{table} STF binary file layout
:align: left
:widths: auto
:name: STF binary file layout
| Length (Bytes) | Content |
| :--- | :--- |
| 4 | Magic number: `STF0` |
| 4 | STF binary format version major |
| 4 | STF binary format version minor |
| 4 | Number of buffers, including the Json definiton buffer |
| 8 * {number of buffers} | Buffer lengths in bytes |
| {length of all buffers} | Buffers |
:::

The Json definition is the first and only required buffer.

## Json Definition
The root Json element is an object. It contains 3 properties: [`stf`](#stf-object), [`resources`](#resources-object) and [`buffers`](#buffers-object).

### `stf` object
The `stf` object holds meta information.

**Properties:**

:::{table} `stf` object properties
:align: left
:widths: auto
:name: stf object properties
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
| version_major | Yes | Int | Major version of STF |
| version_minor | Yes | Int | Minor version of STF |
| root | Yes | resource-ID | ID of the root resource |
| meta | No | Map<String, String> | Meta information such as authors, license or documentation link. |
| generator | No | String | The name of the STF implementation that created this file. |
| timestamp | No | String | Timestamp as a String in the ISO format. |
| metric_multiplier | No | Float | Which number represents one meter. The default value is `1.0`. |
:::

The root resource must be a [`stf.prefab`](../modules/stf/stf_prefab.md). It represents the assets scene-hierarchy.

:::{admonition} `stf` object example
:class: example
```json
"stf": {
	"version_major": 0,
	"version_minor": 0,
	"meta": {
		"asset_name": "STF Example 1"
	},
	"metric_multiplier": 1.0,
	"root": "5f1ea7e8-ee26-46c9-91dc-cd002cb9b0a5"
}
```
:::

### `resources` object
The `resources` object is a map of resource objects identified by an ID.

The various resource objects describe the files actual content. Any further properties are defined by each resources module.

**Resource object base properties:**

:::{table} Resource object base properties
:align: left
:widths: auto
:name: resource object base properties
| Key | Required | Type | Description |
| :--- | :--- | :--- | :--- |
| type |Yes |String |Type of the resource. |
| referenced_resources |No |List<Resource-ID> |IDs of resources this resource references. |
| referenced_buffers |No |List<Buffer-ID> |IDs of buffers this resource references. |
| name |No |String |Display name of the resource. |
| version_major |No |Int |Major version of this resource. The default value is `0`. |
| version_minor |No |Int |Major version of this resource. The default value is `0`. |
| degraded |No |Boolean |Has this resource lost information at some point, but retained the same ID. The default is `False`. |
:::

Resources, other than from the [`stf.*` namespace](../modules/stf/index.md), must store all references to other resources and buffers in the `referenced_resources` and `referenced_buffers` fields respectively.\
If an STF implementation doesn't support a resource, it will preserve and re-export it along with all its relationships.

#### Resource Kinds
Resources can be `Data`, `Node`, `Instance` and `Component` kinds.
Each of these kinds has additional properties.

The information about what `kind` a resource is, must be known by the resource-type's implementation and is not contained in STF files itself.

##### Data
Suppport for module plugins of this kind is required.

**Data resource base properties:**

:::{table} Data resource base properties
:align: left
:widths: auto
:name: Data resource base properties
|Key |Required |Type |Description |
| :--- | :--- | :--- | :--- |
|fallback |No |Resource-ID |ID of a resource that should be used in case this one's type is not supported in this implementation |
|components |No |List<Resource-ID> |Component resource IDs |
:::

##### Node
For now only [`stf.node`](../modules/stf/stf_node.md) and [`stf.bone`](../modules/stf/stf_bone.md) exist.
Suppport for module plugins of this kind is not required.

**Node resource base properties:**

:::{table} Node resource base properties
:align: left
:widths: auto
:name: Node resource base properties
|Key |Required |Type |Description |
| :--- | :--- | :--- | :--- |
|enabled |No |boolean |True by default |
|children |No |List<Resource-ID> |IDs of child-nodes |
|components |No |List<Resource-ID> |Component resource IDs |
:::

##### Instance
They represent an instance of a `data` resource in the scene hierarchy.
These include for example mesh or armature instances.
Instances can provide data relevant for the instance of the resource, such as an armatures pose or meshes blendshape value or material assignments.
An instance resource can be referenced only once by a `Node` resource.
Suppport for module plugins of this kind is required.

**Instance resource properties:**

:::{table} Instance resource base properties
:align: left
:widths: auto
:name: Instance resource base properties
|Key |Required |Type |Description |
| :--- | :--- | :--- | :--- |
|enabled |No |boolean |True by default |
:::

##### Component
They Represents additional functionality or information for `Data` and `Node` resources.
A component resource can be referenced only once by a `Data` or `Node` resource.
Suppport for module plugins of this kind is required.

**Component resource properties:**

:::{table} Component resource base properties
:align: left
:widths: auto
:name: Component resource base properties
|Key |Required |Type |Description |
| :--- | :--- | :--- | :--- |
|enabled |No |boolean |True by default |
|overrides |No |List<Resource-ID> |References `Component` kind types that should not be processed, if this type is supported |
:::

:::{admonition} `resources` object example
:class: example
```json
"resources": {
	"b5f96f63-d5ce-4210-b4d6-8f43fbf557dd": {
		"type": "stf.material",
		"name": "Body Material",
		"properties": {
			"albedo.texture": {
				"type": "image",
				"values": [
					{
						"image": "f518a35d-d788-4692-a2dd-84d036d259e8"
					}
				]
			}
		}
	},
	"60b9192c-0c82-434b-b1cf-27d8add2c071": {
		"type": "stf.image",
		"name": "Awesome Texture.png",
		"format": "png",
		"buffer": "d07b09a0-3184-4a39-8650-d1fc90c64df2",
		"data_type": "color"
	},
	"3ca7f62c-b2a8-4315-bb1d-e4c6118ead70": {
		"type": "stf.texture",
		"resolution": [2048, 2048],
		"quality": 0.7,
		"texture_type": "color",
		"downscale_priority": 0
	}
}
```
:::

### `buffers` object
The `buffers` object is a map of buffer objects identified by an ID.
Each buffer object has a `type` property. Any further properties are defined in the buffer-type's definition.

For now, `stf.buffer.included` is the only supported buffer type. Support for hot-loading different buffer-types is not required.

#### `stf.buffer.included`
This type represents a buffer contained in the same file.

`stf.buffer.included` properties:

:::{table} `stf.buffer.included` properties
:align: left
:widths: auto
:name: stf.buffer.included properties
|Key |Required |Type |Description |
| :--- | :--- | :--- | :--- |
|index |Yes |Int |Index of the binary buffer in the file. An index of 0 means the first buffer after the Json definition buffer. |
:::

:::{admonition} `buffers` object example
:class: example
```json
"buffers": {
	"2c04d7f9-96cd-4867-baf3-2a54d4d31a67": {
		"type": "stf.buffer.included",
		"index": 666
	}
}
```
:::

### Minimal Definition Example
:::{admonition} Default Cube.stf
:class: example dropdown
```{literalinclude} assets/minimal.stf.json
:language: json
:tab-width: 3
```
:::
