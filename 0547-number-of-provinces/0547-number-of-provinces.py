class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    
        visited = set()
        
        def dfs(node):
            visited.add(node)
            
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
            return True
        count = 0
        for k in graph:
            if k not in visited:
                count+=dfs(k)
        return count