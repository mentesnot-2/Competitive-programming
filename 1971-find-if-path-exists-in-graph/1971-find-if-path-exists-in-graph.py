class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for a,b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
                
            graph[a].append(b)
            graph[b].append(a)
        def dfs(source,visited):
            if source == destination:
                return True
            visited.add(source)
            for node in graph[source]:
                if node not in visited:
                    found = dfs(node,visited)
                    if found:
                        return found
            return False
        visited = set()
        return dfs(source,visited)