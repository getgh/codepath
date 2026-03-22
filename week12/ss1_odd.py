# # Problem 1: Counting Iron Man's Suits (Set Version 1)
# def count_suits_iterative(suits):
#     count = 0
#     for suit in suits:
#         count += 1
#     return count


# def count_suits_recursive(suits):
#     if not suits:
#         return 0
#     return 1 + count_suits_recursive(suits[1:])

# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))
# # Similarity: Both have a linear time complexity of O(n).
# # Differences-> 
#     # Iterative Solution: Efficient O(1) extra space, only stores one integer.
#     # Recursive Solution: Less efficient O(n) space because each recursive call adds a new layer to the stack.














# # Problem 3: Counting Iron Man's Unique Suits (Set Version 1)

# def count_suits_iterative(suits):
#     unique_suits = set()
#     for suit in suits:
#         unique_suits.add(suit)
#     return len(unique_suits)

# def count_suits_recursive(suits, unique_suits=None):
#     if unique_suits is None:
#         unique_suits = set()
    
#     if not suits:
#         return len(unique_suits)
    
#     unique_suits.add(suits[0])
    
#     return count_suits_recursive(suits[1:], unique_suits)
# print(count_suits_iterative(["Mark I", "Mark I", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))
# # Similarities: Both solutions utilize a set to handle the uniqueness logic. They both visit every element in the input list once to ensure no suit is missed.
# # Differences: The recursive version is more memory-intensive because it creates a new slice of the list (suits[1:]) and a new stack frame for every element in the list.














# # Problem 5: Calculating the Power of the Fantastic Four (Set Version 1)
# def power_of_four(n):
#     if n == 0:
#         return 1
#     if n > 0:
#         return 4 * power_of_four(n - 1)
#     if n < 0:
#         return 1 / power_of_four(-n)

# print(power_of_four(2))
# print(power_of_four(-2))















# # Problem 7: Counting Vibranium Deposits (Set Version 1)
# def count_deposits(resources):
#     if not resources:
#         return 0
    
#     count = 1 if resources[0] == "V" else 0
    
#     return count + count_deposits(resources[1:])

# print(count_deposits("VVVVV"))
# print(count_deposits("VXVYGA"))





# Problem 9: Merging Missions II (Set Version 1)
# The Case for Iterative: In production environment (with in Python), the iterative solution is best. Python has a default recursion limit of 1,000. For merge two lists that each had 1,000 nodes, the recursive version will crash, whereas the iterative version would handle millions of nodes without issue. For this reason I would prefer based on the input and computation size.
