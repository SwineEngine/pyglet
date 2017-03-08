
"""EXT_scene_marker
http://oss.sgi.com/projects/ogl-sample/registry/EXT/scene_marker.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
glBeginSceneEXT = _get_function('glBeginSceneEXT', [], None)
glEndSceneEXT = _get_function('glEndSceneEXT', [], None)