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


# # Problem 1: Grafting Apples (Set Version 1)
# root = TreeNode("Trunk")

# root.left = TreeNode("Mcintosh")
# root.right = TreeNode("Granny Smith")

# root.left.left = TreeNode("Fuji")
# root.left.right = TreeNode("Opal")

# root.right.left = TreeNode("Crab")
# root.right.right = TreeNode("Gala")
# print_tree(root)













# # Problem 3: Ivy Cutting (Set Version 1)
# def right_vine(root):
#     if not root:
#         return []
    
#     path = []
#     current = root
    
#     while current:
#         path.append(current.val)
#         current = current.right
        
#     return path

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))















# # Problem 5: Count the Tree Leaves (Set Version 1)
# def count_leaves(root):
#     if root is None:
#         return 0
    
#     if root.left is None and root.right is None:
#         return 1
    
#     return count_leaves(root.left) + count_leaves(root.right)

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """

# oak1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))


# print(count_leaves(oak1))
# print(count_leaves(oak2))











# # Problem 7: Foraging Berries (Set Version 1)
# def harvest_berries(root, threshold):
#     if not root:
#         return 0
    
#     current_harvest = root.val if root.val > threshold else 0
    
#     return current_harvest + harvest_berries(root.left, threshold) + harvest_berries(root.right, threshold)

# """
#        4
#      /   \
#    10     6
#   /  \     \
#  5    8    20
# """
# bush = TreeNode(4, TreeNode(10, TreeNode(5), TreeNode(8)), TreeNode(6, None, TreeNode(20)))

# print(harvest_berries(bush, 6))
# print(harvest_berries(bush, 30))
