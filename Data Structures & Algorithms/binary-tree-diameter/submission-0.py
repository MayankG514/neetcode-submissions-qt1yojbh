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
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        d = ld + rd
        sub = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))

        return max(d,sub)