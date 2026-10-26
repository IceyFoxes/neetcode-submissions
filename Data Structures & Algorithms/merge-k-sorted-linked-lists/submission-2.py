# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                node1 = lists[i]
                if i + 1 >= len(lists):
                    merged_lists.append(node1)
                    continue
                node2 = lists[i + 1]
                
                # merge the 2 lists
                def merge(l1, l2):
                    dummy = ListNode()
                    tail = dummy
                    
                    while l1 and l2:
                        if l1.val < l2.val:
                            tail.next = l1
                            l1 = l1.next
                        else:
                            tail.next = l2
                            l2 = l2.next
                        tail = tail.next
                        
                    if l1:
                        tail.next = l1
                    if l2:
                        tail.next = l2
                        
                    return dummy.next

                merged_node = merge(node1, node2)
                merged_lists.append(merged_node)
            
            lists = merged_lists
        return lists[0]
        