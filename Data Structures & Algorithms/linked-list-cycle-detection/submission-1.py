# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next or not head.next.next:
                return False
            
        rabbit = head.next.next
        turtle = head.next

        while rabbit != turtle:
            if not rabbit.next or not rabbit.next.next:
                return False
            rabbit = rabbit.next.next
            turtle = turtle.next

        return True