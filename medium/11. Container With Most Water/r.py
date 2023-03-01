from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr_len = len(height)
        max_value = 0
        marker_1, marker_2 = 0, arr_len - 1
        for _ in range(arr_len):
            curr_S = abs(marker_1 - marker_2) * min((height[marker_1], height[marker_2]))
            if max_value < curr_S:
                max_value  = curr_S
            if height[marker_1] > height[marker_2]:
                marker_2 -= 1
            else:
                marker_1 += 1
        return max_value

"""TESTS
1)Runtime 773 ms
Beats 63.96%
Memory 27.2 MB
Beats 93.6%
2)Runtime 755 ms
Beats 78.7%
Memory 27.4 MB
Beats 84.27%"""