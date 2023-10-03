class Solution:
    def containsCycle(self, grid):
        m = len(grid)
        n = len(grid[0])
        seen = [[False] * n for _ in range(m)]

        dirs = [0, 1, 0, -1, 0]

        def dfs(i, j, prevI, prevJ, c):
            seen[i][j] = True

            for k in range(4):
                x = i + dirs[k]
                y = j + dirs[k + 1]
                if x < 0 or x == m or y < 0 or y == n:
                    continue
                if x == prevI and y == prevJ:
                    continue
                if grid[x][y] != c:
                    continue
                if seen[x][y]:
                    return True
                if dfs(x, y, i, j, c):
                    return True

            return False

        for i in range(m):
            for j in range(n):
                if seen[i][j]:
                    continue
                if dfs(i, j, -1, -1, grid[i][j]):
                    return True

        return False
