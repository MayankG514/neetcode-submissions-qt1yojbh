# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        if abs(lh-rh) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
