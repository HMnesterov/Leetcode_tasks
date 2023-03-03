from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(list)
        boxes = defaultdict(list)

        def detect_box_key(row, col):
            if 0 <= row <= 2:
                row = 0
            elif 3 <= row <= 5:
                row = 1
            elif 6 <= row <= 8:
                row = 2

            if 0 <= col <= 2:
                col = 0
            elif 3 <= col <= 5:
                col = 1
            elif 6 <= col <= 8:
                col = 2
            return f"{row}{col}"

        for indx, line in enumerate(board):
            values = []
            for indx1, value in enumerate(line):
                try:
                    value = int(value)
                except:
                    continue
                if value in values:
                    return False
                values.append(value)
                if value in columns[indx1]:
                    return False
                columns[indx1].append(value)

                box_key = detect_box_key(indx, indx1)

                if value in boxes[box_key]:
                    return False
                boxes[box_key].append(value)

        return True


"""TESTS:
1)Runtime 109 ms
Beats 27.95%
Memory 13.9 MB
Beats 73.20%
2)Runtime 110 ms
Beats 26.6%
Memory 14 MB
Beats 25.73%"""
