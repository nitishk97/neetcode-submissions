# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def height(node):
            if not node:
                return 0
            nonlocal res
            left = height(node.left)
            right = height(node.right)
            res = max(res, left+right)
            return 1+max(left,right)
        height(root)
        return res
        
        