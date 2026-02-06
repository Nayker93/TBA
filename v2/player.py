# Define the Player class.
class Player():
    """
    This class represents a player. A Player is composed of a name, a current room,
    and a history of visited rooms.

    Attributes:
        name (str): The name of the player.
        current_room (Room): The current room of the player.
        history (list[Room]): The history of previous rooms.

    Methods:
        __init__(self, name) : The constructor.
        move(self, direction) : Move the player to the room in the given direction.
                                Return True if the player moved, False otherwise.     

    Examples:

    >>> player = Player("Indiana")
    >>> player.name
    'Indiana'
    >>> player.current_room = Cave
    >>> player.current_room.name
    'Cave'
    >>> player.move("N")
    'Aucune porte dans cette direction !\n'
    False
    >>> player.move("N")
    '\nVous êtes dans une sombre grotte humide.\n\nSorties: N\n
    True

    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits.get(direction)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Add the current room to history, then move to the next room.
        self.history.append(self.current_room)
        self.current_room = next_room
        
        print(self.current_room.get_long_description())
        return True
    
    def get_history(self):
        if not self.history:
            return ""

        room_history = ["\nVous avez déja visité les pièces suivantes:"]
        for room in self.history:
            room_history.append(f"    - {room.description}")
        return "\n".join(room_history)

    def back(self):
        if not self.history:
            print("\nAucun retour en arrière possible.\n")
            return False

        self.current_room = self.history.pop()
        print(self.current_room.get_long_description())
        return True
    