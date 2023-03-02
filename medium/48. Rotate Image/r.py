class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        lines = []
        for i in range(n):
            line = []
            for j in range(n - 1, -1, -1):
                line.append(matrix[j][i])
            lines.append(line)
        for indx, line in enumerate(lines):
            matrix[indx] = line
        return matrix

"""TESTS:
1)Runtime 29 ms
Beats 96.7%
Memory 13.8 MB
Beats 64.30%
2)Runtime 29 ms
Beats 96.7%
Memory 13.7 MB
Beats 97.76%
"""
