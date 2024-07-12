#![image](https://github.com/abhyudaya12/Data_Structures_Algorithms/assets/28287783/949197ba-d31b-4d75-a29a-c4be3708ebfc)

### Beats 92%+ solutions

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 1
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if not curr.left and not curr.right:
                    return level
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level+=1
        return level
```
