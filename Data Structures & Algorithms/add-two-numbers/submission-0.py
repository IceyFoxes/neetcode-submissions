# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        number1 = []
        number2 = []
        while l1:
            number1.append(str(l1.val))
            l1 = l1.next
        while l2:
            number2.append(str(l2.val))
            l2 = l2.next
        
        number1.reverse()
        number2.reverse()
        n1 = int(''.join(number1))
        n2 = int(''.join(number2))
        
        n3 = str(n1 + n2)
        n3 = n3[::-1]

        dummy = ListNode(0)
        start = dummy
        for char in n3:
            dummy.next = ListNode(int(char))
            dummy = dummy.next
        
        return start.next
