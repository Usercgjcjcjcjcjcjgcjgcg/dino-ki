"""
This class implements a frame grabber.

When run, it yields a constant stream of stills from the screen.

Example:
    fg = FrameGrabber()
    for _ in range(10):
        f = fg.get_frame()
        do_something_with(f)
"""


class FrameGrabber(object):

    def __init__(self):
        raise NotImplementedError

    def get_frame(self):
        raise NotImplementedError
