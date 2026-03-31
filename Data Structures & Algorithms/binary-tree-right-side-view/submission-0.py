# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = collections.deque()
        q.append(root)
        ans = []

        while q:
            res = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if len(res)>0:
                ans.append(res[-1])
        return ans





                    
