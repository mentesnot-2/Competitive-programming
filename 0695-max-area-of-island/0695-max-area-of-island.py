class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        longest = 0
        seen = set()
        
        def dfs(row,col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == 0 or (row, col) in seen:
                return 0
            seen.add((row,col))
            count = 1
            count+=dfs(row - 1, col)
            count+=dfs(row + 1, col)
            count+=dfs(row, col - 1)
            count+=dfs(row, col + 1)
            return count
        
        
        
        for r in range(m):
            for c in range(n):
                size = dfs(r,c)
                if size > longest:
                    longest = size
        return longest
                
                
            
                
        