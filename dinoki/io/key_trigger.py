"""
This class implements a key trigger.

It can be used to simulate key events useful for our interaction with the game.

Example:
    kt = KeyTrigger()
    ...
    if should_jump:
        kt.trigger_up()
"""


class KeyTrigger(object):

    def __init__(self):
        raise NotImplementedError

    def trigger_up(self):
        raise NotImplementedError
