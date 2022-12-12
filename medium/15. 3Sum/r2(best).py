from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        unique_answers = set()
        positive_nums, negative_nums, zeroes, = [], [], []
        for number in nums:
            if number > 0:
                positive_nums.append(number)
            elif number < 0:
                negative_nums.append(number)

            else:
                zeroes.append(0)
        set_n, set_p = set(negative_nums), set(positive_nums)
        if zeroes:
            for n in set_n:
                if n * -1 in set_p:
                    unique_answers.add((0, n, n * -1))

            if len(zeroes) >= 3:
                unique_answers.add((0, 0, 0))

        len_pos = len(positive_nums)
        for i in range(len_pos):
            for j in range(i + 1, len_pos):

                target = (positive_nums[i] + positive_nums[j]) * -1
                if target in set_n:
                    unique_answers.add(tuple(sorted([target, positive_nums[i], positive_nums[j]])))

        len_neg = len(negative_nums)
        for i in range(len_neg):
            for j in range(i + 1, len_neg):

                target = (negative_nums[i] + negative_nums[j]) * -1
                if target in set_p:
                    unique_answers.add(tuple(sorted([target, negative_nums[i], negative_nums[j]])))

        return list(unique_answers)


"""TESTS:
1)Runtime 1971 ms
Beats 60.90%
Memory 18.3 MB
Beats 23.83%

2)Runtime 1867 ms
Beats 64.18%
Memory 18.3 MB
Beats 23.83%

"""
