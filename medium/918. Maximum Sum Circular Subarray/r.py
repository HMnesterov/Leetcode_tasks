class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        import sys

        def kadane_alg(array):
            max_so_far, max_ending = -sys.maxsize, 0
            min_so_far, min_ending = sys.maxsize, 0
            for i in range(len(array)):
                max_ending += array[i]
                if max_so_far < max_ending:
                    max_so_far = max_ending
                if max_ending < 0:
                    max_ending = 0

                min_ending += array[i]
                if min_so_far > min_ending:
                    min_so_far = min_ending
                if min_ending > 0:
                    min_ending = 0

            return max_so_far, min_so_far

        maxm, minm = kadane_alg(nums)
        if maxm > 0:
            return max([maxm, sum(nums) - minm])
        return maxm



"""TESTS
1)Runtime 397 ms
Beats 99.92%
Memory 19.1 MB
Beats 43.34%"""