class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        if len(temperatures) == 1:
            return 0

        for indx, value in enumerate(temperatures):
            if not stack:
                stack.append([indx, value])
            else:
                while stack:
                    last = stack.pop(-1)
                    if temperatures[indx] > last[1]:
                        result[last[0]] = indx - last[0]
                    else:
                        stack.append(last)
                        break
                stack.append([indx, value])

        return result


"""TESTS
1)Runtime
1560 ms
Beats
75.86%
Memory
30.3 MB
Beats
15.95%

2)Runtime
1575 ms
Beats
75.54%
Memory
30.3 MB
Beats
15.46%"""