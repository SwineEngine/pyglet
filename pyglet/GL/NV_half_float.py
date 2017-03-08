
"""NV_half_float
http://oss.sgi.com/projects/ogl-sample/registry/NV/half_float.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_HALF_FLOAT_NV = 0x140B
GLhalf = unsigned short
glColor3hNV = _get_function('glColor3hNV', [GLhalf, GLhalf, GLhalf], None)
glColor3hvNV = _get_function('glColor3hvNV', [_ctypes.POINTER(GLhalf)], None)
glColor4hNV = _get_function('glColor4hNV', [GLhalf, GLhalf, GLhalf, GLhalf], None)
glColor4hvNV = _get_function('glColor4hvNV', [_ctypes.POINTER(GLhalf)], None)
glFogCoordhNV = _get_function('glFogCoordhNV', [GLhalf], None)
glFogCoordhvNV = _get_function('glFogCoordhvNV', [_ctypes.POINTER(GLhalf)], None)
glMultiTexCoord1hNV = _get_function('glMultiTexCoord1hNV', [_ctypes.c_uint, GLhalf], None)
glMultiTexCoord1hvNV = _get_function('glMultiTexCoord1hvNV', [_ctypes.c_uint, _ctypes.POINTER(GLhalf)], None)
glMultiTexCoord2hNV = _get_function('glMultiTexCoord2hNV', [_ctypes.c_uint, GLhalf, GLhalf], None)
glMultiTexCoord2hvNV = _get_function('glMultiTexCoord2hvNV', [_ctypes.c_uint, _ctypes.POINTER(GLhalf)], None)
glMultiTexCoord3hNV = _get_function('glMultiTexCoord3hNV', [_ctypes.c_uint, GLhalf, GLhalf, GLhalf], None)
glMultiTexCoord3hvNV = _get_function('glMultiTexCoord3hvNV', [_ctypes.c_uint, _ctypes.POINTER(GLhalf)], None)
glMultiTexCoord4hNV = _get_function('glMultiTexCoord4hNV', [_ctypes.c_uint, GLhalf, GLhalf, GLhalf, GLhalf], None)
glMultiTexCoord4hvNV = _get_function('glMultiTexCoord4hvNV', [_ctypes.c_uint, _ctypes.POINTER(GLhalf)], None)
glNormal3hNV = _get_function('glNormal3hNV', [GLhalf, GLhalf, GLhalf], None)
glNormal3hvNV = _get_function('glNormal3hvNV', [_ctypes.POINTER(GLhalf)], None)
glSecondaryColor3hNV = _get_function('glSecondaryColor3hNV', [GLhalf, GLhalf, GLhalf], None)
glSecondaryColor3hvNV = _get_function('glSecondaryColor3hvNV', [_ctypes.POINTER(GLhalf)], None)
glTexCoord1hNV = _get_function('glTexCoord1hNV', [GLhalf], None)
glTexCoord1hvNV = _get_function('glTexCoord1hvNV', [_ctypes.POINTER(GLhalf)], None)
glTexCoord2hNV = _get_function('glTexCoord2hNV', [GLhalf, GLhalf], None)
glTexCoord2hvNV = _get_function('glTexCoord2hvNV', [_ctypes.POINTER(GLhalf)], None)
glTexCoord3hNV = _get_function('glTexCoord3hNV', [GLhalf, GLhalf, GLhalf], None)
glTexCoord3hvNV = _get_function('glTexCoord3hvNV', [_ctypes.POINTER(GLhalf)], None)
glTexCoord4hNV = _get_function('glTexCoord4hNV', [GLhalf, GLhalf, GLhalf, GLhalf], None)
glTexCoord4hvNV = _get_function('glTexCoord4hvNV', [_ctypes.POINTER(GLhalf)], None)
glVertex2hNV = _get_function('glVertex2hNV', [GLhalf, GLhalf], None)
glVertex2hvNV = _get_function('glVertex2hvNV', [_ctypes.POINTER(GLhalf)], None)
glVertex3hNV = _get_function('glVertex3hNV', [GLhalf, GLhalf, GLhalf], None)
glVertex3hvNV = _get_function('glVertex3hvNV', [_ctypes.POINTER(GLhalf)], None)
glVertex4hNV = _get_function('glVertex4hNV', [GLhalf, GLhalf, GLhalf, GLhalf], None)
glVertex4hvNV = _get_function('glVertex4hvNV', [_ctypes.POINTER(GLhalf)], None)
glVertexAttrib1hNV = _get_function('glVertexAttrib1hNV', [_ctypes.c_uint, GLhalf], None)
glVertexAttrib1hvNV = _get_function('glVertexAttrib1hvNV', [_ctypes.c_uint, _ctypes.POINTER(GLhalf)], None)
glVertexAttrib2hNV = _get_function('glVertexAttrib2hNV', [_ctypes.c_uint, GLhalf, GLhalf], None)
glVertexAttrib2hvNV = _get_function('glVertexAttrib2hvNV', [_ctypes.c_uint, _ctypes.POINTER(GLhalf)], None)
glVertexAttrib3hNV = _get_function('glVertexAttrib3hNV', [_ctypes.c_uint, GLhalf, GLhalf, GLhalf], None)
glVertexAttrib3hvNV = _get_function('glVertexAttrib3hvNV', [_ctypes.c_uint, _ctypes.POINTER(GLhalf)], None)
glVertexAttrib4hNV = _get_function('glVertexAttrib4hNV', [_ctypes.c_uint, GLhalf, GLhalf, GLhalf, GLhalf], None)
glVertexAttrib4hvNV = _get_function('glVertexAttrib4hvNV', [_ctypes.c_uint, _ctypes.POINTER(GLhalf)], None)
glVertexAttribs1hvNV = _get_function('glVertexAttribs1hvNV', [_ctypes.c_uint, _ctypes.c_int, _ctypes.POINTER(GLhalf)], None)
glVertexAttribs2hvNV = _get_function('glVertexAttribs2hvNV', [_ctypes.c_uint, _ctypes.c_int, _ctypes.POINTER(GLhalf)], None)
glVertexAttribs3hvNV = _get_function('glVertexAttribs3hvNV', [_ctypes.c_uint, _ctypes.c_int, _ctypes.POINTER(GLhalf)], None)
glVertexAttribs4hvNV = _get_function('glVertexAttribs4hvNV', [_ctypes.c_uint, _ctypes.c_int, _ctypes.POINTER(GLhalf)], None)
glVertexWeighthNV = _get_function('glVertexWeighthNV', [GLhalf], None)
glVertexWeighthvNV = _get_function('glVertexWeighthvNV', [_ctypes.POINTER(GLhalf)], None)