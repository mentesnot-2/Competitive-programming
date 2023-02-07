class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        wSum=0
        l=0
        min_sub=float("inf")
        for i in range(len(nums)):
            wSum+=nums[i]
            while wSum>=target:
                min_sub=min(min_sub,i-l+1)
                wSum-=nums[l]
                l+=1
        return 0 if min_sub==float("inf") else min_sub