
"""SGIX_async_pixel
http://oss.sgi.com/projects/ogl-sample/registry/SGIX/async_pixel.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_ASYNC_TEX_IMAGE_SGIX = 0x835C
GL_ASYNC_DRAW_PIXELS_SGIX = 0x835D
GL_ASYNC_READ_PIXELS_SGIX = 0x835E
GL_MAX_ASYNC_TEX_IMAGE_SGIX = 0x835F
GL_MAX_ASYNC_DRAW_PIXELS_SGIX = 0x8360
GL_MAX_ASYNC_READ_PIXELS_SGIX = 0x8361