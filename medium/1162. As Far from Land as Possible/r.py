from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        n = len(grid)

        dist = 0

        q = deque()
        # arrays to keep track of the row and column movements
        drow = [0, -1, 0, 1]
        dcol = [-1, 0, 1, 0]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))

        if len(q) == n * n:
            return -1

        while q:

            size = len(q)

            dist += 1

            for _ in range(size):

                r, c = q.popleft()

                for i in range(4):

                    nrow, ncol = r + drow[i], c + dcol[i]

                    if 0 <= nrow < n and 0 <= ncol < n and grid[nrow][ncol] == 0:
                        grid[nrow][ncol] = 1

                        q.append((nrow, ncol))

        return dist - 1