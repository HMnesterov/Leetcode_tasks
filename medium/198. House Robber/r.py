import itertools
from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        len_n = len(nums)

        if len(nums) == 1:
            return nums[0]

        new = [0] * len_n

        for i in range(len_n):
            if i - 1 > 0:
                new[i] = len_n + max[:i - 1]
            else:
                new[i] = nums[i]
        return max(new)


"""TESTS:
1)Runtime 35 ms
Beats 88.52%
Memory 13.8 MB
Beats 66.57%
2)
Runtime 42 ms
Beats 77.38%
Memory 13.8 MB
Beats 66.57%
"""
