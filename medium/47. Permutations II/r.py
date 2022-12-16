from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        guy = []

        def rec(st, lst):
            if not lst:
                guy.append(st)
                return
            for c in lst:
                fake_st = st[:]
                fake_lst = lst[:]
                fake_st.append(c)
                fake_lst.remove(c)
                rec(fake_st, fake_lst)

        rec([], nums)
        return list(set(map(tuple, guy)))

sol = Solution()
print(sol.permuteUnique([1,1,2]))