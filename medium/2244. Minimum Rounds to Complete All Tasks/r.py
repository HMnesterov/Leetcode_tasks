from collections import Counter
from typing import List
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        hash_table = Counter(tasks)
        count = 0
        for task in hash_table.values():
            if task < 2:
                return -1
            if task % 3 == 0:
                count += task // 3

            elif task == 2:
                count += 1

            else:
                count += abs(task // -3)
        return count

"""TESTS:
1)Runtime 2083 ms
Beats 45.41%
Memory 28.1 MB
Beats 96.23%
2)Runtime 2081 ms
Beats 45.46%
Memory 28.1 MB
Beats 97.83%"""