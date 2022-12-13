from typing import List


class Solution:
    values = set()

    def rec(self, count, cord_row, cord_column):
        val = 0
        count += self.matrix[cord_row][cord_column]
        if self.check_valid_coords(cord_row + 1, cord_column - 1):
            self.rec(count, cord_row + 1, cord_column - 1)
            val += 1
        if self.check_valid_coords(cord_row + 1, cord_column):
            self.rec(count, cord_row + 1, cord_column)
            val += 1
        if self.check_valid_coords(cord_row + 1, cord_column + 1):
            self.rec(count, cord_row + 1, cord_column + 1)
            val += 1
        if val is 0:
            self.values.add(count)

    def check_valid_coords(self, cord_row, cord_columns):
        if 0 <= cord_row < self.rows and 0 <= cord_columns < self.columns:
            return True
        return False

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        if self.rows == 1 and self.columns == 1:
            return matrix[0][0]

        for i in range(self.columns):
            self.rec(0, 0, i)

        return min(self.values)

