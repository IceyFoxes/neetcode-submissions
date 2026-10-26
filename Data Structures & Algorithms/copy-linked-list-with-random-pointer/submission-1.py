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
        if not head:
            return None
        # save the head
        saved = head

        while head:
            # create a copy
            val = head.val
            copy = Node(val)
        
            # link original to clone and clone to original
            next_node = head.next
            head.next = copy
            copy.next = next_node

            head = next_node
            
        # second pass to finish the randoms
        head = saved
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next

        # last pass to restore the original
        head = saved
        res = head.next
        while head:
            copy_node = head.next
            # Fix the original list's next pointer
            head.next = copy_node.next
            # Fix the cloned list's next pointer
            if copy_node.next:
                copy_node.next = copy_node.next.next
            
            # Move head forward
            head = head.next
            
        return res






