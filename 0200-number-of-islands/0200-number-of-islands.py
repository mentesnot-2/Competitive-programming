class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        n, m = len(grid), len(grid[0])
        seen = set()
        islands = 0
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= n or col >= m or grid[row][col] == "0" or (row, col) in seen:
                return
            
            seen.add((row, col))
            
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
            
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    islands += 1
                    
        return islands
