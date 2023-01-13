class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l=0
        r=len(piles)-2
        count=0
        while l<r:
            count+=piles[r]
            r-=2
            l+=1
        return count