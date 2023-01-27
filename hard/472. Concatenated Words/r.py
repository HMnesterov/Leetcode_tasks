from functools import lru_cache
from typing import List


@lru_cache(maxsize=None)
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_SET = set(words)
        words.sort(reverse=True)

        def check_valid_or_not(string):
            for i in range(1, len(string)):
                prefix = string[:i]
                suffix = string[i:]
                if prefix in word_SET and (suffix in word_SET or check_valid_or_not(suffix)):
                    return True

        examples = set()
        for word in words:
            if check_valid_or_not(word):
                examples.add(word)

        return examples

"""TESTS:
1)Runtime 413 ms
Beats 70.40%
Memory 27.8 MB
Beats 37.94%

2)Runtime 389 ms
Beats 79.14%
Memory 27.7 MB
Beats 47.98%"""