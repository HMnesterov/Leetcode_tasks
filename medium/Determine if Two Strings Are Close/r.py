from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if word1 == word2:
            return True
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        t1 = sorted(Counter(word1).values())
        t2 = sorted(Counter(word2).values())
        return t1 == t2