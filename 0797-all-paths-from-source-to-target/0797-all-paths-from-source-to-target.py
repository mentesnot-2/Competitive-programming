class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def dfs(src,path):
            if src == len(graph) - 1:
                res.append(path)
                return
            for v in graph[src]:
                dfs(v,path + [v])
            return res  
        return dfs(0,[0])  
        