class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for i in range(n):
           a, b = b , a + b
        return a


"""TESTS:
1)Runtime 45 ms
Beats 71.45%
Memory 13.8 MB
Beats 58.8%
"""