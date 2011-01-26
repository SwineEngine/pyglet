# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

'''
'''
from __future__ import with_statement

__docformat__ = 'restructuredtext'
__version__ = '$Id: $'

from pyglet.app.base import PlatformEventLoop
from pyglet.libs.darwin import *

# Prepare the default application.
NSApplication.sharedApplication()

class CocoaEventLoop(PlatformEventLoop):

    def start(self):
        self._pool = NSAutoreleasePool.alloc().init()
        # finishLaunching should be called after there is an autorelease pool.
        NSApp().finishLaunching()

    def step(self, timeout=None):

        # Recycle the autorelease pool.
        del self._pool
        self._pool = NSAutoreleasePool.alloc().init()

        # Determine the timeout date.
        if timeout is None:
            # Using distantFuture as untilDate means that nextEventMatchingMask
            # will wait until the next event comes along.
            timeout_date = NSDate.distantFuture()
        else:
            timeout_date = NSDate.date().addTimeInterval_(timeout)

        # Retrieve the next event (if any).  We wait for an event to show up
        # and then process it, or if timeout_date expires we simply return.
        # We only process one event per call of step().
        self._is_running.set()
        event = NSApp().nextEventMatchingMask_untilDate_inMode_dequeue_(
                NSAnyEventMask, timeout_date, NSDefaultRunLoopMode, True)

        # Dispatch the event (if any).
        if event is not None:
            event_type = event.type()
            if event_type != NSApplicationDefined:
                # For key events, we send out special pyglet-specific actions
                # which replace the keyDown:, keyUp:, and flagsChanged: messages
                # because NSApplication translates multiple key presses into key 
                # equivalents before sending them on, which means that some keyUp:
                # messages are never sent for individual keys.   Our pyglet-specific
                # replacements ensure that we see all the raw key presses & releases.
                # We also filter out key-down repeats since pyglet only sends one
                # on_key_press event per key press.
                if event_type == NSKeyDown and not event.isARepeat():
                    NSApp().sendAction_to_from_("pygletKeyDown:", None, event)
                elif event_type == NSKeyUp:
                    NSApp().sendAction_to_from_("pygletKeyUp:", None, event)
                elif event_type == NSFlagsChanged:
                    NSApp().sendAction_to_from_("pygletFlagsChanged:", None, event)

                # Send the event on as usual.  The responder will still receive the normal
                # keyUp:, keyDown:, and flagsChanged: events, along with everything else.
                NSApp().sendEvent_(event)

            NSApp().updateWindows()
            did_time_out = False
        else:
            did_time_out = True

        self._is_running.clear()

        # pyglet.app.run() uses _run_estimated() by default, which checks
        # to see if we timed out or not.  If we tell it the truth about 
        # whether or not we timed out, then the framerate drops significantly,
        # and CPU usage decreases.  If you want to be honest, then uncomment
        # the following line:
#        return did_time_out
        # If you want better FPS, then lie:
        return False
    
    def stop(self):
        del self._pool

    def notify(self):
        enter_autorelease_pool()
        notifyEvent = NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                    NSApplicationDefined, # type
                    NSPoint(0.0, 0.0),    # location
                    0,                    # modifierFlags
                    0,                    # timestamp
                    0,                    # windowNumber
                    None,                 # graphicsContext
                    0,                    # subtype
                    0,                    # data1
                    0,                    # data2
                    )
        NSApp().postEvent_atStart_(notifyEvent, False)
        exit_autorelease_pool()