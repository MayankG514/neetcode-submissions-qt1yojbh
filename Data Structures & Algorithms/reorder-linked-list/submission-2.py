# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        newHead = None
        curr= head
        l = []

        while curr:
            l.append(curr)
            curr = curr.next

        if len(l) < 3:
            return None

        le, r = 0,len(l)-1
        curr = head

        while le<r:
            l[le].next = l[r]
            le+=1
            if le>=r:
                break
            l[r].next = l[le]
            r-=1
        l[le].next = None        
