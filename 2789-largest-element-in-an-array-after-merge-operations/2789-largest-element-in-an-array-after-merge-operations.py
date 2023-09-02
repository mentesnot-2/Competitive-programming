class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums) - 1
        l = nums[n]
        for i in range(n - 1,-1,-1):
            l = l + nums[i] if nums[i] <= l else nums[i]
        return l
            
        