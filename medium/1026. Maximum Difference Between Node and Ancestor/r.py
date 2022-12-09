class Solution:
    container = []

    def recursion_func(self, root, old):
        if not root:
            return

        old.append(root.val)
        if not root.left and not root.right:
            self.container.append(abs(min(old) - max(old)))
        if root.left:
            self.recursion_func(root.left, old[:])
        if root.right:
            self.recursion_func(root.right, old[:])

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        print(self.container)

        self.recursion_func(root, [])

        return max(self.container)