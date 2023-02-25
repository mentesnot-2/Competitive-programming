class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxPro=0
        while r<len(prices):
            if prices[r]>prices[l]:
                maxPro=max(maxPro,prices[r]-prices[l])
          
            else:
                l=r
            r+=1
        return maxPro