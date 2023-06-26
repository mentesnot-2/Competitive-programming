class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        left = 0
        minLen = float("inf")
        for i in range(len(nums)):
            sum+=nums[i]
            while sum>=target:
                minLen = min(minLen,i - left + 1)
                sum-=nums[left]
                left+=1
        return minLen if minLen != float("inf") else 0
            
        