from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], a: int) -> int:
        count = 0
        new_guy = list(map(lambda x: capacity[x] - rocks[x], range(len(rocks))))
        new_guy.sort()
        for c in new_guy:
            a -= c
            if a >= 0:
                count +=1
                continue
            return count
        return count


"""TESTS:
1)Runtime 887 ms
Beats 99.67%
Memory 22.1 MB
Beats 87.83%
2)Runtime 904 ms
Beats 99.34%
Memory 22.1 MB
Beats 87.83%

"""
