class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        numberOfComponents = 0
        def dfs(isConnected,node,visited):
            visited[node] = True
            for i in range(n):
                if isConnected[node][i] and not visited[i]:
                    dfs(isConnected,i,visited)


        for j in range(n):
            if not visited[j]:
                numberOfComponents+=1
                
                dfs(isConnected,j,visited)
        
        return numberOfComponents
