# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue = deque([(1, root)])
        max_depth = 1
        while len(queue) > 0:
            depth, node = queue.popleft()
            if depth > max_depth:
                max_depth = depth
            if node.left is not None:
                queue.append((depth + 1, node.left))
            if node.right is not None:
                queue.append((depth + 1, node.right))
         
        return max_depth
        