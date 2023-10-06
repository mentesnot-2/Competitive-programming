class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        graph = defaultdict()
        
        for a,b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        for i in graph:
            if len(graph[i]) == n :
                return i
        print(graph)
        return 0
                
        