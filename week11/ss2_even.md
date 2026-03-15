# Problem Set Version 2
# Problem 2: Clearing the Path
# Time Complexity: O(N): n is the total number of nodes in the linked list
# Space Complexity: O(1): fixed number of pointers slow, fast
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def clear_trail(trailhead):
    visited = set()
    current = trailhead
    prev = None
    
    while current:
        if current in visited:
            prev.next = None
            break
        visited.add(current)
        prev = current
        current = current.next
    return trailhead

marker1 = Node("Trailhead")
marker2 = Node("Trail Fork")
marker3 = Node("The Falls")
marker4 = Node("Peak")
marker1.next = marker2
marker2.next = marker3
marker3.next = marker4
marker4.next = marker2

print_linked_list(clear_trail(marker1))





# Problem 4: Controlled Burns
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def selective_trail_clearing(trailhead, m, n):
    if not trailhead or m <= 0:
        return None
    
    if n <= 0:
        return trailhead

    curr = trailhead
    
    while curr:
        for _ in range(m - 1):
            if curr.next:
                curr = curr.next
            else:
                return trailhead 
        
        skip_ptr = curr.next
        for _ in range(n):
            if skip_ptr:
                skip_ptr = skip_ptr.next
            else:
                break
        
        curr.next = skip_ptr
        
        curr = skip_ptr

    return trailhead

trailhead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))

print_linked_list(selective_trail_clearing(trailhead, 2, 3))

trailhead = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12))))))))))))

print_linked_list(selective_trail_clearing(trailhead, 2, 3))



# Problem 6: Merging Trail Segments
# Time Complexity: O(N) : n is the total number of nodes in the input list
# Space Complexity: O(1) : this only use a few temporary variables tail, current, segment_sum that do not grow with the input size
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_trail(trailhead):
    if not trailhead:
        return None
    
    dummy = Node(0)
    tail = dummy
    
    current = trailhead.next
    segment_sum = 0
    
    while current:
        if current.value == 0:
            tail.next = Node(segment_sum)
            tail = tail.next
            
            segment_sum = 0
        else:
            segment_sum += current.value
            
        current = current.next
        
    return dummy.next
trail1 = Node(0, Node(3, Node(1, Node(0, Node(4, Node(5, Node(2, Node(0))))))))
trail2 = Node(0, Node(1, Node(0, Node(3, Node(0, Node(2, Node(2, Node(0))))))))

print_linked_list(merge_trail(trail1))
print_linked_list(merge_trail(trail2))
