from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        elems_count = Counter(p)
        len_p = len(p)
        values = []
        for index, value in enumerate(s):
            if value in elems_count:
                elems_count[value] -= 1
            if index >= len_p and s[index - len_p] in elems_count:
                elems_count[s[index - len_p]] += 1
            if all([i == 0 for i in elems_count.values()]):
                values.append(index - len_p + 1)
        return values


"""TESTS:
1)Runtime 213 ms
Beats 51.64%
Memory 15.1 MB
Beats 74.41%
2)Runtime 214 ms 
Beats 51.52%
Memory 15.2 MB
Beats 74.41%
"""