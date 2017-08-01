#!/usr/bin/env python

'''
'''

__docformat__ = 'restructuredtext'
__version__ = ''

from pyglet.window.key import *

# From SDL: src/video/quartz/SDL_QuartzKeys.h
# These are the Macintosh key scancode constants -- from Inside Macintosh

QZ_ESCAPE = 0x35
QZ_F1 = 0x7A
QZ_F2 = 0x78
QZ_F3 = 0x63
QZ_F4 = 0x76
QZ_F5 = 0x60
QZ_F6 = 0x61
QZ_F7 = 0x62
QZ_F8 = 0x64
QZ_F9 = 0x65
QZ_F10 = 0x6D
QZ_F11 = 0x67
QZ_F12 = 0x6F
QZ_PRINT = 0x69
QZ_SCROLLOCK = 0x6B
QZ_PAUSE = 0x71
QZ_POWER = 0x7F
QZ_BACKQUOTE = 0x32
QZ_1 = 0x12
QZ_2 = 0x13
QZ_3 = 0x14
QZ_4 = 0x15
QZ_5 = 0x17
QZ_6 = 0x16
QZ_7 = 0x1A
QZ_8 = 0x1C
QZ_9 = 0x19
QZ_0 = 0x1D
QZ_MINUS = 0x1B
QZ_EQUALS = 0x18
QZ_BACKSPACE = 0x33
QZ_INSERT = 0x72
QZ_HOME = 0x73
QZ_PAGEUP = 0x74
QZ_NUMLOCK = 0x47
QZ_KP_EQUALS = 0x51
QZ_KP_DIVIDE = 0x4B
QZ_KP_MULTIPLY = 0x43
QZ_TAB = 0x30
QZ_q = 0x0C
QZ_w = 0x0D
QZ_e = 0x0E
QZ_r = 0x0F
QZ_t = 0x11
QZ_y = 0x10
QZ_u = 0x20
QZ_i = 0x22
QZ_o = 0x1F
QZ_p = 0x23
QZ_LEFTBRACKET = 0x21
QZ_RIGHTBRACKET = 0x1E
QZ_BACKSLASH = 0x2A
QZ_DELETE = 0x75
QZ_END = 0x77
QZ_PAGEDOWN = 0x79
QZ_KP7 = 0x59
QZ_KP8 = 0x5B
QZ_KP9 = 0x5C
QZ_KP_MINUS = 0x4E
QZ_CAPSLOCK = 0x39
QZ_a = 0x00
QZ_s = 0x01
QZ_d = 0x02
QZ_f = 0x03
QZ_g = 0x05
QZ_h = 0x04
QZ_j = 0x26
QZ_k = 0x28
QZ_l = 0x25
QZ_SEMICOLON = 0x29
QZ_QUOTE = 0x27
QZ_RETURN = 0x24
QZ_KP4 = 0x56
QZ_KP5 = 0x57
QZ_KP6 = 0x58
QZ_KP_PLUS = 0x45
QZ_LSHIFT = 0x38
QZ_z = 0x06
QZ_x = 0x07
QZ_c = 0x08
QZ_v = 0x09
QZ_b = 0x0B
QZ_n = 0x2D
QZ_m = 0x2E
QZ_COMMA = 0x2B
QZ_PERIOD = 0x2F
QZ_SLASH = 0x2C
QZ_RSHIFT = 0x3C
QZ_UP = 0x7E
QZ_KP1 = 0x53
QZ_KP2 = 0x54
QZ_KP3 = 0x55
QZ_KP_ENTER = 0x4C
QZ_LCTRL = 0x3B
QZ_LALT = 0x3A
QZ_LMETA = 0x37
QZ_SPACE = 0x31
QZ_RMETA = 0x36
QZ_RALT = 0x3D
QZ_RCTRL = 0x3E
QZ_LEFT = 0x7B
QZ_DOWN = 0x7D
QZ_RIGHT = 0x7C
QZ_KP0 = 0x52
QZ_KP_PERIOD = 0x41
QZ_IBOOK_ENTER = 0x34
QZ_IBOOK_LEFT = 0x3B
QZ_IBOOK_RIGHT = 0x3C
QZ_IBOOK_DOWN = 0x3D
QZ_IBOOK_UP = 0x3E

keymap = {
    QZ_ESCAPE: K_ESCAPE,
    QZ_F1: K_F1,
    QZ_F2: K_F2,
    QZ_F3: K_F3,
    QZ_F4: K_F4,
    QZ_F5: K_F5,
    QZ_F6: K_F6,
    QZ_F7: K_F7,
    QZ_F8: K_F8,
    QZ_F9: K_F9,
    QZ_F10: K_F10,
    QZ_F11: K_F11,
    QZ_F12: K_F12,
    QZ_PRINT: K_PRINT,
    QZ_SCROLLOCK: K_SCROLLLOCK,
    QZ_PAUSE: K_PAUSE,
    #QZ_POWER: K_POWER,
    QZ_BACKQUOTE: K_QUOTELEFT,
    QZ_1: K_1,
    QZ_2: K_2,
    QZ_3: K_3,
    QZ_4: K_4,
    QZ_5: K_5,
    QZ_6: K_6,
    QZ_7: K_7,
    QZ_8: K_8,
    QZ_9: K_9,
    QZ_0: K_0,
    QZ_MINUS: K_MINUS,
    QZ_EQUALS: K_EQUAL,
    QZ_BACKSPACE: K_BACKSPACE,
    QZ_INSERT: K_INSERT,
    QZ_HOME: K_HOME,
    QZ_PAGEUP: K_PAGEUP,
    QZ_NUMLOCK: K_NUMLOCK,
    QZ_KP_EQUALS: K_NUM_EQUAL,
    QZ_KP_DIVIDE: K_NUM_DIVIDE,
    QZ_KP_MULTIPLY: K_NUM_MULTIPLY,
    QZ_TAB: K_TAB,
    QZ_q: K_Q,
    QZ_w: K_W,
    QZ_e: K_E,
    QZ_r: K_R,
    QZ_t: K_T,
    QZ_y: K_Y,
    QZ_u: K_U,
    QZ_i: K_I,
    QZ_o: K_O,
    QZ_p: K_P,
    QZ_LEFTBRACKET: K_BRACKETLEFT,
    QZ_RIGHTBRACKET: K_BRACKETRIGHT,
    QZ_BACKSLASH: K_BACKSLASH,
    QZ_DELETE: K_DELETE,
    QZ_END: K_END,
    QZ_PAGEDOWN: K_PAGEDOWN,
    QZ_KP7: K_NUM_7,
    QZ_KP8: K_NUM_8,
    QZ_KP9: K_NUM_9,
    QZ_KP_MINUS: K_NUM_SUBTRACT,
    QZ_CAPSLOCK: K_CAPSLOCK,
    QZ_a: K_A,
    QZ_s: K_S,
    QZ_d: K_D,
    QZ_f: K_F,
    QZ_g: K_G,
    QZ_h: K_H,
    QZ_j: K_J,
    QZ_k: K_K,
    QZ_l: K_L,
    QZ_SEMICOLON: K_SEMICOLON,
    QZ_QUOTE: K_APOSTROPHE,
    QZ_RETURN: K_RETURN,
    QZ_KP4: K_NUM_4,
    QZ_KP5: K_NUM_5,
    QZ_KP6: K_NUM_6,
    QZ_KP_PLUS: K_NUM_ADD,
    QZ_LSHIFT: K_LSHIFT,
    QZ_z: K_Z,
    QZ_x: K_X,
    QZ_c: K_C,
    QZ_v: K_V,
    QZ_b: K_B,
    QZ_n: K_N,
    QZ_m: K_M,
    QZ_COMMA: K_COMMA,
    QZ_PERIOD: K_PERIOD,
    QZ_SLASH: K_SLASH,
    QZ_RSHIFT: K_RSHIFT,
    QZ_UP: K_UP,
    QZ_KP1: K_NUM_1,
    QZ_KP2: K_NUM_2,
    QZ_KP3: K_NUM_3,
    QZ_KP_ENTER: K_NUM_ENTER,
    QZ_LCTRL: K_LCTRL,
    QZ_LALT: K_LALT,
    QZ_LMETA: K_LMETA,
    QZ_SPACE: K_SPACE,
    QZ_RMETA: K_RMETA,
    QZ_RALT: K_RALT,
    QZ_RCTRL: K_RCTRL,
    QZ_LEFT: K_LEFT,
    QZ_DOWN: K_DOWN,
    QZ_RIGHT: K_RIGHT,
    QZ_KP0: K_NUM_0,
    QZ_KP_PERIOD: K_NUM_DECIMAL,
    QZ_IBOOK_ENTER: K_ENTER,
    QZ_IBOOK_LEFT: K_LEFT,
    QZ_IBOOK_RIGHT: K_RIGHT,
    QZ_IBOOK_DOWN: K_DOWN,
    QZ_IBOOK_UP: K_UP,
}

