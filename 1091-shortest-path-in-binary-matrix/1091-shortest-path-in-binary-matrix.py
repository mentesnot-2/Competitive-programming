class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0,0,1)])
        visited = set((0,0))
        direct = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

        while q:
            r,c,l = q.popleft()

            if (min(r,c) < 0 or max(r,c) >= N or grid[r][c] == 1):
                continue
            if r == N - 1 and c == N -1:
                return l
            for newR,newC in direct:
                if (r + newR,c + newC) not in visited:
                    q.append((r + newR,c + newC,l + 1))
                    visited.add((r + newR,c + newC))
        return -1
        