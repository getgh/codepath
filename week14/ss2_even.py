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



















# # Problem 2: Pumpkin Patch Path (Set Version 2)

# def max_pumpkins_path(root):
#     if not root:
#         return []
    
#     if not root.left and not root.right:
#         return [root.val]
    
#     left_path = max_pumpkins_path(root.left)
#     right_path = max_pumpkins_path(root.right)
    
#     if sum(left_path) >= sum(right_path):
#         return [root.val] + left_path
#     else:
#         return [root.val] + right_path
# pumpkin_quantities = [7, 3, 10, 1, None, 5, 15]
# root1 = build_tree(pumpkin_quantities)
# pumpkin_quantities = [12,3, 8, 4, 50, None, 10]
# root2 = build_tree(pumpkin_quantities)

# print(max_pumpkins_path(root1)) 
# print(max_pumpkins_path(root2))











# # Problem 4: Counting Room Clusters (Set Version 2)
# def count_clusters(hotel):
#     if not hotel:
#         return 0
    
#     def traverse(node, parent_val):
#         if not node:
#             return 0
        
#         current_cluster_count = 1 if node.val != parent_val else 0
        
#         left_clusters = traverse(node.left, node.val)
#         right_clusters = traverse(node.right, node.val)
        
#         return current_cluster_count + left_clusters + right_clusters

#     return traverse(hotel, None)


# themes = ["👻", "👻", "🧛🏾", "👻", "🧛🏾", None, "🧛🏾"]
# hotel = build_tree(themes)

# print(count_clusters(hotel))















# # Problem 6: Sectioning Off Cursed Zones (Set Version 2)
# def smallest_subtree_with_deepest_rooms(hotel):
#     def dfs(node):
#         if not node:
#             return 0, None
        
#         left_depth, left_node = dfs(node.left)
#         right_depth, right_node = dfs(node.right)
        
#         if left_depth > right_depth:
#             return left_depth + 1, left_node
        
#         if right_depth > left_depth:
#             return right_depth + 1, right_node
        
#         return left_depth + 1, node

#     depth, result_node = dfs(hotel)
#     return result_node

# rooms = ["Lobby", 101, 102, 201, 202, 203, 204, None, None, "😱", "👻"]
# hotel1 = build_tree(rooms)

# rooms = ["Lobby", 101, 102, None, "💀"]
# hotel2 = build_tree(rooms)

# print_tree(smallest_subtree_with_deepest_rooms(hotel1))
# print_tree(smallest_subtree_with_deepest_rooms(hotel2))
