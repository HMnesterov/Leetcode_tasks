from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def bfs(node):

            node.right, node.left = node.left, node.right
            if node.left: bfs(node.left)
            if node.right: bfs(node.right)

        test = root
        if not test:
            return
        bfs(test)

        return root


"""TESTS:
1)Runtime 29 ms
Beat 86.44%
Memory 13.9 MB
Beats 78.39%

2)Runtime 27 ms
Beats 92.80%
Memory 13.9 MB
Beats 48.39%"""