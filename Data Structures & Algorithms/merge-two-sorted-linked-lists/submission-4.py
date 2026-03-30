# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        
        l1 = list1
        l2 = list2
        newhead  = None
        curr = None

        while l1 and l2:
            if l1.val > l2.val:
                if not newhead:
                    newhead = l2
                    curr = newhead
                else:
                    curr.next = l2
                    curr = curr.next
                l2 = l2.next

            elif l2.val >= l1.val:
                if not newhead:
                    newhead = l1
                    curr = newhead
                else:
                    curr.next = l1
                    curr = curr.next
                l1 = l1.next
        
        if l2 and not l1:
            curr.next = l2
        
        if l1 and not l2:
            curr.next = l1
        
        return newhead

            
                
