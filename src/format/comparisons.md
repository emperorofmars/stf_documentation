# Comparison to other Formats

## FBX
FBX is the industry standard. Unfortunately it is not extensible, undocumented, and its official implementation is proprietary.

Many open-source projects, like Blender and Godot, rely on unofficial reverse engineered implementations, with varying success.

## glTF 2.0
Similar to glTF 2.0, an STF file consists of a Json definition and binary data.
Contrary to glTF, STF is made for interchange of 3d assets, not runtime loading or asset-streaming.

GLTF is made to be delivered to the end-user and loaded directly into video-memory.
STF is made to be delivered to a games-developer or artist.

Game-engines are responsible for runtime optimization (at asset-import and/or build time), not the 3d file format or 3d modeling tool.

## USD
The [official OpenUSD FAQ](https://openusd.org/release/usdfaq.html#isn-t-usd-just-another-file-format) does a better job at explaining this, than the author of this documentation ever could.

USD can instantiate assets from other regular 3D file-formats, similar to how game-engine scenes can instantiate assets from imported 3d models.

USD does not replace regular 3d file-formats and vice versa. STF is a "regular 3d file-formats" in this sense.
