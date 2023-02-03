class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        left=nums[0]
        best=max(nums)
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                left=nums[i]
            else:
                left+=nums[i]
            best=max(best,left)
        return best