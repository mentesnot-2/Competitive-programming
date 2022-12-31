class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum=0
        start=0
        average=float("-inf")
        for i in range(len(nums)):
            windowSum+=nums[i]
            if (i-start+1)==k:
                average=max(average,windowSum/k)
                windowSum-=nums[start]
                start+=1
        return average
        