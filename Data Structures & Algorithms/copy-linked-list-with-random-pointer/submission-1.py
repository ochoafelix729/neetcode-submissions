"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None

        head_copy = None
        ptr = head
        prev_node = None

        node_map = {}

        index = 0
        while ptr:
            node_copy = Node(ptr.val)
            if ptr == head:
                head_copy = node_copy
            else:
                prev_node.next = node_copy
            prev_node = node_copy
            node_map[ptr] = node_copy
            ptr = ptr.next
            index += 1
        
        ptr1 = head
        ptr2 = head_copy
        while ptr1:
            ptr2.random = node_map[ptr1.random] if ptr1.random else None
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return head_copy
            
            