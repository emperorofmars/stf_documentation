# Comparison to other Formats

## FBX
FBX is the industry standard. Unfortunately it is not extensible, undocumented, and its official implementation is proprietary.

Many open-source projects, like Blender and Godot, rely on unofficial reverse engineered implementations, with varying success and limited compatibility.

Artists must remember to use very specific export settings in Blender, in order for the model to not break in Unity. Animation support in Blender is limited and only supports the export of baked animations.

## glTF 2.0
GLTF is made to be delivered to the end-user and to be loaded as directly as possible into video-memory.\
STF is made to be delivered to a games-developer or artist and to be loaded into a modeling-tool/DCC or game-engines editor.

GLTF 2.0 forces optimization decisions at export from the DCCs.\
STF contains information on how to optimize the asset during the build in the game-engine. These can be different decisions, depending on the export target.

**Game-engines are responsible for runtime optimization (at asset-import and/or build time), not the 3d file format or 3d DCCs.**

Due to the nature of glTF 2.0, a lot of information is no longer present or explicitly expressed, such as the relationship between meshes and mesh-instances.\
Some implementations don't deal with that at all, and simply import mesh-resource per instance, leading to increased VRAM use and game-bundle sizes.

GLTF 2.0 has only limited support for animations, implementations are often forced to bake animations. This again, may be less of an issue in a runtime-loading context, but is detrimental if the file intended to be used for interchange, like between game-engines and DCCs.

## USD
The [official OpenUSD FAQ](https://openusd.org/release/usdfaq.html#isn-t-usd-just-another-file-format) does a better job at explaining this, than the author of this document ever could.

USD can instantiate assets from other regular 3D file-formats, similar to how game-engine scenes can instantiate assets from imported 3d models.

USD does not replace regular 3d file-formats and vice versa. STF is a "regular 3d file-formats" in this sense.
