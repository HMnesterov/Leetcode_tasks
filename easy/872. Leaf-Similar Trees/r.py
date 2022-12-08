# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_all_leafes(self, root, lst):
        if not root:
            return
        if root.left:
            self.find_all_leafes(root.left, lst)
        if root.right:
            self.find_all_leafes(root.right, lst)
        elif not root.left:
            lst.append(root.val)

    def leafSimilar(self, root1, root2) -> bool:
        lst1 = []
        lst2 = []
        self.find_all_leafes(root1, lst1)
        self.find_all_leafes(root2, lst2)
        return lst1 == lst2


"""TESTS:
1)Runtime 33 ms
Beats 94.35%
Memory 13.9 MB
Beats 87.58%
2)Runtime 40 ms
Beats 85.61%
Memory 13.9 MB
Beats 87.25%


"""