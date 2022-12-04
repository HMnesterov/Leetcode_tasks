class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        r = Counter(s)
        return ''.join(sorted(list(s), key=lambda x: (r[x], x), reverse=True))
