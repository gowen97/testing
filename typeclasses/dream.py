from typeclasses.objects import Object

class Dream(Object):
    """
This creates a dream.
"""
    def at_object_creation(self):
        "This is called only once, when object is first created."
        #add a persistent attribute (description) to object
        self.db.desc = "This is the substance of the dream that you are spinning."
        
    pass
