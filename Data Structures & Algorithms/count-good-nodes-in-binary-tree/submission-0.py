# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 1
        queue = deque([(root,root.val)]) #(node, maxValue) -> maxValue seen until we reach that node
        while queue:
            node, maxValue = queue.popleft()
            if node.left:
                if node.left.val>=maxValue:
                    count+=1
                    queue.append((node.left, node.left.val))
                else:
                    queue.append((node.left, maxValue))
            if node.right:
                if node.right.val>=maxValue:
                    count+=1
                    queue.append((node.right, node.right.val))
                else:
                    queue.append((node.right, maxValue))
        return count



        