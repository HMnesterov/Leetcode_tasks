from math import ceil
from typing import List
from collections import defaultdict


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0
        connection = defaultdict(list)
        previous = -1

        fuel = 0
        for i in roads:
            connection[i[0]].append(i[1])
            connection[i[1]].append(i[0])

        def dfs(node, previous):
            nonlocal fuel
            elems_count = 1
            for child in connection[node]:
                if child == previous:
                    continue

                elems_count += dfs(child, node)
            if node > 0:
                fuel += int(ceil(elems_count / seats))
            return elems_count

        dfs(0, previous)
        return fuel