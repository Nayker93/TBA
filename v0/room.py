# Define the Room class.

class Room:
    """
    This class represents a room. A Room is composed of a name, a description and exits.

    Attributes:
        name (str): The name of the room.
        description (str): The description of the room.
        exits (dict): A dictionary mapping directions to rooms.

    Methods:
        __init__(self, name, description) : The constructor.
        get_exit(self, direction) : Return the room in the given direction.
        get_exit_string(self) : Return a string describing the room's exits.
        get_long_description(self) : Return a long description of this room including exits.

    Examples:

    >>> room = Room("Cave", "dans une sombre grotte humide.")
    >>> room.name
    'Cave'
    >>> room.description
    'dans une sombre grotte humide.'
    >>> room.exits
    {}
    >>> room.exits = {"N" : another_room}
    >>> room.get_exit("N") == another_room
    True
    >>> room.get_exit("S") is None
    True
    >>> room.get_exit_string()
    'Sorties: N'
    >>> room.get_long_description()
    '\nVous êtes dans une sombre grotte humide.\n\nSorties: N\n

    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"
