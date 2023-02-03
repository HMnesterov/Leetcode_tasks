from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        dict_i = defaultdict(str)

        while s:
            try:
                for i in range(numRows):
                    dict_i[i] += s[i]
                s = s[i:]
            except IndexError:
                break

            try:
                count = 0
                for i in range(numRows - 2, 0, -1):
                    dict_i[i] += s[count]
                    count += 1
                s = s[numRows - 2:]
            except IndexError:
                break
        new_str = ''.join([dict_i[i] for i in dict_i])
        return new_str

"""TESTS:
1)Runtime 62 ms
Beats 69.88%
Memory 14 MB
Beats 72.54%
2)Runtime 59 ms
Beats 79.81%
Memory 13.9 MB
Beats 89.34%"""