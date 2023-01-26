from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        best_view, nodes = defaultdict(list), set()
        flights.sort(key=lambda x: x[2], reverse=True)

        for start, end, price in flights:
            best_view[start].append([end, price])
            nodes.add(end)
        if src not in best_view or dst not in nodes:
            return -1

        cheapest, way = float('inf'), [[end, price, 0] for end, price in best_view[src]]
        while way:
            end, price, stop = way.pop()

            if price >= cheapest:
                continue
            if end == dst:
                cheapest = price
            elif stop < k and end in best_view:
                for e, pr in best_view[end]:
                    if price + pr < cheapest:
                        way += [[e, price + pr, stop + 1]]
        return cheapest if cheapest != float('inf') else -1


"""TESTS
1)Runtime 135 ms
Beats 67.41%
Memory 152.2 MB
Beats 4.38%"""