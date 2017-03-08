
"""ARB_texture_rectangle
http://oss.sgi.com/projects/ogl-sample/registry/ARB/texture_rectangle.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_TEXTURE_RECTANGLE_ARB = 0x84F5
GL_TEXTURE_BINDING_RECTANGLE_ARB = 0x84F6
GL_PROXY_TEXTURE_RECTANGLE_ARB = 0x84F7
GL_MAX_RECTANGLE_TEXTURE_SIZE_ARB = 0x84F8
GL_SAMPLER_2D_RECT_ARB = 0x8B63
GL_SAMPLER_2D_RECT_SHADOW_ARB = 0x8B64