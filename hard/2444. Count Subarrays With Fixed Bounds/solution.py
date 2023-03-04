from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:


        count = 0
        border = -1
        lastMIN, lastMAX = -1, -1
        for indx, value in enumerate(nums):
            if minK <= value <= maxK:
                lastMIN = indx if value == minK else lastMIN
                lastMAX = indx if value == maxK else lastMAX

                count += max([0, min([lastMIN, lastMAX]) - border])

            else:
                lastMIN, lastMAX = -1, -1
                border = indx
        return count

    """TESTS:
    1)Runtime
955 ms
Beats
35.5%
Memory
28.6 MB
Beats
41.16%"""