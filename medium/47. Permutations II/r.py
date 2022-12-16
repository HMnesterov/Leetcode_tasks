from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        guy = set()

        def rec(st, lst):
            if not lst:
                guy.add(tuple(st))
                return
            for c in lst:
                fake_st = st[:]
                fake_lst = lst[:]
                fake_st.append(c)
                fake_lst.remove(c)
                rec(fake_st, fake_lst)

        rec([], nums)
        return guy

"""TESTS:
1)Runtime 256 ms
Beats 26.41%
Memory 14.5 MB
Beats 26.16%"""