from functools import lru_cache
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True
        @lru_cache(None)
        def func(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in wordDict and (suffix in wordDict or func(suffix)):
                    return True

        return True if func(s) else False

"""TESTS
1)Runtime 80 ms
Beats 20.36%
Memory 14.1 MB
Beats 43.59%
"""