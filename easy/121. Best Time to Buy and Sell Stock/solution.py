from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_value = prices.pop(0)
        max_value = min_value
        if not prices:
            return 0
        for i in prices:

            if min_value > i:
                diff = max_value - min_value

                result = diff if diff > result else result
                min_value, max_value = i, i
                continue

            if max_value < i:
                max_value = i
        else:
            diff = max_value - min_value
            result = diff if diff > result else result
        return result

"""TESTS:
1)Runtime 883 ms
Beats 99.90%
Memory 25.1 MB
Beats 32.77%
2)Runtime 873 ms
Beats 99.93%
Memory 25 MB
Beats 32.77%"""