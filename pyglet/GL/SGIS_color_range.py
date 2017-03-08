
"""SGIS_color_range
http://oss.sgi.com/projects/ogl-sample/registry/SGIS/color_range.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_EXTENDED_RANGE_SGIS = 0x85A5
GL_MIN_RED_SGIS = 0x85A6
GL_MAX_RED_SGIS = 0x85A7
GL_MIN_GREEN_SGIS = 0x85A8
GL_MAX_GREEN_SGIS = 0x85A9
GL_MIN_BLUE_SGIS = 0x85AA
GL_MAX_BLUE_SGIS = 0x85AB
GL_MIN_ALPHA_SGIS = 0x85AC
GL_MAX_ALPHA_SGIS = 0x85AD