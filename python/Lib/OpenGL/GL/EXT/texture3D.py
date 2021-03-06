'''OpenGL extension EXT.texture3D

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.texture3D to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension defines 3-dimensional texture mapping.  In order to
	define a 3D texture image conveniently, this extension also defines the
	in-memory formats for 3D images, and adds pixel storage modes to support
	them.
	
	One important application of 3D textures is rendering volumes of image
	data.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture3D.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.texture3D import *
### END AUTOGENERATED SECTION