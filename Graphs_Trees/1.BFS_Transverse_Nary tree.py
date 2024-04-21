"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        level = 0
        queue = deque([root])
        while queue:
            level = level + 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for child in curr.children:
                    queue.append(child)
        return level
