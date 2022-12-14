class Solution:
    def numTrees(self, n: int) -> int:
        from math import factorial
        # CATALAN NUMBERS
        return int(factorial(2 * n) / (factorial(n + 1) * factorial(n)))


"""TESTS
1)Runtime 32 ms
Beats 92.15%
Memory 13.9 MB
Beats 4.66%
2)Runtime 35 ms
Beats 86.32%
Memory 13.8 MB
Beats 61.75%
"""