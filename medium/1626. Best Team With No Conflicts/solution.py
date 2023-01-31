from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        len_sc = len(ages)
        array = sorted(zip(ages, scores, [0] * len_sc))

        for i in range(len_sc):
            current_var = array[i]
            potential_variants = filter(lambda x: x[1] <= current_var[1], array[:i])
            try:
                best = max(potential_variants, key=lambda x: x[2])[2]
            except ValueError:
                best = 0
            array[i] = [current_var[0], current_var[1], current_var[1] + best]

        return max(array, key=lambda x: x[2])[2]

"""TESTS
1)Runtime 1508 ms
Beats 81.56%
Memory 14.3 MB
Beats 51.77%

2)Runtime 1503 ms
Beats 81.56%
Memory 14.3 MB
Beats 22.70%"""