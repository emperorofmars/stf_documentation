# STF - Squirrel Transfer Format

[A modular file-format for 3D assets]{.stf-subtitle}
*Intended for (not only) games-development use-cases.*

:::{warning}
Please note, STF is a work in progress and likely to change.
:::

<br>

**Install STF support for:**
::::{grid}

:::{grid-item-card} Blender
*Version 4.5+*
```{button-ref} installation/blender
:class: stf-button
:outline:
:expand:
Installation
```
```{button-ref} guide/blender
:class: stf-button
:outline:
:expand:
User Guide
```
:::

:::{grid-item-card} Unity
*Version 2022.3+*
```{button-ref} installation/unity
:class: stf-button
:outline:
:expand:
Installation
```
```{button-ref} guide/unity
:class: stf-button
:outline:
:expand:
User Guide
```
:::

:::{grid-item-card} Godot
*Version 4.6+*
```{button-ref} installation/godot
:class: stf-button
:outline:
:expand:
Installation
```
```{button-ref} guide/godot
:class: stf-button
:outline:
:expand:
User Guide
```
:::

::::

{octicon}`zap` _Try to import this [example model](https://squirrelbite.itch.io/stf-avatar-showcase)!_

[Relevant future implementation targets include: 3dsMax, Unreal Engine, Maya, Bevy, BabylonJs, ...]{.stf-info-box}

## Advantages
* **Made Games-Development**\
	STF files are meant to be imported into game-engine projects (Godot, Unity, Unreal, ...), and are also usable for further editing in 3d modeling tools (Blender, 3dsMax, ...).
	[STF stores original information as well as baked results.\
	I.e. STF contains the original topology of meshes, including n-gons, but also the triangulation.\
	Animations store original unbaked keyframes, as well as baked tracks.]{.stf-info-box}

* **Artist Friendly**\
	Import & export times are short and artists don't have to fiddle with unnecessary settings to avoid breakage.

* **Easy to Develop**\
	STF's modular nature leads to very loose coupling in the source-code and easy collaboration in the development of STF implementations.
	[A functioning implementation that handles some core resource-types can be usually developed in a day or two.\
	Third parties can easily develop and distribute custom resources.]{.stf-info-box}

## Concept
STF is a binary format, consisting of a binary header, a Json definition and arbitrary binary buffers.

By itself it is merely a shell format. Its implementations provide a framework to parse and serialize arbitrary **resources**, which are defined separately.

Resources are stored as Json-objects, and can represent anything, nodes in a scene hierarchy, meshes, textures, animations, ...\
Every resource object is referenced by a unique ID, and contains `type` property.
Depending on the `type`, a "handler" class / function will be selected to handle import / export.

A few resources, including but not limited to [`stf.prefab`](resources/stf/stf_prefab.md), [`stf.mesh`](resources/stf/stf_mesh.md), [`stf.material`](resources/stf/stf_material.md) or [`stf.image`](resources/stf/stf_image.md), are provided by default.

It should be possible to extend any STF implementation with custom resource-handlers, if at all possible.

:::{seealso}
**Read the [STF Format Reference](format/stf_format.md)**

Learn how STF compares to other 3d file-formats: [Comparisons](format/comparisons.md)
:::

:::{admonition} `resources` object example
:class: example
```json
// ...
"resources": {
	"0060c2b8-d856-4459-a88a-16e659792e6f": {
		"type": "stf.material",
		"name": "Body",
		"properties": {
			"albedo.texture": {
				"type": "image",
				"values": [
					{
						"image": 0
					}
				]
			}
		},
		"style_hints": [
			"realistic",
			"pbr"
		],
		"shader_targets": {
			"blender": [
				"ShaderNodeBsdfPrincipled"
			]
		},
		"referenced_resources": [
			"f518a35d-d788-4692-a2dd-84d036d259e8"
		]
	},
	{
		// ...
	}
},
// ...
```
:::

**Anatomy of an STF file**
![Description of the layout of an STF file. You can this information in the STF Format Reference!](img/stf_anatomy.png)


```{toctree}
:hidden:
Home <self>
```

```{toctree}
:hidden:
:caption: Guides
Installation <installation/index.md>
Usage <guide/index.md>
```

```{toctree}
:hidden:
:caption: Reference
format/stf_format.md
STF Resources <resources/index.md>
Comparisons <format/comparisons.md>
```
