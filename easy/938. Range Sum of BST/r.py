# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def recursive_run(self, node, low, high, col):
        if not node:
            return
        if node.right:
            self.recursive_run(node.right, low, high, col)
        if node.left:
            self.recursive_run(node.left, low, high, col)

        if low <= node.val <= high:
            col.append(node.val)

    def rangeSumBST(self, root, low: int, high: int) -> int:
        collector = [0]
        self.recursive_run(root, low, high, collector)
        return sum(collector)


"""TESTS:
1)Runtime
251 ms
Beats
87.17%
Memory
23 MB
Beats
92.23%

2)

Runtime
255 ms
Beats
86.22%
Memory
23 MB
Beats
80.66%
"""
