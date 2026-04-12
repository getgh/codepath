# Problem 1: Merging Cookie Orders (Set Version 1)
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


# # Problem 1: Merging Cookie Orders (Set Version 1)
# def merge_orders(order1, order2):
#     if not order1:
#         return order2
#     if not order2:
#         return order1
#     v = order2.val + order1.val
#     st = TreeNode(v)

#     st.left = merge_orders(order1.left, order2.left)
#     st.right = merge_orders(order1.right, order2.right)
    
#     return st

# cookies1 = [1, 3, 2, 5]
# cookies2 = [2, 1, 3, None, 4, None, 7]
# order1 = build_tree(cookies1)
# order2 = build_tree(cookies2)

# print_tree(merge_orders(order1, order2))










# # Problem 3: Maximum Tiers in Cake (Set Version 1)
# def max_tiers(cake):
#     if not cake:
#         return 0
    
#     left_height = max_tiers(cake.left)
#     right_height = max_tiers(cake.right)
    
#     return max(left_height, right_height) + 1

# cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
# cake = build_tree(cake_sections)

# print(max_tiers(cake))










# Problem 5: Can Fulfill Order (Set Version 1)
def can_fulfill_order(inventory, order_size):
    if not inventory:
        return False
    
    if not inventory.left and not inventory.right:
        return inventory.val == order_size
    
    new_order_size = order_size - inventory.val
    
    return (can_fulfill_order(inventory.left, new_order_size) or 
            can_fulfill_order(inventory.right, new_order_size))

quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)

print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))
