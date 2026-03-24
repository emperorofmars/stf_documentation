# Comparison to other Formats

## FBX
FBX is the industry standard. Unfortunately it is not extensible, and its official implementation is proprietary.

Many open-source projects, including Blender and Godot, rely on unofficial reverse engineered implementations, with varying success and limited compatibility.

Artists must remember to use very specific export settings in Blender, in order for the model to not break in Unity. Animation support in Blender is limited and only supports the export of baked animations.

## glTF 2.0
STF is made for games-development, glTF is made for games distribution.\
These formats do not compete.

GLTF 2.0 is made to be loaded as directly as possible into video-memory on end-users devices.\
STF is made to be loaded into game-engine projects and 3d modeling-tools (DCCs) on games-developers or artists devices.

GLTF 2.0 forces optimization decisions at export time from DCCs. *E.g. a lot of information is no longer present or explicitly expressed, such as the relationship between meshes and mesh-instances.*\
STF contains information on how to optimize the asset during the build by the game-engines editor. These decisions can be different and mutually exclusive, depending on the export target and project settings.

**Game-engines are responsible for runtime optimization (at asset-import and/or build time), not 3d file formats or DCCs.**

## USD
The [official OpenUSD FAQ](https://openusd.org/release/usdfaq.html#isn-t-usd-just-another-file-format) does a better job at explaining this, than the author of this document ever could.

USD can instantiate assets from other regular 3D file-formats, similar to how game-engine scenes can instantiate assets from imported 3d models.

USD does not replace regular 3d file-formats and vice versa. STF is a "regular 3d file-format" in this sense.
