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
        hm = {None: None}
        curr = head
        newHead = None

        while curr:
            copy = Node(curr.val)
            hm[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = hm[curr]
            copy.next = hm[curr.next]
            copy.random = hm[curr.random]
            curr = curr.next
        
        return hm[head]

            # if not newHead:
            #     newHead = Node(curr.val,curr.next,None)
            #     curr2 = newHead
            #     hm[curr2] = node.random
            # else:
            #     n = Node(curr.val,curr.next,None)
            #     curr2.next = n

            
            # curr = curr.next