# Problem Set Version 1
# Problem 1: New Horizons
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

apollo = Villager("Apollo", "Eagle", "pah")

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 







# Problem 3: Update Catchphrase
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

bones = Villager("Bones", "Dog", "yip yip")
bones.catchphrase = "ruff it up"

print(bones.greet_player("Samia"))










# Problem 5: Add Furniture
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def add_item(self, item_name):
        valid_items = {
            "acoustic guitar", 
            "ironwood kitchenette", 
            "rattan armchair", 
            "kotatsu", 
            "cacao tree"
        }
        
        if item_name in valid_items:
            self.furniture.append(item_name)

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)











# Problem 7: Group by Personality
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []

def of_personality_type(townies, personality_type):
    names = []
    for villager in townies:
        if villager.personality == personality_type:
            names.append(villager.name)
    return names

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))











# Problem 9: Nook's Cranny
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

tommy = Node("Tommy")
tom_nook = Node("Tom Nook", tommy)


tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy

print(tom_nook.value) 
print(tom_nook.next.value) 
print(tommy.value) 
print(tommy.next) 














# Problem 11: Saharah
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

tommy = Node("Tommy")
timmy = Node("Timmy", tommy)
tom_nook = Node("Tom Nook", timmy)

tom_nook.next = None
saharah = Node("Saharah")
tommy.next = saharah

print(tom_nook.next) 
print(timmy.value) 
print(timmy.next.value)  
print(tommy.value) 
print(tommy.next.value)
print(saharah.value)  
print(saharah.next) 
