class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l=high-low+1
        m=l//2
        
        if l%2 and low%2:
            return m+1
        return m
        