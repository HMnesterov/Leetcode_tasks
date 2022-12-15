class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        if text1 == text2:
            return len(text1)
        len_1 = len(text1)
        len_2 = len(text2)
        matrix = [[0 for _ in range(len_2)] for j in range(len_1)]
        for k in range(len_2):
            if text1[:0 + 1] in text2[:k + 1]:
                matrix[0][k] += 1
        i = 0
        for i in range(1, len_1):
            for j in range(len_2):

                if text1[:i + 1][-1] == text2[:j + 1][-1]:
                    try:
                        lst = matrix[i-1][:j] + [0]
                    except:
                        lst = 0
                    matrix[i][j] += (1 + max(lst))
                else:
                    lst = []
                    if 0 <= i - 1 < len_1:
                        lst.append(matrix[i - 1][j])
                    if 0 <= j - 1 < len_1:
                        lst.append(matrix[i][j - 1])
                    matrix[i][j] = max(lst)
        return max(matrix[i])



"""TESTS
1)Runtime 1351 ms
Beats 35.25%
Memory 22.8 MB
Beats 43.63%
2)Runtime 1343 ms
Beats 35.73%
Memory 22.8 MB
Beats 43.63%"""