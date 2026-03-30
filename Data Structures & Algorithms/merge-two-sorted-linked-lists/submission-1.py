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
        
        l1curr = list1
        l2curr = list2
        newhead = None
        curr = None

        while l1curr and l2curr:
            if l1curr.val <= l2curr.val:
                if newhead is None:
                    newhead = l1curr
                    curr = newhead
                else:
                    curr.next = l1curr
                    curr = curr.next

                l1curr = l1curr.next
            
            elif l2curr.val < l1curr.val:
                if newhead is None:
                    newhead = l2curr
                    curr = newhead
                else:
                    curr.next = l2curr
                    curr = curr.next
                l2curr = l2curr.next

        if l2curr is None and l1curr is not None :
            curr.next = l1curr
        
        if l1curr is None and l2curr is not None:
            curr.next = l2curr
        
        print(newhead)
        return newhead

