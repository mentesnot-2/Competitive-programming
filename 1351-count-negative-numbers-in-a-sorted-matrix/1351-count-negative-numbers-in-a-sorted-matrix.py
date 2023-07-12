class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        
        for row in grid:
            low,high = 0, n - 1
            while low <= high:
                mid = low + (high - low)//2
                
                if row[mid] < 0:
                    high = mid -1
                else:
                    low = mid + 1
            count +=(n - low)
            
        return count