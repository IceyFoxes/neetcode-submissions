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
            # save the head
            saved = head
            map = {None : None}
            prev = Node(0)

            while head:
                # create a copy
                val = head.val
                copy = Node(val)

                # link the previous clone
                prev.next = copy
                prev = copy
            
                # add them to the dictionary
                map[head] = copy

                head = head.next
            
            # second pass to finish the randoms
            head = saved
            res = map[head]

            while head:
                copy_node = map[head]
                random_node = head.random
                copy_random_node = map[random_node]
                copy_node.random = copy_random_node

                head = head.next
            
            return res






