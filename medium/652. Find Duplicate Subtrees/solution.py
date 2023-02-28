# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import Optional


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hash_table = defaultdict(int)
        result = set()

        def dfs(root):
            if not root:
                return '$'

            if not root.right and not root.left:
                string = root.val
                hash_table[string] += 1
                if hash_table[string] == 2:
                    result.add(root)

            string = str(root.val) + ',' + dfs(root.left) + ',' + dfs(root.right)
            hash_table[string] += 1

            if hash_table[string] == 2:
                result.add(root)
            return string

        dfs(root)
        return result
