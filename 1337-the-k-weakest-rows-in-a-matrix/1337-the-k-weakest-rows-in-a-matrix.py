class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        candidates = []
        
        for i,row in enumerate(mat):
            candidates.append([sum(row),i])
            
        candidates.sort(key = lambda c : (c[0],c[1]))
        res = []
        
        for i in range(k):
            res.append(candidates[i][1])
        return res
        