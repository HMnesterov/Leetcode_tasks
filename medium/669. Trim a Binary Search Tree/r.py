# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if low <= root.val <= high:
                return root
            if root.left:
                return root.left
            if root.right:
                return root.right

        return dfs(root)

"""TESTS:
1)Runtime 63 ms
Beats 21.2%
Memory 16.2 MB
Beats 91.8%
2)Runtime
63 ms
Beats
21.2%
Memory
16.2 MB
Beats
91.8%
"""
