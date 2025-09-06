# adventure_game.py

class Room:
    def __init__(self, name, explanation, objects=None):
        self.name = name
        self.explanation = explanation
        self.objects = objects if objects else []
        self.joint_rooms = {}

    def connect(self, direction, room):
        self.joint_rooms[direction] = room

    def get_description(self):
        return f"{self.name}\n\n{self.explanation}\n"

    def get_items(self):
        if self.objects:
            return "You see: " + ", ".join(self.objects) + "\n"
        else:
            return ""

    def get_available_directions(self):
        return "Available directions: " + ", ".join(self.joint_rooms.keys()) + "\n"

class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.stores = []

    def move(self, direction):
        if direction in self.current_room.joint_rooms:
            self.current_room = self.current_room.joint_rooms[direction]
            return f"You move to the {direction}.\n"
        else:
            return "You can't go there.\n"

    def take_item(self, item):
        if item in self.current_room.objects:
            self.current_room.objects.remove(item)
            self.stores.append(item)
            return f"You take the {item}.\n"
        else:
            return f"There is no {item} here.\n"

    def get_store(self):
        if self.stores:
            return "You have: " + ", ".join(self.stores) + "\n"
        else:
            return "You have nothing.\n"

def create_world():
    # Create rooms
    kitchen = Room("Kitchen", "Dirty room with flies.")
    dance_room = Room("Ballroom", "Room with wooden floor and grand entrance.")
    dining_hall = Room("Dining Hall", "A large room.")
    
    # Add objects to rooms
    kitchen.objects = ["knife", "apple"]
    dance_room.objects = ["candlestick"]
    dining_hall.objects = ["goblet", "map"]

    # Connect rooms
    kitchen.connect("south", dining_hall)
    dining_hall.connect("north", kitchen)
    dining_hall.connect("west", dance_room)
    dance_room.connect("east", dining_hall)

    return kitchen

def play_game():
    starting_room = create_world()
    player = Player(starting_room)

    print("Welcome to the Adventure Game!")
    print("Type 'help' for a list of commands.\n")

    while True:
        print(player.current_room.get_description())
        print(player.current_room.get_items())
        print(player.current_room.get_available_directions())

        command = input("> ").strip().lower().split()

        if not command:
            continue

        action = command[0]

        if action == "quit":
            print("Thanks for playing!")
            break
        elif action == "look":
            continue
        elif action == "move":
            if len(command) < 2:
                print("Move where?")
            else:
                direction = command[1]
                print(player.move(direction))
        elif action == "take":
            if len(command) < 2:
                print("Take what?")
            else:
                item = command[1]
                print(player.take_item(item))
        elif action == "stores":
            print(player.get_store())
        elif action == "help":
            print("Commands:")
            print("  look - Look anywhere in the room.")
            print("  move [direction] - Move in north, south, east, west")
            print("  take [item] - Take an item")
            print("  stores - Show your stores")
            print("  quit - Quit")
        else:
            print("Enter correct")

if __name__ == "__main__":
    play_game()
