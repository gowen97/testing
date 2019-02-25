"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from evennia.contrib.ingame_python.typeclasses import EventRoom
from commands.default_cmdsets import ChargenCmdset


class Room(EventRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    pass

class Library(Room):
    """
    This is where all the dream-objects get stored and accessed.
    """
    pass

class ChargenRoom(Room):
    """
    This room class is used by character-generation rooms.
    """
    def at_object_creation(self):
        "this is called only at first creation"
        self.cmdset.add(ChargenCmdset, permanent=True)
        
