from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root


# # Problem 2: Searching Ariel's Treasures (Set Version 2)
# def locate_treasure(grotto, treasure):
#     current = grotto
    
#     while current:
#         if current.val == treasure:
#             return True
        
#         elif treasure < current.val:
#             current = current.left
            
#         else:
#             current = current.right
            
#     return False
# """
#              Snarfblat
#             /        \
#         Gadget       Whatzit
#        /     \           \
# Dinglehopper Gizmo       Whozit
# """


# # Using build_tree() function at the top of page
# values = ["Snarfblat", "Gadget", "Whatzit", "Dinglehopper", "Gizmo", None, "Whozit"]
# grotto = build_tree(values)

# print(locate_treasure(grotto, "Dinglehopper"))  
# print(locate_treasure(grotto, "Thingamabob")) 









# # Problem 4: Sorting Pearls by Size (Set Version 2)
# def smallest_to_largest_recursive(pearls):
#     sorted_list = []
    
#     def inorder_traversal(node):
#         if node:
#             inorder_traversal(node.left)   
#             sorted_list.append(node.val) 
#             inorder_traversal(node.right)  
    
#     inorder_traversal(pearls)
#     return sorted_list

# def smallest_to_largest_iterative(pearls):
#     sorted_list = []
#     stack = []
#     current = pearls
    
#     while current is not None or stack:
#         while current is not None:
#             stack.append(current)
#             current = current.left
        
#         current = stack.pop()
#         sorted_list.append(current.val)
        
#         current = current.right
        
#     return sorted_list
# """
#         3
#        / \
#       /   \ 
#      1     5
#       \   / \
#        2 4   8
# """

# # Use build_tree() function at top of page
# values = [3, 1, 5, None, 2, 4, 8]
# pearls = build_tree(values)

# print(smallest_to_largest_recursive(pearls))
# print(smallest_to_largest_iterative(pearls))








# # Problem 6: Remove Invasive Species (Set Version 2)
# def remove_species(root, name):
#     if not root:
#         return None

#     if name < root.val:
#         root.left = remove_species(root.left, name)
#     elif name > root.val:
#         root.right = remove_species(root.right, name)
#     else:
        
#         if not root.left:
#             return root.right
#         elif not root.right:
#             return root.left

#         successor = find_min(root.right)
#         root.val = successor.val
#         root.right = remove_species(root.right, successor.val)

#     return root

# def find_min(node):
#     current = node
#     while current.left:
#         current = current.left
#     return current

# """
#                 Dugong
#              /         \
#        Brain Coral   Lionfish
#               \       /       \
#          Clownfish Giant Clam  Seagrass
# """
# # Use build_tree() function at top of page
# values = ["Dugong", "Brain Coral", "Lionfish", None, "Clownfish", "Giant Clam", "Seagrass"]
# ecosystem = build_tree(values)

# # Using print_tree() function at top of page
# print_tree(remove_species(ecosystem, "Lionfish"))







