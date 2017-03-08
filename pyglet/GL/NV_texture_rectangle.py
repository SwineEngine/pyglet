
"""NV_texture_rectangle
http://oss.sgi.com/projects/ogl-sample/registry/NV/texture_rectangle.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_TEXTURE_RECTANGLE_NV = 0x84F5
GL_TEXTURE_BINDING_RECTANGLE_NV = 0x84F6
GL_PROXY_TEXTURE_RECTANGLE_NV = 0x84F7
GL_MAX_RECTANGLE_TEXTURE_SIZE_NV = 0x84F8