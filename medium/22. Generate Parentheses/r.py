from typing import List


class Solution:
    lst = set()

    def generateParenthesis(self, n: int) -> List[str]:

        def check(stroka, n):
            count = 0
            for c in stroka:
                if c == "(":
                    count += 1
                else:
                    count -= 1
                if count < 0:
                    return False
            if count and n is 0:
                return False
            return True

        def recursion_func(stroka, n):
            if n > 0:
                if check(stroka + '(', n - 1):
                    recursion_func(stroka + '(', n - 1)
                if check(stroka + ')', n - 1):
                    recursion_func(stroka + ')', n - 1)
            else:
                self.lst.add(stroka)

        recursion_func('', n * 2)
        return list(self.lst)



"""TESTS:
1)Runtime 32 ms
Beats 97.29%
Memory 14.1 MB
Beats 98.47%"""