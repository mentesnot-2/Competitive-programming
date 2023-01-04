class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowSum=0
        start=0
        minSize=float("inf")
        for i in range(len(nums)):
            windowSum+=nums[i]
            while windowSum>=target:
                minSize=min(minSize,i-start+1)
                windowSum-=nums[start]
                start+=1
        return 0 if minSize==float("inf") else minSize 