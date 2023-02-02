from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash_table = {}
        for indx, value in enumerate(order):
            hash_table[value] = indx

        def check_two_words(word1, word2, hash_table):
            if word1 == word2:
                return True
            for indx, value in enumerate(word1):
                try:
                    if hash_table[value] == hash_table[word2[indx]]:
                        continue
                    if not hash_table[value] < hash_table[word2[indx]]:
                        return False
                    return True
                except IndexError:
                    return False
            return True

        for v in range(len(words)):
            try:
                if not check_two_words(words[v], words[v + 1], hash_table):
                    return False
            except:
                return True
        return True

"""TESTS
1) Runtime 34 ms Beats 89.52% Memory 14 MB Beats 31.27%
2)Runtime 38 ms
Beats 74.83%
Memory 13.9 MB
Beats 31.27%"""