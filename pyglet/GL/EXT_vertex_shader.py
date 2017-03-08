
"""EXT_vertex_shader
http://oss.sgi.com/projects/ogl-sample/registry/EXT/vertex_shader.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GL_VERTEX_SHADER_EXT = 0x8780
GL_VERTEX_SHADER_BINDING_EXT = 0x8781
GL_OP_INDEX_EXT = 0x8782
GL_OP_NEGATE_EXT = 0x8783
GL_OP_DOT3_EXT = 0x8784
GL_OP_DOT4_EXT = 0x8785
GL_OP_MUL_EXT = 0x8786
GL_OP_ADD_EXT = 0x8787
GL_OP_MADD_EXT = 0x8788
GL_OP_FRAC_EXT = 0x8789
GL_OP_MAX_EXT = 0x878A
GL_OP_MIN_EXT = 0x878B
GL_OP_SET_GE_EXT = 0x878C
GL_OP_SET_LT_EXT = 0x878D
GL_OP_CLAMP_EXT = 0x878E
GL_OP_FLOOR_EXT = 0x878F
GL_OP_ROUND_EXT = 0x8790
GL_OP_EXP_BASE_2_EXT = 0x8791
GL_OP_LOG_BASE_2_EXT = 0x8792
GL_OP_POWER_EXT = 0x8793
GL_OP_RECIP_EXT = 0x8794
GL_OP_RECIP_SQRT_EXT = 0x8795
GL_OP_SUB_EXT = 0x8796
GL_OP_CROSS_PRODUCT_EXT = 0x8797
GL_OP_MULTIPLY_MATRIX_EXT = 0x8798
GL_OP_MOV_EXT = 0x8799
GL_OUTPUT_VERTEX_EXT = 0x879A
GL_OUTPUT_COLOR0_EXT = 0x879B
GL_OUTPUT_COLOR1_EXT = 0x879C
GL_OUTPUT_TEXTURE_COORD0_EXT = 0x879D
GL_OUTPUT_TEXTURE_COORD1_EXT = 0x879E
GL_OUTPUT_TEXTURE_COORD2_EXT = 0x879F
GL_OUTPUT_TEXTURE_COORD3_EXT = 0x87A0
GL_OUTPUT_TEXTURE_COORD4_EXT = 0x87A1
GL_OUTPUT_TEXTURE_COORD5_EXT = 0x87A2
GL_OUTPUT_TEXTURE_COORD6_EXT = 0x87A3
GL_OUTPUT_TEXTURE_COORD7_EXT = 0x87A4
GL_OUTPUT_TEXTURE_COORD8_EXT = 0x87A5
GL_OUTPUT_TEXTURE_COORD9_EXT = 0x87A6
GL_OUTPUT_TEXTURE_COORD10_EXT = 0x87A7
GL_OUTPUT_TEXTURE_COORD11_EXT = 0x87A8
GL_OUTPUT_TEXTURE_COORD12_EXT = 0x87A9
GL_OUTPUT_TEXTURE_COORD13_EXT = 0x87AA
GL_OUTPUT_TEXTURE_COORD14_EXT = 0x87AB
GL_OUTPUT_TEXTURE_COORD15_EXT = 0x87AC
GL_OUTPUT_TEXTURE_COORD16_EXT = 0x87AD
GL_OUTPUT_TEXTURE_COORD17_EXT = 0x87AE
GL_OUTPUT_TEXTURE_COORD18_EXT = 0x87AF
GL_OUTPUT_TEXTURE_COORD19_EXT = 0x87B0
GL_OUTPUT_TEXTURE_COORD20_EXT = 0x87B1
GL_OUTPUT_TEXTURE_COORD21_EXT = 0x87B2
GL_OUTPUT_TEXTURE_COORD22_EXT = 0x87B3
GL_OUTPUT_TEXTURE_COORD23_EXT = 0x87B4
GL_OUTPUT_TEXTURE_COORD24_EXT = 0x87B5
GL_OUTPUT_TEXTURE_COORD25_EXT = 0x87B6
GL_OUTPUT_TEXTURE_COORD26_EXT = 0x87B7
GL_OUTPUT_TEXTURE_COORD27_EXT = 0x87B8
GL_OUTPUT_TEXTURE_COORD28_EXT = 0x87B9
GL_OUTPUT_TEXTURE_COORD29_EXT = 0x87BA
GL_OUTPUT_TEXTURE_COORD30_EXT = 0x87BB
GL_OUTPUT_TEXTURE_COORD31_EXT = 0x87BC
GL_OUTPUT_FOG_EXT = 0x87BD
GL_SCALAR_EXT = 0x87BE
GL_VECTOR_EXT = 0x87BF
GL_MATRIX_EXT = 0x87C0
GL_VARIANT_EXT = 0x87C1
GL_INVARIANT_EXT = 0x87C2
GL_LOCAL_CONSTANT_EXT = 0x87C3
GL_LOCAL_EXT = 0x87C4
GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT = 0x87C5
GL_MAX_VERTEX_SHADER_VARIANTS_EXT = 0x87C6
GL_MAX_VERTEX_SHADER_INVARIANTS_EXT = 0x87C7
GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 0x87C8
GL_MAX_VERTEX_SHADER_LOCALS_EXT = 0x87C9
GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT = 0x87CA
GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT = 0x87CB
GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT = 0x87CC
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 0x87CD
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT = 0x87CE
GL_VERTEX_SHADER_INSTRUCTIONS_EXT = 0x87CF
GL_VERTEX_SHADER_VARIANTS_EXT = 0x87D0
GL_VERTEX_SHADER_INVARIANTS_EXT = 0x87D1
GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 0x87D2
GL_VERTEX_SHADER_LOCALS_EXT = 0x87D3
GL_VERTEX_SHADER_OPTIMIZED_EXT = 0x87D4
GL_X_EXT = 0x87D5
GL_Y_EXT = 0x87D6
GL_Z_EXT = 0x87D7
GL_W_EXT = 0x87D8
GL_NEGATIVE_X_EXT = 0x87D9
GL_NEGATIVE_Y_EXT = 0x87DA
GL_NEGATIVE_Z_EXT = 0x87DB
GL_NEGATIVE_W_EXT = 0x87DC
GL_ZERO_EXT = 0x87DD
GL_ONE_EXT = 0x87DE
GL_NEGATIVE_ONE_EXT = 0x87DF
GL_NORMALIZED_RANGE_EXT = 0x87E0
GL_FULL_RANGE_EXT = 0x87E1
GL_CURRENT_VERTEX_EXT = 0x87E2
GL_MVP_MATRIX_EXT = 0x87E3
GL_VARIANT_VALUE_EXT = 0x87E4
GL_VARIANT_DATATYPE_EXT = 0x87E5
GL_VARIANT_ARRAY_STRIDE_EXT = 0x87E6
GL_VARIANT_ARRAY_TYPE_EXT = 0x87E7
GL_VARIANT_ARRAY_EXT = 0x87E8
GL_VARIANT_ARRAY_POINTER_EXT = 0x87E9
GL_INVARIANT_VALUE_EXT = 0x87EA
GL_INVARIANT_DATATYPE_EXT = 0x87EB
GL_LOCAL_CONSTANT_VALUE_EXT = 0x87EC
GL_LOCAL_CONSTANT_DATATYPE_EXT = 0x87ED
glBeginVertexShaderEXT = _get_function('glBeginVertexShaderEXT', [], None)
glEndVertexShaderEXT = _get_function('glEndVertexShaderEXT', [], None)
glBindVertexShaderEXT = _get_function('glBindVertexShaderEXT', [_ctypes.c_uint], None)
glGenVertexShadersEXT = _get_function('glGenVertexShadersEXT', [_ctypes.c_uint], _ctypes.c_uint)
glDeleteVertexShaderEXT = _get_function('glDeleteVertexShaderEXT', [_ctypes.c_uint], None)
glShaderOp1EXT = _get_function('glShaderOp1EXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint], None)
glShaderOp2EXT = _get_function('glShaderOp2EXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint], None)
glShaderOp3EXT = _get_function('glShaderOp3EXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint], None)
glSwizzleEXT = _get_function('glSwizzleEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint], None)
glWriteMaskEXT = _get_function('glWriteMaskEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint], None)
glInsertComponentEXT = _get_function('glInsertComponentEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint], None)
glExtractComponentEXT = _get_function('glExtractComponentEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint], None)
glGenSymbolsEXT = _get_function('glGenSymbolsEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint], _ctypes.c_uint)
glSetInvariantEXT = _get_function('glSetInvariantEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_void_p], None)
glSetLocalConstantEXT = _get_function('glSetLocalConstantEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_void_p], None)
glVariantbvEXT = _get_function('glVariantbvEXT', [_ctypes.c_uint, _ctypes.POINTER(_ctypes.c_byte)], None)
glVariantsvEXT = _get_function('glVariantsvEXT', [_ctypes.c_uint, _ctypes.POINTER(_ctypes.c_short)], None)
glVariantivEXT = _get_function('glVariantivEXT', [_ctypes.c_uint, _ctypes.POINTER(_ctypes.c_int)], None)
glVariantfvEXT = _get_function('glVariantfvEXT', [_ctypes.c_uint, _ctypes.POINTER(_ctypes.c_float)], None)
glVariantdvEXT = _get_function('glVariantdvEXT', [_ctypes.c_uint, _ctypes.POINTER(_ctypes.c_double)], None)
glVariantubvEXT = _get_function('glVariantubvEXT', [_ctypes.c_uint, _ctypes.c_char_p], None)
glVariantusvEXT = _get_function('glVariantusvEXT', [_ctypes.c_uint, _ctypes.POINTER(_ctypes.c_ushort)], None)
glVariantuivEXT = _get_function('glVariantuivEXT', [_ctypes.c_uint, _ctypes.POINTER(_ctypes.c_uint)], None)
glVariantPointerEXT = _get_function('glVariantPointerEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint, _ctypes.c_void_p], None)
glEnableVariantClientStateEXT = _get_function('glEnableVariantClientStateEXT', [_ctypes.c_uint], None)
glDisableVariantClientStateEXT = _get_function('glDisableVariantClientStateEXT', [_ctypes.c_uint], None)
glBindLightParameterEXT = _get_function('glBindLightParameterEXT', [_ctypes.c_uint, _ctypes.c_uint], _ctypes.c_uint)
glBindMaterialParameterEXT = _get_function('glBindMaterialParameterEXT', [_ctypes.c_uint, _ctypes.c_uint], _ctypes.c_uint)
glBindTexGenParameterEXT = _get_function('glBindTexGenParameterEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_uint], _ctypes.c_uint)
glBindTextureUnitParameterEXT = _get_function('glBindTextureUnitParameterEXT', [_ctypes.c_uint, _ctypes.c_uint], _ctypes.c_uint)
glBindParameterEXT = _get_function('glBindParameterEXT', [_ctypes.c_uint], _ctypes.c_uint)
glIsVariantEnabledEXT = _get_function('glIsVariantEnabledEXT', [_ctypes.c_uint, _ctypes.c_uint], _ctypes.c_ubyte)
glGetVariantBooleanvEXT = _get_function('glGetVariantBooleanvEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_char_p], None)
glGetVariantIntegervEXT = _get_function('glGetVariantIntegervEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.POINTER(_ctypes.c_int)], None)
glGetVariantFloatvEXT = _get_function('glGetVariantFloatvEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.POINTER(_ctypes.c_float)], None)
glGetVariantPointervEXT = _get_function('glGetVariantPointervEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.POINTER(_ctypes.c_void_p)], None)
glGetInvariantBooleanvEXT = _get_function('glGetInvariantBooleanvEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_char_p], None)
glGetInvariantIntegervEXT = _get_function('glGetInvariantIntegervEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.POINTER(_ctypes.c_int)], None)
glGetInvariantFloatvEXT = _get_function('glGetInvariantFloatvEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.POINTER(_ctypes.c_float)], None)
glGetLocalConstantBooleanvEXT = _get_function('glGetLocalConstantBooleanvEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.c_char_p], None)
glGetLocalConstantIntegervEXT = _get_function('glGetLocalConstantIntegervEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.POINTER(_ctypes.c_int)], None)
glGetLocalConstantFloatvEXT = _get_function('glGetLocalConstantFloatvEXT', [_ctypes.c_uint, _ctypes.c_uint, _ctypes.POINTER(_ctypes.c_float)], None)