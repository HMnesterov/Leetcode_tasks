class Solution:
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        for indx, value in enumerate(nums):
            if value == target:
                return indx
            try:
                if value < target < nums[indx + 1]:
                    return indx + 1
            except:
                return indx + 1
        return indx

"""TESTS:
1)Runtime 51 ms
Beats 71.26%
Memory 14.8 MB
Beats 31.55%
2)Runtime 55 ms
Beats 46.82%
Memory 14.7 MB
Beats 73.66%
"""