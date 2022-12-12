from typing import List


class Solution:
    def threeSum(self, nums: List[int]):
        unique = set()

        diction = {}

        if len(set(nums)) == 1:
            return [[0, 0, 0]] if nums[0] == 0 else []
        for indx, digit in enumerate(nums):
            diction[digit] = indx
        for indx, x in enumerate(nums):
            for indx1, digit in enumerate(nums):
                target = (x + digit) * -1
                try:
                    last = diction[target]
                    if indx != indx1 != last and last != indx:
                        unique.add(tuple(sorted([x, digit, target])))
                except:
                    continue
        return list(unique)


"""TESTS:
1)Runtime 6977 ms
Beats 8.73%
Memory 18.3 MB
Beats 23.83%
"""
