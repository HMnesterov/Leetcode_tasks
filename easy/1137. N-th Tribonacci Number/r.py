class Solution:
    def tribonacci(self, n: int) -> int:
        if  n == 0:
            return 0
        dig1, dig2, dig3 = 0, 1, 1
        for i in range(n - 2):
            new_dig = dig1 + dig2 + dig3
            dig3, dig2, dig1 = new_dig, dig3, dig2
        return dig3

"""TESTS
1)Runtime 33 ms
Beats 64.92%
Memory 13.9 MB
Beats 54.1%
2)Runtime 31 ms
Beats 76.51%
Memory 13.8 MB
Beats 54.1% 
"""