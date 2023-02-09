from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = [set() for _ in range(26)]
        for idea in ideas:
            groups[ord(idea[0]) - ord('a')].add(idea[1:])

        answer = 0
        for i in range(25):
            for j in range(i + 1, 26):
                mutuals = 0
                for ideaA in groups[i]:
                    if ideaA in groups[j]:
                        mutuals += 1
                answer += 2 * (len(groups[i]) - mutuals) * (len(groups[j]) - mutuals)

        return answer

