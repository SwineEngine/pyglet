#!/usr/bin/env python

'''Base class for rendering tests.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id$'

import os
import unittest

from pyglet.gl import *
import pyglet.window
from pyglet.window.event import *
from pyglet.window.key import *
import pyglet.clock
from pyglet.image import load_image
from pyglet.sprite import *

ball_png = os.path.join(os.path.dirname(__file__), 'small_ball.png')

class RenderBase(unittest.TestCase):
    w = None
    def init_window(self, vx, vy):
        self.w = pyglet.window.Window(width=vx, height=vy)
        self.vx, self.vy = vx, vy

    def set_map(self, m, resize=False):
        if resize:
            vx, vy = m.pxw, m.pxh
            self.w.set_size(vx, vy)
        else:
            vx = self.w.width
            vy = self.w.height

        self.view = FlatView(0, 0, vx, vy, layers=[m])

        self.w.push_handlers(self.view.camera)

        self.keyboard = KeyboardStateHandler()
        self.w.push_handlers(self.keyboard)

    marker = None
    def show_focus(self):
        # add in a "sprite"
        self.marker = ImageSprite(load_image(ball_png))
        self.view.sprites.append(self.marker)

    def run_test(self):
        clock = pyglet.clock.Clock(fps_limit=30)
        while not self.w.has_exit:
            clock.tick()
            self.w.dispatch_events()
            self.view.fx += (self.keyboard[K_RIGHT] - self.keyboard[K_LEFT]) * 5
            self.view.fy += (self.keyboard[K_UP] - self.keyboard[K_DOWN]) * 5
            if self.marker is not None:
                self.marker.x = self.view.fx
                self.marker.y = self.view.fy
            self.view.clear()
            self.view.draw()
            self.w.flip()
        self.w.close()

