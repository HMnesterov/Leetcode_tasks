from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        alls = set()
        target = len(graph) - 1
        visited = [0]
        not_visited = graph[0]
        way = [0]
        diction = {i: graph[i] for i in range(target + 1)}

        def rec(visited, not_visited, way):
            if way[-1] == target:
                alls.add(tuple(way))
            else:
                for next in not_visited:
                    if next not in visited:
                        new_v = visited[:] + [next]
                        new_n = diction[next]
                        rec(new_v, new_n, way[:] + [next])

        rec(visited, not_visited, way)
        return alls
"""Tests
Runtime
104 ms
Beats
84.93%
Memory
16.2 MB
Beats
6.92%"""