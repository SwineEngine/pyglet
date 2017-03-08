
"""EXT_texture_cube_map
http://www.nvidia.com/dev_content/nvopenglspecs/GL_EXT_texture_cube_map.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_NORMAL_MAP_EXT = 0x8511
GL_REFLECTION_MAP_EXT = 0x8512
GL_TEXTURE_CUBE_MAP_EXT = 0x8513
GL_TEXTURE_BINDING_CUBE_MAP_EXT = 0x8514
GL_TEXTURE_CUBE_MAP_POSITIVE_X_EXT = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_EXT = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_EXT = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_EXT = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_EXT = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_EXT = 0x851A
GL_PROXY_TEXTURE_CUBE_MAP_EXT = 0x851B
GL_MAX_CUBE_MAP_TEXTURE_SIZE_EXT = 0x851C