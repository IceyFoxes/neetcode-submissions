# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        start = slow.next
        slow.next = None

        prev = None
        while start:
            next_node = start.next
            start.next = prev
            prev = start
            start = next_node


        first, second = head, prev 

        while second:
            tmp1, tmp2 = first.next, second.next
            
            # 2. Re-wire the pointers (first points to second, second points to next part of first)
            first.next = second
            second.next = tmp1
            
            first, second = tmp1, tmp2






