# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l= 0

        while curr:
            l+=1
            curr=curr.next
        
        removeIndex = l - n
        if removeIndex == 0:
            return head.next

        curr = head
        k = 0

        while k<(l-n):
            if (k+1) == removeIndex:
                curr.next = curr.next.next
                break
            k+=1
            curr = curr.next

        return head
        
        
        
