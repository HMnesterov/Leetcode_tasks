from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        array = []
        for i in range(n):
            array.append(nums[i])
            array.append(nums[i + n])
        return array

"""
1)Runtime 60 ms
Beats 84.21%
Memory 14.1 MB
Beats 86.30%
2)Runtime 56 ms
Beats 94.54%
Memory 14.2 MB
Beats 33.52%"""