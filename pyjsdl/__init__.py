#Pyjsdl - Python-to-JavaScript Multimedia Framework
#Copyright (c) 2011, 2013 James Garnon
#Licensed under the MIT License
#See LICENSE.txt for full license text

"""
**Pyjsdl - Pyjs Canvas Library**
"""

__version__ = '0.28'

from pyjsdl import env
from pyjsdl import util
from pyjsdl.display import Display
from pyjsdl.surface import Surface
from pyjsdl.rect import Rect
from pyjsdl.image import Image
from pyjsdl.event import Event
from pyjsdl.key import Key
from pyjsdl.mouse import Mouse
from pyjsdl.color import Color
from pyjsdl.mixer import Mixer
from pyjsdl.time import Time
from pyjsdl.vector import Vector2
from pyjsdl import draw
from pyjsdl import transform
from pyjsdl import surface
from pyjsdl import surfarray
from pyjsdl import mask
from pyjsdl import font
from pyjsdl import sprite
from pyjsdl import cursors
from pyjsdl import version
from pyjsdl.constants import *


__docformat__ = 'restructuredtext'


_initialized = False

def init():
    """
    Initialize module.
    """
    global time, display, image, event, key, mouse, mixer, _initialized
    if _initialized:
        return
    else:
        _initialized = True
    event = Event()
    env.set_env('event', event)
    time = Time()
    display = Display()
    image = Image()
    mixer = Mixer()
    mouse = Mouse()
    key = Key()

init()


def setup(callback, images=None):
    """
    Initialize module for script execution.

    Argument include callback function to run and optional images list to preload.
    Callback function can also be an object with a run method to call.
    The images can be image URL, or file-like object or base64 data in format (name.ext,data).
    """
    display.setup(callback, images)


def set_callback(callback):
    """
    Set callback function.

    Argument callback function to run.
    Callback function can also be an object with a run method to call.
    """
    display.set_callback(callback)


def setup_images(images):
    """
    Add images to image preload list.

    The argument is an image or list of images representing an image URL, or file-like object or base64 data in format (name.ext,data).
    Image preloading occurs at setup call.
    """
    display.set_images(images)


def quit():
    """
    Terminates canvas repaint and callback function.
    """
    canvas = display.get_canvas()
    canvas.stop()
    mixer.quit()
    time._stop_timers()


class error(RuntimeError):
    """
    Exception object.
    """
    pass


def bounding_rect_return(setting):
    """
    Bounding rect return.

    Set whether blit/draw return bounding Rect.
    Setting (bool) defaults to True on module initialization.
    """
    surface.bounding_rect_return(setting)
    draw.bounding_rect_return(setting)

