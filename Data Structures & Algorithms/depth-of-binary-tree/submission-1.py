# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        stack = [(1, root)]
        max_depth = 1
        while len(stack) > 0:
            depth, node = stack.pop()
            if depth > max_depth:
                max_depth = depth
            if node.left is not None:
                stack.append((depth + 1, node.left))
            if node.right is not None:
                stack.append((depth + 1, node.right))
         
        return max_depth
        