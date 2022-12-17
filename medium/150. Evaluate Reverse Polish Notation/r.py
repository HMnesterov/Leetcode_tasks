from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = []
        for i in tokens:
            if i not in '/-*+':
                stack.append(int(i))
            else:
                x = stack.pop(-1)
                y = stack.pop(-1)
                stack.append(int(eval(f"{y}{i}{x}")))

        return stack[0]


"""TESTS:
1)
Runtime 124 ms
Beats 67.64%
Memory 14.4 MB
Beats 60.84%
2)Runtime 136 ms
Beats 60.56%
Memory 14.3 MB
Beats 60.84%"""