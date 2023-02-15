from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for indx, value in enumerate(str(k)[::-1], 1):
            try:
                num[-indx] += int(value)
            except IndexError:
                num.insert(0, int(value))
        len_n = len(num)
        for i in range(len_n - 1, -1, -1):
            summa = num[i]
            if summa >= 10:
                num[i] = summa % 10
            else:
                continue

            if 0 <= i - 1 <= len_n - 1:
                num[i - 1] += summa // 10

            else:
                num.insert(0, summa // 10)

        return num


"""TESTS:
1)Runtime 275 ms
Beats 93.42%
Memory 15 MB
Beats 65.15%"""