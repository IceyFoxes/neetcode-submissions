# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        m1 = 0
        m2 = 0
        sum1 = 0
        sum2 = 0

        while l1:
            sum1 += l1.val * (10 ** m1)
            m1 += 1
            l1 = l1.next
        while l2:
            sum2 += l2.val * (10 ** m2)
            m2 += 1
            l2 = l2.next
        
        n3 = sum1 + sum2
        if n3 == 0:
            return ListNode(0)

        dummy = ListNode(0)
        start = dummy
        while n3 > 0:
            quotient = n3 // 10
            remainder = n3 - quotient * 10
            n3 = quotient

            dummy.next = ListNode(remainder)
            dummy = dummy.next
        
        return start.next
