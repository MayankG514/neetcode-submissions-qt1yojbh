# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        return 1 + max(self.maxDepth(node.right), self.maxDepth(node.left))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root: 
            return 0
        
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        diameter = ld + rd

        sub = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))


        return max(diameter,sub)
        