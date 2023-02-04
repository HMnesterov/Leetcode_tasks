from collections import Counter



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, len_s1 = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
            if i >= len_s1 and s2[i - len_s1] in cntr:
                cntr[s2[i - len_s1]] += 1

            if all([cntr[i] == 0 for i in cntr]):
                return True

        return False
