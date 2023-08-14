import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)
        print(heapq.nlargest(2,nums))
        return heapq.nlargest(k,nums)[k-1]
        