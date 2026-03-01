# Problem Set Version 2
# Problem 2: Update Linked List Sequence
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

shy_guy = Node("Shy Guy")
diddy_kong = Node("Diddy Kong")
dry_bones = Node("Dry Bones")
shy_guy.next = diddy_kong
diddy_kong.next = dry_bones

link = Node("Link")
link.next = diddy_kong
shy_guy.next = link

toad = Node("Toad")
toad.next = dry_bones
diddy_kong.next = toad


print("Current List:")
print_linked_list(shy_guy)











# Problem 4: Increment Linked List Node Values
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def increment_ll(head):
    current = head
    while current:
        current.value += 1
        current = current.next
    return head




node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(increment_ll(node_one))












# Problem 6: Making the Cut
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def top_n_finishers(head, n):
    finishers = []
    current = head
    count = 0
    
    while current and count < n:
        finishers.append(current.value)
        current = current.next
        count += 1
        
    return finishers





head = Node("Daisy", Node("Mario", Node("Toad", Node("Yoshi"))))

# Linked List: Daisy -> Mario -> Toad -> Yoshi
print(top_n_finishers(head, 3))

# Linked List: Daisy -> Mario -> Toad -> Yoshi
print(top_n_finishers(head, 5))











# Problem 8: Array to Linked List
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value.character, end=" -> " if current.next else "\n")
        current = current.next
def arr_to_ll(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
        
    return head


mario = Player("Mario", "Mushmellow")
luigi = Player("Luigi", "Standard LG")
peach = Player("Peach", "Bumble V")

print_linked_list(arr_to_ll([mario, luigi, peach]))
print_linked_list(arr_to_ll([peach]))









# Problem 10: Find Length of Doubly Linked List from Any Node
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def get_length(node):
    if not node:
        return 0
    
    length = 0
    
    current = node
    while current:
        length += 1
        current = current.prev
        
    current = node.next
    while current:
        length += 1
        current = current.next
        
    return length


yoshi_falls = Node("Yoshi Falls")
moo_moo_farm = Node("Moo Moo Farm")
rainbow_road = Node("Rainbow Road")
dk_mountain = Node("DK Mountain")
yoshi_falls.next = moo_moo_farm
moo_moo_farm.next = rainbow_road
rainbow_road.next = dk_mountain
dk_mountain.prev = rainbow_road
rainbow_road.prev = moo_moo_farm
moo_moo_farm.prev = yoshi_falls

# List: Yoshi Falls <-> Moo Moo Farm <-> Rainbow Road <-> DK Mountain
print(get_length(rainbow_road))












