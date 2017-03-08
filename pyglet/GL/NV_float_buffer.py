
"""NV_float_buffer
http://oss.sgi.com/projects/ogl-sample/registry/NV/float_buffer.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_FLOAT_R_NV = 0x8880
GL_FLOAT_RG_NV = 0x8881
GL_FLOAT_RGB_NV = 0x8882
GL_FLOAT_RGBA_NV = 0x8883
GL_FLOAT_R16_NV = 0x8884
GL_FLOAT_R32_NV = 0x8885
GL_FLOAT_RG16_NV = 0x8886
GL_FLOAT_RG32_NV = 0x8887
GL_FLOAT_RGB16_NV = 0x8888
GL_FLOAT_RGB32_NV = 0x8889
GL_FLOAT_RGBA16_NV = 0x888A
GL_FLOAT_RGBA32_NV = 0x888B
GL_TEXTURE_FLOAT_COMPONENTS_NV = 0x888C
GL_FLOAT_CLEAR_COLOR_VALUE_NV = 0x888D
GL_FLOAT_RGBA_MODE_NV = 0x888E