class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashSet = set()
        
        for a,b in edges:
            if a not in hashSet:
                hashSet.add(a)
            else:
                return a
            if b not in hashSet:
                hashSet.add(b)
            else:
                return b
                
                
        