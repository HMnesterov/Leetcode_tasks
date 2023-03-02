from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results_bank = set()
        table = {i: indx for indx, i in enumerate(nums)}
        n = len(nums)

        for x in range(n):
            for j in range(x + 1, n):
                for k in range(j + 1, n):
                    required = target - nums[x] - nums[j] - nums[k]
                    try:
                        z = table[required]
                    except KeyError:
                        continue
                    if z not in (x, j, k):
                        results_bank.add(tuple(sorted([nums[x], nums[j], nums[k], required])))

        return results_bank


"""TESTS:
1)Runtime 3055 ms
Beats 7.7%
Memory 13.9 MB
Beats 55.7%
2)Runtime 3084 ms
Beats 6.94%
Memory 13.9 MB
Beats 89.40%"""
