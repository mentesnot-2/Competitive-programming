class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        mx = float("-inf")
        if len(nums) < 2: return 0
        for i in range(1,len(nums)):
            if (nums[i] - nums[i - 1]) > mx:
                mx = (nums[i] - nums[i - 1])
        return mx