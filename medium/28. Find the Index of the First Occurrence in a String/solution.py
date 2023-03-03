class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        i = 0
        if n < m:
            return -1
        while i < n:
            if haystack[i:i + m ] == needle:
                return i
            i += 1
        return -1

"""TESTS:
1)Runtime 23 ms
Beats 97.85%
Memory 13.9 MB
Beats 11.3%"""