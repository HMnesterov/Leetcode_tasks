from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        count = 0
        start = []
        end = []
        empty_count = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    empty_count += 1
                elif grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == 2:
                    end = [i, j]
        visited = start


        vertical_border = len(grid)

        horizontal_border = len(grid[0])

        def recursion_func(visited, way):
            nonlocal count
            coords = ((-1, 0), (1, 0), (0, -1), (0, 1))
            default_i, default_j = way
            ways_to_go = [[default_i + i, default_j + j] for i, j in coords
                          if 0 <= default_i + i < vertical_border and
                          0 <= default_j + j < horizontal_border
                          and [default_i + i, default_j + j] not in visited and grid[default_i + i][
                              default_j + j] != -1]
            if not ways_to_go:

                x, y = way
                if end == [x, y] and len(visited) == empty_count:


                    count += 1

            else:
                for new_way in ways_to_go:
                    new = visited[:]

                    new.append(new_way)

                    recursion_func(new, new_way[:])

        recursion_func([visited], visited)
        return count


"""TESTS
Runtime
129 ms
Beats
38.63%
Memory
13.9 MB
Beats
93.68%"""