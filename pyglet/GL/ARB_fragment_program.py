
"""ARB_fragment_program
http://oss.sgi.com/projects/ogl-sample/registry/ARB/fragment_program.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_FRAGMENT_PROGRAM_ARB = 0x8804
GL_PROGRAM_ALU_INSTRUCTIONS_ARB = 0x8805
GL_PROGRAM_TEX_INSTRUCTIONS_ARB = 0x8806
GL_PROGRAM_TEX_INDIRECTIONS_ARB = 0x8807
GL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = 0x8808
GL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = 0x8809
GL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = 0x880A
GL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB = 0x880B
GL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB = 0x880C
GL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB = 0x880D
GL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = 0x880E
GL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = 0x880F
GL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = 0x8810
GL_MAX_TEXTURE_COORDS_ARB = 0x8871
GL_MAX_TEXTURE_IMAGE_UNITS_ARB = 0x8872