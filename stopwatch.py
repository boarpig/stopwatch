#!/usr/bin/python2

import pyglet
from pyglet.window import key
from time import time, strftime, localtime

running = False
begin, now, total = 0, 0, 0
size = (320, 240)
format = "%.2f"

window = pyglet.window.Window(size[0], size[1], caption="Stopwatch", \
                              visible=False)
label = pyglet.text.Label('0.00', font_size=36,
                          x=window.width/2, y=window.height/2,
                          anchor_x='center', anchor_y='center')
window.set_visible()

@window.event
def on_key_release(symbol, modifiers):
    global now, begin, running, total
    if symbol == key.SPACE:
        if not running:
            running = True
            begin = time()
        else:
            running = False
            now = time()
            total += now - begin
    if symbol == key.BACKSPACE:
        total = 0
        begin = time()
        running = False

@window.event
def on_draw():
    window.clear()
    label.draw()

def update_time(dt):
    global now, begin, total
    if running:
        now = time()
        label.text = format % (now - begin + total) 
    else:
        label.text = format % (total)

pyglet.clock.schedule_interval(update_time, 0.01)
pyglet.app.run()
