import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if n == 1:
            return True
        connected = dict()
        for c in edges:
            if sorted([c[0], c[1]]) == sorted([source, destination]):
                return True

            connected[c[0]] = connected.get(c[0], []) + [c[1]]
            connected[c[1]] = connected.get(c[1], []) + [c[0]]
        visited = [False] * n
        visited[source] = True

        try:
            sous = connected[source]
        except:
            return False
        queue = collections.deque([source])
        while queue:
            curr_graph = queue.popleft()
            if curr_graph == destination:
                return True
            for next_graph in connected[curr_graph]:
                if not visited[next_graph]:
                    visited[next_graph] = True
                    queue.append(next_graph)



#Runtime
#5114 ms
#Beats
#15.64%
#Memory
#103.8 MB
#Beats
#85.63%