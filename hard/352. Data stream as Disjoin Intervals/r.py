from typing import List


class SummaryRanges:

    def __init__(self):
        self.stream = set()

    def addNum(self, value: int) -> None:
        self.stream.add(value)

    def getIntervals(self) -> List[List[int]]:

        values = sorted(self.stream)
        ways = []
        while values:
            a = values.pop(0)

            last_val = a

            for indx, value in enumerate(values):
                if value - last_val == 1:
                    last_val = value
                else:
                    values = values[indx:]

                    ways.append([a, last_val])
                    break
            else:
                ways.append([a, last_val])
                return ways
        return ways

"""TESTS:
1)Runtime 407 ms
Beats 34.45%
Memory 18.9 MB
Beats 99%
2)Runtime 405 ms
Beats 34.45%
Memory 19 MB
Beats 75.92%
"""