from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(map(list, permutations(nums)))

"""TESTS
1)Runtime 87 ms
Beats 30.67%
Memory 14 MB
Beats 84.82%
2)Runtime 83 ms
Beats 41.39%
Memory 14 MB
Beats 84.82% 
"""