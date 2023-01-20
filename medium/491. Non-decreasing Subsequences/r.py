from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def rec(indx, subsequence):
            nonlocal res
            if len(subsequence) > 1:
                res.add(tuple(subsequence))
            if indx == len(nums):
                return
            if not subsequence or nums[indx] >= subsequence[-1]:
                rec(indx + 1, subsequence + [nums[indx]])
            rec(indx + 1, subsequence)

        rec(0, [])
        return res
s = Solution()
print(s.findSubsequences(nums = [4,6,7,7]))

"""TESTS
1)Runtime 252 ms
Beats 58.91%
Memory 22.3 MB 
Beats 45.63%"""
