from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canMonkeyEatAll(piles, speed, timer):
            for pile in piles:
                required_time = ceil(pile / speed)
                timer -= required_time
                if timer < 0:
                    return False
            return True

        answer = float('inf')

        MIN = 1
        MAX = max(piles)
        while MIN < MAX:
            MIDDLE = (MAX + MIN) // 2
            if canMonkeyEatAll(piles, MIDDLE, h):
                answer = MIDDLE if MIDDLE < answer else answer
                MAX = MIDDLE
            else:
                MIN = MIDDLE + 1
        return MIN

"""TESTS:
1)Runtime 434 ms
Beats 85.55%
Memory 15.4 MB
Beats 62.86%
2)Runtime 418 ms
Beats 88.31%
Memory 15.5 MB
Beats 16.17%"""

