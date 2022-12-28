from heapq import heapify, heapreplace
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-x for x in piles]
        heapify(pq)
        for _ in range(k): heapreplace(pq, pq[0]//2)
        return -sum(pq)

