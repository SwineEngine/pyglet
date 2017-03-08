
"""ATI_draw_buffers
http://oss.sgi.com/projects/ogl-sample/registry/ATI/draw_buffers.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_MAX_DRAW_BUFFERS_ATI = 0x8824
GL_DRAW_BUFFER0_ATI = 0x8825
GL_DRAW_BUFFER1_ATI = 0x8826
GL_DRAW_BUFFER2_ATI = 0x8827
GL_DRAW_BUFFER3_ATI = 0x8828
GL_DRAW_BUFFER4_ATI = 0x8829
GL_DRAW_BUFFER5_ATI = 0x882A
GL_DRAW_BUFFER6_ATI = 0x882B
GL_DRAW_BUFFER7_ATI = 0x882C
GL_DRAW_BUFFER8_ATI = 0x882D
GL_DRAW_BUFFER9_ATI = 0x882E
GL_DRAW_BUFFER10_ATI = 0x882F
GL_DRAW_BUFFER11_ATI = 0x8830
GL_DRAW_BUFFER12_ATI = 0x8831
GL_DRAW_BUFFER13_ATI = 0x8832
GL_DRAW_BUFFER14_ATI = 0x8833
GL_DRAW_BUFFER15_ATI = 0x8834
glDrawBuffersATI = _get_function('glDrawBuffersATI', [_ctypes.c_int, _ctypes.POINTER(_ctypes.c_uint)], None)