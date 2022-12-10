from idlelib.tree import TreeNode


class Solution:
    def node_sum(self, node: TreeNode):
        if node is None:
            return 0
        return node.val + self.node_sum(node.left) + self.node_sum(node.right)

    def checkMax(self, x: int):
        self.max_value = max(self.max_value, (x * (self.total - x)))

    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            self.checkMax(node.val)
            return node.val
        CurSum = node.val + self.dfs(node.left) + self.dfs(node.right)
        self.checkMax(CurSum)
        return CurSum

    def maxProduct(self, node: TreeNode):
        self.total = self.node_sum(node)
        self.max_value = 0
        self.dfs(node.right)
        self.dfs(node.left)
        return self.max_value % (10 ** 9 + 7)


"""TESTS:
1)Runtime
1032 ms
Beats
14.62%
Memory
75 MB
Beats
72.50%
"""