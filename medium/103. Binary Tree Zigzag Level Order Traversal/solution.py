# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [root]
        answer = []
        if not root:
            return
        if not root.right and not root.left:
            return [[root.val]]
        count = 0
        while result:
            new_level = []
            current = []
            for x in result:
                if x.left:
                    new_level.append(x.left)
                if x.right:
                    new_level.append(x.right)
                current.append(x.val)
            result = new_level
            if current:
                if count % 2 == 0:
                    answer.append(current)
                else:
                    answer.append(current[::-1])
                count += 1
        return answer

"""TESTS:
1)Runtime 33 ms
Beats 76.15%
Memory 14.2 MB
Beats 10.32%
2)Runtime 38 ms
Beats 45.29%
Memory 14.1 MB
Beats 94.5%"""