import pyglet

window = pyglet.window.Window(400, 400)

active_events = {}

@window.event
def on_mouse_press(x, y, button, modifiers):
    print("Press", button)
    if button in active_events:
        print("press for button {} with active events {}".format(button, active_events[button]))

    active_events[button] = ["press"]

@window.event
def on_mouse_release(x, y, button, modifiers):
    print("Release", button)
    events = active_events.get(button, None)
    if not events:
        print("release for button {} without previous events".format(button))
    elif events[0] != "press":
        print("release for button {} but no press at start: {}".format(button, events))
    del active_events[button]

@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    events = active_events.get(button, None)
    if not events:
        active_events[button] = ["drag"]

    else:
        events.append("drag")

@window.event
def on_key_press(symbol, modifiers):
    print("on_key_press")

@window.event
def on_key_release(symbol, modifiers):
    print("on_key_release")


pyglet.app.run()
