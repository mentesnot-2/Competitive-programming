from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        minute = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                l, r = queue.popleft()
                for dr, dc in directions:
                    nl, nr = l + dr, r + dc
                    if 0 <= nl < m and 0 <= nr < n and grid[nl][nr] == 1:
                        grid[nl][nr] = 2  
                        queue.append((nl, nr))
            if queue:  
                minute += 1
        for row in grid:
            if 1 in row:
                return -1
        return minute
