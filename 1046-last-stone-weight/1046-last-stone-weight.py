import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        heapq.heapify(stones)
        
        if (len(stones) == 1) :
            return stones[0]
        elif len(stones) == 0:
            return 0

        lrg,sml = heapq.nlargest(2,stones)
        stones = heapq.nsmallest(n - 2,stones)
        
        if lrg != sml:
            stones = heapq.nsmallest(n - 2,stones)
            heapq.heappush(stones,lrg - sml)
       
        return self.lastStoneWeight(stones)
        