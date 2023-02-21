from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = left + int((right - left) // 2)
            if middle % 2 == 1:
                middle -= 1

            if nums[middle] != nums[middle + 1] and nums[middle] != nums[middle - 1]:
                return nums[middle]

            if nums[middle] != nums[middle + 1]:
                right = middle + 1
                continue
            left = middle + 2
        return nums[left]


"""TESTS:
1)Runtime 175 ms Beats 78.27% Memory 23.7 MB Beats 86.81%
2) Runtime 182 ms Beats 55.3% Memory 23.7 MB Beats 86.81%"""